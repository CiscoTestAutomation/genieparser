#!/usr/bin/python3
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
                                                    ShowInterfacesDescription)

#############################################################################
# unitest For show ipv4 vrf all interface
#############################################################################

class test_show_ipv4_vrf_all_interface(unittest.TestCase):

    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
'GigabitEthernet0/0/0/0': {'int_status': 'up',
                            'ipv4': {'192.168.1.242/24': {'ip': '192.168.1.242',
                                                          'prefix_length': '24'},
                                     'broadcast_forwarding': 'disabled',
                                     'icmp_redirects': 'never sent',
                                     'icmp_replies': 'never sent',
                                     'icmp_unreachables': 'always sent',
                                     'mtu': 1514,
                                     'mtu_available': 1500,
                                     'proxy_arp': 'disabled',
                                     'table_id': '0xe0000003'},
                            'multicast_groups': ['224.0.0.5', '224.0.0.6'],
                            'oper_status': 'up',
                            'vrf': 'VRF1:111',
                            'vrf_id': '0x60000003'},
 'GigabitEthernet0/0/0/1': {'int_status': 'up',
                            'ipv4': {'192.168.2.249/24': {'ip': '192.168.2.249',
                                                          'prefix_length': '24'},
                                     'broadcast_forwarding': 'disabled',
                                     'icmp_redirects': 'never sent',
                                     'icmp_replies': 'never sent',
                                     'icmp_unreachables': 'always sent',
                                     'mtu': 1514,
                                     'mtu_available': 1500,
                                     'proxy_arp': 'disabled',
                                     'table_id': '0xe0000000'},
                            'multicast_groups': ['224.0.0.2'],
                            'oper_status': 'up',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/2': {'int_status': 'shutdown',
                            'oper_status': 'down',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/3': {'int_status': 'shutdown',
                            'oper_status': 'down',
                            'vrf': 'V20:MBN',
                            'vrf_id': '0x0'},
 'GigabitEthernet0/0/0/4': {'int_status': 'shutdown',
                            'oper_status': 'down',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/5': {'int_status': 'shutdown',
                            'oper_status': 'down',
                            'vrf': 'default',
                            'vrf_id': '0x60000000'},
 'GigabitEthernet0/0/0/6': {'int_status': 'shutdown',
                            'oper_status': 'down',
                            'vrf': 'bobby',
                            'vrf_id': '0x60000001'},
 'MgmtEth0/RP0/CPU0/0': {'int_status': 'up',
                         'oper_status': 'up',
                         'vrf': 'bobby',
                         'vrf_id': '0x60000001'},
}



    golden_output = {'execute.return_value': '''
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

if __name__ == '__main__':
    unittest.main()










