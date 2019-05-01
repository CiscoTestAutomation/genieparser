#!/bin/env python

import sys
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from textwrap import dedent

ats_mock = Mock()
with patch.dict('sys.modules',
        {'ats' : ats_mock}, autospec=True):
    import genie.parsergen
    from genie.parsergen import oper_fill
    from genie.parsergen import oper_check
    from genie.parsergen import oper_fill_tabular
    from genie.parsergen.examples.parsergen.pyAts import parsergen_demo_mkpg

import xml.etree.ElementTree as ET

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.iosxe.show_interface import ShowInterfacesSwitchport,\
                                        ShowIpInterfaceBriefPipeVlan,\
                                        ShowInterfaces, ShowIpInterface,\
                                        ShowIpv6Interface, \
                                        ShowInterfacesTrunk, \
                                        ShowInterfacesCounters, \
                                        ShowInterfacesAccounting, \
                                        ShowIpInterfaceBriefPipeIp,\
                                        ShowInterfacesStats


class test_show_interface_parsergen(unittest.TestCase):

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
# unitest For show ip interfaces brief pipe ip
#############################################################################
class test_show_ip_interfaces_brief_pipe_ip(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'interface':
        {'GigabitEthernet0/0': {'interface_ok': 'YES',
                                      'interface_status': 'up',
                                      'ip_address': '10.1.18.80',
                                      'method': 'manual',
                                      'protocol_status': 'up'}}}

    golden_output = {'execute.return_value': '''
        R1#sh ip int brief | i 10.1.18.80 
        GigabitEthernet0/0     10.1.18.80      YES manual up                    up   
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

# Comment out due to old version of yang, will enhance it
# class test_show_interface_brief_pipe_vlan_yang(unittest.TestCase):

#     device = Device(name='aDevice')
#     device1 = Device(name='bDevice')
#     golden_parsed_output = {'interface': {'Vlan1': {'vlan_id': {'1': {'ip_address': 'unassigned'}}},
#                                           'Vlan100': {'vlan_id': {'100': {'ip_address': '192.168.234.1'}}}}}

#     class etree_holder():
#       def __init__(self):
#         self.data = ET.fromstring('''
#           <data>
#             <native xmlns="http://cisco.com/ns/yang/ned/ios">
#               <interface>
#                 <Vlan>
#                   <name>1</name>
#                   <ip>
#                     <no-address>
#                       <address>false</address>
#                     </no-address>
#                   </ip>
#                   <shutdown/>
#                 </Vlan>
#                 <Vlan>
#                   <name>100</name>
#                   <ip>
#                     <address>
#                       <primary>
#                         <address>192.168.234.1</address>
#                         <mask>255.255.255.0</mask>
#                       </primary>
#                     </address>
#                   </ip>
#                   <ipv6>
#                     <address>
#                       <prefix-list>
#                         <prefix>2001::12:30/128</prefix>
#                       </prefix-list>
#                     </address>
#                   </ipv6>
#                 </Vlan>
#               </interface>
#             </native>
#           </data>
#         ''')
    
#     golden_output = {'get.return_value': etree_holder()}

#     def test_golden(self):
#         self.device = Mock(**self.golden_output)
#         intf_obj = ShowIpInterfaceBriefPipeVlan(device=self.device)
#         intf_obj.context = Context.yang.value
#         parsed_output = intf_obj.parse()
#         self.assertEqual(parsed_output,self.golden_parsed_output)

#     empty_parsed_output = {'interface': {}}

#     class empty_etree_holder():
#       def __init__(self):
#         self.data = ET.fromstring('''
#           <data>
#             <native xmlns="http://cisco.com/ns/yang/ned/ios">
#               <interface>
#                 <Vlan>
#                 </Vlan>
#               </interface>
#             </native>
#           </data>
#         ''')

#     empty_output = {'get.return_value': empty_etree_holder()}

#     def test_empty(self):
#         self.device1 = Mock(**self.empty_output)
#         intf_obj = ShowIpInterfaceBriefPipeVlan(device=self.device1)
#         intf_obj.context = Context.yang.value
#         parsed_output = intf_obj.parse()
#         self.assertEqual(parsed_output,self.empty_parsed_output)


#############################################################################
# unitest For Show Interfaces switchport
#############################################################################
class test_show_interfaces_switchport(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        "GigabitEthernet1/0/4": {
            "switchport_mode": "trunk",
            "pruning_vlans": "2-1001",
            'operational_mode': 'trunk',
            "switchport_enable": True,
            "trunk_vlans": "200-211",
            "capture_mode": False,
            "private_vlan": {
                 "native_vlan_tagging": True,
                 "encapsulation": "dot1q"
            },
            "access_vlan": "1",
            "unknown_unicast_blocked": False,
            "native_vlan_tagging": True,
            "unknown_multicast_blocked": False,
            "protected": False,
            "negotiation_of_trunk": True,
            "capture_vlans": "all",
            "encapsulation": {
                 "operational_encapsulation": "dot1q",
                 "native_vlan": "1",
                 "administrative_encapsulation": "dot1q"
            }
       },
       "GigabitEthernet1/0/2": {
            "pruning_vlans": "2-1001",
            "switchport_enable": True,
            "unknown_multicast_blocked": False,
            "trunk_vlans": "100-110",
            "port_channel": {
                "port_channel_int": "Port-channel12",
                "port_channel_member": True
            },
            "access_vlan": "1",
            "operational_mode": "trunk",
            "unknown_unicast_blocked": False,
            "capture_mode": False,
            "private_vlan": {
                 "native_vlan_tagging": True,
                 "encapsulation": "dot1q",
                 "operational": "10 (VLAN0010) 100 (VLAN0100)",
                 "trunk_mappings": "10 (VLAN0010) 100 (VLAN0100)"
            },
            "encapsulation": {
                 "operational_encapsulation": "dot1q",
                 "native_vlan": "1",
                 "administrative_encapsulation": "dot1q"
            },
            "protected": False,
            "native_vlan_tagging": True,
            "negotiation_of_trunk": True,
            "capture_vlans": "all",
            "switchport_mode": "trunk"
       },
       "GigabitEthernet1/0/5": {
            "switchport_mode": "static access",
            "pruning_vlans": "2-1001",
            "switchport_enable": True,
            "trunk_vlans": "all",
            'operational_mode': 'down',
            "capture_mode": False,
            "private_vlan": {
                 "native_vlan_tagging": True,
                 "encapsulation": "dot1q"
            },
            "access_vlan": "1",
            "unknown_unicast_blocked": False,
            "native_vlan_tagging": True,
            "unknown_multicast_blocked": False,
            "protected": False,
            "negotiation_of_trunk": False,
            "capture_vlans": "all",
            "encapsulation": {
                 "native_vlan": "1",
                 "administrative_encapsulation": "dot1q"
            }
       },
       "Port-channel12": {
            "switchport_enable": True,
              "private_vlan": {
                   "encapsulation": "dot1q",
                   "native_vlan_tagging": True
              },
              "native_vlan_tagging": False,
              "negotiation_of_trunk": True,
              "unknown_unicast_blocked": False,
              "protected": False,
              "encapsulation": {
                   "administrative_encapsulation": "dot1q",
                   "native_vlan": "0"
              },
              "switchport_mode": "trunk",
              "unknown_multicast_blocked": False,
              "trunk_vlans": "100-110",
              "operational_mode": "down",
              "pruning_vlans": "2-1001",
              "port_channel": {
                   "port_channel_member": True,
                   "port_channel_member_intfs": [
                        "GigabitEthernet1/0/2"
                   ]
              }
         }
    }


    golden_output = {'execute.return_value': '''
        Name: Gi1/0/2
        Switchport: Enabled
        Administrative Mode: trunk
        Operational Mode: trunk (member of bundle Po12)
        Administrative Trunking Encapsulation: dot1q
        Operational Trunking Encapsulation: dot1q
        Negotiation of Trunking: On
        Access Mode VLAN: 1 (default)
        Trunking Native Mode VLAN: 1 (default)
        Administrative Native VLAN tagging: enabled
        Voice VLAN: none
        Administrative private-vlan host-association: none 
        Administrative private-vlan mapping: none 
        Administrative private-vlan trunk native VLAN: none
        Administrative private-vlan trunk Native VLAN tagging: enabled
        Administrative private-vlan trunk encapsulation: dot1q
        Administrative private-vlan trunk normal VLANs: none
        Administrative private-vlan trunk associations: none
        Administrative private-vlan trunk mappings:
          10 (VLAN0010) 100 (VLAN0100)
        Operational private-vlan:
          10 (VLAN0010) 100 (VLAN0100)
        Trunking VLANs Enabled: 100-110
        Pruning VLANs Enabled: 2-1001
        Capture Mode Disabled
        Capture VLANs Allowed: ALL

        Protected: false
        Unknown unicast blocked: disabled
        Unknown multicast blocked: disabled
        Appliance trust: none

        Name: Gi1/0/4
        Switchport: Enabled
        Administrative Mode: trunk
        Operational Mode: trunk
        Administrative Trunking Encapsulation: dot1q
        Operational Trunking Encapsulation: dot1q
        Negotiation of Trunking: On
        Access Mode VLAN: 1 (default)
        Trunking Native Mode VLAN: 1 (default)
        Administrative Native VLAN tagging: enabled
        Voice VLAN: none
        Administrative private-vlan host-association: none 
        Administrative private-vlan mapping: none 
        Administrative private-vlan trunk native VLAN: none
        Administrative private-vlan trunk Native VLAN tagging: enabled
        Administrative private-vlan trunk encapsulation: dot1q
        Administrative private-vlan trunk normal VLANs: none
        Administrative private-vlan trunk associations: none
        Administrative private-vlan trunk mappings: none
        Operational private-vlan: none
        Trunking VLANs Enabled: 200-211
        Pruning VLANs Enabled: 2-1001
        Capture Mode Disabled
        Capture VLANs Allowed: ALL

        Protected: false
        Unknown unicast blocked: disabled
        Unknown multicast blocked: disabled
        Appliance trust: none

        Name: Gi1/0/5
        Switchport: Enabled
        Administrative Mode: static access
        Operational Mode: down
        Administrative Trunking Encapsulation: dot1q
        Negotiation of Trunking: Off
        Access Mode VLAN: 1 (default)
        Trunking Native Mode VLAN: 1 (default)
        Administrative Native VLAN tagging: enabled
        Voice VLAN: none
        Administrative private-vlan host-association: none 
        Administrative private-vlan mapping: none 
        Administrative private-vlan trunk native VLAN: none
        Administrative private-vlan trunk Native VLAN tagging: enabled
        Administrative private-vlan trunk encapsulation: dot1q
        Administrative private-vlan trunk normal VLANs: none
        Administrative private-vlan trunk associations: none
        Administrative private-vlan trunk mappings: none
        Operational private-vlan: none
        Trunking VLANs Enabled: ALL
        Pruning VLANs Enabled: 2-1001
        Capture Mode Disabled
        Capture VLANs Allowed: ALL
                  
        Protected: false
        Unknown unicast blocked: disabled
        Unknown multicast blocked: disabled
        Appliance trust: none

        Name: Po12
        Switchport: Enabled
        Administrative Mode: trunk
        Operational Mode: down
        Administrative Trunking Encapsulation: dot1q
        Negotiation of Trunking: On
        Access Mode VLAN: unassigned
        Trunking Native Mode VLAN: 0 (Inactive)
        Administrative Native VLAN tagging: disabled
        Voice VLAN: none
        Administrative private-vlan host-association: none 
        Administrative private-vlan mapping: none 
        Administrative private-vlan trunk native VLAN: none
        Administrative private-vlan trunk Native VLAN tagging: enabled
        Administrative private-vlan trunk encapsulation: dot1q
        Administrative private-vlan trunk normal VLANs: none
        Administrative private-vlan trunk associations: none
        Administrative private-vlan trunk mappings: none
        Operational private-vlan: none
        Trunking VLANs Enabled: 100-110
        Pruning VLANs Enabled: 2-1001

        Protected: false
        Unknown unicast blocked: disabled
        Unknown multicast blocked: disabled
        Appliance trust: none
    '''}

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
# unitest For Show Interfaces
#############################################################################
class test_show_interfaces(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        "Port-channel12": {
            "flow_control": {
                 "send": False,
                 "receive": False
            },
            "type": "EtherChannel",
            "counters": {
                 "out_buffer_failure": 0,
                 "out_underruns": 0,
                 "in_giants": 0,
                 "in_throttles": 0,
                 "in_frame": 0,
                 "in_ignored": 0,
                 "last_clear": "1d23h",
                 "out_interface_resets": 2,
                 "in_mac_pause_frames": 0,
                 "out_collision": 0,
                 "rate": {
                      "out_rate_pkts": 0,
                      "load_interval": 300,
                      "out_rate": 0,
                      "in_rate": 2000,
                      "in_rate_pkts": 2
                 },
                 "in_watchdog": 0,
                 "out_deferred": 0,
                 "out_mac_pause_frames": 0,
                 "in_pkts": 961622,
                 "in_multicast_pkts": 4286699522,
                 "in_runts": 0,
                 "out_unknown_protocl_drops": 0,
                 "in_no_buffer": 0,
                 "out_buffers_swapped": 0,
                 "out_lost_carrier": 0,
                 "out_errors": 0,
                 "in_errors": 0,
                 "in_octets": 72614643,
                 "in_crc_errors": 0,
                 "out_no_carrier": 0,
                 "in_with_dribble": 0,
                 "in_broadcast_pkts": 944788,
                 "out_pkts": 39281,
                 "out_late_collision": 0,
                 "out_octets": 6235318,
                 "in_overrun": 0,
                 "out_babble": 0
            },
            "auto_negotiate": True,
            "phys_address": "0057.d228.1a02",
            "keepalive": 10,
            "output_hang": "never",
            "txload": "1/255",
            "oper_status": "up",
            "arp_type": "arpa",
            "rxload": "1/255",
            "duplex_mode": "full",
            "link_type": "auto",
            "queues": {
                 "input_queue_size": 0,
                 "total_output_drop": 0,
                 "input_queue_drops": 0,
                 "input_queue_max": 2000,
                 "output_queue_size": 0,
                 "input_queue_flushes": 0,
                 "output_queue_max": 0,
                 "queue_strategy": "fifo"
            },
            "encapsulations": {
                 "encapsulation": "qinq virtual lan",
                 "first_dot1q": "10",
                 "second_dot1q": "20",
            },
            "last_input": "never",
            "last_output": "1d22h",
            "line_protocol": "up",
            "mac_address": "0057.d228.1a02",
            "connected": True,
            "port_channel": {
                 "port_channel_member": True,
                 "port_channel_member_intfs": ['GigabitEthernet1/0/2'],
            },
            "arp_timeout": "04:00:00",
            "bandwidth": 1000000,
            "port_speed": "1000",
            "enabled": True,
            "mtu": 1500,
            "delay": 10,
            "reliability": "255/255"
       },
       "GigabitEthernet1/0/1": {
            "flow_control": {
                 "send": False,
                 "receive": False
            },
            "type": "Gigabit Ethernet",
            "counters": {
                 "out_buffer_failure": 0,
                 "out_underruns": 0,
                 "in_giants": 0,
                 "in_throttles": 0,
                 "in_frame": 0,
                 "in_ignored": 0,
                 "last_clear": "1d02h",
                 "out_interface_resets": 2,
                 "in_mac_pause_frames": 0,
                 "out_collision": 0,
                 "rate": {
                      "out_rate_pkts": 0,
                      "load_interval": 30,
                      "out_rate": 0,
                      "in_rate": 0,
                      "in_rate_pkts": 0
                 },
                 "in_watchdog": 0,
                 "out_deferred": 0,
                 "out_mac_pause_frames": 0,
                 "in_pkts": 12127,
                 "in_multicast_pkts": 4171,
                 "in_runts": 0,
                 "out_unknown_protocl_drops": 0,
                 "in_no_buffer": 0,
                 "out_buffers_swapped": 0,
                 "out_lost_carrier": 0,
                 "out_errors": 0,
                 "in_errors": 0,
                 "in_octets": 2297417,
                 "in_crc_errors": 0,
                 "out_no_carrier": 0,
                 "in_with_dribble": 0,
                 "in_broadcast_pkts": 0,
                 "out_pkts": 12229,
                 "out_late_collision": 0,
                 "out_octets": 2321107,
                 "in_overrun": 0,
                 "out_babble": 0
            },
            "phys_address": "0057.d228.1a64",
            "keepalive": 10,
            "output_hang": "never",
            "txload": "1/255",
            "description": "desc",
            "oper_status": "down",
            "arp_type": "arpa",
            "rxload": "1/255",
            "duplex_mode": "auto",
            "queues": {
                 "input_queue_size": 0,
                 "total_output_drop": 0,
                 "input_queue_drops": 0,
                 "input_queue_max": 375,
                 "output_queue_size": 0,
                 "input_queue_flushes": 0,
                 "output_queue_max": 40,
                 "queue_strategy": "fifo"
            },
            "ipv4": {
                 "10.1.1.1/24": {
                      "prefix_length": "24",
                      "ip": "10.1.1.1"
                 }
            },
            "encapsulations": {
                 "encapsulation": "arpa"
            },
            "last_input": "never",
            "last_output": "04:39:18",
            "line_protocol": "down",
            "mac_address": "0057.d228.1a64",
            "connected": False,
            "port_channel": {
                 "port_channel_member": False
            },
            "media_type": "10/100/1000BaseTX",
            "bandwidth": 768,
            "port_speed": "1000",
            "enabled": False,
            "arp_timeout": "04:00:00",
            "mtu": 1500,
            "delay": 3330,
            "reliability": "255/255"
       },
       "GigabitEthernet3": {
            "flow_control": {
                 "send": False,
                 "receive": False
            },
            "type": "CSR vNIC",
            'auto_negotiate': True,
            'duplex_mode': 'full',
            'link_type': 'auto',
            'media_type': 'RJ45',
            'port_speed': '1000',
            "counters": {
                 "out_buffer_failure": 0,
                 "out_underruns": 0,
                 "in_giants": 0,
                 "in_throttles": 0,
                 "in_frame": 0,
                 "in_ignored": 0,
                 "last_clear": "never",
                 "out_interface_resets": 1,
                 "in_mac_pause_frames": 0,
                 "out_collision": 0,
                 "in_crc_errors": 0,
                 "rate": {
                      "out_rate_pkts": 0,
                      "load_interval": 300,
                      "out_rate": 0,
                      "in_rate": 0,
                      "in_rate_pkts": 0
                 },
                 "in_watchdog": 0,
                 "out_deferred": 0,
                 "out_mac_pause_frames": 0,
                 "in_pkts": 6,
                 "in_multicast_pkts": 0,
                 "in_runts": 0,
                 "in_no_buffer": 0,
                 "out_buffers_swapped": 0,
                 "out_errors": 0,
                 "in_errors": 0,
                 "in_octets": 480,
                 "out_unknown_protocl_drops": 0,
                 "out_no_carrier": 0,
                 "out_lost_carrier": 0,
                 "in_broadcast_pkts": 0,
                 "out_pkts": 28,
                 "out_late_collision": 0,
                 "out_octets": 7820,
                 "in_overrun": 0,
                 "out_babble": 0
            },
            "phys_address": "5254.0072.9b0c",
            "keepalive": 10,
            "output_hang": "never",
            "txload": "1/255",
            "reliability": "255/255",
            "arp_type": "arpa",
            "rxload": "1/255",
            "queues": {
                 "input_queue_size": 0,
                 "total_output_drop": 0,
                 "input_queue_drops": 0,
                 "input_queue_max": 375,
                 "output_queue_size": 0,
                 "input_queue_flushes": 0,
                 "output_queue_max": 40,
                 "queue_strategy": "fifo"
            },
            "ipv4": {
                 "192.168.154.1/24": {
                      "prefix_length": "24",
                      "ip": "192.168.154.1"
                 },
                 "unnumbered": {
                      "interface_ref": "Loopback0"
                 }
            },
            "encapsulations": {
                 "encapsulation": "arpa"
            },
            "last_output": "00:00:27",
            "line_protocol": "up",
            "mac_address": "5254.0072.9b0c",
            "oper_status": "up",
            "port_channel": {
                 "port_channel_member": False
            },
            "arp_timeout": "04:00:00",
            "bandwidth": 1000000,
            "enabled": True,
            "mtu": 1500,
            "delay": 10,
            "last_input": "never"
       },
       "Loopback0": {
            "queues": {
                 "input_queue_size": 0,
                 "total_output_drop": 0,
                 "input_queue_drops": 0,
                 "input_queue_max": 75,
                 "output_queue_size": 0,
                 "input_queue_flushes": 0,
                 "output_queue_max": 0,
                 "queue_strategy": "fifo"
            },
            "mtu": 1514,
            "encapsulations": {
                 "encapsulation": "loopback"
            },
            "last_output": "never",
            "type": "Loopback",
            "line_protocol": "up",
            "oper_status": "up",
            "keepalive": 10,
            "output_hang": "never",
            "txload": "1/255",
            "counters": {
                 "out_buffer_failure": 0,
                 "out_underruns": 0,
                 "in_giants": 0,
                 "in_throttles": 0,
                 "in_frame": 0,
                 "in_ignored": 0,
                 "last_clear": "1d04h",
                 "out_interface_resets": 0,
                 "out_collision": 0,
                 "rate": {
                      "out_rate_pkts": 0,
                      "load_interval": 300,
                      "out_rate": 0,
                      "in_rate": 0,
                      "in_rate_pkts": 0
                 },
                 "in_pkts": 0,
                 "in_multicast_pkts": 0,
                 "in_runts": 0,
                 "in_no_buffer": 0,
                 "out_buffers_swapped": 0,
                 "out_errors": 0,
                 "in_errors": 0,
                 "in_octets": 0,
                 "in_crc_errors": 0,
                 "out_unknown_protocl_drops": 0,
                 "in_broadcast_pkts": 0,
                 "out_pkts": 72,
                 "out_octets": 5760,
                 "in_overrun": 0,
                 "in_abort": 0
            },
            "reliability": "255/255",
            "bandwidth": 8000000,
            "port_channel": {
                 "port_channel_member": False
            },
            "enabled": True,
            "ipv4": {
                 "192.168.154.1/24": {
                      "prefix_length": "24",
                      "ip": "192.168.154.1"
                 }
            },
            "rxload": "1/255",
            "delay": 5000,
            "last_input": "1d02h"
       },
       "Vlan100": {
            "type": "Ethernet SVI",
            "counters": {
                 "out_buffer_failure": 0,
                 "out_underruns": 0,
                 "in_giants": 0,
                 "in_throttles": 0,
                 "in_frame": 0,
                 "in_ignored": 0,
                 "last_clear": "1d04h",
                 "out_interface_resets": 0,
                 "rate": {
                      "out_rate_pkts": 0,
                      "load_interval": 300,
                      "out_rate": 0,
                      "in_rate": 0,
                      "in_rate_pkts": 0
                 },
                 "in_pkts": 50790,
                 "in_multicast_pkts": 0,
                 "in_runts": 0,
                 "in_no_buffer": 0,
                 "out_buffers_swapped": 0,
                 "out_errors": 0,
                 "in_errors": 0,
                 "in_octets": 3657594,
                 "in_crc_errors": 0,
                 "out_unknown_protocl_drops": 0,
                 "in_broadcast_pkts": 0,
                 "out_pkts": 72,
                 "out_octets": 5526,
                 "in_overrun": 0
            },
            "phys_address": "0057.d228.1a51",
            "queues": {
                 "input_queue_size": 0,
                 "total_output_drop": 0,
                 "input_queue_drops": 0,
                 "input_queue_max": 375,
                 "output_queue_size": 0,
                 "input_queue_flushes": 0,
                 "output_queue_max": 40,
                 "queue_strategy": "fifo"
            },
            "txload": "1/255",
            "reliability": "255/255",
            "arp_type": "arpa",
            "rxload": "1/255",
            "output_hang": "never",
            "ipv4": {
                 "192.168.234.1/24": {
                      "prefix_length": "24",
                      "ip": "192.168.234.1"
                 }
            },
            "encapsulations": {
                 "encapsulation": "arpa"
            },
            "last_output": "1d03h",
            "line_protocol": "up",
            "mac_address": "0057.d228.1a51",
            "oper_status": "up",
            "port_channel": {
                 "port_channel_member": False
            },
            "arp_timeout": "04:00:00",
            "bandwidth": 1000000,
            "enabled": True,
            "mtu": 1500,
            "delay": 10,
            "last_input": "never"
       },
       "GigabitEthernet1/0/2": {
            "flow_control": {
                 "send": False,
                 "receive": False
            },
            "type": "Gigabit Ethernet",
            "counters": {
                 "out_buffer_failure": 0,
                 "out_underruns": 0,
                 "in_giants": 0,
                 "in_throttles": 0,
                 "in_frame": 0,
                 "in_ignored": 0,
                 "last_clear": "1d02h",
                 "out_interface_resets": 5,
                 "in_mac_pause_frames": 0,
                 "out_collision": 0,
                 "rate": {
                      "out_rate_pkts": 0,
                      "load_interval": 300,
                      "out_rate": 0,
                      "in_rate": 3000,
                      "in_rate_pkts": 5
                 },
                 "in_watchdog": 0,
                 "out_deferred": 0,
                 "out_mac_pause_frames": 0,
                 "in_pkts": 545526,
                 "in_multicast_pkts": 535961,
                 "in_runts": 0,
                 "out_unknown_protocl_drops": 0,
                 "in_no_buffer": 0,
                 "out_buffers_swapped": 0,
                 "out_lost_carrier": 0,
                 "out_errors": 0,
                 "in_errors": 0,
                 "in_octets": 41210298,
                 "in_crc_errors": 0,
                 "out_no_carrier": 0,
                 "in_with_dribble": 0,
                 "in_broadcast_pkts": 535961,
                 "out_pkts": 23376,
                 "out_late_collision": 0,
                 "out_octets": 3642296,
                 "in_overrun": 0,
                 "out_babble": 0
            },
            "phys_address": "0057.d228.1a02",
            "keepalive": 10,
            "output_hang": "never",
            "txload": "1/255",
            "oper_status": "up",
            "arp_type": "arpa",
            "media_type": "10/100/1000BaseTX",
            "rxload": "1/255",
            "duplex_mode": "full",
            "queues": {
                 "input_queue_size": 0,
                 "total_output_drop": 0,
                 "input_queue_drops": 0,
                 "input_queue_max": 2000,
                 "output_queue_size": 0,
                 "input_queue_flushes": 0,
                 "output_queue_max": 40,
                 "queue_strategy": "fifo"
            },
            "encapsulations": {
                 "encapsulation": "arpa"
            },
            "last_input": "never",
            "last_output": "00:00:02",
            "line_protocol": "up",
            "mac_address": "0057.d228.1a02",
            "connected": True,
            "port_channel": {
                 "port_channel_member": True,
                 'port_channel_int': 'Port-channel12',
            },
            "arp_timeout": "04:00:00",
            "bandwidth": 1000000,
            "port_speed": "1000",
            "enabled": True,
            "mtu": 1500,
            "delay": 10,
            "reliability": "255/255"
       },
       "GigabitEthernet0/0/4": {
            "arp_timeout": "04:00:00",
            "arp_type": "arpa",
            "bandwidth": 1000000,
            "counters": {
                 "in_broadcast_pkts": 0,
                 "in_crc_errors": 0,
                 "in_errors": 0,
                 "in_frame": 0,
                 "in_giants": 0,
                 "in_ignored": 0,
                 "in_mac_pause_frames": 0,
                 "in_multicast_pkts": 0,
                 "in_no_buffer": 0,
                 "in_octets": 0,
                 "in_overrun": 0,
                 "in_pkts": 0,
                 "in_runts": 0,
                 "in_throttles": 0,
                 "in_watchdog": 0,
                 "last_clear": "never",
                 "out_babble": 0,
                 "out_collision": 0,
                 "out_deferred": 0,
                 "out_errors": 0,
                 "out_interface_resets": 1,
                 "out_late_collision": 0,
                 "out_lost_carrier": 0,
                 "out_mac_pause_frames": 0,
                 "out_no_carrier": 0,
                 "out_octets": 0,
                 "out_pkts": 0,
                 "out_underruns": 0,
                 "out_unknown_protocl_drops": 0,
                 "rate": {
                     "in_rate": 0,
                     "in_rate_pkts": 0,
                     "load_interval": 300,
                     "out_rate": 0,
                     "out_rate_pkts": 0
                 }
            },
            "delay": 10,
            "enabled": False,
            "encapsulations": {
                 "encapsulation": "arpa"
            },
            "flow_control": {
                 "receive": False, "send": False
            },
            "last_input": "never",
            "last_output": "never",
            "line_protocol": "down",
            "mac_address": "380e.4d6c.7006",
            "phys_address": "380e.4d6c.7006",
            "mtu": 1500,
            "oper_status": "down",
            "output_hang": "never",
            "port_channel": {
                 "port_channel_member": False
            },
            "queues": {
                 "input_queue_drops": 0,
                 "input_queue_flushes": 0,
                 "input_queue_max": 375,
                 "input_queue_size": 0,
                 "output_queue_max": 40,
                 "output_queue_size": 0,
                 "queue_strategy": "fifo",
                 "total_output_drop": 0
            },
            "reliability": "255/255",
            "rxload": "1/255",
            "txload": "1/255",
            "type": "BUILT-IN-2T+6X1GE"
       }

    }

    golden_output = {'execute.return_value': '''
        GigabitEthernet1/0/1 is administratively down, line protocol is down (disabled) 
          Hardware is Gigabit Ethernet, address is 0057.d228.1a64 (bia 0057.d228.1a64)
          Description: desc
          Internet address is 10.1.1.1/24
          MTU 1500 bytes, BW 768 Kbit/sec, DLY 3330 usec, 
             reliability 255/255, txload 1/255, rxload 1/255
          Encapsulation ARPA, loopback not set
          Keepalive set (10 sec)
          Auto-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
          input flow-control is off, output flow-control is unsupported 
          ARP type: ARPA, ARP Timeout 04:00:00
          Last input never, output 04:39:18, output hang never
          Last clearing of "show interface" counters 1d02h
          Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
          Queueing strategy: fifo
          Output queue: 0/40 (size/max)
          30 second input rate 0 bits/sec, 0 packets/sec
          30 second output rate 0 bits/sec, 0 packets/sec
             12127 packets input, 2297417 bytes, 0 no buffer
             Received 4173 broadcasts (0 IP multicasts)
             0 runts, 0 giants, 0 throttles 
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
             0 watchdog, 4171 multicast, 0 pause input
             0 input packets with dribble condition detected
             12229 packets output, 2321107 bytes, 0 underruns
             0 output errors, 0 collisions, 2 interface resets
             0 unknown protocol drops
             0 babbles, 0 late collision, 0 deferred
             0 lost carrier, 0 no carrier, 0 pause output
             0 output buffer failures, 0 output buffers swapped out
        GigabitEthernet1/0/2 is up, line protocol is up (connected) 
          Hardware is Gigabit Ethernet, address is 0057.d228.1a02 (bia 0057.d228.1a02)
          MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
             reliability 255/255, txload 1/255, rxload 1/255
          Encapsulation ARPA, loopback not set
          Keepalive set (10 sec)
          Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
          input flow-control is off, output flow-control is unsupported 
          ARP type: ARPA, ARP Timeout 04:00:00
          Last input never, output 00:00:02, output hang never
          Last clearing of "show interface" counters 1d02h
          Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
          Queueing strategy: fifo
          Output queue: 0/40 (size/max)
          5 minute input rate 3000 bits/sec, 5 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
             545526 packets input, 41210298 bytes, 0 no buffer
             Received 535996 broadcasts (535961 multicasts)
             0 runts, 0 giants, 0 throttles 
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
             0 watchdog, 535961 multicast, 0 pause input
             0 input packets with dribble condition detected
             23376 packets output, 3642296 bytes, 0 underruns
             0 output errors, 0 collisions, 5 interface resets
             0 unknown protocol drops
             0 babbles, 0 late collision, 0 deferred
             0 lost carrier, 0 no carrier, 0 pause output
             0 output buffer failures, 0 output buffers swapped out
        GigabitEthernet3 is up, line protocol is up 
          Hardware is CSR vNIC, address is 5254.0072.9b0c (bia 5254.0072.9b0c)
          Interface is unnumbered. Using address of Loopback0 (192.168.154.1)
          MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
             reliability 255/255, txload 1/255, rxload 1/255
          Encapsulation ARPA, loopback not set
         Keepalive set (10 sec)
          Full Duplex, 1000Mbps, link type is auto, media type is RJ45
          output flow-control is unsupported, input flow-control is unsupported
          ARP type: ARPA, ARP Timeout 04:00:00
          Last input never, output 00:00:27, output hang never
          Last clearing of "show interface" counters never
          Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
          Queueing strategy: fifo
          Output queue: 0/40 (size/max)
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
             6 packets input, 480 bytes, 0 no buffer
             Received 0 broadcasts (0 IP multicasts)
             0 runts, 0 giants, 0 throttles 
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
             0 watchdog, 0 multicast, 0 pause input
             28 packets output, 7820 bytes, 0 underruns
             0 output errors, 0 collisions, 1 interface resets
             0 unknown protocol drops
             0 babbles, 0 late collision, 0 deferred
             0 lost carrier, 0 no carrier, 0 pause output
             0 output buffer failures, 0 output buffers swapped out
        Loopback0 is up, line protocol is up 
          Hardware is Loopback
          Internet address is 192.168.154.1/24
          MTU 1514 bytes, BW 8000000 Kbit/sec, DLY 5000 usec, 
             reliability 255/255, txload 1/255, rxload 1/255
          Encapsulation LOOPBACK, loopback not set
          Keepalive set (10 sec)
          Last input 1d02h, output never, output hang never
          Last clearing of "show interface" counters 1d04h
          Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
          Queueing strategy: fifo
          Output queue: 0/0 (size/max)
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
             0 packets input, 0 bytes, 0 no buffer
             Received 0 broadcasts (0 IP multicasts)
             0 runts, 0 giants, 0 throttles 
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
             72 packets output, 5760 bytes, 0 underruns
             0 output errors, 0 collisions, 0 interface resets
             0 unknown protocol drops
             0 output buffer failures, 0 output buffers swapped out
        Vlan100 is up, line protocol is up 
          Hardware is Ethernet SVI, address is 0057.d228.1a51 (bia 0057.d228.1a51)
          Internet address is 192.168.234.1/24
          MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
             reliability 255/255, txload 1/255, rxload 1/255
          Encapsulation ARPA, loopback not set
          Keepalive not supported 
          ARP type: ARPA, ARP Timeout 04:00:00
          Last input never, output 1d03h, output hang never
          Last clearing of "show interface" counters 1d04h
          Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
          Queueing strategy: fifo
          Output queue: 0/40 (size/max)
          5 minute input rate 0 bits/sec, 0 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
             50790 packets input, 3657594 bytes, 0 no buffer
             Received 0 broadcasts (0 IP multicasts)
             0 runts, 0 giants, 0 throttles 
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
             72 packets output, 5526 bytes, 0 underruns
             0 output errors, 0 interface resets
             0 unknown protocol drops
             0 output buffer failures, 0 output buffers swapped out
        Port-channel12 is up, line protocol is up (connected) 
          Hardware is EtherChannel, address is 0057.d228.1a02 (bia 0057.d228.1a02)
          MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
             reliability 255/255, txload 1/255, rxload 1/255
          Encapsulation QinQ Virtual LAN, outer ID  10, inner ID 20
          Keepalive set (10 sec)
          Full-duplex, 1000Mb/s, link type is auto, media type is 
          input flow-control is off, output flow-control is unsupported 
          Members in this channel: Gi1/0/2 
          ARP type: ARPA, ARP Timeout 04:00:00
          Last input never, output 1d22h, output hang never
          Last clearing of "show interface" counters 1d23h
          Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
          Queueing strategy: fifo
          Output queue: 0/0 (size/max)
          5 minute input rate 2000 bits/sec, 2 packets/sec
          5 minute output rate 0 bits/sec, 0 packets/sec
             961622 packets input, 72614643 bytes, 0 no buffer
             Received 944818 broadcasts (944788 multicasts)
             0 runts, 0 giants, 0 throttles 
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
             0 watchdog, 4286699522 multicast, 0 pause input
             0 input packets with dribble condition detected
             39281 packets output, 6235318 bytes, 0 underruns
             0 output errors, 0 collisions, 2 interface resets
             0 unknown protocol drops
             0 babbles, 0 late collision, 0 deferred
             0 lost carrier, 0 no carrier, 0 pause output
             0 output buffer failures, 0 output buffers swapped out
        GigabitEthernet0/0/4 is administratively down, line protocol is down
          Hardware is BUILT-IN-2T+6X1GE, address is 380e.4d6c.7006 (bia 380e.4d6c.7006)
          MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec,
             reliability 255/255, txload 1/255, rxload 1/255
          Encapsulation ARPA, loopback not set
          Keepalive not supported
          Full Duplex, 1000Mbps, link type is auto, media type is unknown media type
          output flow-control is unsupported, input flow-control is unsupported
          ARP type: ARPA, ARP Timeout 04:00:00
          Last input never, output never, output hang never
          Last clearing of "show interface" counters never
          Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
             0 output errors, 0 collisions, 1 interface resets
             0 unknown protocol drops
             0 babbles, 0 late collision, 0 deferred
             0 lost carrier, 0 no carrier, 0 pause output

    '''}

    golden_interface_output = {'execute.return_value': '''
    CE1#show interfaces GigabitEthernet1
  GigabitEthernet1 is up, line protocol is up
  Hardware is CSR vNIC, address is 5e00.0001.0000 (bia 5e00.0001.0000)
  Internet address is 172.16.1.243/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec,
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full Duplex, 1000Mbps, link type is auto, media type is Virtual
  output flow-control is unsupported, input flow-control is unsupported
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:02, output 00:00:25, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 32000 bits/sec, 28 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     7658 packets input, 1125842 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     44 packets output, 4324 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out

    '''}

    golden_parsed_interface_output={
            "GigabitEthernet1": {
                "rxload": "1/255",
                "phys_address": "5e00.0001.0000",
                "flow_control": {
                    "send": False,
                    "receive": False
                },
                "arp_type": "arpa",
                "type": "CSR vNIC",
                "enabled": True,
                "media_type": "Virtual",
                "last_input": "00:00:02",
                "link_type": "auto",
                "last_output": "00:00:25",
                "counters": {
                    "in_errors": 0,
                    "in_frame": 0,
                    "in_watchdog": 0,
                    "out_babble": 0,
                    "in_overrun": 0,
                    "out_collision": 0,
                    "out_buffer_failure": 0,
                    "out_no_carrier": 0,
                    "in_runts": 0,
                    "out_late_collision": 0,
                    "in_mac_pause_frames": 0,
                    "out_underruns": 0,
                    "out_pkts": 44,
                    "in_ignored": 0,
                    "in_pkts": 7658,
                    "out_buffers_swapped": 0,
                    "out_interface_resets": 1,
                    "rate": {
                        "out_rate": 0,
                        "load_interval": 300,
                        "in_rate_pkts": 28,
                        "out_rate_pkts": 0,
                        "in_rate": 32000
                    },
                    "out_mac_pause_frames": 0,
                    "in_broadcast_pkts": 0,
                    "in_no_buffer": 0,
                    "out_deferred": 0,
                    "in_crc_errors": 0,
                    "out_octets": 4324,
                    "out_lost_carrier": 0,
                    "in_octets": 1125842,
                    "out_unknown_protocl_drops": 0,
                    "last_clear": "never",
                    "in_throttles": 0,
                    "in_multicast_pkts": 0,
                    "out_errors": 0,
                    "in_giants": 0
                },
                "keepalive": 10,
                "mtu": 1500,
                "delay": 10,
                "encapsulations": {
                    "encapsulation": "arpa"
                },
                "ipv4": {
                    "172.16.1.243/24": {
                        "ip": "172.16.1.243",
                        "prefix_length": "24"
                    }
                },
                "queues": {
                    "output_queue_size": 0,
                    "input_queue_size": 0,
                    "input_queue_flushes": 0,
                    "queue_strategy": "fifo",
                    "total_output_drop": 0,
                    "output_queue_max": 40,
                    "input_queue_drops": 0,
                    "input_queue_max": 375
                },
                "auto_negotiate": True,
                "line_protocol": "up",
                "oper_status": "up",
                "duplex_mode": "full",
                "bandwidth": 1000000,
                "arp_timeout": "04:00:00",
                "port_speed": "1000",
                "port_channel": {
                    "port_channel_member": False
                },
                "output_hang": "never",
                "txload": "1/255",
                "mac_address": "5e00.0001.0000",
                "reliability": "255/255"
            }
        }

    golden_output2 = {'execute.return_value': '''
show interfaces
Vlan1 is administratively down, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 1 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan15 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan101 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.205.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 29000 bits/sec, 50 packets/sec
  5 minute output rate 5000 bits/sec, 10 packets/sec
     3673498 packets input, 279750798 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     813812 packets output, 60257018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan102 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.106.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 29000 bits/sec, 40 packets/sec
  5 minute output rate 5000 bits/sec, 10 packets/sec
     3632279 packets input, 276659268 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     804940 packets output, 59536912 bytes, 0 underruns
     0 output errors, 7 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan103 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.9.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 29000 bits/sec, 50 packets/sec
  5 minute output rate 5000 bits/sec, 10 packets/sec
     3673834 packets input, 279772748 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     813848 packets output, 60159890 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan104 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.169.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 30000 bits/sec, 50 packets/sec
  5 minute output rate 5000 bits/sec, 10 packets/sec
     3673653 packets input, 279762130 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     813767 packets output, 60155916 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan105 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.76.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 29000 bits/sec, 50 packets/sec
  5 minute output rate 5000 bits/sec, 10 packets/sec
     3673610 packets input, 279756472 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     813890 packets output, 60162584 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan106 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.240.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 30000 bits/sec, 51 packets/sec
  5 minute output rate 6000 bits/sec, 11 packets/sec
     3673779 packets input, 279773894 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     813865 packets output, 60163538 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan107 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.151.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 30000 bits/sec, 51 packets/sec
  5 minute output rate 6000 bits/sec, 11 packets/sec
     3673882 packets input, 279781700 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     813903 packets output, 60165230 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan108 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.64.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 31000 bits/sec, 51 packets/sec
  5 minute output rate 6000 bits/sec, 11 packets/sec
     3673638 packets input, 279766630 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     813842 packets output, 60162384 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan109 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.234.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 30000 bits/sec, 51 packets/sec
  5 minute output rate 6000 bits/sec, 11 packets/sec
     3673894 packets input, 279781274 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     817800 packets output, 62192557 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan110 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.151.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 31000 bits/sec, 51 packets/sec
  5 minute output rate 6000 bits/sec, 11 packets/sec
     3674136 packets input, 279796126 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     813960 packets output, 60168004 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan111 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.70.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 31000 bits/sec, 51 packets/sec
  5 minute output rate 6000 bits/sec, 11 packets/sec
     3673792 packets input, 279763870 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     822081 packets output, 60848654 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan112 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.246.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 30000 bits/sec, 51 packets/sec
  5 minute output rate 6000 bits/sec, 11 packets/sec
     3673848 packets input, 279779396 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     813978 packets output, 60170234 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan113 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.169.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 31000 bits/sec, 51 packets/sec
  5 minute output rate 6000 bits/sec, 11 packets/sec
     3674092 packets input, 279792690 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     813962 packets output, 60168782 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan114 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.94.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 30000 bits/sec, 51 packets/sec
  5 minute output rate 6000 bits/sec, 11 packets/sec
     3674118 packets input, 279801252 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     813964 packets output, 60167610 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan115 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.21.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 31000 bits/sec, 52 packets/sec
  5 minute output rate 6000 bits/sec, 11 packets/sec
     3688257 packets input, 280917432 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     813950 packets output, 60167218 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan116 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.205.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 30000 bits/sec, 50 packets/sec
  5 minute output rate 6000 bits/sec, 11 packets/sec
     3674429 packets input, 279815742 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     816877 packets output, 60383316 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan117 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.136.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 30000 bits/sec, 50 packets/sec
  5 minute output rate 6000 bits/sec, 11 packets/sec
     3674114 packets input, 279794536 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     814083 packets output, 60178182 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan118 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.69.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 31000 bits/sec, 51 packets/sec
  5 minute output rate 6000 bits/sec, 11 packets/sec
     3674811 packets input, 279845876 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     813994 packets output, 60171406 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan119 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.4.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 30000 bits/sec, 51 packets/sec
  5 minute output rate 6000 bits/sec, 11 packets/sec
     3691322 packets input, 281116276 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     814073 packets output, 60175212 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan120 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.196.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 30000 bits/sec, 50 packets/sec
  5 minute output rate 6000 bits/sec, 11 packets/sec
     3673948 packets input, 279785038 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     813996 packets output, 60171120 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan121 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.135.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:20, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan122 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.76.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:20, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan123 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.19.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:20, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan124 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.219.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:20, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan125 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.166.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:24, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan126 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.115.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:24, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan127 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.66.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:24, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan128 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.19.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:28, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan129 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.229.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:28, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan130 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.186.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:28, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan131 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.145.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:28, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan132 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.106.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:32, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan133 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.69.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:32, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan134 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.34.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:32, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan135 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.1.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:32, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan136 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.225.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:37, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan137 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.196.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:37, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan138 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.169.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:37, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan139 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.144.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:41, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan140 is up, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.121.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 06:39:41, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     163 packets output, 14018 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/0 is up, line protocol is up 
  Hardware is RP management port, address is 70b3.1760.0500 (bia 70b3.1760.0500)
  Internet address is 10.9.1.20/16
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full Duplex, 1000Mbps, link type is auto, media type is RJ45
  output flow-control is unsupported, input flow-control is unsupported
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:15, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 818000 bits/sec, 675 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     10341900 packets input, 2319228471 bytes, 0 no buffer
     Received 420554 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     8840 packets output, 993196 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/1 is down, line protocol is down (notconnect) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0500 (bia 70b3.1760.0500)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:20
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/2 is up, line protocol is up (connected) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0501 (bia 70b3.1760.0501)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 40Gb/s, link type is force-up, media type is QSFP 40G SR4 SFP
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:03, output hang never
  Last clearing of "show interface" counters 20:01:24
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 293000 bits/sec, 454 packets/sec
  5 minute output rate 58000 bits/sec, 104 packets/sec
     32521304 packets input, 2684387777 bytes, 0 no buffer
     Received 1481610 broadcasts (1476582 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1476582 multicast, 0 pause input
     0 input packets with dribble condition detected
     7498024 packets output, 525513005 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     2 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/3 is down, line protocol is down (notconnect) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0502 (bia 70b3.1760.0502)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:24
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/4 is up, line protocol is up (connected) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0503 (bia 70b3.1760.0503)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 40Gb/s, link type is force-up, media type is QSFP 40G SR BD SFP
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:15, output 00:00:03, output hang never
  Last clearing of "show interface" counters 20:01:24
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 102000 bits/sec, 186 packets/sec
  5 minute output rate 329000 bits/sec, 524 packets/sec
     13376239 packets input, 910225278 bytes, 0 no buffer
     Received 6304 broadcasts (6304 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 6304 multicast, 0 pause input
     0 input packets with dribble condition detected
     37674953 packets output, 3020267756 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/5 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0504 (bia 70b3.1760.0504)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:28
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/6 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0505 (bia 70b3.1760.0505)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:28
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/7 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0506 (bia 70b3.1760.0506)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:33
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/8 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0507 (bia 70b3.1760.0507)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:33
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/9 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0508 (bia 70b3.1760.0508)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:33
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/10 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0509 (bia 70b3.1760.0509)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:37
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/11 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.050a (bia 70b3.1760.050a)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:37
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/12 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.050b (bia 70b3.1760.050b)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:37
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/13 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.050c (bia 70b3.1760.050c)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:41
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/14 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.050d (bia 70b3.1760.050d)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:41
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/15 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.050e (bia 70b3.1760.050e)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:41
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/16 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.050f (bia 70b3.1760.050f)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:45
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/17 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0510 (bia 70b3.1760.0510)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:45
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/18 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0511 (bia 70b3.1760.0511)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:45
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/19 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0512 (bia 70b3.1760.0512)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:50
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/20 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0513 (bia 70b3.1760.0513)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:50
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/21 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0514 (bia 70b3.1760.0514)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:50
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/22 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0515 (bia 70b3.1760.0515)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:54
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/23 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0516 (bia 70b3.1760.0516)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:54
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/24 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0517 (bia 70b3.1760.0517)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:54
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/25 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0518 (bia 70b3.1760.0518)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:58
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/26 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.0519 (bia 70b3.1760.0519)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:58
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/27 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.051a (bia 70b3.1760.051a)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:01:58
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/28 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.051b (bia 70b3.1760.051b)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:02
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/29 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.051c (bia 70b3.1760.051c)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:02
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/30 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.051d (bia 70b3.1760.051d)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:02
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/31 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.051e (bia 70b3.1760.051e)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:07
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/0/32 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 70b3.1760.051f (bia 70b3.1760.051f)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:07
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/33 is down, line protocol is down (inactive) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.0520 (bia 70b3.1760.0520)
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:07
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/34 is down, line protocol is down (inactive) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.0521 (bia 70b3.1760.0521)
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:11
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/35 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Description: connected to Ixia 1/6
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  1., loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Gb/s, link type is force-up, media type is QSFP 100G SR4
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:18, output 00:00:00, output hang never
  Last clearing of "show interface" counters 20:02:11
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 25000 bits/sec, 15 packets/sec
     550971 packets input, 121771829 bytes, 0 no buffer
     Received 172754 broadcasts (0 IP multicasts)
     0 runts, 206 giants, 0 throttles 
     206 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 172604 multicast, 0 pause input
     0 input packets with dribble condition detected
     1536769 packets output, 437624881 bytes, 0 underruns
     0 output errors, 0 collisions, 33 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/35.1 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.19.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  501.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13266 packets input, 2503842 bytes
     13769 packets output, 2168924 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.2 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.76.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  502.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13254 packets input, 2501935 bytes
     13784 packets output, 2170079 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.3 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.135.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  503.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13281 packets input, 2505791 bytes
     13764 packets output, 2169079 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.4 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.196.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  504.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13273 packets input, 2500301 bytes
     13766 packets output, 2168845 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.5 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.4.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  505.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13253 packets input, 2497502 bytes
     13750 packets output, 2167640 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.6 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.69.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  506.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13261 packets input, 2502193 bytes
     13744 packets output, 2167636 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.7 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.136.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  507.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13350 packets input, 2513375 bytes
     13781 packets output, 2169851 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.8 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.205.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  508.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13292 packets input, 2510082 bytes
     13777 packets output, 2169702 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.9 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.21.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  509.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13332 packets input, 2511802 bytes
     13770 packets output, 2169056 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.10 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.94.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  510.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13282 packets input, 2502910 bytes
     13777 packets output, 2168425 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.11 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.169.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  511.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13281 packets input, 2501618 bytes
     13756 packets output, 2168163 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.12 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.246.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  512.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13255 packets input, 2502717 bytes
     13765 packets output, 2168956 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.13 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.70.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  513.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13266 packets input, 2502358 bytes
     13773 packets output, 2169451 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.14 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.151.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  514.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13347 packets input, 2513180 bytes
     13794 packets output, 2171050 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.15 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.234.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  515.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13260 packets input, 2497442 bytes
     13787 packets output, 2169487 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.16 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.64.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  516.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13336 packets input, 2512146 bytes
     13773 packets output, 2169512 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.17 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.151.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  517.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13287 packets input, 2505612 bytes
     13796 packets output, 2170930 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.18 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.240.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  518.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13263 packets input, 2502019 bytes
     13780 packets output, 2169941 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.19 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.76.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  519.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13353 packets input, 2509614 bytes
     13787 packets output, 2170375 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.20 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.169.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  520.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     13280 packets input, 2504934 bytes
     13772 packets output, 2169331 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.101 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.9.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  101.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     25478 packets input, 2598532 bytes
     0 packets output, 0 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.102 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.106.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  102.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     25477 packets input, 2598430 bytes
     0 packets output, 0 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.103 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.205.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  103.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     25479 packets input, 2598634 bytes
     0 packets output, 0 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.104 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.51.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  104.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     25479 packets input, 2598634 bytes
     0 packets output, 0 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.105 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.154.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  105.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     25477 packets input, 2598430 bytes
     0 packets output, 0 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.106 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.4.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  106.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     25479 packets input, 2598634 bytes
     0 packets output, 0 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.107 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.111.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  107.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     25476 packets input, 2598344 bytes
     0 packets output, 0 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.108 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.220.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  108.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     25478 packets input, 2598532 bytes
     0 packets output, 0 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.109 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.76.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  109.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     25478 packets input, 2598532 bytes
     0 packets output, 0 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/35.110 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.189.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  110.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     25478 packets input, 2598532 bytes
     0 packets output, 0 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/36 is down, line protocol is down (notconnect) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.0523 (bia 70b3.1760.0523)
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:32
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/37 is down, line protocol is down (notconnect) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.0524 (bia 70b3.1760.0524)
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:32
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/38 is down, line protocol is down (notconnect) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.0525 (bia 70b3.1760.0525)
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:32
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/39 is down, line protocol is down (notconnect) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.0526 (bia 70b3.1760.0526)
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:37
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/40 is down, line protocol is down (notconnect) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.0527 (bia 70b3.1760.0527)
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:37
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/41 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.4.2/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Gb/s, link type is force-up, media type is QSFP 100G SR4
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output 00:00:00, output hang never
  Last clearing of "show interface" counters 20:02:37
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  30 second input rate 39000 bits/sec, 50 packets/sec
  30 second output rate 35000 bits/sec, 48 packets/sec
     3581103 packets input, 340490834 bytes, 0 no buffer
     Received 20250 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 20089 multicast, 0 pause input
     0 input packets with dribble condition detected
     3494815 packets output, 323841840 bytes, 0 underruns
     0 output errors, 0 collisions, 5 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/42 is down, line protocol is down (notconnect) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.0529 (bia 70b3.1760.0529)
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:41
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/43 is down, line protocol is down (notconnect) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.052a (bia 70b3.1760.052a)
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:41
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/44 is down, line protocol is down (notconnect) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.052b (bia 70b3.1760.052b)
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:41
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/45 is down, line protocol is down (notconnect) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.052c (bia 70b3.1760.052c)
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:45
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/46 is down, line protocol is down (notconnect) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.052d (bia 70b3.1760.052d)
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:45
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/47 is down, line protocol is down (notconnect) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.052e (bia 70b3.1760.052e)
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:02:45
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/48 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 172.16.94.2/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  1., loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Gb/s, link type is force-up, media type is QSFP 100G SR4
  Fec is auto
  input flow-control is on, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters 20:02:49
  Input queue: 3/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  30 second input rate 330000 bits/sec, 550 packets/sec
  30 second output rate 301000 bits/sec, 547 packets/sec
     39665255 packets input, 3012714995 bytes, 0 no buffer
     Received 548242 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 548066 multicast, 0 pause input
     0 input packets with dribble condition detected
     39424533 packets output, 2729787452 bytes, 0 underruns
     0 output errors, 0 collisions, 16 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
HundredGigE1/0/48.1 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.51.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  201.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     3426695 packets input, 222402380 bytes
     1729535 packets output, 112615606 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/48.2 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.205.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  202.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     3430077 packets input, 222808882 bytes
     1733061 packets output, 113033370 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/48.3 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.106.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  203.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     3426685 packets input, 222402736 bytes
     1729514 packets output, 112614680 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/48.4 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.9.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  204.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     3426926 packets input, 222417026 bytes
     1729722 packets output, 112627684 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/48.5 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.169.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  205.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     3426916 packets input, 222416748 bytes
     1729694 packets output, 112626186 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/48.6 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.76.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  206.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     3427206 packets input, 222434908 bytes
     1729813 packets output, 112633620 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/48.7 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.240.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  207.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     3426971 packets input, 222419906 bytes
     1729823 packets output, 112634178 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/48.8 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.151.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  208.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     3426971 packets input, 222419256 bytes
     1729821 packets output, 112634398 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/48.9 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.64.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  209.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     3426848 packets input, 222412094 bytes
     1729707 packets output, 112626654 bytes
  Last clearing of "show interface" counters never
HundredGigE1/0/48.10 is up, line protocol is up (connected) 
  Hardware is Hundred Gigabit Ethernet, address is 70b3.1760.059f (bia 70b3.1760.059f)
  Internet address is 192.168.234.1/24
  MTU 1500 bytes, BW 100000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  210.
  ARP type: ARPA, ARP Timeout 04:00:00
  Keepalive set (10 sec)
     3427137 packets input, 222430124 bytes
     1729798 packets output, 112632450 bytes
  Last clearing of "show interface" counters never
Bluetooth0/4 is administratively down, line protocol is down 
  Hardware is BT management port, address is 70b3.1760.0500 (bia 70b3.1760.0500)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Unknown, Unknown, link type is auto, media type is RJ45
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
     1 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
Port-channel2 is up, line protocol is up (connected) 
  Hardware is EtherChannel, address is 70b3.1760.0501 (bia 70b3.1760.0501)
  MTU 1500 bytes, BW 80000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 40Gb/s, link type is force-up, media type is N/A
  input flow-control is on, output flow-control is unsupported 
  Members in this channel: Fo1/0/2 Fo1/0/4 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:04:37, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 389000 bits/sec, 630 packets/sec
  5 minute output rate 385000 bits/sec, 622 packets/sec
     45955737 packets input, 3599101746 bytes, 0 no buffer
     Received 1489774 broadcasts (1484746 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1484746 multicast, 0 pause input
     0 input packets with dribble condition detected
     45228880 packets output, 3550088514 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
Loopback1 is up, line protocol is up 
  Hardware is Loopback
  Internet address is 192.168.154.1/32
  MTU 1514 bytes, BW 8000000 Kbit/sec, DLY 5000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation LOOPBACK, loopback not set
  Keepalive set (10 sec)
  Last input 00:00:43, output never, output hang never
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
     1383 packets output, 33608 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     1375 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Loopback10 is up, line protocol is up 
  Hardware is Loopback
  MTU 1514 bytes, BW 8000000 Kbit/sec, DLY 5000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation LOOPBACK, loopback not set
  Keepalive set (10 sec)
  Last input never, output never, output hang never
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
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Loopback101 is up, line protocol is up 
  Hardware is Loopback
  Internet address is 10.204.1.2/32
  MTU 1514 bytes, BW 8000000 Kbit/sec, DLY 5000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation LOOPBACK, loopback not set
  Keepalive set (10 sec)
  Last input 00:00:22, output never, output hang never
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
     1338 packets output, 159232 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Loopback102 is up, line protocol is up 
  Hardware is Loopback
  Internet address is 10.154.1.2/32
  MTU 1514 bytes, BW 8000000 Kbit/sec, DLY 5000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation LOOPBACK, loopback not set
  Keepalive set (10 sec)
  Last input 00:00:16, output never, output hang never
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
     1343 packets output, 160112 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Tunnel0 is up, line protocol is up 
  Hardware is Tunnel
  Description: Pim Register Tunnel (Encap) for Embedded RP
  MTU 1452 bytes, BW 100 Kbit/sec, DLY 50000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation TUNNEL, loopback not set
  Keepalive not set
  Tunnel linestate evaluation up
  Tunnel source 191:168:101:2::1 (Vlan102), destination ::
   Tunnel Subblocks:
      src-track:
         Tunnel0 source tracking subblock associated with Vlan102
          Set of tunnels with source Vlan102, 1 member (includes iterators), on interface <OK>
  Tunnel protocol/transport PIM/IPv6
  Tunnel TTL 65
  Tunnel transport MTU 1452 bytes
  Tunnel is transmit only
  Tunnel transmit bandwidth 8000 (kbps)
  Tunnel receive bandwidth 8000 (kbps)
  Last input never, output never, output hang never
  Last clearing of "show interface" counters 20:03:05
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
Tunnel1 is up, line protocol is up 
  Hardware is Tunnel
  Internet address is 172.16.25.1/24
  MTU 17868 bytes, BW 100 Kbit/sec, DLY 50000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation TUNNEL, loopback not set
  Keepalive not set
  Tunnel linestate evaluation up
  Tunnel source 10.154.1.2 (Loopback102), destination 10.154.1.1
   Tunnel Subblocks:
      src-track:
         Tunnel1 source tracking subblock associated with Loopback102
          Set of tunnels with source Loopback102, 10 members (includes iterators), on interface <OK>
  Tunnel protocol/transport GRE/IP
    Key disabled, sequencing disabled
    Checksumming of packets disabled
  Tunnel TTL 255, Fast tunneling enabled
  Tunnel transport MTU 1476 bytes
  Tunnel transmit bandwidth 8000 (kbps)
  Tunnel receive bandwidth 8000 (kbps)
  Last input never, output 00:00:00, output hang never
  Last clearing of "show interface" counters 20:03:11
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 11176
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     27765 packets output, 2695512 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Tunnel2 is up, line protocol is up 
  Hardware is Tunnel
  Internet address is 172.16.121.1/24
  MTU 17868 bytes, BW 100 Kbit/sec, DLY 50000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation TUNNEL, loopback not set
  Keepalive not set
  Tunnel linestate evaluation up
  Tunnel source 10.154.1.2 (Loopback102), destination 10.154.1.1
   Tunnel Subblocks:
      src-track:
         Tunnel2 source tracking subblock associated with Loopback102
          Set of tunnels with source Loopback102, 10 members (includes iterators), on interface <OK>
  Tunnel protocol/transport GRE/IP
    Key disabled, sequencing disabled
    Checksumming of packets disabled
  Tunnel TTL 255, Fast tunneling enabled
  Tunnel transport MTU 1476 bytes
  Tunnel transmit bandwidth 8000 (kbps)
  Tunnel receive bandwidth 8000 (kbps)
  Last input never, output 00:00:04, output hang never
  Last clearing of "show interface" counters 20:03:11
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 11178
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     27789 packets output, 2697642 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Tunnel3 is up, line protocol is up 
  Hardware is Tunnel
  Internet address is 172.16.219.1/24
  MTU 17868 bytes, BW 100 Kbit/sec, DLY 50000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation TUNNEL, loopback not set
  Keepalive not set
  Tunnel linestate evaluation up
  Tunnel source 10.154.1.2 (Loopback102), destination 10.154.1.1
   Tunnel Subblocks:
      src-track:
         Tunnel3 source tracking subblock associated with Loopback102
          Set of tunnels with source Loopback102, 10 members (includes iterators), on interface <OK>
  Tunnel protocol/transport GRE/IP
    Key disabled, sequencing disabled
    Checksumming of packets disabled
  Tunnel TTL 255, Fast tunneling enabled
  Tunnel transport MTU 1476 bytes
  Tunnel transmit bandwidth 8000 (kbps)
  Tunnel receive bandwidth 8000 (kbps)
  Last input never, output 00:00:01, output hang never
  Last clearing of "show interface" counters 20:03:11
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 11179
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     27780 packets output, 2696882 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Tunnel4 is up, line protocol is up 
  Hardware is Tunnel
  Internet address is 172.16.64.1/24
  MTU 17868 bytes, BW 100 Kbit/sec, DLY 50000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation TUNNEL, loopback not set
  Keepalive not set
  Tunnel linestate evaluation up
  Tunnel source 10.154.1.2 (Loopback102), destination 10.154.1.1
   Tunnel Subblocks:
      src-track:
         Tunnel4 source tracking subblock associated with Loopback102
          Set of tunnels with source Loopback102, 10 members (includes iterators), on interface <OK>
  Tunnel protocol/transport GRE/IP
    Key disabled, sequencing disabled
    Checksumming of packets disabled
  Tunnel TTL 255, Fast tunneling enabled
  Tunnel transport MTU 1476 bytes
  Tunnel transmit bandwidth 8000 (kbps)
  Tunnel receive bandwidth 8000 (kbps)
  Last input never, output 00:00:01, output hang never
  Last clearing of "show interface" counters 20:03:15
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 11180
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     27765 packets output, 2695606 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Tunnel5 is up, line protocol is up 
  Hardware is Tunnel
  Internet address is 172.16.166.1/24
  MTU 17868 bytes, BW 100 Kbit/sec, DLY 50000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation TUNNEL, loopback not set
  Keepalive not set
  Tunnel linestate evaluation up
  Tunnel source 10.154.1.2 (Loopback102), destination 10.154.1.1
   Tunnel Subblocks:
      src-track:
         Tunnel5 source tracking subblock associated with Loopback102
          Set of tunnels with source Loopback102, 10 members (includes iterators), on interface <OK>
  Tunnel protocol/transport GRE/IP
    Key disabled, sequencing disabled
    Checksumming of packets disabled
  Tunnel TTL 255, Fast tunneling enabled
  Tunnel transport MTU 1476 bytes
  Tunnel transmit bandwidth 8000 (kbps)
  Tunnel receive bandwidth 8000 (kbps)
  Last input never, output 00:00:01, output hang never
  Last clearing of "show interface" counters 20:03:15
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 11176
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     27769 packets output, 2695894 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Tunnel6 is up, line protocol is up 
  Hardware is Tunnel
  Internet address is 172.16.15.1/24
  MTU 17868 bytes, BW 100 Kbit/sec, DLY 50000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation TUNNEL, loopback not set
  Keepalive not set
  Tunnel linestate evaluation up
  Tunnel source 10.154.1.2 (Loopback102), destination 10.154.1.1
   Tunnel Subblocks:
      src-track:
         Tunnel6 source tracking subblock associated with Loopback102
          Set of tunnels with source Loopback102, 10 members (includes iterators), on interface <OK>
  Tunnel protocol/transport GRE/IP
    Key disabled, sequencing disabled
    Checksumming of packets disabled
  Tunnel TTL 255, Fast tunneling enabled
  Tunnel transport MTU 1476 bytes
  Tunnel transmit bandwidth 8000 (kbps)
  Tunnel receive bandwidth 8000 (kbps)
  Last input never, output 00:00:02, output hang never
  Last clearing of "show interface" counters 20:03:19
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 11172
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     27752 packets output, 2694338 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Tunnel7 is up, line protocol is up 
  Hardware is Tunnel
  Internet address is 172.16.121.1/24
  MTU 17868 bytes, BW 100 Kbit/sec, DLY 50000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation TUNNEL, loopback not set
  Keepalive not set
  Tunnel linestate evaluation up
  Tunnel source 10.154.1.2 (Loopback102), destination 10.154.1.1
   Tunnel Subblocks:
      src-track:
         Tunnel7 source tracking subblock associated with Loopback102
          Set of tunnels with source Loopback102, 10 members (includes iterators), on interface <OK>
  Tunnel protocol/transport GRE/IP
    Key disabled, sequencing disabled
    Checksumming of packets disabled
  Tunnel TTL 255, Fast tunneling enabled
  Tunnel transport MTU 1476 bytes
  Tunnel transmit bandwidth 8000 (kbps)
  Tunnel receive bandwidth 8000 (kbps)
  Last input never, output 00:00:02, output hang never
  Last clearing of "show interface" counters 20:03:19
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 11176
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     27778 packets output, 2696668 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Tunnel8 is up, line protocol is up 
  Hardware is Tunnel
  Internet address is 172.16.229.1/24
  MTU 17868 bytes, BW 100 Kbit/sec, DLY 50000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation TUNNEL, loopback not set
  Keepalive not set
  Tunnel linestate evaluation up
  Tunnel source 10.154.1.2 (Loopback102), destination 10.154.1.1
   Tunnel Subblocks:
      src-track:
         Tunnel8 source tracking subblock associated with Loopback102
          Set of tunnels with source Loopback102, 10 members (includes iterators), on interface <OK>
  Tunnel protocol/transport GRE/IP
    Key disabled, sequencing disabled
    Checksumming of packets disabled
  Tunnel TTL 255, Fast tunneling enabled
  Tunnel transport MTU 1476 bytes
  Tunnel transmit bandwidth 8000 (kbps)
  Tunnel receive bandwidth 8000 (kbps)
  Last input never, output 00:00:02, output hang never
  Last clearing of "show interface" counters 20:03:19
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 11176
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     27756 packets output, 2694776 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Tunnel9 is up, line protocol is up 
  Hardware is Tunnel
  Internet address is 172.16.84.1/24
  MTU 17868 bytes, BW 100 Kbit/sec, DLY 50000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation TUNNEL, loopback not set
  Keepalive not set
  Tunnel linestate evaluation up
  Tunnel source 10.154.1.2 (Loopback102), destination 10.154.1.1
   Tunnel Subblocks:
      src-track:
         Tunnel9 source tracking subblock associated with Loopback102
          Set of tunnels with source Loopback102, 10 members (includes iterators), on interface <OK>
  Tunnel protocol/transport GRE/IP
    Key disabled, sequencing disabled
    Checksumming of packets disabled
  Tunnel TTL 255, Fast tunneling enabled
  Tunnel transport MTU 1476 bytes
  Tunnel transmit bandwidth 8000 (kbps)
  Tunnel receive bandwidth 8000 (kbps)
  Last input never, output 00:00:00, output hang never
  Last clearing of "show interface" counters 20:03:23
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 11176
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     27775 packets output, 2696372 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Tunnel10 is up, line protocol is up 
  Hardware is Tunnel
  Internet address is 172.16.186.1/24
  MTU 17868 bytes, BW 100 Kbit/sec, DLY 50000 usec, 
     reliability 255/255, txload 40/255, rxload 135/255
  Encapsulation TUNNEL, loopback not set
  Keepalive not set
  Tunnel linestate evaluation up
  Tunnel source 10.154.1.2 (Loopback102), destination 10.154.1.1
   Tunnel Subblocks:
      src-track:
         Tunnel10 source tracking subblock associated with Loopback102
          Set of tunnels with source Loopback102, 10 members (includes iterators), on interface <OK>
  Tunnel protocol/transport GRE/IP
    Key disabled, sequencing disabled
    Checksumming of packets disabled
  Tunnel TTL 255, Fast tunneling enabled
  Tunnel transport MTU 1476 bytes
  Tunnel transmit bandwidth 8000 (kbps)
  Tunnel receive bandwidth 8000 (kbps)
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters 20:03:23
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 34678
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 53000 bits/sec, 94 packets/sec
  5 minute output rate 16000 bits/sec, 23 packets/sec
     6832599 packets input, 479845002 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     1674895 packets output, 151072685 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
    '''
}
    golden_parsed_output2={
'Tunnel8': {
    'bandwidth': 100,
    'output_hang': 'never',
    'last_input': 'never',
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 11176,
        'output_queue_max': 0,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'type': 'Tunnel',
    'oper_status': 'up',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 2694776,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': '20:03:19',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'in_abort': 0,
        'out_pkts': 27756,
        },
    'rxload': '1/255',
    'ipv4': {
        '172.16.229.1/24': {
            'ip': '172.16.229.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'tunnel',
        },
    'delay': 50000,
    'txload': '1/255',
    'line_protocol': 'up',
    'reliability': '255/255',
    'enabled': True,
    'mtu': 17868,
    'last_output': '00:00:02',
    },
'HundredGigE1/0/35.9': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.21.1/24': {
            'ip': '172.16.21.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'HundredGigE1/0/43': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Hundred Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.052a',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:41',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.052a',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/35.12': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.246.1/24': {
            'ip': '172.16.246.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Vlan138': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.169.1/24': {
            'ip': '172.16.169.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:37',
    },
'FortyGigabitEthernet1/0/31': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.051e',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:07',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.051e',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'FortyGigabitEthernet1/0/21': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0514',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:50',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0514',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'Vlan113': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 51,
            'load_interval': 300,
            'in_rate': 31000,
            'out_rate_pkts': 11,
            'out_rate': 6000,
            },
        'in_octets': 279792690,
        'in_giants': 0,
        'in_pkts': 3674092,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60168782,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 813962,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.169.1/24': {
            'ip': '172.16.169.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'HundredGigE1/0/34': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Hundred Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0521',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:11',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0521',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'FortyGigabitEthernet1/0/10': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0509',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:37',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0509',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'Vlan125': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.166.1/24': {
            'ip': '172.16.166.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:24',
    },
'HundredGigE1/0/35.5': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.4.1/24': {
            'ip': '172.16.4.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'FortyGigabitEthernet1/0/20': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0513',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:50',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0513',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/48.3': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.106.1/24': {
            'ip': '192.168.106.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Tunnel0': {
    'bandwidth': 100,
    'output_hang': 'never',
    'last_input': 'never',
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 0,
        'output_queue_max': 0,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'txload': '1/255',
    'type': 'Tunnel',
    'oper_status': 'up',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 0,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': '20:03:05',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'in_abort': 0,
        'out_pkts': 0,
        },
    'rxload': '1/255',
    'encapsulations': {
        'encapsulation': 'tunnel',
        },
    'delay': 50000,
    'description': 'Pim Register Tunnel (Encap) for Embedded RP',
    'line_protocol': 'up',
    'reliability': '255/255',
    'enabled': True,
    'mtu': 1452,
    'last_output': 'never',
    },
'Tunnel9': {
    'bandwidth': 100,
    'output_hang': 'never',
    'last_input': 'never',
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 11176,
        'output_queue_max': 0,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'type': 'Tunnel',
    'oper_status': 'up',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 2696372,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': '20:03:23',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'in_abort': 0,
        'out_pkts': 27775,
        },
    'rxload': '1/255',
    'ipv4': {
        '172.16.84.1/24': {
            'ip': '172.16.84.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'tunnel',
        },
    'delay': 50000,
    'txload': '1/255',
    'line_protocol': 'up',
    'reliability': '255/255',
    'enabled': True,
    'mtu': 17868,
    'last_output': '00:00:00',
    },
'HundredGigE1/0/35.106': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.4.1/24': {
            'ip': '192.168.4.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Vlan132': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.106.1/24': {
            'ip': '172.16.106.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:32',
    },
