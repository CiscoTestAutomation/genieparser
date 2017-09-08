#!/bin/env python

import sys
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from textwrap import dedent

ats_mock = Mock()
with patch.dict('sys.modules',
        {'ats' : ats_mock}, autospec=True):
    import parsergen
    from parsergen import oper_fill
    from parsergen import oper_check
    from parsergen import oper_fill_tabular
    from parsergen.examples.parsergen.pyAts import parsergen_demo_mkpg

import xml.etree.ElementTree as ET

from ats.topology import Device

from genie.ops.base import Context

from metaparser.util.exceptions import SchemaEmptyParserError

from parser.iosxe.show_interface import ShowInterfacesSwitchport,\
                                        ShowIpInterfaceBriefPipeVlan,\
                                        ShowInterfaces


# class test_show_interfaces_switchport(unittest.TestCase):
#     device = Device(name='aDevice')
#     device1 = Device(name='bDevice')
#     empty_output = {'execute.return_value': ''}
#     golden_parsed_output = {'interface': 
#                             {'Gi1/0/1': 
#                                 {'switchport_mode': {'trunk': {'vlan_id': {'16': {'admin_trunking_encapsulation': 'dot1q'}}}}},
#                              'Gi1/0/3': 
#                                 {'switchport_mode': {'trunk': {'vlan_id': {'1': {'admin_trunking_encapsulation': 'dot1q'},
#                                                                            '300': {}}}}},
#                              'Gi1/0/4': {},
#                              'Gi1/0/5': 
#                                 {'switchport_mode': {'trunk': {'vlan_id': {'1': {'admin_trunking_encapsulation': 'dot1q'}}}}},
#                              'Gi2/0/15': 
#                                 {'switchport_mode': {'static access': {'vlan_id': {'1': {'admin_trunking_encapsulation': 'dot1q'}}}}}}
#                             }


#     golden_output = {'execute.return_value': '''
# Name: Gi1/0/1
# Switchport: Enabled
# Administrative Mode: trunk
# Operational Mode: trunk
# Administrative Trunking Encapsulation: dot1q
# Operational Trunking Encapsulation: dot1q
# Negotiation of Trunking: On
# Access Mode VLAN: 100 (VLAN0100, Suspended)
# Trunking Native Mode VLAN: 16 (Inactive)
# Administrative Native VLAN tagging: enabled
# Voice VLAN: none
# Administrative private-vlan host-association: none 
# Administrative private-vlan mapping: none 
# Administrative private-vlan trunk native VLAN: none
# Administrative private-vlan trunk Native VLAN tagging: enabled
# Administrative private-vlan trunk encapsulation: dot1q
# Administrative private-vlan trunk normal VLANs: none
# Administrative private-vlan trunk associations: none
# Administrative private-vlan trunk mappings: none
# Operational private-vlan: none
# Trunking VLANs Enabled: 20
# Pruning VLANs Enabled: 2-1001
# Capture Mode Disabled
# Capture VLANs Allowed: ALL

# Protected: false
# Unknown unicast blocked: disabled
# Unknown multicast blocked: disabled
# Appliance trust: none

# Name: Gi1/0/3
# Switchport: Enabled
# Administrative Mode: trunk
# Operational Mode: trunk
# Administrative Trunking Encapsulation: dot1q
# Operational Trunking Encapsulation: dot1q
# Negotiation of Trunking: On
# Access Mode VLAN: 300 (Inactive)
# Trunking Native Mode VLAN: 1 (default)
# Administrative Native VLAN tagging: enabled
# Voice VLAN: none
# Administrative private-vlan host-association: none 
# Administrative private-vlan mapping: none 
# Administrative private-vlan trunk native VLAN: none
# Administrative private-vlan trunk Native VLAN tagging: enabled
# Administrative private-vlan trunk encapsulation: dot1q
# Administrative private-vlan trunk normal VLANs: none
# Administrative private-vlan trunk associations: none
# Administrative private-vlan trunk mappings: none
# Operational private-vlan: none
# Trunking VLANs Enabled: 400
# Pruning VLANs Enabled: 2-1001
# Capture Mode Disabled
# Capture VLANs Allowed: ALL

