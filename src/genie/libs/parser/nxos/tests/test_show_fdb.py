#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.nxos.show_fdb import ShowMacAddressTableVni


class test_show_mac_address_table_vni(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'mac_address':
                              {'0000.04b1.0000':
                                {'entry': 'C',
                                 'evi': '1001',
                                 'mac_aging_time': '0',
                                 'mac_type': 'dynamic',
                                 'next_hop': '10.9.0.101',
                                 'ntfy': 'F',
                                 'ports': 'None',
                                 'secure': 'F'}
                              }
                            }

    golden_output = {'execute.return_value': '''\
      CH-P2-TOR-1# sh mac address-table vni 2001001 | grep nve1 
      C 1001     0000.04b1.0000   dynamic  0         F      F    nve1(10.9.0.101)
    '''
    }

    golden_parsed_output_1 = {'mac_address':
                                {'0000.0191.0000':
                                    {'entry': '*',
                                     'evi': '1001',
                                     'mac_aging_time': '0',
                                     'mac_type': 'dynamic',
                                     'next_hop': 'None',
                                     'ntfy': 'F',
                                     'ports': 'Eth1/11',
                                     'secure': 'F'},
                                '00f1.0000.0000':
                                    {'entry': '*',
                                     'evi': '1001',
                                     'mac_aging_time': '0',
                                     'mac_type': 'dynamic',
                                     'next_hop': 'None',
                                     'ntfy': 'F',
                                     'ports': 'Eth1/11',
                                     'secure': 'F'},
                                '00f5.0000.0000':
                                    {'entry': '*',
                                     'evi': '1001',
                                     'mac_aging_time': '0',
                                     'mac_type': 'dynamic',
                                     'next_hop': 'None',
                                     'ntfy': 'F',
                                     'ports': 'Eth1/11',
                                     'secure': 'F'}
                                }
                            }

    golden_output_1 = {'execute.return_value': '''\
        CH-P2-TOR-1# sh mac address-table local vni 2001001 
        Legend: 
                * - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC
                age - seconds since last seen,+ - primary entry using vPC Peer-Link,
                (T) - True, (F) - False, C - ControlPlane MAC, ~ - vsan
           VLAN     MAC Address      Type      age     Secure NTFY Ports
        ---------+-----------------+--------+---------+------+----+------------------
        * 1001     0000.0191.0000   dynamic  0         F      F    Eth1/11
        * 1001     00f1.0000.0000   dynamic  0         F      F    Eth1/11
        * 1001     00f5.0000.0000   dynamic  0         F      F    Eth1/11
    '''
    }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowMacAddressTableVni(device=self.device)
        parsed_output = obj.parse(vni='2001001', intf='nve1')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowMacAddressTableVni(device=self.device)
        parsed_output = obj.parse(vni='2001001')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMacAddressTableVni(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vni='2001001', intf='nve1')


if __name__ == '__main__':
    unittest.main()