'HundredGigE1/0/48.6': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.76.1/24': {
            'ip': '192.168.76.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'HundredGigE1/0/48.7': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.240.1/24': {
            'ip': '192.168.240.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'HundredGigE1/0/36': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Hundred Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0523',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:32',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0523',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'Vlan118': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 51,
            'load_interval': 300,
            'in_rate': 31000,
            'out_rate_pkts': 11,
            'out_rate': 6000,
            },
        'in_octets': 279845876,
        'in_giants': 0,
        'in_pkts': 3674811,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60171406,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 813994,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.69.1/24': {
            'ip': '172.16.69.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'Vlan101': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 50,
            'load_interval': 300,
            'in_rate': 29000,
            'out_rate_pkts': 10,
            'out_rate': 5000,
            },
        'in_octets': 279750798,
        'in_giants': 0,
        'in_pkts': 3673498,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60257018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 813812,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.205.1/24': {
            'ip': '172.16.205.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'FortyGigabitEthernet1/0/3': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0502',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:24',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0502',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'Vlan112': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 51,
            'load_interval': 300,
            'in_rate': 30000,
            'out_rate_pkts': 11,
            'out_rate': 6000,
            },
        'in_octets': 279779396,
        'in_giants': 0,
        'in_pkts': 3673848,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60170234,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 813978,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.246.1/24': {
            'ip': '172.16.246.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'FortyGigabitEthernet1/0/17': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0510',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:45',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0510',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'FortyGigabitEthernet1/0/28': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.051b',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:02',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.051b',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/45': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Hundred Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.052c',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:45',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.052c',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/35.15': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.234.1/24': {
            'ip': '172.16.234.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Vlan105': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 50,
            'load_interval': 300,
            'in_rate': 29000,
            'out_rate_pkts': 10,
            'out_rate': 5000,
            },
        'in_octets': 279756472,
        'in_giants': 0,
        'in_pkts': 3673610,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60162584,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 813890,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.76.1/24': {
            'ip': '172.16.76.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'FortyGigabitEthernet1/0/29': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.051c',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:02',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.051c',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'FortyGigabitEthernet1/0/22': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0515',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:54',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0515',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'Vlan104': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 50,
            'load_interval': 300,
            'in_rate': 30000,
            'out_rate_pkts': 10,
            'out_rate': 5000,
            },
        'in_octets': 279762130,
        'in_giants': 0,
        'in_pkts': 3673653,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60155916,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 813767,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.169.1/24': {
            'ip': '172.16.169.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'Vlan128': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.19.1/24': {
            'ip': '172.16.19.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:28',
    },
