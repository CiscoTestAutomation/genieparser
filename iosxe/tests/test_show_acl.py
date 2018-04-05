#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from parser.iosxe.show_acl import ShowAccessLists


class test_show_access_lists(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'acl_name': {'aces': {'10': {'actions': {'forwarding': 'permit',
                                               'logging': 'log-none'},
                                      'matches': {'l3': {'ipv4': {'destination_ipv4_network': {'any': {'destination_ipv4_network': 'any'}},
                                                                  'protocol': 'ipv4',
                                                                  'source_ipv4_network': {'any': {'source_ipv4_network': 'any'}}}},
                                                  'l4': {'ipv4': {'established': False,
                                                                  'sequence_number': 10}}},
                                      'name': '10',
                                      'statistics': {'matched_packets': 10031}}},
                      'name': 'acl_name',
                      'type': 'ipv4-acl-type'},
         'ipv4_acl': {'aces': {'10': {'actions': {'forwarding': 'permit',
                                               'logging': 'log-none'},
                                      'matches': {'l3': {'tcp': {'destination_ipv4_network': {'any': {'destination_ipv4_network': 'any'}},
                                                                 'protocol': 'tcp',
                                                                 'source_ipv4_network': {'any': {'source_ipv4_network': 'any'}}}},
                                                  'l4': {'tcp': {'destination_port': {'operator': {'operator': 'eq',
                                                                                                   'port': 80}},
                                                                 'established': False,
                                                                 'sequence_number': 10}}},
                                      'name': '10'},
                               '20': {'actions': {'forwarding': 'permit',
                                               'logging': 'log-none'},
                                      'matches': {'l3': {'tcp': {'destination_ipv4_network': {'any': {'destination_ipv4_network': 'any'}},
                                                                 'protocol': 'tcp',
                                                                 'source_ipv4_network': {'any': {'source_ipv4_network': 'any'}}}},
                                                  'l4': {'tcp': {'destination_port': {'operator': {'operator': 'eq',
                                                                                                   'port': 22}},
                                                                 'established': False,
                                                                 'sequence_number': 20}}},
                                      'name': '20'}},
                      'name': 'ipv4_acl',
                      'type': 'ipv4-acl-type'},
         'test1': {'aces': {'10': {'actions': {'forwarding': 'permit',
                                               'logging': 'log-syslog'},
                                   'matches': {'l3': {'pim': {'destination_ipv4_network': {'any': {'destination_ipv4_network': 'any'}},
                                                              'dscp': 'default',
                                                              'protocol': 'pim',
                                                              'source_ipv4_network': {'any': {'source_ipv4_network': 'any'}}}},
                                               'l4': {'pim': {'established': False,
                                                              'sequence_number': 10}}},
                                   'name': '10'},
                            '20': {'actions': {'forwarding': 'permit',
                                               'logging': 'log-none'},
                                   'matches': {'l3': {'icmp': {'source_ipv4_network': {'0.1.1.1 255.0.0.0': {'source_ipv4_network': '0.1.1.1 '
                                                                                                                                              '255.0.0.0'}},
                                                               'protocol': 'icmp',
                                                               'destination_ipv4_network': {'any': {'destination_ipv4_network': 'any'}}}},
                                               'l4': {'icmp': {'code': 66,
                                                               'established': False,
                                                               'sequence_number': 20,
                                                               'type': 10}}},
                                   'name': '20'}},
                   'name': 'test1',
                   'type': 'ipv4-acl-type'},
         'test22': {'aces': {'10': {'actions': {'forwarding': 'permit',
                                               'logging': 'log-syslog'},
                                    'matches': {'l3': {'tcp': {'source_ipv4_network': {'192.168.1.0 0.0.0.255': {'source_ipv4_network': '192.168.1.0 '
                                                                                                                                                  '0.0.0.255'}},
                                                               'protocol': 'tcp',
                                                               'destination_ipv4_network': {'1.1.1.1': {'destination_ipv4_network': '1.1.1.1'}}}},
                                                'l4': {'tcp': {'established': True,
                                                               'sequence_number': 10}}},
                                    'name': '10'},
                             '20': {'actions': {'forwarding': 'permit',
                                               'logging': 'log-none'},
                                    'matches': {'l3': {'tcp': {'destination_ipv4_network': {'any': {'destination_ipv4_network': 'any'}},
                                                               'precedence': 'network',
                                                               'protocol': 'tcp',
                                                               'source_ipv4_network': {'2.2.2.2': {'source_ipv4_network': '2.2.2.2'}},
                                                               'ttl': 255,
                                                               'ttl_operator': 'eq'}},
                                                'l4': {'tcp': {'established': False,
                                                               'sequence_number': 20,
                                                               'source_port': {'operator': {'operator': 'eq',
                                                                                            'port': 'www telnet 443'}}}}},
                                    'name': '20'},
                             '30': {'actions': {'forwarding': 'deny',
                                               'logging': 'log-none'},
                                    'matches': {'l3': {'ipv4': {'destination_ipv4_network': {'any': {'destination_ipv4_network': 'any'}},
                                                                'protocol': 'ipv4',
                                                                'source_ipv4_network': {'any': {'source_ipv4_network': 'any'}}}},
                                                'l4': {'ipv4': {'established': False,
                                                                'sequence_number': 30}}},
                                    'name': '30'},
                             '40': {'actions': {'forwarding': 'permit',
                                               'logging': 'log-none'},
                                    'matches': {'l3': {'tcp': {'destination_ipv4_network': {'any': {'destination_ipv4_network': 'any'}},
                                                               'protocol': 'tcp',
                                                               'source_ipv4_network': {'any': {'source_ipv4_network': 'any'}}}},
                                                'l4': {'tcp': {'established': False,
                                                               'sequence_number': 40,
                                                               'source_port': {'range': {'lower_port': 20,
                                                                                         'upper_port': 179}}}}},
                                    'name': '40'}},
                    'name': 'test22',
                    'type': 'ipv4-acl-type'},
          'ipv6_acl': {'aces': {'20': {'actions': {'forwarding': 'permit',
                                                  'logging': 'log-none'},
                                      'matches': {'l3': {'ipv6': {'destination_ipv4_network': {'2001:1::2': {'destination_ipv4_network': '2001:1::2'}},
                                                                  'protocol': 'ipv6',
                                                                  'source_ipv4_network': {'2001::1': {'source_ipv4_network': '2001::1'}}}},
                                                  'l4': {'ipv6': {'established': False,
                                                                  'sequence_number': 20}}},
                                      'name': '20'},
                               '30': {'actions': {'forwarding': 'permit',
                                                  'logging': 'log-none'},
                                      'matches': {'l3': {'tcp': {'destination_ipv4_network': {'2001:2::2': {'destination_ipv4_network': '2001:2::2'}},
                                                                 'protocol': 'tcp',
                                                                 'source_ipv4_network': {'any': {'source_ipv4_network': 'any'}}}},
                                                  'l4': {'tcp': {'established': False,
                                                                 'sequence_number': 30,
                                                                 'source_port': {'operator': {'operator': 'eq',
                                                                                              'port': 'www '
                                                                                                      '8443'}}}}},
                                      'name': '30'},
                               '80': {'actions': {'forwarding': 'permit',
                                                  'logging': 'log-syslog'},
                                      'matches': {'l3': {'ipv6': {'destination_ipv4_network': {'1:1::1 6:6::6': {'destination_ipv4_network': '1:1::1 '
                                                                                                                                             '6:6::6'}},
                                                                  'protocol': 'ipv6',
                                                                  'source_ipv4_network': {'3:3::3 4:4::4': {'source_ipv4_network': '3:3::3 '
                                                                                                                                   '4:4::4'}}}},
                                                  'l4': {'ipv6': {'established': False,
                                                                  'sequence_number': 80}}},
                                      'name': '80'}},
                      'name': 'ipv6_acl',
                      'type': 'ipv6-acl-type'},
         'preauth_v6': {'aces': {'10': {'actions': {'forwarding': 'permit',
                                                    'logging': 'log-none'},
                                        'matches': {'l3': {'udp': {'destination_ipv4_network': {'any': {'destination_ipv4_network': 'any'}},
                                                                   'protocol': 'udp',
                                                                   'source_ipv4_network': {'any': {'source_ipv4_network': 'any'}}}},
                                                    'l4': {'udp': {'destination_port': {'operator': {'operator': 'eq',
                                                                                                     'port': 53}},
                                                                   'established': False,
                                                                   'sequence_number': 10}}},
                                        'name': '10'},
                                 '20': {'actions': {'forwarding': 'permit',
                                                    'logging': 'log-syslog'},
                                        'matches': {'l3': {'esp': {'destination_ipv4_network': {'any': {'destination_ipv4_network': 'any'}},
                                                                   'dscp': 'cs7',
                                                                   'protocol': 'esp',
                                                                   'source_ipv4_network': {'any': {'source_ipv4_network': 'any'}}}},
                                                    'l4': {'esp': {'established': False,
                                                                   'sequence_number': 20}}},
                                        'name': '20'},
                                 '30': {'actions': {'forwarding': 'deny',
                                                    'logging': 'log-none'},
                                        'matches': {'l3': {'ipv6': {'destination_ipv4_network': {'any': {'destination_ipv4_network': 'any'}},
                                                                    'protocol': 'ipv6',
                                                                    'source_ipv4_network': {'any': {'source_ipv4_network': 'any'}}}},
                                                    'l4': {'ipv6': {'established': False,
                                                                    'sequence_number': 30}}},
                                        'name': '30'}},
                        'name': 'preauth_v6',
                        'per_user': True,
                        'type': 'ipv6-acl-type'},
             'mac_acl': {'aces': {'10': {'actions': {'forwarding': 'permit',
                                                     'logging': 'log-none'},
                                         'matches': {'l2': {'eth': {'destination_mac_address': 'any',
                                                                    'source_mac_address': 'any'}}},
                                         'name': '10'},
                                  '20': {'actions': {'forwarding': 'deny',
                                                     'logging': 'log-none'},
                                         'matches': {'l2': {'eth': {'destination_mac_address': 'any',
                                                                    'ether_type': 'msdos',
                                                                    'source_mac_address': 'any'}}},
                                         'name': '20'},
                                  '30': {'actions': {'forwarding': 'deny',
                                                     'logging': 'log-none'},
                                         'matches': {'l2': {'eth': {'destination_mac_address': 'any',
                                                                    'source_mac_address': 'any',
                                                                    'vlan': 10}}},
                                         'name': '30'},
                                  '40': {'actions': {'forwarding': 'permit',
                                                     'logging': 'log-none'},
                                         'matches': {'l2': {'eth': {'destination_mac_address': '0003.0003.0003',
                                                                    'lsap': '0x1 '
                                                                            '0xD8FE',
                                                                    'source_mac_address': '0001.0002.0033'}}},
                                         'name': '40'},
                                  '50': {'actions': {'forwarding': 'permit',
                                                     'logging': 'log-none'},
                                         'matches': {'l2': {'eth': {'cos': 4,
                                                                    'destination_mac_address': 'any',
                                                                    'ether_type': 'aarp',
                                                                    'source_mac_address': 'any',
                                                                    'vlan': 20}}},
                                         'name': '50'}},
                         'name': 'mac_acl',
                         'type': 'eth-acl-type'}
    }

    golden_output = {'execute.return_value': '''\
        Extended IP access list acl_name
            10 permit ip any any (10031 matches)
        Extended IP access list ipv4_acl
            10 permit tcp any any eq www
            20 permit tcp any any eq 22
        Extended IP access list test1
            10 permit pim any any dscp default option 222 log
            20 permit icmp 0.1.1.1 255.0.0.0 any 10 66
        Extended IP access list test22
            10 permit tcp 192.168.1.0 0.0.0.255 host 1.1.1.1 established log
            20 permit tcp host 2.2.2.2 eq www telnet 443 any precedence network ttl eq 255
            30 deny ip any any
            40 permit tcp any range ftp-data bgp any
        IPv6 access list ipv6_acl
            permit ipv6 host 2001::1 host 2001:1::2 sequence 20
            permit tcp any eq www 8443 host 2001:2::2 sequence 30
            permit ipv6 3:3::3 4:4::4 1:1::1 6:6::6 log sequence 80
        IPv6 access list preauth_v6 (per-user)
            permit udp any any eq domain sequence 10
            permit esp any any dscp cs7 log sequence 20
            deny ipv6 any any sequence 30
        Extended MAC access list mac_acl 
            permit any any
            deny   any any msdos
            deny   any any vlan 10
            permit host 0001.0002.0033 host 0003.0003.0003 lsap 0x1 0xD8FE
            permit any any aarp cos 4 vlan 20
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowAccessLists(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowAccessLists(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()

