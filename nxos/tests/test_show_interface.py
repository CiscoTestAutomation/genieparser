import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError

from parser.nxos.show_interface import ShowIpInterfaceBrief, \
                                                  ShowIpInterfaceBriefPipeVlan, \
                                                  ShowInterfaceSwitchport, \
                                                  ShowInterfaceBrief


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

class test_show_interface_switchport(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'interface': 
    {'Ethernet4/5': 
        {'switchport_mode': {'access': {'vlan_id': {'1': {}}}}},
     'port-channel30': 
        {'switchport_mode': {'trunk': {'vlan_id': {'1': {}}}}}
    }
}

    golden_output = {'execute.return_value': '''
Name: Ethernet4/5
  Switchport: Enabled
  Switchport Monitor: Not enabled 
  Operational Mode: access
  Access Mode VLAN: 1 (default)
  Trunking Native Mode VLAN: 1 (default)
  Trunking VLANs Allowed: none
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
Name: port-channel30
  Switchport: Enabled
  Switchport Monitor: Not enabled 
  Operational Mode: trunk
  Access Mode VLAN: 1 (default)
  Trunking Native Mode VLAN: 1 (default)
  Trunking VLANs Allowed: 1-101,200,401-4094
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

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowInterfaceSwitchport(device=self.device)
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowInterfaceSwitchport(device=self.device1)
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