'Loopback102': {
    'bandwidth': 8000000,
    'output_hang': 'never',
    'last_input': '00:00:16',
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 0,
        'output_queue_max': 0,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'type': 'Loopback',
    'oper_status': 'up',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 160112,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'in_abort': 0,
        'out_pkts': 1343,
        },
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '10.154.1.2/32': {
            'ip': '10.154.1.2',
            'prefix_length': '32',
            },
        },
    'encapsulations': {
        'encapsulation': 'loopback',
        },
    'delay': 5000,
    'txload': '1/255',
    'line_protocol': 'up',
    'reliability': '255/255',
    'enabled': True,
    'mtu': 1514,
    'last_output': 'never',
    },
'HundredGigE1/0/38': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Hundred Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0525',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:32',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0525',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/47': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Hundred Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.052e',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:45',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.052e',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'Vlan114': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 51,
            'load_interval': 300,
            'in_rate': 30000,
            'out_rate_pkts': 11,
            'out_rate': 6000,
            },
        'in_octets': 279801252,
        'in_giants': 0,
        'in_pkts': 3674118,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60167610,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 813964,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.94.1/24': {
            'ip': '172.16.94.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'FortyGigabitEthernet1/0/5': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0504',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:28',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0504',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/35.105': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.154.1/24': {
            'ip': '192.168.154.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Port-channel2': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': True,
    'type': 'EtherChannel',
    'mtu': 1500,
    'rxload': '1/255',
    'keepalive': 10,
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 80000000,
    'port_channel': {
        'port_channel_member': True,
        'port_channel_member_intfs': ['FortyGigabitEthernet1/0/2', 'FortyGigabitEthernet1/0/4'],
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.0501',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 630,
            'load_interval': 300,
            'in_rate': 389000,
            'out_rate_pkts': 622,
            'out_rate': 385000,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 45955737,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 1484746,
        'in_runts': 0,
        'in_octets': 3599101746,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': 'never',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 3550088514,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 45228880,
        'in_giants': 0,
        'out_interface_resets': 1,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 1484746,
        },
    'oper_status': 'up',
    'mac_address': '70b3.1760.0501',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:04:37',
    },
