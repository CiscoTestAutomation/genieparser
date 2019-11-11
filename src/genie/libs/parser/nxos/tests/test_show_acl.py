#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.nxos.show_acl import ShowAccessLists

class TestShowAccessLists(unittest.TestCase):
    dev = Device(name='device')
    empty_output = {'execute.return_value': ''}

    device_output1 = {'execute.return_value': '''
    R3_n9kv# show access-lists

    IP access list acl_name
            10 permit ip any any
    IP access list ipv4_acl
            10 permit tcp any any eq www
            20 permit tcp any any eq 22
            30 permit tcp any any eq 443
    IP access list ipv4_ext
    IPv6 access list ipv6_acl
            10 permit ipv6 any any log
            20 permit ipv6 2001::1/128 2001:1::2/128
            30 permit tcp any eq 8443 2001:2::2/128
    IPv6 access list ipv6_acl2
            10 permit udp any any
    MAC access list mac_acl
            10 permit aaaa.bbbb.cccc 0000.0000.0000 bbbb.cccc.dddd bbbb.cccc.dddd aa
    rp
            20 permit 0000.0000.0000 0000.0000.0000 any
            30 deny 0000.0000.0000 0000.0000.0000 aaaa.bbbb.cccc 0000.0000.0000 0x80
    41
            40 deny any any vlan 10
            50 permit aaaa.aaaa.aaaa ffff.ffff.0000 any aarp
    IP access list test22
            10 permit tcp 192.168.1.0 0.0.0.255 1.1.1.1/32 established log
            20 permit tcp 2.2.2.2/32 eq www any precedence network ttl 255
            30 deny ip any any
    '''}

    parsed_output1 = {
    'acl_name': {
        'aces': {
            10: {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ip': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'ip',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                },
                'name': '10',
            },
        },
        'name': 'acl_name',
        'type': 'ip-acl-type',
    },
    'ipv4_acl': {
        'aces': {
            10: {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'tcp': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'tcp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'tcp': {
                            'destination_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': 'www',
                                },
                            },
                        },
                    },
                },
                'name': '10',
            },
            20: {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'tcp': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'tcp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'tcp': {
                            'destination_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': '22',
                                },
                            },
                        },
                    },
                },
                'name': '20',
            },
            30: {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'tcp': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'tcp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'tcp': {
                            'destination_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': '443',
                                },
                            },
                        },
                    },
                },
                'name': '30',
            },
        },
        'name': 'ipv4_acl',
        'type': 'ip-acl-type',
    },
    'ipv4_ext': {
        'name': 'ipv4_ext',
        'type': 'ip-acl-type',
    },
    'ipv6_acl': {
        'aces': {
            10: {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'ipv6',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                },
                'name': '10',
            },
            20: {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                '2001:1::2/128': {
                                    'destination_network': '2001:1::2/128',
                                },
                            },
                            'protocol': 'ipv6',
                            'source_network': {
                                '2001::1/128': {
                                    'source_network': '2001::1/128',
                                },
                            },
                        },
                    },
                },
                'name': '20',
            },
            30: {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'tcp': {
                            'destination_network': {
                                '2001:2::2/128': {
                                    'destination_network': '2001:2::2/128',
                                },
                            },
                            'protocol': 'tcp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'tcp': {
                            'source_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': '8443',
                                },
                            },
                        },
                    },
                },
                'name': '30',
            },
        },
        'name': 'ipv6_acl',
        'type': 'ipv6-acl-type',
    },
    'ipv6_acl2': {
        'aces': {
            10: {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l2': {
                        'eth': {
                            'destination_mac_address': 'any',
                            'ether_type': 'aarp',
                            'source_mac_address': 'aaaa.aaaa.aaaa ffff.ffff.0000',
                            'vlan': 10,
                        },
                    },
                    'l3': {
                        'udp': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'udp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                },
                'name': '50',
            },
        },
        'name': 'ipv6_acl2',
        'type': 'ipv6-acl-type',
    },
    'mac_acl': {
        'name': 'mac_acl',
        'type': 'mac-acl-type',
    },
    'test22': {
        'aces': {
            10: {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'tcp': {
                            'destination_network': {
                                '1.1.1.1/32': {
                                    'destination_network': '1.1.1.1/32',
                                },
                            },
                            'protocol': 'tcp',
                            'source_network': {
                                '192.168.1.0 0.0.0.255': {
                                    'source_network': '192.168.1.0 0.0.0.255',
                                },
                            },
                        },
                    },
                    'l4': {
                        'tcp': {
                            'established': True,
                        },
                    },
                },
                'name': '10',
            },
            20: {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'tcp': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'precedence': 'network',
                            'protocol': 'tcp',
                            'source_network': {
                                '2.2.2.2/32': {
                                    'source_network': '2.2.2.2/32',
                                },
                            },
                            'ttl': 255,
                        },
                    },
                    'l4': {
                        'tcp': {
                            'source_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': 'www',
                                },
                            },
                        },
                    },
                },
                'name': '20',
            },
            30: {
                'actions': {
                    'forwarding': 'deny',
                },
                'matches': {
                    'l3': {
                        'ip': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'ip',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                },
                'name': '30',
            },
        },
        'name': 'test22',
        'type': 'ip-acl-type',
    },
}

    device_output2 = {'execute.return_value': '''
    Router# show access-list NTP-ACL

IP access list NTP-ACL
        statistics per-entry 
        10 permit ip 10.1.50.64/32 any [match=0] 
        20 permit ip 172.18.106.1/32 any [match=4] 
        40 permit ip any any [match=4] '''}

    parsed_output2 = {
    'NTP-ACL': {
        'aces': {
            10: {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ip': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'ip',
                            'source_network': {
                                '10.1.50.64/32': {
                                    'source_network': '10.1.50.64/32',
                                },
                            },
                        },
                    },
                },
                'name': '10',
            },
            20: {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ip': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'ip',
                            'source_network': {
                                '172.18.106.1/32': {
                                    'source_network': '172.18.106.1/32',
                                },
                            },
                        },
                    },
                },
                'name': '20',
                'statistics': {
                    'matched_packets': 4,
                },
            },
            40: {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ip': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'ip',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                },
                'name': '40',
                'statistics': {
                    'matched_packets': 4,
                },
            },
        },
        'name': 'NTP-ACL',
        'type': 'ip-acl-type',
    },
}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowAccessLists(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.device_output1)
        obj = ShowAccessLists(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.parsed_output1)

    def test_golden2(self):
        self.maxDiff = None
        self.dev = Mock(**self.device_output2)
        obj = ShowAccessLists(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.parsed_output2)