# Protected: false
# Unknown unicast blocked: disabled
# Unknown multicast blocked: disabled
# Appliance trust: none

# Name: Gi1/0/4
# Switchport: Enabled
# Administrative Mode: dynamic auto
# Operational Mode: static access
# Administrative Trunking Encapsulation: dot1q
# Operational Trunking Encapsulation: native
# Negotiation of Trunking: On
# Access Mode VLAN: 1 (default)
# Trunking Native Mode VLAN: 1 (default)
# Administrative Native VLAN tagging: enabled
# Voice VLAN: none
# Administrative private-vlan host-association: none 
# Administrative private-vlan mapping: none 
# Administrative private-vlan trunk native VLAN: none
# Administrative private-vlan trunk Native VLAN tagging: enabled
# Administrative private-vlan trunk encapsulation: dot1q
# Administrative private-vlan trunk normal VLANs: none
# Administrative private-vlan trunk associations: none
# Administrative private-vlan trunk mappings: none
# Operational private-vlan: none
# Trunking VLANs Enabled: ALL
# Pruning VLANs Enabled: 2-1001
# Capture Mode Disabled
# Capture VLANs Allowed: ALL

# Protected: false
# Unknown unicast blocked: disabled
# Unknown multicast blocked: disabled
# Appliance trust: none

# Name: Gi1/0/5
# Switchport: Enabled
# Administrative Mode: trunk
# Operational Mode: down
# Administrative Trunking Encapsulation: dot1q
# Negotiation of Trunking: On
# Access Mode VLAN: 1 (default)
# Trunking Native Mode VLAN: 1 (default)
# Administrative Native VLAN tagging: enabled
# Voice VLAN: none
# Administrative private-vlan host-association: none 
# Administrative private-vlan mapping: none 
# Administrative private-vlan trunk native VLAN: none
# Administrative private-vlan trunk Native VLAN tagging: enabled
# Administrative private-vlan trunk encapsulation: dot1q
# Administrative private-vlan trunk normal VLANs: none
# Administrative private-vlan trunk associations: none
# Administrative private-vlan trunk mappings: none
# Operational private-vlan: none
# Trunking VLANs Enabled: 200,201
# Pruning VLANs Enabled: 2-1001
# Capture Mode Disabled
# Capture VLANs Allowed: ALL

# Protected: false
# Unknown unicast blocked: disabled
# Unknown multicast blocked: disabled
# Appliance trust: none

# Name: Gi2/0/15
# Switchport: Enabled
# Administrative Mode: static access
# Operational Mode: down
# Administrative Trunking Encapsulation: dot1q
# Negotiation of Trunking: Off
# Access Mode VLAN: 400 (VLAN0400)
# Trunking Native Mode VLAN: 1 (default)
# Administrative Native VLAN tagging: enabled
# Voice VLAN: none
# Administrative private-vlan host-association: none 
# Administrative private-vlan mapping: none 
# Administrative private-vlan trunk native VLAN: none
# Administrative private-vlan trunk Native VLAN tagging: enabled
# Administrative private-vlan trunk encapsulation: dot1q
# Administrative private-vlan trunk normal VLANs: none
# Administrative private-vlan trunk associations: none
# Administrative private-vlan trunk mappings: none
# Operational private-vlan: none
# Trunking VLANs Enabled: ALL
# Pruning VLANs Enabled: 2-1001
# Capture Mode Disabled
# Capture VLANs Allowed: ALL

# Protected: false
# Unknown unicast blocked: disabled
# Unknown multicast blocked: disabled
# Appliance trust: none

# '''}