'HundredGigE1/0/35.104': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.51.1/24': {
            'ip': '192.168.51.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'FortyGigabitEthernet1/0/19': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0512',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:50',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0512',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'FortyGigabitEthernet1/0/7': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0506',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:33',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0506',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/35.102': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.106.1/24': {
            'ip': '192.168.106.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'FortyGigabitEthernet1/0/30': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.051d',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:02',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.051d',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/35.7': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.136.1/24': {
            'ip': '172.16.136.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'GigabitEthernet0/0': {
    'media_type': 'RJ45',
    'output_hang': 'never',
    'last_input': '00:00:00',
    'duplex_mode': 'full',
    'flow_control': {
        'send': False,
        'receive': False,
        },
    'type': 'RP management port',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': '1000',
    'phys_address': '70b3.1760.0500',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 675,
            'load_interval': 300,
            'in_rate': 818000,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_no_carrier': 0,
        'out_babble': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 10341900,
        'out_deferred': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 2319228471,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'out_lost_carrier': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'in_broadcast_pkts': 0,
        'out_unknown_protocl_drops': 0,
        'out_octets': 993196,
        'out_mac_pause_frames': 0,
        'last_clear': 'never',
        'in_overrun': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'out_pkts': 8840,
        },
    'oper_status': 'up',
    'mac_address': '70b3.1760.0500',
    'ipv4': {
        '10.9.1.20/16': {
            'ip': '10.9.1.20',
            'prefix_length': '16',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'link_type': 'auto',
    'last_output': '00:00:15',
    },
'Tunnel3': {
    'bandwidth': 100,
    'output_hang': 'never',
    'last_input': 'never',
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 11179,
        'output_queue_max': 0,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'type': 'Tunnel',
    'oper_status': 'up',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 2696882,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': '20:03:11',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'in_abort': 0,
        'out_pkts': 27780,
        },
    'rxload': '1/255',
    'ipv4': {
        '172.16.219.1/24': {
            'ip': '172.16.219.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'tunnel',
        },
    'delay': 50000,
    'txload': '1/255',
    'line_protocol': 'up',
    'reliability': '255/255',
    'enabled': True,
    'mtu': 17868,
    'last_output': '00:00:01',
    },
'Vlan108': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 51,
            'load_interval': 300,
            'in_rate': 31000,
            'out_rate_pkts': 11,
            'out_rate': 6000,
            },
        'in_octets': 279766630,
        'in_giants': 0,
        'in_pkts': 3673638,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60162384,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 813842,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.64.1/24': {
            'ip': '172.16.64.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'HundredGigE1/0/35.17': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.151.1/24': {
            'ip': '172.16.151.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'HundredGigE1/0/35.1': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.19.1/24': {
            'ip': '172.16.19.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Tunnel5': {
    'bandwidth': 100,
    'output_hang': 'never',
    'last_input': 'never',
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 11176,
        'output_queue_max': 0,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'type': 'Tunnel',
    'oper_status': 'up',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 2695894,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': '20:03:15',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'in_abort': 0,
        'out_pkts': 27769,
        },
    'rxload': '1/255',
    'ipv4': {
        '172.16.166.1/24': {
            'ip': '172.16.166.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'tunnel',
        },
    'delay': 50000,
    'txload': '1/255',
    'line_protocol': 'up',
    'reliability': '255/255',
    'enabled': True,
    'mtu': 17868,
    'last_output': '00:00:01',
    },
'FortyGigabitEthernet1/0/12': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.050b',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:37',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.050b',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'FortyGigabitEthernet1/0/24': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0517',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:54',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0517',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'FortyGigabitEthernet1/0/1': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0500',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:20',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0500',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'Vlan111': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 51,
            'load_interval': 300,
            'in_rate': 31000,
            'out_rate_pkts': 11,
            'out_rate': 6000,
            },
        'in_octets': 279763870,
        'in_giants': 0,
        'in_pkts': 3673792,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60848654,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 822081,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.70.1/24': {
            'ip': '172.16.70.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'Tunnel2': {
    'bandwidth': 100,
    'output_hang': 'never',
    'last_input': 'never',
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 11178,
        'output_queue_max': 0,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'type': 'Tunnel',
    'oper_status': 'up',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 2697642,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': '20:03:11',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'in_abort': 0,
        'out_pkts': 27789,
        },
    'rxload': '1/255',
    'ipv4': {
        '172.16.121.1/24': {
            'ip': '172.16.121.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'tunnel',
        },
    'delay': 50000,
    'txload': '1/255',
    'line_protocol': 'up',
    'reliability': '255/255',
    'enabled': True,
    'mtu': 17868,
    'last_output': '00:00:04',
    },
