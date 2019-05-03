#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.nxos.show_fdb import ShowMacAddressTableVni, ShowMacAddressTable, \
    ShowMacAddressTableAgingTime, ShowMacAddressTableLimit, ShowSystemInternalL2fwderMac


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
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowMacAddressTableVni(device=self.device)
        parsed_output = obj.parse(vni='2001001')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMacAddressTableVni(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vni='2001001', intf='nve1')


class test_show_mac_address_table_aging_time(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'mac_aging_time': 120}

    golden_output = {'execute.return_value': '''\
        N95_1# show mac address-table aging-time 
        Aging Time
        ----------
            120
    '''
                     }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowMacAddressTableAgingTime(device=self.device)
        # import pdb; pdb.set_trace()
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMacAddressTableAgingTime(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_mac_address_table(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'mac_address': {'0000.dead.beef': {'entry': 'G',
                                                               'evi': '-',
                                                               'mac_aging_time': '-',
                                                               'mac_type': 'static',
                                                               'next_hop': 'None',
                                                               'ntfy': 'F',
                                                               'ports': 'sup-eth1(R)',
                                                               'secure': 'F'},
                                            '5e00.c000.0007': {'entry': 'G',
                                                               'evi': '1009',
                                                               'mac_aging_time': '-',
                                                               'mac_type': 'static',
                                                               'next_hop': 'None',
                                                               'ntfy': 'F',
                                                               'ports': 'sup-eth1(R)',
                                                               'secure': 'F'},
                                            'aaaa.bbbb.cccc': {'entry': '*',
                                                               'evi': '30',
                                                               'mac_aging_time': '-',
                                                               'mac_type': 'static',
                                                               'next_hop': 'None',
                                                               'ntfy': 'F',
                                                               'ports': 'Drop',
                                                               'secure': 'F'}}}

    golden_output = {'execute.return_value': '''\
    N95_1# show mac address-table 
    Legend: 
            * - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC
            age - seconds since last seen,+ - primary entry using vPC Peer-Link,
            (T) - True, (F) - False, C - ControlPlane MAC, ~ - vsan
       VLAN     MAC Address      Type      age     Secure NTFY Ports
    ---------+-----------------+--------+---------+------+----+------------------
    *   10     aaaa.bbbb.cccc   static   -         F      F    Eth1/2
    *   20     aaaa.bbbb.cccc   static   -         F      F    Drop
    *   30     aaaa.bbbb.cccc   static   -         F      F    Drop
    G    -     0000.dead.beef   static   -         F      F    sup-eth1(R)
    G    -     5e00.c000.0007   static   -         F      F     (R)
    G    -     5e00.c000.0007   static   -         F      F    sup-eth1(R) (Lo0)
    G  100     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G  101     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G  102     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G  103     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G  105     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G  106     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G  107     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G  108     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G  109     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G  110     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G  111     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G  112     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G  113     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G  114     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G 1000     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G 1005     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G 1006     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G 1007     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G 1008     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    G 1009     5e00.c000.0007   static   -         F      F    sup-eth1(R)
    '''
                     }

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowMacAddressTable(device=self.device)

        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMacAddressTable(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_mac_address_table_limit(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'configured_system_action': 'Flood',
                            'configured_system_limit': 111,
                            'current_system_count': 3,
                            'currently_system_is': 'Flooding Unknown SA',
                            'mac_table': {'vlans': {'1': {'cfg_action': 'Flood',
                                                          'conf_limit': 196000,
                                                          'curr_count': 0,
                                                          'currently': 'Flooding Unknown SA',
                                                          'vlan': 1},
                                                    '10': {'cfg_action': 'Flood',
                                                           'conf_limit': 196000,
                                                           'curr_count': 1,
                                                           'currently': 'Flooding Unknown SA',
                                                           'vlan': 10},
                                                    '100': {'cfg_action': 'Flood',
                                                            'conf_limit': 200,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 100},
                                                    '1000': {'cfg_action': 'Flood',
                                                             'conf_limit': 196000,
                                                             'curr_count': 0,
                                                             'currently': 'Flooding Unknown SA',
                                                             'vlan': 1000},
                                                    '1005': {'cfg_action': 'Flood',
                                                             'conf_limit': 196000,
                                                             'curr_count': 0,
                                                             'currently': 'Flooding Unknown SA',
                                                             'vlan': 1005},
                                                    '1006': {'cfg_action': 'Flood',
                                                             'conf_limit': 196000,
                                                             'curr_count': 0,
                                                             'currently': 'Flooding Unknown SA',
                                                             'vlan': 1006},
                                                    '1007': {'cfg_action': 'Flood',
                                                             'conf_limit': 196000,
                                                             'curr_count': 0,
                                                             'currently': 'Flooding Unknown SA',
                                                             'vlan': 1007},
                                                    '1008': {'cfg_action': 'Flood',
                                                             'conf_limit': 196000,
                                                             'curr_count': 0,
                                                             'currently': 'Flooding Unknown SA',
                                                             'vlan': 1008},
                                                    '1009': {'cfg_action': 'Flood',
                                                             'conf_limit': 196000,
                                                             'curr_count': 0,
                                                             'currently': 'Flooding Unknown SA',
                                                             'vlan': 1009},
                                                    '101': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 101},
                                                    '102': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 102},
                                                    '103': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 103},
                                                    '104': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 104},
                                                    '105': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 105},
                                                    '106': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 106},
                                                    '107': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 107},
                                                    '108': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 108},
                                                    '109': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 109},
                                                    '110': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 110},
                                                    '111': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 111},
                                                    '112': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 112},
                                                    '113': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 113},
                                                    '114': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 114},
                                                    '115': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 115},
                                                    '185': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 185},
                                                    '20': {'cfg_action': 'Flood',
                                                           'conf_limit': 196000,
                                                           'curr_count': 1,
                                                           'currently': 'Flooding Unknown SA',
                                                           'vlan': 20},
                                                    '285': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 285},
                                                    '30': {'cfg_action': 'Flood',
                                                           'conf_limit': 196000,
                                                           'curr_count': 1,
                                                           'currently': 'Flooding Unknown SA',
                                                           'vlan': 30},
                                                    '910': {'cfg_action': 'Flood',
                                                            'conf_limit': 196000,
                                                            'curr_count': 0,
                                                            'currently': 'Flooding Unknown SA',
                                                            'vlan': 910}}}
                            }

    golden_output = {'execute.return_value': '''\
        N95_1# show mac address-table limit 
         
        Configured System Limit: 111
        Current System Count: 3
        Configured System Action: Flood
        Currently System is: Flooding Unknown SA
         
         
        Vlan    Conf Limit     Curr Count    Cfg Action    Currently
        ----    ------------   ---------     ---------    --------
        1       196000              0           Flood         Flooding Unknown SA
        10      196000              1           Flood         Flooding Unknown SA
        20      196000              1           Flood         Flooding Unknown SA
        30      196000              1           Flood         Flooding Unknown SA
        100     200               0           Flood         Flooding Unknown SA
        101     196000              0           Flood         Flooding Unknown SA
        102     196000              0           Flood         Flooding Unknown SA
        103     196000              0           Flood         Flooding Unknown SA
        104     196000              0           Flood         Flooding Unknown SA
        105     196000              0           Flood         Flooding Unknown SA
        106     196000              0           Flood         Flooding Unknown SA
        107     196000              0           Flood         Flooding Unknown SA
        108     196000              0           Flood         Flooding Unknown SA
        109     196000              0           Flood         Flooding Unknown SA
        110     196000              0           Flood         Flooding Unknown SA
        111     196000              0           Flood         Flooding Unknown SA
        112     196000              0           Flood         Flooding Unknown SA
        113     196000              0           Flood         Flooding Unknown SA
        114     196000              0           Flood         Flooding Unknown SA
        115     196000              0           Flood         Flooding Unknown SA
        185     196000              0           Flood         Flooding Unknown SA
        285     196000              0           Flood         Flooding Unknown SA
        910     196000              0           Flood         Flooding Unknown SA
        1000    196000              0           Flood         Flooding Unknown SA
        1005    196000              0           Flood         Flooding Unknown SA
        1006    196000              0           Flood         Flooding Unknown SA
        1007    196000              0           Flood         Flooding Unknown SA
        1008    196000              0           Flood         Flooding Unknown SA
        1009    196000              0           Flood         Flooding Unknown SA
    '''
                     }

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowMacAddressTableLimit(device=self.device)
        # import pdb; pdb.set_trace()
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMacAddressTableLimit(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_system_internal_l2fwder_mac(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'mac_table': {'vlans': {'-': {'entry': 'G',
                                                          'mac_address': '5e00:c000:0007',
                                                          'mac_aging_time': '-',
                                                          'mac_type': 'static',
                                                          'ntfy': 'F',
                                                          'ports': 'sup-eth1(R)',
                                                          'secure': 'F',
                                                          'vlan': '-'},
                                                    '1': {'entry': '*',
                                                          'mac_address': 'fa16.3eef.6e79',
                                                          'mac_aging_time': '00:01:02',
                                                          'mac_type': 'dynamic',
                                                          'ntfy': 'F',
                                                          'ports': 'Eth1/4',
                                                          'secure': 'F',
                                                          'vlan': '1'},
                                                    '10': {'entry': '*',
                                                           'mac_address': 'aaaa.bbbb.cccc',
                                                           'mac_aging_time': '-',
                                                           'mac_type': 'static',
                                                           'ntfy': 'F',
                                                           'ports': 'Eth1/2',
                                                           'secure': 'F',
                                                           'vlan': '10'},
                                                    '100': {'entry': '*',
                                                            'mac_address': 'fa16.3eef.6e79',
                                                            'mac_aging_time': '00:05:38',
                                                            'mac_type': 'dynamic',
                                                            'ntfy': 'F',
                                                            'ports': 'Eth1/4',
                                                            'secure': 'F',
                                                            'vlan': '100'},
                                                    '1000': {'entry': 'G',
                                                             'mac_address': '5e00.c000.0007',
                                                             'mac_aging_time': '-',
                                                             'mac_type': 'static',
                                                             'ntfy': 'F',
                                                             'ports': 'sup-eth1(R)',
                                                             'secure': 'F',
                                                             'vlan': '1000'},
                                                    '1005': {'entry': 'G',
                                                             'mac_address': '5e00.c000.0007',
                                                             'mac_aging_time': '-',
                                                             'mac_type': 'static',
                                                             'ntfy': 'F',
                                                             'ports': 'sup-eth1(R)',
                                                             'secure': 'F',
                                                             'vlan': '1005'},
                                                    '1006': {'entry': 'G',
                                                             'mac_address': '5e00.c000.0007',
                                                             'mac_aging_time': '-',
                                                             'mac_type': 'static',
                                                             'ntfy': 'F',
                                                             'ports': 'sup-eth1(R)',
                                                             'secure': 'F',
                                                             'vlan': '1006'},
                                                    '1007': {'entry': 'G',
                                                             'mac_address': '5e00.c000.0007',
                                                             'mac_aging_time': '-',
                                                             'mac_type': 'static',
                                                             'ntfy': 'F',
                                                             'ports': 'sup-eth1(R)',
                                                             'secure': 'F',
                                                             'vlan': '1007'},
                                                    '1008': {'entry': 'G',
                                                             'mac_address': '5e00.c000.0007',
                                                             'mac_aging_time': '-',
                                                             'mac_type': 'static',
                                                             'ntfy': 'F',
                                                             'ports': 'sup-eth1(R)',
                                                             'secure': 'F',
                                                             'vlan': '1008'},
                                                    '1009': {'entry': 'G',
                                                             'mac_address': '5e00.c000.0007',
                                                             'mac_aging_time': '-',
                                                             'mac_type': 'static',
                                                             'ntfy': 'F',
                                                             'ports': 'sup-eth1(R)',
                                                             'secure': 'F',
                                                             'vlan': '1009'},
                                                    '101': {'entry': 'G',
                                                            'mac_address': '5e00.c000.0007',
                                                            'mac_aging_time': '-',
                                                            'mac_type': 'static',
                                                            'ntfy': 'F',
                                                            'ports': 'sup-eth1(R)',
                                                            'secure': 'F',
                                                            'vlan': '101'},
                                                    '102': {'entry': 'G',
                                                            'mac_address': '5e00.c000.0007',
                                                            'mac_aging_time': '-',
                                                            'mac_type': 'static',
                                                            'ntfy': 'F',
                                                            'ports': 'sup-eth1(R)',
                                                            'secure': 'F',
                                                            'vlan': '102'},
                                                    '103': {'entry': 'G',
                                                            'mac_address': '5e00.c000.0007',
                                                            'mac_aging_time': '-',
                                                            'mac_type': 'static',
                                                            'ntfy': 'F',
                                                            'ports': 'sup-eth1(R)',
                                                            'secure': 'F',
                                                            'vlan': '103'},
                                                    '105': {'entry': 'G',
                                                            'mac_address': '5e00.c000.0007',
                                                            'mac_aging_time': '-',
                                                            'mac_type': 'static',
                                                            'ntfy': 'F',
                                                            'ports': 'sup-eth1(R)',
                                                            'secure': 'F',
                                                            'vlan': '105'},
                                                    '106': {'entry': 'G',
                                                            'mac_address': '5e00.c000.0007',
                                                            'mac_aging_time': '-',
                                                            'mac_type': 'static',
                                                            'ntfy': 'F',
                                                            'ports': 'sup-eth1(R)',
                                                            'secure': 'F',
                                                            'vlan': '106'},
                                                    '107': {'entry': 'G',
                                                            'mac_address': '5e00.c000.0007',
                                                            'mac_aging_time': '-',
                                                            'mac_type': 'static',
                                                            'ntfy': 'F',
                                                            'ports': 'sup-eth1(R)',
                                                            'secure': 'F',
                                                            'vlan': '107'},
                                                    '108': {'entry': 'G',
                                                            'mac_address': '5e00.c000.0007',
                                                            'mac_aging_time': '-',
                                                            'mac_type': 'static',
                                                            'ntfy': 'F',
                                                            'ports': 'sup-eth1(R)',
                                                            'secure': 'F',
                                                            'vlan': '108'},
                                                    '109': {'entry': 'G',
                                                            'mac_address': '5e00.c000.0007',
                                                            'mac_aging_time': '-',
                                                            'mac_type': 'static',
                                                            'ntfy': 'F',
                                                            'ports': 'sup-eth1(R)',
                                                            'secure': 'F',
                                                            'vlan': '109'},
                                                    '110': {'entry': 'G',
                                                            'mac_address': '5e00.c000.0007',
                                                            'mac_aging_time': '-',
                                                            'mac_type': 'static',
                                                            'ntfy': 'F',
                                                            'ports': 'sup-eth1(R)',
                                                            'secure': 'F',
                                                            'vlan': '110'},
                                                    '111': {'entry': 'G',
                                                            'mac_address': '5e00.c000.0007',
                                                            'mac_aging_time': '-',
                                                            'mac_type': 'static',
                                                            'ntfy': 'F',
                                                            'ports': 'sup-eth1(R)',
                                                            'secure': 'F',
                                                            'vlan': '111'},
                                                    '112': {'entry': 'G',
                                                            'mac_address': '5e00.c000.0007',
                                                            'mac_aging_time': '-',
                                                            'mac_type': 'static',
                                                            'ntfy': 'F',
                                                            'ports': 'sup-eth1(R)',
                                                            'secure': 'F',
                                                            'vlan': '112'},
                                                    '113': {'entry': 'G',
                                                            'mac_address': '5e00.c000.0007',
                                                            'mac_aging_time': '-',
                                                            'mac_type': 'static',
                                                            'ntfy': 'F',
                                                            'ports': 'sup-eth1(R)',
                                                            'secure': 'F',
                                                            'vlan': '113'},
                                                    '114': {'entry': 'G',
                                                            'mac_address': '5e00.c000.0007',
                                                            'mac_aging_time': '-',
                                                            'mac_type': 'static',
                                                            'ntfy': 'F',
                                                            'ports': 'sup-eth1(R)',
                                                            'secure': 'F',
                                                            'vlan': '114'}}}}

    golden_output = {'execute.return_value': '''\
        N95_1# show system internal l2fwder mac
        Legend: 
                * - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC
                age - seconds since last seen,+ - primary entry using vPC Peer-Link,
                (T) - True, (F) - False, C - ControlPlane MAC
           VLAN     MAC Address      Type      age     Secure NTFY Ports
        ---------+-----------------+--------+---------+------+----+------------------
        G   114    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G   112    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G   113    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G   110    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G   111    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G   108    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G   109    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G   106    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G   107    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G   105    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G   102    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G   103    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G   100    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G   101    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G     -    5e00:c000:0007    static   -          F     F   sup-eth1(R)
        *     1    fa16.3eef.6e79   dynamic   00:01:02   F     F     Eth1/4  
        *   100    fa16.3eef.6e79   dynamic   00:05:38   F     F     Eth1/4  
        G  1008    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G  1009    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G  1006    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G  1007    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G  1005    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        G  1000    5e00.c000.0007    static   -          F     F   sup-eth1(R)
        *    10    aaaa.bbbb.cccc    static   -          F     F     Eth1/2  
            1           1         -00:00:de:ad:be:ef         -             1
    '''
                     }

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowSystemInternalL2fwderMac(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemInternalL2fwderMac(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