#     def test_golden(self):
#         self.device = Mock(**self.golden_output)
#         intf_obj = ShowInterfacesSwitchport(device=self.device)
#         parsed_output = intf_obj.parse()
#         self.assertEqual(parsed_output,self.golden_parsed_output)

#     def test_empty(self):
#         self.device1 = Mock(**self.empty_output)
#         intf_obj = ShowInterfacesSwitchport(device=self.device1)
#         with self.assertRaises(SchemaEmptyParserError):
#             parsed_output = intf_obj.parse()

# class test_show_interface_parsergen(unittest.TestCase):

#     def test_tabular_parser(self):
#         self.showCommandOutput='''
#             R1#show ip interface brief 
#             Interface              IP-Address      OK? Method Status                Protocol
#             GigabitEthernet0/0     10.1.10.20      YES NVRAM  up                    up      
#             GigabitEthernet1/0/1   unassigned      YES unset  up                    up         
#             GigabitEthernet1/0/10  unassigned      YES unset  down                  down      
# '''

#         self.outputDict = {'GigabitEthernet0/0': {'IP-Address': '10.1.10.20',
#                                                   'Interface': 'GigabitEthernet0/0',
#                                                   'Method': 'NVRAM',
#                                                   'OK?': 'YES',
#                                                   'Protocol': 'up',
#                                                   'Status': 'up'},
#                            'GigabitEthernet1/0/1': {'IP-Address': 'unassigned',
#                                                     'Interface': 'GigabitEthernet1/0/1',
#                                                     'Method': 'unset',
#                                                     'OK?': 'YES',
#                                                     'Protocol': 'up',
#                                                     'Status': 'up'},
#                            'GigabitEthernet1/0/10': {'IP-Address': 'unassigned',
#                                                      'Interface': 'GigabitEthernet1/0/10',
#                                                      'Method': 'unset',
#                                                      'OK?': 'YES',
#                                                      'Protocol': 'down',
#                                                      'Status': 'down'}}

#         # Define how device stub will behave when accessed by production parser.
#         device_kwargs = {'is_connected.return_value':True,
#                          'execute.return_value':dedent(self.showCommandOutput)}
#         device1 = Mock(**device_kwargs)
#         device1.name='router3'

#         result = parsergen.oper_fill_tabular(device=device1,
#                                              show_command="show ip interface brief",
#                                              refresh_cache=True,
#                                              header_fields=
#                                                  [ "Interface",
#                                                    "IP-Address",
#                                                    "OK\?",
#                                                    "Method",
#                                                    "Status",
#                                                    "Protocol" ],
#                                              label_fields=
#                                                  [ "Interface",
#                                                    "IP-Address",
#                                                    "OK?",
#                                                    "Method",
#                                                    "Status",
#                                                    "Protocol" ],
#                                              index=[0])

#         self.assertEqual(result.entries, self.outputDict)
#         args, kwargs = device1.execute.call_args
#         self.assertTrue('show ip interface brief' in args,
#             msg='The expected command was not sent to the router')

# class test_show_interface_brief_pipe_vlan_yang(unittest.TestCase):

#     device = Device(name='aDevice')
#     device1 = Device(name='bDevice')
#     golden_parsed_output = {'interface': {'Vlan1': {'vlan_id': {'1': {'ip_address': 'unassigned'}}},
#                                           'Vlan100': {'vlan_id': {'100': {'ip_address': '201.0.12.1'}}}}}

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
#                         <address>201.0.12.1</address>
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


# class test_show_interfaces_switchport_yang(unittest.TestCase):