'Vlan103': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 50,
            'load_interval': 300,
            'in_rate': 29000,
            'out_rate_pkts': 10,
            'out_rate': 5000,
            },
        'in_octets': 279772748,
        'in_giants': 0,
        'in_pkts': 3673834,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60159890,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 813848,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.9.1/24': {
            'ip': '172.16.9.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'Vlan135': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.1.1/24': {
            'ip': '172.16.1.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:32',
    },
'Bluetooth0/4': {
    'output_hang': 'never',
    'last_input': 'never',
    'flow_control': {
        'send': False,
        'receive': False,
        },
    'type': 'BT management port',
    'mtu': 1500,
    'rxload': '1/255',
    'keepalive': 10,
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.0500',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_no_carrier': 0,
        'out_babble': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'out_lost_carrier': 1,
        'in_throttles': 0,
        'in_frame': 0,
        'in_broadcast_pkts': 0,
        'out_unknown_protocl_drops': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'last_clear': 'never',
        'in_overrun': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'out_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0500',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'last_output': 'never',
    },
'HundredGigE1/0/48.5': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.169.1/24': {
            'ip': '192.168.169.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Vlan140': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.121.1/24': {
            'ip': '172.16.121.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:41',
    },
'Vlan106': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 51,
            'load_interval': 300,
            'in_rate': 30000,
            'out_rate_pkts': 11,
            'out_rate': 6000,
            },
        'in_octets': 279773894,
        'in_giants': 0,
        'in_pkts': 3673779,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60163538,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 813865,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.240.1/24': {
            'ip': '172.16.240.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'Vlan102': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 40,
            'load_interval': 300,
            'in_rate': 29000,
            'out_rate_pkts': 10,
            'out_rate': 5000,
            },
        'in_octets': 276659268,
        'in_giants': 0,
        'in_pkts': 3632279,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 59536912,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 7,
        'out_pkts': 804940,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.106.1/24': {
            'ip': '172.16.106.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'Tunnel7': {
    'bandwidth': 100,
    'output_hang': 'never',
    'last_input': 'never',
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 11176,
        'output_queue_max': 0,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'type': 'Tunnel',
    'oper_status': 'up',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 2696668,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': '20:03:19',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'in_abort': 0,
        'out_pkts': 27778,
        },
    'rxload': '1/255',
    'ipv4': {
        '172.16.121.1/24': {
            'ip': '172.16.121.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'tunnel',
        },
    'delay': 50000,
    'txload': '1/255',
    'line_protocol': 'up',
    'reliability': '255/255',
    'enabled': True,
    'mtu': 17868,
    'last_output': '00:00:02',
    },
'HundredGigE1/0/33': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Hundred Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0520',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:07',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0520',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'Loopback101': {
    'bandwidth': 8000000,
    'output_hang': 'never',
    'last_input': '00:00:22',
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 0,
        'output_queue_max': 0,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'type': 'Loopback',
    'oper_status': 'up',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 159232,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'in_abort': 0,
        'out_pkts': 1338,
        },
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '10.204.1.2/32': {
            'ip': '10.204.1.2',
            'prefix_length': '32',
            },
        },
    'encapsulations': {
        'encapsulation': 'loopback',
        },
    'delay': 5000,
    'txload': '1/255',
    'line_protocol': 'up',
    'reliability': '255/255',
    'enabled': True,
    'mtu': 1514,
    'last_output': 'never',
    },
'HundredGigE1/0/48.2': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.205.1/24': {
            'ip': '192.168.205.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Loopback10': {
    'bandwidth': 8000000,
    'output_hang': 'never',
    'last_input': 'never',
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 0,
        'output_queue_max': 0,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'type': 'Loopback',
    'oper_status': 'up',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 0,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'in_abort': 0,
        'out_pkts': 0,
        },
    'rxload': '1/255',
    'encapsulations': {
        'encapsulation': 'loopback',
        },
    'keepalive': 10,
    'delay': 5000,
    'txload': '1/255',
    'line_protocol': 'up',
    'reliability': '255/255',
    'enabled': True,
    'mtu': 1514,
    'last_output': 'never',
    },
'HundredGigE1/0/40': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Hundred Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0527',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:37',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0527',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/35.110': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.189.1/24': {
            'ip': '192.168.189.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Vlan136': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.225.1/24': {
            'ip': '172.16.225.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:37',
    },
'FortyGigabitEthernet1/0/32': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.051f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:07',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.051f',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/46': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Hundred Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.052d',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:45',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.052d',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'Tunnel1': {
    'bandwidth': 100,
    'output_hang': 'never',
    'last_input': 'never',
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 11176,
        'output_queue_max': 0,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'type': 'Tunnel',
    'oper_status': 'up',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 2695512,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': '20:03:11',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'in_abort': 0,
        'out_pkts': 27765,
        },
    'rxload': '1/255',
    'ipv4': {
        '172.16.25.1/24': {
            'ip': '172.16.25.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'tunnel',
        },
    'delay': 50000,
    'txload': '1/255',
    'line_protocol': 'up',
    'reliability': '255/255',
    'enabled': True,
    'mtu': 17868,
    'last_output': '00:00:00',
    },
'Tunnel10': {
    'bandwidth': 100,
    'output_hang': 'never',
    'last_input': '00:00:00',
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 34678,
        'output_queue_max': 0,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'type': 'Tunnel',
    'oper_status': 'up',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 94,
            'load_interval': 300,
            'in_rate': 53000,
            'out_rate_pkts': 23,
            'out_rate': 16000,
            },
        'in_octets': 479845002,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 6832599,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 151072685,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': '20:03:23',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'in_abort': 0,
        'out_pkts': 1674895,
        },
    'rxload': '135/255',
    'ipv4': {
        '172.16.186.1/24': {
            'ip': '172.16.186.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'tunnel',
        },
    'delay': 50000,
    'txload': '40/255',
    'line_protocol': 'up',
    'reliability': '255/255',
    'enabled': True,
    'mtu': 17868,
    'last_output': '00:00:00',
    },
'HundredGigE1/0/35.19': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.76.1/24': {
            'ip': '172.16.76.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'FortyGigabitEthernet1/0/14': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.050d',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:41',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.050d',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/35.10': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.94.1/24': {
            'ip': '172.16.94.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Vlan122': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.76.1/24': {
            'ip': '172.16.76.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:20',
    },
'HundredGigE1/0/44': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Hundred Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.052b',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:41',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.052b',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'Vlan130': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.186.1/24': {
            'ip': '172.16.186.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:28',
    },
'HundredGigE1/0/42': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Hundred Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0529',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:41',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0529',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'FortyGigabitEthernet1/0/26': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0519',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:58',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0519',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/35.101': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.9.1/24': {
            'ip': '192.168.9.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Vlan127': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.66.1/24': {
            'ip': '172.16.66.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:24',
    },