#     device = Device(name='aDevice')
#     device1 = Device(name='bDevice')
#     empty_output = {'execute.return_value': ''}
#     golden_parsed_output = {'interface': {'Gigabitethernet0/0': {},
#                'Gigabitethernet1/0/1': {},
#                'Gigabitethernet1/0/10': {'switchport_mode': {'access': {'vlan_id': {'400': {}}}}},
#                'Gigabitethernet1/0/11': {},
#                'Gigabitethernet1/0/12': {},
#                'Gigabitethernet1/0/13': {},
#                'Gigabitethernet1/0/14': {},
#                'Gigabitethernet1/0/15': {},
#                'Gigabitethernet1/0/16': {},
#                'Gigabitethernet1/0/17': {},
#                'Gigabitethernet1/0/18': {},
#                'Gigabitethernet1/0/19': {},
#                'Gigabitethernet1/0/2': {'switchport_mode': {'trunk': {'vlan_id': {'300': {}}}}},
#                'Gigabitethernet1/0/20': {},
#                'Gigabitethernet1/0/21': {},
#                'Gigabitethernet1/0/22': {},
#                'Gigabitethernet1/0/23': {},
#                'Gigabitethernet1/0/24': {},
#                'Gigabitethernet1/0/3': {'switchport_mode': {'trunk': {'vlan_id': {'300': {'allowed_vlans': '400'}}}}},
#                'Gigabitethernet1/0/4': {},
#                'Gigabitethernet1/0/5': {'switchport_mode': {'trunk': {}}},
#                'Gigabitethernet1/0/6': {},
#                'Gigabitethernet1/0/7': {},
#                'Gigabitethernet1/0/8': {},
#                'Gigabitethernet1/0/9': {},
#                'Gigabitethernet1/1/1': {},
#                'Gigabitethernet1/1/2': {},
#                'Gigabitethernet1/1/3': {},
#                'Gigabitethernet1/1/4': {},
#                'Gigabitethernet2/0/1': {},
#                'Gigabitethernet2/0/10': {},
#                'Gigabitethernet2/0/11': {},
#                'Gigabitethernet2/0/12': {},
#                'Gigabitethernet2/0/13': {},
#                'Gigabitethernet2/0/14': {},
#                'Gigabitethernet2/0/15': {'switchport_mode': {'access': {'vlan_id': {'400': {}}}}},
#                'Gigabitethernet2/0/16': {},
#                'Gigabitethernet2/0/17': {},
#                'Gigabitethernet2/0/18': {},
#                'Gigabitethernet2/0/19': {},
#                'Gigabitethernet2/0/2': {},
#                'Gigabitethernet2/0/20': {},
#                'Gigabitethernet2/0/21': {},
#                'Gigabitethernet2/0/22': {},
#                'Gigabitethernet2/0/23': {},
#                'Gigabitethernet2/0/24': {},
#                'Gigabitethernet2/0/3': {},
#                'Gigabitethernet2/0/4': {},
#                'Gigabitethernet2/0/5': {},
#                'Gigabitethernet2/0/6': {},
#                'Gigabitethernet2/0/7': {},
#                'Gigabitethernet2/0/8': {},
#                'Gigabitethernet2/0/9': {},
#                'Gigabitethernet2/1/1': {},
#                'Gigabitethernet2/1/2': {},
#                'Gigabitethernet2/1/3': {},
#                'Gigabitethernet2/1/4': {},
#                'Gigabitethernet3/0/1': {},
#                'Gigabitethernet3/0/10': {},
#                'Gigabitethernet3/0/11': {},
#                'Gigabitethernet3/0/12': {},
#                'Gigabitethernet3/0/13': {},
#                'Gigabitethernet3/0/14': {},
#                'Gigabitethernet3/0/15': {},
#                'Gigabitethernet3/0/16': {},
#                'Gigabitethernet3/0/17': {},
#                'Gigabitethernet3/0/18': {},
#                'Gigabitethernet3/0/19': {},
#                'Gigabitethernet3/0/2': {},
#                'Gigabitethernet3/0/20': {},
#                'Gigabitethernet3/0/21': {},
#                'Gigabitethernet3/0/22': {},
#                'Gigabitethernet3/0/23': {},
#                'Gigabitethernet3/0/24': {},
#                'Gigabitethernet3/0/3': {},
#                'Gigabitethernet3/0/4': {},
#                'Gigabitethernet3/0/5': {},
#                'Gigabitethernet3/0/6': {},
#                'Gigabitethernet3/0/7': {},
#                'Gigabitethernet3/0/8': {},
#                'Gigabitethernet3/0/9': {},
#                'Gigabitethernet3/1/1': {},
#                'Gigabitethernet3/1/2': {},
#                'Gigabitethernet3/1/3': {},
#                'Gigabitethernet3/1/4': {},
#                'Gigabitethernet4/0/1': {},
#                'Gigabitethernet4/0/10': {},
#                'Gigabitethernet4/0/11': {},
#                'Gigabitethernet4/0/12': {},
#                'Gigabitethernet4/0/13': {},
#                'Gigabitethernet4/0/14': {},
#                'Gigabitethernet4/0/15': {},
#                'Gigabitethernet4/0/16': {},
#                'Gigabitethernet4/0/17': {},
#                'Gigabitethernet4/0/18': {},
#                'Gigabitethernet4/0/19': {},
#                'Gigabitethernet4/0/2': {},
#                'Gigabitethernet4/0/20': {},
#                'Gigabitethernet4/0/21': {},
#                'Gigabitethernet4/0/22': {},
#                'Gigabitethernet4/0/23': {},
#                'Gigabitethernet4/0/24': {},
#                'Gigabitethernet4/0/3': {},
#                'Gigabitethernet4/0/4': {},
#                'Gigabitethernet4/0/5': {},
#                'Gigabitethernet4/0/6': {},
#                'Gigabitethernet4/0/7': {},
#                'Gigabitethernet4/0/8': {},
#                'Gigabitethernet4/0/9': {},
#                'Gigabitethernet4/1/1': {},
#                'Gigabitethernet4/1/2': {},
#                'Gigabitethernet4/1/3': {},
#                'Gigabitethernet4/1/4': {},
#                'Gigabitethernet5/0/1': {},
#                'Gigabitethernet5/0/10': {},
#                'Gigabitethernet5/0/11': {},
#                'Gigabitethernet5/0/12': {},
#                'Gigabitethernet5/0/13': {},
#                'Gigabitethernet5/0/14': {},
#                'Gigabitethernet5/0/15': {},
#                'Gigabitethernet5/0/16': {},
#                'Gigabitethernet5/0/17': {},
#                'Gigabitethernet5/0/18': {},
#                'Gigabitethernet5/0/19': {},
#                'Gigabitethernet5/0/2': {},
#                'Gigabitethernet5/0/20': {},
#                'Gigabitethernet5/0/21': {},
#                'Gigabitethernet5/0/22': {},
#                'Gigabitethernet5/0/23': {},
#                'Gigabitethernet5/0/24': {},
#                'Gigabitethernet5/0/3': {},
#                'Gigabitethernet5/0/4': {},
#                'Gigabitethernet5/0/5': {},
#                'Gigabitethernet5/0/6': {},
#                'Gigabitethernet5/0/7': {},
#                'Gigabitethernet5/0/8': {},
#                'Gigabitethernet5/0/9': {},
#                'Gigabitethernet5/1/1': {},
#                'Gigabitethernet5/1/2': {},
#                'Gigabitethernet5/1/3': {},
#                'Gigabitethernet5/1/4': {}}
# }