'HundredGigE1/0/35.6': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.69.1/24': {
            'ip': '172.16.69.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'FortyGigabitEthernet1/0/23': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0516',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:54',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0516',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'FortyGigabitEthernet1/0/25': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0518',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:58',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0518',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/35.103': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.205.1/24': {
            'ip': '192.168.205.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'HundredGigE1/0/35.4': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.196.1/24': {
            'ip': '172.16.196.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Tunnel4': {
    'bandwidth': 100,
    'output_hang': 'never',
    'last_input': 'never',
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 11180,
        'output_queue_max': 0,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'type': 'Tunnel',
    'oper_status': 'up',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 2695606,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': '20:03:15',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'in_abort': 0,
        'out_pkts': 27765,
        },
    'rxload': '1/255',
    'ipv4': {
        '172.16.64.1/24': {
            'ip': '172.16.64.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'tunnel',
        },
    'delay': 50000,
    'txload': '1/255',
    'line_protocol': 'up',
    'reliability': '255/255',
    'enabled': True,
    'mtu': 17868,
    'last_output': '00:00:01',
    },
'HundredGigE1/0/48.9': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.64.1/24': {
            'ip': '192.168.64.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'HundredGigE1/0/35.13': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.70.1/24': {
            'ip': '172.16.70.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Vlan109': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 51,
            'load_interval': 300,
            'in_rate': 30000,
            'out_rate_pkts': 11,
            'out_rate': 6000,
            },
        'in_octets': 279781274,
        'in_giants': 0,
        'in_pkts': 3673894,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 62192557,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 817800,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.234.1/24': {
            'ip': '172.16.234.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'Loopback1': {
    'bandwidth': 8000000,
    'output_hang': 'never',
    'last_input': '00:00:43',
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 0,
        'output_queue_max': 0,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'type': 'Loopback',
    'oper_status': 'up',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 33608,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 1375,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'in_abort': 0,
        'out_pkts': 1383,
        },
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.154.1/32': {
            'ip': '192.168.154.1',
            'prefix_length': '32',
            },
        },
    'encapsulations': {
        'encapsulation': 'loopback',
        },
    'delay': 5000,
    'txload': '1/255',
    'line_protocol': 'up',
    'reliability': '255/255',
    'enabled': True,
    'mtu': 1514,
    'last_output': 'never',
    },
'FortyGigabitEthernet1/0/2': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': True,
    'type': 'Forty Gigabit Ethernet',
    'mtu': 1500,
    'rxload': '1/255',
    'keepalive': 10,
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': True,
        'port_channel_int': 'Port-channel2',
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.0501',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 454,
            'load_interval': 300,
            'in_rate': 293000,
            'out_rate_pkts': 104,
            'out_rate': 58000,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 32521304,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 1476582,
        'in_runts': 0,
        'in_octets': 2684387777,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:24',
        'out_unknown_protocl_drops': 2,
        'out_lost_carrier': 0,
        'out_octets': 525513005,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 7498024,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 1476582,
        },
    'oper_status': 'up',
    'mac_address': '70b3.1760.0501',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:03',
    },
'HundredGigE1/0/35.109': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.76.1/24': {
            'ip': '192.168.76.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Vlan124': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.219.1/24': {
            'ip': '172.16.219.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:20',
    },
'Vlan110': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 51,
            'load_interval': 300,
            'in_rate': 31000,
            'out_rate_pkts': 11,
            'out_rate': 6000,
            },
        'in_octets': 279796126,
        'in_giants': 0,
        'in_pkts': 3674136,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60168004,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 813960,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.151.1/24': {
            'ip': '172.16.151.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'FortyGigabitEthernet1/0/18': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0511',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:45',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0511',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'FortyGigabitEthernet1/0/9': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0508',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:33',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0508',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/35.2': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.76.1/24': {
            'ip': '172.16.76.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Vlan137': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.196.1/24': {
            'ip': '172.16.196.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:37',
    },
'HundredGigE1/0/48.4': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.9.1/24': {
            'ip': '192.168.9.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'HundredGigE1/0/35.18': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.240.1/24': {
            'ip': '172.16.240.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Vlan120': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 50,
            'load_interval': 300,
            'in_rate': 30000,
            'out_rate_pkts': 11,
            'out_rate': 6000,
            },
        'in_octets': 279785038,
        'in_giants': 0,
        'in_pkts': 3673948,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60171120,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 813996,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.196.1/24': {
            'ip': '172.16.196.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'HundredGigE1/0/48': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': True,
    'type': 'Hundred Gigabit Ethernet',
    'mtu': 1500,
    'rxload': '1/255',
    'keepalive': 10,
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 3,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 550,
            'load_interval': 30,
            'in_rate': 330000,
            'out_rate_pkts': 547,
            'out_rate': 301000,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 39665255,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 548066,
        'in_runts': 0,
        'in_octets': 3012714995,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:49',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 2729787452,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 39424533,
        'in_giants': 0,
        'out_interface_resets': 16,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'up',
    'mac_address': '70b3.1760.059f',
    'ipv4': {
        '172.16.94.2/24': {
            'ip': '172.16.94.2',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'dot1q',
        'first_dot1q': '1',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'Vlan134': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.34.1/24': {
            'ip': '172.16.34.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:32',
    },
'Vlan133': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.69.1/24': {
            'ip': '172.16.69.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:32',
    },
'HundredGigE1/0/35.20': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.169.1/24': {
            'ip': '172.16.169.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Vlan121': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.135.1/24': {
            'ip': '172.16.135.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:20',
    },
'Tunnel6': {
    'bandwidth': 100,
    'output_hang': 'never',
    'last_input': 'never',
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 75,
        'total_output_drop': 11172,
        'output_queue_max': 0,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'type': 'Tunnel',
    'oper_status': 'up',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 2694338,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': '20:03:19',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 0,
        'in_abort': 0,
        'out_pkts': 27752,
        },
    'rxload': '1/255',
    'ipv4': {
        '172.16.15.1/24': {
            'ip': '172.16.15.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'tunnel',
        },
    'delay': 50000,
    'txload': '1/255',
    'line_protocol': 'up',
    'reliability': '255/255',
    'enabled': True,
    'mtu': 17868,
    'last_output': '00:00:02',
    },
'HundredGigE1/0/48.1': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.51.1/24': {
            'ip': '192.168.51.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'FortyGigabitEthernet1/0/15': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.050e',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:41',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.050e',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'Vlan1': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 0,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 1,
        'out_pkts': 0,
        },
    'oper_status': 'down',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'last_output': 'never',
    },
'FortyGigabitEthernet1/0/13': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.050c',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:41',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.050c',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/35.108': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.220.1/24': {
            'ip': '192.168.220.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'FortyGigabitEthernet1/0/16': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.050f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:45',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.050f',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/35.3': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.135.1/24': {
            'ip': '172.16.135.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'HundredGigE1/0/39': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Hundred Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0526',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:37',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0526',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'FortyGigabitEthernet1/0/11': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.050a',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:37',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.050a',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'HundredGigE1/0/35.14': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.151.1/24': {
            'ip': '172.16.151.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Vlan131': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.145.1/24': {
            'ip': '172.16.145.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:28',
    },
'Vlan119': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 51,
            'load_interval': 300,
            'in_rate': 30000,
            'out_rate_pkts': 11,
            'out_rate': 6000,
            },
        'in_octets': 281116276,
        'in_giants': 0,
        'in_pkts': 3691322,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60175212,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 814073,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.4.1/24': {
            'ip': '172.16.4.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'HundredGigE1/0/37': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Hundred Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0524',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:32',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0524',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'FortyGigabitEthernet1/0/4': {
    'output_hang': 'never',
    'last_input': '00:00:15',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': True,
    'type': 'Forty Gigabit Ethernet',
    'mtu': 1500,
    'rxload': '1/255',
    'keepalive': 10,
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': True,
        'port_channel_int': 'Port-channel2',
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.0503',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 186,
            'load_interval': 300,
            'in_rate': 102000,
            'out_rate_pkts': 524,
            'out_rate': 329000,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 13376239,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 6304,
        'in_runts': 0,
        'in_octets': 910225278,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:24',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 3020267756,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 37674953,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 6304,
        },
    'oper_status': 'up',
    'mac_address': '70b3.1760.0503',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:03',
    },
'HundredGigE1/0/48.8': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.151.1/24': {
            'ip': '192.168.151.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'HundredGigE1/0/35': {
    'output_hang': 'never',
    'last_input': '00:00:18',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': True,
    'type': 'Hundred Gigabit Ethernet',
    'mtu': 1500,
    'rxload': '1/255',
    'keepalive': 10,
    'description': 'connected to Ixia 1/6',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 206,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 15,
            'out_rate': 25000,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 550971,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 172604,
        'in_runts': 0,
        'in_octets': 121771829,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:11',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 437624881,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 1536769,
        'in_giants': 206,
        'out_interface_resets': 33,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'up',
    'encapsulations': {
        'encapsulation': 'dot1q',
        'first_dot1q': '1',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'Vlan117': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 50,
            'load_interval': 300,
            'in_rate': 30000,
            'out_rate_pkts': 11,
            'out_rate': 6000,
            },
        'in_octets': 279794536,
        'in_giants': 0,
        'in_pkts': 3674114,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60178182,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 814083,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.136.1/24': {
            'ip': '172.16.136.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'HundredGigE1/0/35.8': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.205.1/24': {
            'ip': '172.16.205.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Vlan139': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.144.1/24': {
            'ip': '172.16.144.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:41',
    },
'Vlan15': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 0,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 0,
        },
    'oper_status': 'down',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': 'never',
    },
'Vlan107': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 51,
            'load_interval': 300,
            'in_rate': 30000,
            'out_rate_pkts': 11,
            'out_rate': 6000,
            },
        'in_octets': 279781700,
        'in_giants': 0,
        'in_pkts': 3673882,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60165230,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 813903,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.151.1/24': {
            'ip': '172.16.151.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'HundredGigE1/0/48.10': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.234.1/24': {
            'ip': '192.168.234.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'HundredGigE1/0/35.107': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '192.168.111.1/24': {
            'ip': '192.168.111.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'FortyGigabitEthernet1/0/8': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0507',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:33',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0507',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'FortyGigabitEthernet1/0/27': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.051a',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:58',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.051a',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'Vlan115': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 52,
            'load_interval': 300,
            'in_rate': 31000,
            'out_rate_pkts': 11,
            'out_rate': 6000,
            },
        'in_octets': 280917432,
        'in_giants': 0,
        'in_pkts': 3688257,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60167218,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 813950,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.21.1/24': {
            'ip': '172.16.21.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'Vlan129': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.229.1/24': {
            'ip': '172.16.229.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:28',
    },
'HundredGigE1/0/41': {
    'output_hang': 'never',
    'last_input': '00:00:01',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': True,
    'type': 'Hundred Gigabit Ethernet',
    'mtu': 1500,
    'rxload': '1/255',
    'keepalive': 10,
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 50,
            'load_interval': 30,
            'in_rate': 39000,
            'out_rate_pkts': 48,
            'out_rate': 35000,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 3581103,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 20089,
        'in_runts': 0,
        'in_octets': 340490834,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:02:37',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 323841840,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 3494815,
        'in_giants': 0,
        'out_interface_resets': 5,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'up',
    'mac_address': '70b3.1760.059f',
    'ipv4': {
        '172.16.4.2/24': {
            'ip': '172.16.4.2',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'HundredGigE1/0/35.11': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.169.1/24': {
            'ip': '172.16.169.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'HundredGigE1/0/35.16': {
    'bandwidth': 100000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'type': 'Hundred Gigabit Ethernet',
    'oper_status': 'up',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'ipv4': {
        '172.16.64.1/24': {
            'ip': '172.16.64.1',
            'prefix_length': '24',
            },
        },
    'connected': True,
    'encapsulations': {
        'encapsulation': 'dot1q',
        },
    'delay': 10,
    'txload': '1/255',
    'mac_address': '70b3.1760.059f',
    'mtu': 1500,
    'reliability': '255/255',
    'enabled': True,
    'line_protocol': 'up',
    },
'Vlan116': {
    'output_hang': 'never',
    'last_input': '00:00:00',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 50,
            'load_interval': 300,
            'in_rate': 30000,
            'out_rate_pkts': 11,
            'out_rate': 6000,
            },
        'in_octets': 279815742,
        'in_giants': 0,
        'in_pkts': 3674429,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 60383316,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 816877,
        },
    'oper_status': 'up',
    'ipv4': {
        '172.16.205.1/24': {
            'ip': '172.16.205.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'up',
    'enabled': True,
    'last_output': '00:00:00',
    },
'Vlan123': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.19.1/24': {
            'ip': '172.16.19.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:20',
    },
'FortyGigabitEthernet1/0/6': {
    'media_type': 'unknown',
    'output_hang': 'never',
    'last_input': 'never',
    'duplex_mode': 'auto',
    'flow_control': {
        'send': False,
        'receive': True,
        },
    'connected': False,
    'type': 'Forty Gigabit Ethernet',
    'arp_timeout': '04:00:00',
    'rxload': '1/255',
    'keepalive': 10,
    'auto_negotiate': True,
    'mtu': 1500,
    'reliability': '255/255',
    'bandwidth': 40000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 2000,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'port_speed': 'auto',
    'phys_address': '70b3.1760.0505',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'out_babble': 0,
        'out_collision': 0,
        'in_pkts': 0,
        'out_deferred': 0,
        'out_errors': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'in_octets': 0,
        'in_watchdog': 0,
        'out_buffers_swapped': 0,
        'in_with_dribble': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'last_clear': '20:01:28',
        'out_unknown_protocl_drops': 0,
        'out_lost_carrier': 0,
        'out_octets': 0,
        'out_mac_pause_frames': 0,
        'out_no_carrier': 0,
        'in_overrun': 0,
        'out_pkts': 0,
        'in_giants': 0,
        'out_interface_resets': 2,
        'out_late_collision': 0,
        'in_mac_pause_frames': 0,
        'in_broadcast_pkts': 0,
        },
    'oper_status': 'down',
    'mac_address': '70b3.1760.0505',
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': False,
    'link_type': 'auto',
    'last_output': 'never',
    },