#     class etree_holder():
#       def __init__(self):
#         self.data = ET.fromstring('''
#           <data>
#             <native xmlns="http://cisco.com/ns/yang/ned/ios">
#               <interface>
#                 <GigabitEthernet>
#                   <name>0/0</name>
#                   <negotiation>
#                     <auto>true</auto>
#                   </negotiation>
#                   <vrf>
#                     <forwarding>Mgmt-vrf</forwarding>
#                   </vrf>
#                   <ip>
#                     <address>
#                       <primary>
#                         <address>10.1.10.20</address>
#                         <mask>255.255.255.0</mask>
#                       </primary>
#                     </address>
#                   </ip>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/1</name>
#                   <switchport-conf>
#                     <switchport>false</switchport>
#                   </switchport-conf>
#                   <ip>
#                     <no-address>
#                       <address>false</address>
#                     </no-address>
#                   </ip>
#                   <standby>
#                     <standby-list>
#                       <group-number>5</group-number>
#                       <priority>110</priority>
#                     </standby-list>
#                   </standby>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/10</name>
#                   <switchport>
#                     <access>
#                       <vlan>
#                         <vlan>400</vlan>
#                       </vlan>
#                     </access>
#                     <mode>
#                       <access/>
#                     </mode>
#                   </switchport>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/11</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/12</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/13</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/14</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/15</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/16</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/17</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/18</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/19</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/2</name>
#                   <switchport>
#                     <access>
#                       <vlan>
#                         <vlan>2</vlan>
#                       </vlan>
#                     </access>
#                     <trunk>
#                       <native>
#                         <vlan>300</vlan>
#                       </native>
#                     </trunk>
#                   </switchport>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/20</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/21</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/22</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/23</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/24</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/3</name>
#                   <switchport>
#                     <access>
#                       <vlan>
#                         <vlan>300</vlan>
#                       </vlan>
#                     </access>
#                     <mode>
#                       <trunk/>
#                     </mode>
#                     <trunk>
#                       <allowed>
#                         <vlan>
#                           <vlans>400</vlans>
#                         </vlan>
#                       </allowed>
#                     </trunk>
#                   </switchport>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/4</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/5</name>
#                   <switchport>
#                     <mode>
#                       <trunk/>
#                     </mode>
#                     <trunk>
#                       <allowed>
#                         <vlan>
#                           <vlans>200,201</vlans>
#                         </vlan>
#                       </allowed>
#                     </trunk>
#                   </switchport>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/6</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/7</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/8</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/0/9</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/1/1</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/1/2</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/1/3</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>1/1/4</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/1</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/10</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/11</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/12</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/13</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/14</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/15</name>
#                   <switchport>
#                     <access>
#                       <vlan>
#                         <vlan>400</vlan>
#                       </vlan>
#                     </access>
#                     <mode>
#                       <access/>
#                     </mode>
#                   </switchport>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/16</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/17</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/18</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/19</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/2</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/20</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/21</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/22</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/23</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/24</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/3</name>
#                   <switchport-conf>
#                     <switchport>false</switchport>
#                   </switchport-conf>
#                   <ip>
#                     <no-address>
#                       <address>false</address>
#                     </no-address>
#                   </ip>
#                   <standby>
#                     <delay>
#                       <minimum>5</minimum>
#                     </delay>
#                     <standby-list>
#                       <group-number>0</group-number>
#                       <name>helsinki</name>
#                     </standby-list>
#                     <standby-list>
#                       <group-number>1</group-number>
#                       <preempt>
#                         <delay>
#                           <minimum>10</minimum>
#                         </delay>
#                       </preempt>
#                     </standby-list>
#                     <standby-list>
#                       <group-number>10</group-number>
#                       <preempt/>
#                     </standby-list>
#                   </standby>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/4</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/5</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/6</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/7</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/8</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/0/9</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/1/1</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/1/2</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/1/3</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>2/1/4</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/1</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/10</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/11</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/12</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/13</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/14</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/15</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/16</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/17</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/18</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/19</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/2</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/20</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/21</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/22</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/23</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/24</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/3</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/4</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/5</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/6</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/7</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/8</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/0/9</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/1/1</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/1/2</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/1/3</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>3/1/4</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/1</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/10</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/11</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/12</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/13</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/14</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/15</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/16</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/17</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/18</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/19</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/2</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/20</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/21</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/22</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/23</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/24</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/3</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/4</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/5</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/6</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/7</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/8</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/0/9</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/1/1</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/1/2</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/1/3</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>4/1/4</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/1</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/10</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/11</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/12</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/13</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/14</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/15</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/16</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/17</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/18</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/19</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/2</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/20</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/21</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/22</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/23</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/24</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/3</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/4</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/5</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/6</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/7</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/8</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/0/9</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/1/1</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/1/2</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/1/3</name>
#                 </GigabitEthernet>
#                 <GigabitEthernet>
#                   <name>5/1/4</name>
#                 </GigabitEthernet>
#               </interface>
#             </native>
#           </data>
#         ''')

#     golden_output = {'get.return_value': etree_holder()}

#     def test_golden(self):
#         self.device = Mock(**self.golden_output)
#         intf_obj = ShowInterfacesSwitchport(device=self.device)
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
#                 <GigabitEthernet>
#                 </GigabitEthernet>
#               </interface>
#             </native>
#           </data>
#         ''')

#     empty_output = {'get.return_value': empty_etree_holder()}

#     def test_empty(self):
#         self.device1 = Mock(**self.empty_output)
#         intf_obj = ShowInterfacesSwitchport(device=self.device1)
#         intf_obj.context = Context.yang.value
#         parsed_output = intf_obj.parse()
#         self.maxDiff = None
#         self.assertEqual(parsed_output,self.empty_parsed_output)

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
                 "in_pause_input": 0,
                 "out_collision": 0,
                 "rate": {
                      "out_rate_pkts": 0,
                      "load_interval": 5,
                      "out_rate": 0,
                      "in_rate": 2000,
                      "in_rate_pkts": 2
                 },
                 "in_watchdog": 0,
                 "out_deferred": 0,
                 "out_pause_output": 0,
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
                 "encapsulation": "arpa"
            },
            "last_input": "never",
            "last_output": "1d22h",
            "line_protocol": "up",
            "mac_address": "0057.d228.1a02",
            "connected": True,
            "port_channel": {
                 "port_channel_member": False
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
                 "in_pause_input": 0,
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
                 "out_pause_output": 0,
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
            "counters": {
                 "out_buffer_failure": 0,
                 "out_underruns": 0,
                 "in_giants": 0,
                 "in_throttles": 0,
                 "in_frame": 0,
                 "in_ignored": 0,
                 "last_clear": "never",
                 "out_interface_resets": 1,
                 "in_pause_input": 0,
                 "out_collision": 0,
                 "in_crc_errors": 0,
                 "rate": {
                      "out_rate_pkts": 0,
                      "load_interval": 5,
                      "out_rate": 0,
                      "in_rate": 0,
                      "in_rate_pkts": 0
                 },
                 "in_watchdog": 0,
                 "out_deferred": 0,
                 "out_pause_output": 0,
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
                 "200.2.1.1/24": {
                      "prefix_length": "24",
                      "ip": "200.2.1.1"
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
                      "load_interval": 5,
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
                 "200.2.1.1/24": {
                      "prefix_length": "24",
                      "ip": "200.2.1.1"
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
                      "load_interval": 5,
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
                 "201.0.12.1/24": {
                      "prefix_length": "24",
                      "ip": "201.0.12.1"
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
                 "in_pause_input": 0,
                 "out_collision": 0,
                 "rate": {
                      "out_rate_pkts": 0,
                      "load_interval": 5,
                      "out_rate": 0,
                      "in_rate": 3000,
                      "in_rate_pkts": 5
                 },
                 "in_watchdog": 0,
                 "out_deferred": 0,
                 "out_pause_output": 0,
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
                 "port_channel_member": False
            },
            "arp_timeout": "04:00:00",
            "bandwidth": 1000000,
            "port_speed": "1000",
            "enabled": True,
            "mtu": 1500,
            "delay": 10,
            "reliability": "255/255"
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
          Interface is unnumbered. Using address of Loopback0 (200.2.1.1)
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
          Internet address is 200.2.1.1/24
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
          Internet address is 201.0.12.1/24
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
          Encapsulation ARPA, loopback not set
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



if __name__ == '__main__':
    unittest.main()