'Vlan126': {
    'output_hang': 'never',
    'last_input': 'never',
    'mac_address': '70b3.1760.059f',
    'connected': False,
    'type': 'Ethernet SVI',
    'mtu': 1500,
    'rxload': '1/255',
    'arp_timeout': '04:00:00',
    'reliability': '255/255',
    'bandwidth': 1000000,
    'port_channel': {
        'port_channel_member': False,
        },
    'queues': {
        'input_queue_max': 375,
        'total_output_drop': 0,
        'output_queue_max': 40,
        'input_queue_size': 0,
        'queue_strategy': 'fifo',
        'input_queue_flushes': 0,
        'output_queue_size': 0,
        'input_queue_drops': 0,
        },
    'arp_type': 'arpa',
    'phys_address': '70b3.1760.059f',
    'counters': {
        'in_ignored': 0,
        'out_underruns': 0,
        'out_buffer_failure': 0,
        'in_errors': 0,
        'in_no_buffer': 0,
        'in_crc_errors': 0,
        'rate': {
            'in_rate_pkts': 0,
            'load_interval': 300,
            'in_rate': 0,
            'out_rate_pkts': 0,
            'out_rate': 0,
            },
        'in_octets': 0,
        'in_giants': 0,
        'in_pkts': 0,
        'in_multicast_pkts': 0,
        'in_runts': 0,
        'out_octets': 14018,
        'out_buffers_swapped': 0,
        'in_overrun': 0,
        'in_throttles': 0,
        'in_frame': 0,
        'out_unknown_protocl_drops': 0,
        'last_clear': 'never',
        'in_broadcast_pkts': 0,
        'out_errors': 0,
        'out_interface_resets': 2,
        'out_pkts': 163,
        },
    'oper_status': 'down',
    'ipv4': {
        '172.16.115.1/24': {
            'ip': '172.16.115.1',
            'prefix_length': '24',
            },
        },
    'encapsulations': {
        'encapsulation': 'arpa',
        },
    'delay': 10,
    'txload': '1/255',
    'line_protocol': 'down',
    'enabled': True,
    'last_output': '06:39:24',
    },
}

    golden_parsed_interface_output_2 = {
        "TenGigabitEthernet0/2/0": {
            "port_channel": {
                "port_channel_member": False
            },
            "enabled": True,
            "line_protocol": "up",
            "oper_status": "up",
            "type": "SPA-1X10GE-L-V2",
            "mac_address": "006b.f1d5.e820",
            "phys_address": "006b.f1d5.e820",
            "description": "toP",
            "ipv4": {
                "10.169.197.94/30": {
                    "ip": "10.169.197.94",
                    "prefix_length": "30"
                }
            },
            "delay": 10,
            "mtu": 1552,
            "bandwidth": 10000000,
            "reliability": "255/255",
            "txload": "2/255",
            "rxload": "2/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "flow_control": {
                "receive": True,
                "send": True
            },
            "carrier_delay_up": 2,
            "carrier_delay_down": 10,
            "arp_type": "arpa",
            "arp_timeout": "04:00:00",
            "last_input": "00:07:19",
            "last_output": "03:51:33",
            "output_hang": "never",
            "queues": {
                "input_queue_size": 0,
                "input_queue_max": 375,
                "input_queue_drops": 0,
                "input_queue_flushes": 0,
                "total_output_drop": 0,
                "queue_strategy": "fifo",
                "output_queue_size": 0,
                "output_queue_max": 40
            },
            "counters": {
                "rate": {
                    "load_interval": 300,
                    "in_rate": 79676000,
                    "in_rate_pkts": 9999,
                    "out_rate": 79998000,
                    "out_rate_pkts": 9999
                },
                "last_clear": "never",
                "in_pkts": 1779405333,
                "in_octets": 1772200805652,
                "in_no_buffer": 0,
                "in_multicast_pkts": 60322,
                "in_broadcast_pkts": 0,
                "in_runts": 0,
                "in_giants": 0,
                "in_throttles": 0,
                "in_errors": 0,
                "in_crc_errors": 0,
                "in_frame": 0,
                "in_overrun": 0,
                "in_ignored": 0,
                "in_watchdog": 0,
                "in_mac_pause_frames": 0,
                "out_pkts": 1791189623,
                "out_octets": 1790956453417,
                "out_underruns": 0,
                "out_errors": 0,
                "out_interface_resets": 2,
                "out_collision": 0,
                "out_unknown_protocl_drops": 291,
                "out_babble": 0,
                "out_late_collision": 0,
                "out_deferred": 0,
                "out_lost_carrier": 0,
                "out_no_carrier": 0,
                "out_mac_pause_frames": 0,
                "out_buffer_failure": 0,
                "out_buffers_swapped": 0
            }
        }
    }

    golden_interface_output_2 = {'execute.return_value': '''
    PE1>show interfaces TenGigabitEthernet 0/2/0  
    Load for five secs: 3%/0%; one minute: 3%; five minutes: 3%
    Time source is NTP, 17:32:09.532 EST Tue Apr 23 2019

    TenGigabitEthernet0/2/0 is up, line protocol is up 
      Hardware is SPA-1X10GE-L-V2, address is 006b.f1d5.e820 (bia 006b.f1d5.e820)
      Description: toP
      Internet address is 10.169.197.94/30
      MTU 1552 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
         reliability 255/255, txload 2/255, rxload 2/255
      Encapsulation ARPA, loopback not set
      Keepalive not supported 
      Full Duplex, 10000Mbps, link type is force-up, media type is 10GBase-SR/SW
      output flow-control is on, input flow-control is on
      Asymmetric Carrier-Delay Up Timer is 2 sec
      Asymmetric Carrier-Delay Down Timer is 10 sec
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input 00:07:19, output 03:51:33, output hang never
      Last clearing of "show interface" counters never
      Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
      Output queue: 0/40 (size/max)
      5 minute input rate 79676000 bits/sec, 9999 packets/sec
      5 minute output rate 79998000 bits/sec, 9999 packets/sec
         1779405333 packets input, 1772200805652 bytes, 0 no buffer
         Received 3 broadcasts (0 IP multicasts)
         0 runts, 0 giants, 0 throttles 
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
         0 watchdog, 60322 multicast, 0 pause input
         1791189623 packets output, 1790956453417 bytes, 0 underruns
         0 output errors, 0 collisions, 2 interface resets
         291 unknown protocol drops
         0 babbles, 0 late collision, 0 deferred
         0 lost carrier, 0 no carrier, 0 pause output
         0 output buffer failures, 0 output buffers swapped out
    PE1>
    '''}

    golden_parsed_interface_output_3 = {
        "GigabitEthernet3": {
            "port_channel": {
                "port_channel_member": False
            },
            "enabled": True,
            "line_protocol": "up",
            "oper_status": "up",
            "type": "CSR vNIC",
            "mac_address": "fa16.3eda.af5b",
            "phys_address": "fa16.3eda.af5b",
            "ipv4": {
                "10.0.2.1/24": {
                    "ip": "10.0.2.1",
                    "prefix_length": "24"
                }
            },
            "delay": 600,
            "mtu": 1500,
            "bandwidth": 1000000,
            "reliability": "255/255",
            "txload": "1/255",
            "rxload": "1/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "keepalive": 10,
            "duplex_mode": "full",
            "port_speed": "1000",
            "link_type": "auto",
            "auto_negotiate": True,
            "media_type": "Virtual",
            "flow_control": {
                "receive": False,
                "send": False
            },
            "carrier_delay": 10,
            "arp_type": "arpa",
            "arp_timeout": "04:00:00",
            "last_input": "00:00:00",
            "last_output": "00:00:00",
            "output_hang": "never",
            "queues": {
                "input_queue_size": 0,
                "input_queue_max": 375,
                "input_queue_drops": 0,
                "input_queue_flushes": 0,
                "total_output_drop": 0,
                "queue_strategy": "fifo",
                "output_queue_size": 0,
                "output_queue_max": 40
            },
            "counters": {
                "rate": {
                    "load_interval": 300,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0
                },
                "last_clear": "never",
                "in_pkts": 101744,
                "in_octets": 9327436,
                "in_no_buffer": 0,
                "in_multicast_pkts": 0,
                "in_broadcast_pkts": 0,
                "in_runts": 0,
                "in_giants": 0,
                "in_throttles": 0,
                "in_errors": 0,
                "in_crc_errors": 0,
                "in_frame": 0,
                "in_overrun": 0,
                "in_ignored": 0,
                "in_watchdog": 0,
                "in_mac_pause_frames": 0,
                "out_pkts": 65026,
                "out_octets": 7387154,
                "out_underruns": 0,
                "out_errors": 0,
                "out_interface_resets": 1,
                "out_collision": 0,
                "out_unknown_protocl_drops": 10110,
                "out_babble": 0,
                "out_late_collision": 0,
                "out_deferred": 0,
                "out_lost_carrier": 0,
                "out_no_carrier": 0,
                "out_mac_pause_frames": 0,
                "out_buffer_failure": 0,
                "out_buffers_swapped": 0
            }
        }
    }

    golden_interface_output_3 = {'execute.return_value': '''
    [2019-04-23 10:53:38,979] +++ csr1000v-1: executing command 'show interfaces GigabitEthernet3' +++
    show interfaces GigabitEthernet3
    GigabitEthernet3 is up, line protocol is up 
      Hardware is CSR vNIC, address is fa16.3eda.af5b (bia fa16.3eda.af5b)
      Internet address is 10.0.2.1/24
      MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 600 usec, 
         reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, loopback not set
      Keepalive set (10 sec)
      Full Duplex, 1000Mbps, link type is auto, media type is Virtual
      output flow-control is unsupported, input flow-control is unsupported
      Carrier delay is 10 sec
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input 00:00:00, output 00:00:00, output hang never
      Last clearing of "show interface" counters never
      Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
      Output queue: 0/40 (size/max)
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         101744 packets input, 9327436 bytes, 0 no buffer
         Received 0 broadcasts (0 IP multicasts)
         0 runts, 0 giants, 0 throttles 
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
         0 watchdog, 0 multicast, 0 pause input
         65026 packets output, 7387154 bytes, 0 underruns
         0 output errors, 0 collisions, 1 interface resets
         10110 unknown protocol drops
         0 babbles, 0 late collision, 0 deferred
         0 lost carrier, 0 no carrier, 0 pause output
         0 output buffer failures, 0 output buffers swapped out
    csr1000v-1#
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
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_interfaces(self):
        self.device = Mock(**self.golden_interface_output)
        interface_obj = ShowInterfaces(device=self.device)
        parsed_output = interface_obj.parse(interface='GigabitEthernet1')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_interface_output)

    def test_show_interfaces_2(self):
        self.device = Mock(**self.golden_interface_output_2)
        interface_obj = ShowInterfaces(device=self.device)
        parsed_output = interface_obj.parse(interface='TenGigabitEthernet0/2/0')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_interface_output_2)

    def test_show_interfaces_3(self):
        self.device = Mock(**self.golden_interface_output_3)
        interface_obj = ShowInterfaces(device=self.device)
        parsed_output = interface_obj.parse(interface='GigabitEthernet3')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_interface_output_3)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        interface_obj = ShowInterfaces(device=self.device)
        parsed_output = interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output2)

#############################################################################
# unitest For Show ip interface
#############################################################################
class test_show_ip_interface(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        "Vlan211": {
            "sevurity_level": "default",
            "ip_route_cache_flags": [
                 "CEF",
                 "Fast"
            ],
            "enabled": True,
            "oper_status": "up",
            "address_determined_by": "configuration file",
            "router_discovery": False,
            "ip_multicast_fast_switching": False,
            "split_horizon": True,
            "bgp_policy_mapping": False,
            "ip_output_packet_accounting": False,
            "mtu": 1500,
            "policy_routing": False,
            "local_proxy_arp": False,
            "proxy_arp": True,
            "network_address_translation": False,
            "ip_cef_switching_turbo_vector": True,
            "icmp": {
                "redirects": "always sent",
                "mask_replies": "never sent",
                "unreachables": "always sent",
            },
            "ipv4": {
                 "192.168.76.1/24": {
                      "prefix_length": "24",
                      "ip": "192.168.76.1",
                      "secondary": False,
                      "broadcase_address": "255.255.255.255"
                 }
            },
            "ip_access_violation_accounting": False,
            "ip_cef_switching": True,
            "unicast_routing_topologies": {
                 "topology": {
                     "base": {
                         "status": "up"
                      }
                  },
            },
            "ip_null_turbo_vector": True,
            "probe_proxy_name_replies": False,
            "ip_fast_switching": True,
            "ip_multicast_distributed_fast_switching": False,
            "tcp_ip_header_compression": False,
            "rtp_ip_header_compression": False,
            "input_features": ["MCI Check"],
            "directed_broadcast_forwarding": False,
            "ip_flow_switching": False
       },
       "GigabitEthernet0/0": {
            "sevurity_level": "default",
            'address_determined_by': 'setup command',
            "ip_route_cache_flags": [
                 "CEF",
                 "Fast"
            ],
            "enabled": True,
            "oper_status": "up",
            "router_discovery": False,
            "ip_multicast_fast_switching": False,
            "split_horizon": True,
            "bgp_policy_mapping": False,
            "ip_output_packet_accounting": False,
            "mtu": 1500,
            "policy_routing": False,
            "local_proxy_arp": False,
            "vrf": "Mgmt-vrf",
            "proxy_arp": True,
            "network_address_translation": False,
            "ip_cef_switching_turbo_vector": True,
            "icmp": {
                "redirects": "always sent",
                "mask_replies": "never sent",
                "unreachables": "always sent",
            },
            "ipv4": {
                 "10.1.8.134/24": {
                      "prefix_length": "24",
                      "ip": "10.1.8.134",
                      "secondary": False,
                      "broadcase_address": "255.255.255.255"
                 }
            },
            "ip_access_violation_accounting": False,
            "ip_cef_switching": True,
            "unicast_routing_topologies": {
                 "topology": {
                     "base": {
                         "status": "up"
                      }
                  },
            },
            "ip_null_turbo_vector": True,
            "probe_proxy_name_replies": False,
            "ip_fast_switching": True,
            "ip_multicast_distributed_fast_switching": False,
            "tcp_ip_header_compression": False,
            "rtp_ip_header_compression": False,
            "input_features": ["MCI Check"],
            "directed_broadcast_forwarding": False,
            "ip_flow_switching": False
       },
       "GigabitEthernet2": {
            "enabled": False,
            "oper_status": "down"
       },
       "GigabitEthernet1/0/1": {
            "sevurity_level": "default",
            'address_determined_by': 'setup command',
            "ip_route_cache_flags": [
                 "CEF",
                 "Fast"
            ],
            "enabled": False,
            "oper_status": "down",
            "router_discovery": False,
            "ip_multicast_fast_switching": False,
            "split_horizon": True,
            "bgp_policy_mapping": False,
            "ip_output_packet_accounting": False,
            "mtu": 1500,
            "policy_routing": False,
            "local_proxy_arp": False,
            "proxy_arp": True,
            "network_address_translation": False,
            "ip_cef_switching_turbo_vector": True,
            "icmp": {
                "redirects": "always sent",
                "mask_replies": "never sent",
                "unreachables": "always sent",
            },
            "ipv4": {
                 "10.1.1.1/24": {
                      "prefix_length": "24",
                      "ip": "10.1.1.1",
                      "secondary": False,
                      "broadcase_address": "255.255.255.255"
                 },
                 "10.2.2.2/24": {
                      "prefix_length": "24",
                      "ip": "10.2.2.2",
                      "secondary": True
                 },
            },
            "ip_access_violation_accounting": False,
            "ip_cef_switching": True,
            "unicast_routing_topologies": {
                 "topology": {
                     "base": {
                         "status": "up"
                      }
                  },
            },
            'wccp': {
              'redirect_outbound': False,
              'redirect_inbound': False,
              'redirect_exclude': False,
            },
            "ip_null_turbo_vector": True,
            "probe_proxy_name_replies": False,
            "ip_fast_switching": True,
            "ip_multicast_distributed_fast_switching": False,
            "tcp_ip_header_compression": False,
            "rtp_ip_header_compression": False,
            "directed_broadcast_forwarding": False,
            "ip_flow_switching": False,
            "input_features": ["MCI Check", "QoS Classification", "QoS Marking"],
        }
    }
    golden_output = {'execute.return_value': '''
        Vlan211 is up, line protocol is up
        Internet address is 192.168.76.1/24
        Broadcast address is 255.255.255.255
        Address determined by configuration file
        MTU is 1500 bytes
        Helper address is not set
        Directed broadcast forwarding is disabled
        Outgoing Common access list is not set 
        Outgoing access list is not set
        Inbound Common access list is not set 
        Inbound  access list is not set
        Proxy ARP is enabled
        Local Proxy ARP is disabled
        Security level is default
        Split horizon is enabled
        ICMP redirects are always sent
        ICMP unreachables are always sent
        ICMP mask replies are never sent
        IP fast switching is enabled
        IP Flow switching is disabled
        IP CEF switching is enabled
        IP CEF switching turbo vector
        IP Null turbo vector
        Associated unicast routing topologies:
            Topology "base", operation state is UP
        IP multicast fast switching is disabled
        IP multicast distributed fast switching is disabled
        IP route-cache flags are Fast, CEF
        Router Discovery is disabled
        IP output packet accounting is disabled
        IP access violation accounting is disabled
        TCP/IP header compression is disabled
        RTP/IP header compression is disabled
        Probe proxy name replies are disabled
        Policy routing is disabled
        Network address translation is disabled
        BGP Policy Mapping is disabled
        Input features: MCI Check
        
        GigabitEthernet0/0 is up, line protocol is up
        Internet address is 10.1.8.134/24
        Broadcast address is 255.255.255.255
        Address determined by setup command
        MTU is 1500 bytes
        Helper address is not set
        Directed broadcast forwarding is disabled
        Outgoing Common access list is not set 
        Outgoing access list is not set
        Inbound Common access list is not set 
        Inbound  access list is not set
        Proxy ARP is enabled
        Local Proxy ARP is disabled
        Security level is default
        Split horizon is enabled
        ICMP redirects are always sent
        ICMP unreachables are always sent
        ICMP mask replies are never sent
        IP fast switching is enabled
        IP Flow switching is disabled
        IP CEF switching is enabled
        IP CEF switching turbo vector
        IP Null turbo vector
        VPN Routing/Forwarding "Mgmt-vrf"
        Associated unicast routing topologies:
            Topology "base", operation state is UP
        IP multicast fast switching is disabled
        IP multicast distributed fast switching is disabled
        IP route-cache flags are Fast, CEF
        Router Discovery is disabled
        IP output packet accounting is disabled
        IP access violation accounting is disabled
        TCP/IP header compression is disabled
        RTP/IP header compression is disabled
        Probe proxy name replies are disabled
        Policy routing is disabled
        Network address translation is disabled
        BGP Policy Mapping is disabled
        Input features: MCI Check

        GigabitEthernet1/0/1 is administratively down, line protocol is down
        Internet address is 10.1.1.1/24
        Broadcast address is 255.255.255.255
        Address determined by setup command
        MTU is 1500 bytes
        Helper address is not set
        Directed broadcast forwarding is disabled
        Secondary address 10.2.2.2/24
        Outgoing Common access list is not set 
        Outgoing access list is not set
        Inbound Common access list is not set 
        Inbound  access list is not set
        Proxy ARP is enabled
        Local Proxy ARP is disabled
        Security level is default
        Split horizon is enabled
        ICMP redirects are always sent
        ICMP unreachables are always sent
        ICMP mask replies are never sent
        IP fast switching is enabled
        IP Flow switching is disabled
        IP CEF switching is enabled
        IP CEF switching turbo vector
        IP Null turbo vector
        Associated unicast routing topologies:
              Topology "base", operation state is UP
        IP multicast fast switching is disabled
        IP multicast distributed fast switching is disabled
        IP route-cache flags are Fast, CEF
        Router Discovery is disabled
        IP output packet accounting is disabled
        IP access violation accounting is disabled
        TCP/IP header compression is disabled
        RTP/IP header compression is disabled
        Probe proxy name replies are disabled
        Policy routing is disabled
        Network address translation is disabled
        BGP Policy Mapping is disabled
        Input features: QoS Classification, QoS Marking, MCI Check
        IPv4 WCCP Redirect outbound is disabled
        IPv4 WCCP Redirect inbound is disabled
        IPv4 WCCP Redirect exclude is disabled


        GigabitEthernet2 is administratively down, line protocol is down
        Internet protocol processing disabled
    '''}

    golden_interface_output = {'execute.return_value':'''
CE1#show ip interface GigabitEthernet1
GigabitEthernet1 is up, line protocol is up
  Internet address is 172.16.1.243/24
  Broadcast address is 255.255.255.255
  Address determined by DHCP
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Outgoing Common access list is not set
  Outgoing access list is not set
  Inbound Common access list is not set
  Inbound  access list is not set
  Proxy ARP is enabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are always sent
  ICMP unreachables are always sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP CEF switching turbo vector
  IP Null turbo vector
  Associated unicast routing topologies:
        Topology "base", operation state is UP
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Probe proxy name replies are disabled
  Policy routing is disabled
  Network address translation is disabled
  BGP Policy Mapping is disabled
  Input features: MCI Check
  IPv4 WCCP Redirect outbound is disabled
  IPv4 WCCP Redirect inbound is disabled
  IPv4 WCCP Redirect exclude is disabled
'''
}
    golden_parsed_interface_output = {
        "GigabitEthernet1": {
            "ip_multicast_fast_switching": True,
            "oper_status": "up",
            "ip_output_packet_accounting": False,
            "address_determined_by": "DHCP",
            "rtp_ip_header_compression": False,
            "ip_multicast_distributed_fast_switching": False,
            "wccp": {
                "redirect_exclude": False,
                "redirect_outbound": False,
                "redirect_inbound": False
            },
            "unicast_routing_topologies": {
                "topology": {
                    "base": {
                        "status": "up"
                    }
                }
            },
            "router_discovery": False,
            "tcp_ip_header_compression": False,
            "probe_proxy_name_replies": False,
            "local_proxy_arp": False,
            "policy_routing": False,
            "mtu": 1500,
            "icmp": {
                "mask_replies": "never sent",
                "unreachables": "always sent",
                "redirects": "always sent"
            },
            "enabled": True,
            "ip_route_cache_flags": [
                "CEF",
                "Fast"
            ],
            "ip_cef_switching": True,
            "ip_fast_switching": True,
            "sevurity_level": "default",
            "directed_broadcast_forwarding": False,
            "proxy_arp": True,
            "ip_null_turbo_vector": True,
            "network_address_translation": False,
            "input_features": [
                "MCI Check"
            ],
            "bgp_policy_mapping": False,
            "split_horizon": True,
            "ip_access_violation_accounting": False,
            "ip_cef_switching_turbo_vector": True,
            "ipv4": {
                "172.16.1.243/24": {
                    "ip": "172.16.1.243",
                    "prefix_length": "24",
                    "broadcase_address": "255.255.255.255",
                    "secondary": False
                }
            },
            "ip_flow_switching": False
        }
    }

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

    def test_interface_golden(self):
        self.device = Mock(**self.golden_interface_output)
        interface_obj = ShowIpInterface(device=self.device)
        parsed_output = interface_obj.parse(interface='GigabitEthernet1')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_interface_output)


#############################################################################
# unitest For show ipv6 interface
#############################################################################
class test_show_ipv6_interface(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        "GigabitEthernet1/0/1": {
            "joined_group_addresses": [
                 "FF02::1"
            ],
            "ipv6": {
                 "2001:DB8:2:2::2/64": {
                      "ip": "2001:DB8:2:2::2",
                      "prefix_length": "64",
                      "status": "tentative"
                 },
                 "2000::1/126": {
                      "ip": "2000::1",
                      "prefix_length": "126",
                      "status": "tentative"
                 },
                 "2001:DB8:1:1::1/64": {
                      "ip": "2001:DB8:1:1::1",
                      "prefix_length": "64",
                      "status": "tentative"
                 },
                 "2001:DB8:4:4:257:D2FF:FE28:1A64/64": {
                      "ip": "2001:DB8:4:4:257:D2FF:FE28:1A64",
                      "prefix_length": "64",
                      "status": "tentative",
                      "eui_64": True
                 },
                 "2001:DB8:3:3::3/64": {
                      "ip": "2001:DB8:3:3::3",
                      "prefix_length": "64",
                      "status": "tentative",
                      "anycast": True
                 },
                 "FE80::257:D2FF:FE28:1A64": {
                      "ip": "FE80::257:D2FF:FE28:1A64",
                      "status": "tentative",
                      "origin": "link_layer",
                 },
                 "enabled": True,
                 "nd": {
                      "dad_attempts": 1,
                      "ns_retransmit_interval": 1000,
                      "dad_enabled": True,
                      "reachable_time": 30000,
                      "using_time": 30000
                 },
                 "icmp": {
                      "error_messages_limited": 100,
                      "redirects": True,
                      "unreachables": "sent"
                 },
            },
            "oper_status": "down",
            "enabled": False,
            "mtu": 1500
       },
       "Vlan211": {
            "joined_group_addresses": [
                 "FF02::1",
                 "FF02::1:FF14:1",
                 "FF02::1:FF28:1A71"
            ],
            "ipv6": {
                 "2001:10::14:1/112": {
                      "ip": "2001:10::14:1",
                      "prefix_length": "112",
                      "status": "valid",
                      'autoconf': {
                          'preferred_lifetime': 604711,
                          'valid_lifetime': 2591911,
                      },
                 },
                 "FE80::257:D2FF:FE28:1A71": {
                      "ip": "FE80::257:D2FF:FE28:1A71",
                      "status": "valid",
                      "origin": "link_layer",
                 },
                 "enabled": True,
                 "nd": {
                      "dad_attempts": 1,
                      "ns_retransmit_interval": 1000,
                      "dad_enabled": True,
                      "reachable_time": 30000,
                      "using_time": 30000
                 },
                 "icmp": {
                      "error_messages_limited": 100,
                      "redirects": True,
                      "unreachables": "sent"
                 },
            },
            "oper_status": "up",
            "enabled": True,
            "autoconf": True,
            "mtu": 1500
       },
       "GigabitEthernet3": {
            "enabled": True,
            "joined_group_addresses": [
                 "FF02::1",
                 "FF02::1:FF1E:4F2",
                 "FF02::2"
            ],
            "ipv6": {
                 "enabled": False,
                 "FE80::5054:FF:FE1E:4F2": {
                      "ip": "FE80::5054:FF:FE1E:4F2",
                      "status": "valid",
                      "origin": "link_layer",
                 },
                 "unnumbered": {
                      "interface_ref": "Loopback0",
                 },
                 "nd": {
                      "dad_attempts": 1,
                      "reachable_time": 30000,
                      "using_time": 30000,
                      "dad_enabled": True
                 },
                 "icmp": {
                      "unreachables": "sent",
                      "redirects": True,
                      "error_messages_limited": 100
                 },
                 "nd": {
                      "dad_attempts": 1,
                      "dad_enabled": True,
                      "reachable_time": 30000,
                      "using_time": 30000,
                      "advertised_reachable_time": 0,
                      "advertised_retransmit_interval": 0,
                      "router_advertisements_interval": 200,
                      "router_advertisements_live": 1800,
                      "advertised_default_router_preference": 'Medium',
                      "advertised_reachable_time_unspecified": True,
                      "advertised_retransmit_interval_unspecified": True,
                 },
            },
            "oper_status": "up",
            "mtu": 1500,
            "addresses_config_method": 'stateless autoconfig',
       }
    }

    golden_output = {'execute.return_value': '''
        Vlan211 is up, line protocol is up
        IPv6 is enabled, link-local address is FE80::257:D2FF:FE28:1A71 
        No Virtual link-local address(es):
        Stateless address autoconfig enabled
        Global unicast address(es):
          2001:10::14:1, subnet is 2001:10::14:0/112 
            valid lifetime 2591911 preferred lifetime 604711
        Joined group address(es):
          FF02::1
          FF02::1:FF14:1
          FF02::1:FF28:1A71
        MTU is 1500 bytes
        ICMP error messages limited to one every 100 milliseconds
        ICMP redirects are enabled
        ICMP unreachables are sent
        ND DAD is enabled, number of DAD attempts: 1
        ND reachable time is 30000 milliseconds (using 30000)
        ND NS retransmit interval is 1000 milliseconds

        GigabitEthernet1/0/1 is administratively down, line protocol is down
        IPv6 is tentative, link-local address is FE80::257:D2FF:FE28:1A64 [TEN]
        No Virtual link-local address(es):
        Description: desc
        Global unicast address(es):
          2000::1, subnet is 2000::/126 [TEN]
          2001:DB8:1:1::1, subnet is 2001:DB8:1:1::/64 [TEN]
          2001:DB8:2:2::2, subnet is 2001:DB8:2:2::/64 [TEN]
          2001:DB8:3:3::3, subnet is 2001:DB8:3:3::/64 [ANY/TEN]
          2001:DB8:4:4:257:D2FF:FE28:1A64, subnet is 2001:DB8:4:4::/64 [EUI/TEN]
        Joined group address(es):
          FF02::1
        MTU is 1500 bytes
        ICMP error messages limited to one every 100 milliseconds
        ICMP redirects are enabled
        ICMP unreachables are sent
        ND DAD is enabled, number of DAD attempts: 1
        ND reachable time is 30000 milliseconds (using 30000)
        ND NS retransmit interval is 1000 milliseconds

        GigabitEthernet3 is up, line protocol is up
          IPv6 is enabled, link-local address is FE80::5054:FF:FE1E:4F2 
          No Virtual link-local address(es):
          Interface is unnumbered. Using address of Loopback0
          No global unicast address is configured
          Joined group address(es):
            FF02::1
            FF02::2
            FF02::1:FF1E:4F2
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
# unitest For show interfaces trunk
#############################################################################
class test_show_interfaces_trunk(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        "interface": {
            "GigabitEthernet1/0/4": {
               "vlans_allowed_active_in_mgmt_domain": '200-211',
               "vlans_allowed_on_trunk": '200-211',
               "mode": "on",
               "native_vlan": "1",
               "status": "trunking",
               "vlans_in_stp_forwarding_not_pruned": '200-211',
               "name": "GigabitEthernet1/0/4",
               "encapsulation": "802.1q"
            },
            "GigabitEthernet1/0/23": {
               "vlans_allowed_active_in_mgmt_domain": '200-211',
               "vlans_allowed_on_trunk": '200-211',
               "mode": "on",
               "native_vlan": "1",
               "status": "trunking",
               "vlans_in_stp_forwarding_not_pruned": '200-211',
               "name": "GigabitEthernet1/0/23",
               "encapsulation": "802.1q"
            },
            "Port-channel12": {
               "vlans_allowed_active_in_mgmt_domain": '100-110',
               "vlans_allowed_on_trunk": '100-110',
               "mode": "on",
               "native_vlan": "1",
               "status": "trunking",
               "vlans_in_stp_forwarding_not_pruned": '100-110',
               "name": "Port-channel12",
               "encapsulation": "802.1q"
            },
            "Port-channel14": {
               "vlans_allowed_active_in_mgmt_domain": '200-211, 300-302',
               "vlans_allowed_on_trunk": '200-211',
               "mode": "on",
               "native_vlan": "1",
               "status": "trunking",
               "vlans_in_stp_forwarding_not_pruned": '200-211',
               "name": "Port-channel14",
               "encapsulation": "802.1q"
            }
        }
    }

    golden_output = {'execute.return_value': '''
        Port        Mode             Encapsulation  Status        Native vlan
        Gi1/0/4     on               802.1q         trunking      1
        Gi1/0/23    on               802.1q         trunking      1
        Po12        on               802.1q         trunking      1
        Po14        on               802.1q         trunking      1

        Port        Vlans allowed on trunk
        Gi1/0/4     200-211
        Gi1/0/23    200-211
        Po12        100-110
        Po14        200-211

        Port        Vlans allowed and active in management domain
        Gi1/0/4     200-211
        Gi1/0/23    200-211
        Po12        100-110
        Po14        200-211, 300-302

        Port        Vlans in spanning tree forwarding state and not pruned
        Gi1/0/4     200-211
        Gi1/0/23    200-211
        Po12        100-110
                  
        Port        Vlans in spanning tree forwarding state and not pruned
        Po14        200-211
    '''}

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


#############################################################################
# unitest For show interfaces <WORD> counters
#############################################################################
class test_show_interfaces_counters(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        "interface": {
            "GigabitEthernet1/0/1": {
               "out": {
                    "mcast_pkts": 188396,
                    "bcast_pkts": 0,
                    "ucast_pkts": 124435064,
                    "name": "GigabitEthernet1/0/1",
                    "octets": 24884341205
               },
               "in": {
                    "mcast_pkts": 214513,
                    "bcast_pkts": 0,
                    "ucast_pkts": 15716712,
                    "name": "GigabitEthernet1/0/1",
                    "octets": 3161931167
               }
            }
        }
    }

    golden_output = {'execute.return_value': '''
        Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
        Gi1/0/1       3161931167       15716712         214513              0 

        Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
        Gi1/0/1      24884341205      124435064         188396              0
    '''}

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
# unitest For show interfaces <interface> accounting
#############################################################################

class test_show_interfaces_accounting(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = \
    {
      "GigabitEthernet1": {
        "accounting": {
          "arp": {
            "chars_in": 4590030,
            "chars_out": 120,
            "pkts_in": 109280,
            "pkts_out": 2
          },
          "ip": {
            "chars_in": 2173570,
            "chars_out": 2167858,
            "pkts_in": 22150,
            "pkts_out": 22121
          },
          "ipv6": {
            "chars_in": 1944,
            "chars_out": 0,
            "pkts_in": 24,
            "pkts_out": 0
          },
          "other": {
            "chars_in": 5306164,
            "chars_out": 120,
            "pkts_in": 112674,
            "pkts_out": 2
          }
        }
      },
      "GigabitEthernet2": {
        "accounting": {
          "arp": {
            "chars_in": 5460,
            "chars_out": 5520,
            "pkts_in": 91,
            "pkts_out": 92
          },
          "ip": {
            "chars_in": 968690,
            "chars_out": 1148402,
            "pkts_in": 11745,
            "pkts_out": 10821
          },
          "ipv6": {
            "chars_in": 70,
            "chars_out": 0,
            "pkts_in": 1,
            "pkts_out": 0
          },
          "other": {
            "chars_in": 741524,
            "chars_out": 5520,
            "pkts_in": 3483,
            "pkts_out": 92
          }
        }
      },
      "GigabitEthernet3": {
        "accounting": {
          "arp": {
            "chars_in": 5460,
            "chars_out": 5520,
            "pkts_in": 91,
            "pkts_out": 92
          },
          "ip": {
            "chars_in": 1190691,
            "chars_out": 1376253,
            "pkts_in": 15271,
            "pkts_out": 14382
          },
          "ipv6": {
            "chars_in": 70,
            "chars_out": 0,
            "pkts_in": 1,
            "pkts_out": 0
          },
          "other": {
            "chars_in": 741524,
            "chars_out": 5520,
            "pkts_in": 3483,
            "pkts_out": 92
          }
        }
      }
    }

    golden_output = {'execute.return_value': '''
show interface accounting
GigabitEthernet1 
                Protocol    Pkts In   Chars In   Pkts Out  Chars Out
                   Other     112674    5306164          2        120
                      IP      22150    2173570      22121    2167858
                     ARP     109280    4590030          2        120
                    IPv6         24       1944          0          0
GigabitEthernet2 
                Protocol    Pkts In   Chars In   Pkts Out  Chars Out
                   Other       3483     741524         92       5520
                      IP      11745     968690      10821    1148402
                     ARP         91       5460         92       5520
                    IPv6          1         70          0          0
GigabitEthernet3 
                Protocol    Pkts In   Chars In   Pkts Out  Chars Out
                   Other       3483     741524         92       5520
                      IP      15271    1190691      14382    1376253
                     ARP         91       5460         92       5520
                    IPv6          1         70          0          0
Loopback0 
                Protocol    Pkts In   Chars In   Pkts Out  Chars Out
No traffic sent or received on this interface.
Loopback1 
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


###################################################
# unit test for show interfaces stats
####################################################
class test_show_interfaces_stats(unittest.TestCase):
    """unit test for show interfaces stats """

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        Router#show interface stats
        Load for five secs: 5%/1%; one minute: 8%; five minutes: 9%
        Time source is NTP, 07:38:10.599 EST Thu Sep 8 2016

        GigabitEthernet0/0
                  Switching path    Pkts In   Chars In   Pkts Out  Chars Out
                       Processor          0          0        225      77625
                     Route cache          0          0          0          0
          Multi-Processor Fwding        950     221250        500      57000
                           Total        950     221250        725     134625
        GigabitEthernet0/1
                  Switching path    Pkts In   Chars In   Pkts Out  Chars Out
                       Processor          1         60        226      77685
                     Route cache          0          0          0          0
          Multi-Processor Fwding        500      57000        500      57000
                           Total        501      57060        726     134685
        GigabitEthernet0/2
                  Switching path    Pkts In   Chars In   Pkts Out  Chars Out
                       Processor          1         60        226      77685
                     Route cache          0          0          0          0
          Multi-Processor Fwding          0          0          0          0
                           Total          1         60        226      77685
        FastEthernet1/0
                  Switching path    Pkts In   Chars In   Pkts Out  Chars Out
                       Processor      34015    5331012       1579     158190
                     Route cache          0          0          0          0
                           Total      34015    5331012       1579     158190
    '''}

    golden_parsed_output = {
        "GigabitEthernet0/0": {
            "switching_path": {
                "processor": {
                    "pkts_in": 0,
                    "chars_in": 0,
                    "pkts_out": 225,
                    "chars_out": 77625
                },
                "route_cache": {
                    "pkts_in": 0,
                    "chars_in": 0,
                    "pkts_out": 0,
                    "chars_out": 0
                },
                "multi_processor_fwding": {
                    "pkts_in": 950,
                    "chars_in": 221250,
                    "pkts_out": 500,
                    "chars_out": 57000
                },
                "total": {
                    "pkts_in": 950,
                    "chars_in": 221250,
                    "pkts_out": 725,
                    "chars_out": 134625
                }
            }
        },
        "GigabitEthernet0/1": {
            "switching_path": {
                "processor": {
                    "pkts_in": 1,
                    "chars_in": 60,
                    "pkts_out": 226,
                    "chars_out": 77685
                },
                "route_cache": {
                    "pkts_in": 0,
                    "chars_in": 0,
                    "pkts_out": 0,
                    "chars_out": 0
                },
                "multi_processor_fwding": {
                    "pkts_in": 500,
                    "chars_in": 57000,
                    "pkts_out": 500,
                    "chars_out": 57000
                },
                "total": {
                    "pkts_in": 501,
                    "chars_in": 57060,
                    "pkts_out": 726,
                    "chars_out": 134685
                }
            }
        },
        "GigabitEthernet0/2": {
            "switching_path": {
                "processor": {
                    "pkts_in": 1,
                    "chars_in": 60,
                    "pkts_out": 226,
                    "chars_out": 77685
                },
                "route_cache": {
                    "pkts_in": 0,
                    "chars_in": 0,
                    "pkts_out": 0,
                    "chars_out": 0
                },
                "multi_processor_fwding": {
                    "pkts_in": 0,
                    "chars_in": 0,
                    "pkts_out": 0,
                    "chars_out": 0
                },
                "total": {
                    "pkts_in": 1,
                    "chars_in": 60,
                    "pkts_out": 226,
                    "chars_out": 77685
                }
            }
        },
        "FastEthernet1/0": {
            "switching_path": {
                "processor": {
                    "pkts_in": 34015,
                    "chars_in": 5331012,
                    "pkts_out": 1579,
                    "chars_out": 158190
                },
                "route_cache": {
                    "pkts_in": 0,
                    "chars_in": 0,
                    "pkts_out": 0,
                    "chars_out": 0
                },
                "total": {
                    "pkts_in": 34015,
                    "chars_in": 5331012,
                    "pkts_out": 1579,
                    "chars_out": 158190
                }
            }
        }
    }

    golden_output_interface = {'execute.return_value': '''
        Router#show interface gigabitEthernet 0/0/0 stats
        Load for five secs: 5%/1%; one minute: 8%; five minutes: 9%
        Time source is NTP, 07:38:10.599 EST Thu Sep 8 2016

        GigabitEthernet0/0/0
                  Switching path    Pkts In   Chars In   Pkts Out  Chars Out
                       Processor         33       2507         33       2490
                     Route cache          0          0          0          0
               Distributed cache      62581   53049894     125156   29719204
                           Total      62614   53052401     125189   29721694
    '''}

    golden_parsed_output_interface = {
        "GigabitEthernet0/0/0": {
            "switching_path": {
                "processor": {
                    "pkts_in": 33,
                    "chars_in": 2507,
                    "pkts_out": 33,
                    "chars_out": 2490
                },
                "route_cache": {
                    "pkts_in": 0,
                    "chars_in": 0,
                    "pkts_out": 0,
                    "chars_out": 0
                },
                "distributed_cache": {
                    "pkts_in": 62581,
                    "chars_in": 53049894,
                    "pkts_out": 125156,
                    "chars_out": 29719204
                },
                "total": {
                    "pkts_in": 62614,
                    "chars_in": 53052401,
                    "pkts_out": 125189,
                    "chars_out": 29721694
                }
            }
        }
    }

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


if __name__ == '__main__':
    unittest.main()