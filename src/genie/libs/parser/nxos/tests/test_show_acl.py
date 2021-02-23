#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.nxos.show_acl import ShowAccessLists, ShowAccessListsSummary

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
            10 permit aaaa.bbff.8888 0000.0000.0000 bbbb.ccff.aaaa bbbb.ccff.aaaa aarp
            20 permit 0000.0000.0000 0000.0000.0000 any
            30 deny 0000.0000.0000 0000.0000.0000 aaaa.bbff.8888 0000.0000.0000 0x8041
            40 deny any any vlan 10
            50 permit aaaa.aaff.5555 ffff.ffff.0000 any aarp
    IP access list test22
            10 permit tcp 192.168.1.0 0.0.0.255 10.4.1.1/32 established log
            20 permit tcp 10.16.2.2/32 eq www any precedence network ttl 255
            30 deny ip any any
    '''}

    parsed_output1 = {
    'acl_name': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
        'type': 'ipv4-acl-type',
    },
    'ipv4_acl': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
            '20': {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
            '30': {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
        'type': 'ipv4-acl-type',
    },
    'ipv4_ext': {
        'name': 'ipv4_ext',
        'type': 'ipv4-acl-type',
    },
    'ipv6_acl': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-syslog',
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
            '20': {
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
            '30': {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
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
            '10': {
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
                            'protocol': 'udp',
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
        'name': 'ipv6_acl2',
        'type': 'ipv6-acl-type',
    },
    'mac_acl': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l2': {
                        'eth': {
                            'destination_mac_address': 'bbbb.ccff.aaaa bbbb.ccff.aaaa',
                            'ether_type': 'aarp',
                            'source_mac_address': 'aaaa.bbff.8888 0000.0000.0000',
                        },
                    },
                },
                'name': '10',
            },
            '20': {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l2': {
                        'eth': {
                            'destination_mac_address': 'any',
                            'source_mac_address': '0000.0000.0000 0000.0000.0000',
                        },
                    },
                },
                'name': '20',
            },
            '30': {
                'actions': {
                    'forwarding': 'deny',
                },
                'matches': {
                    'l2': {
                        'eth': {
                            'destination_mac_address': 'aaaa.bbff.8888 0000.0000.0000',
                            'source_mac_address': '0000.0000.0000 0000.0000.0000',
                            'mac_protocol_number': '0x8041',
                        },
                    },
                },
                'name': '30',
            },
            '40': {
                'actions': {
                    'forwarding': 'deny',
                },
                'matches': {
                    'l2': {
                        'eth': {
                            'destination_mac_address': 'any',
                            'source_mac_address': 'any',
                            'vlan': 10,
                        },
                    },
                },
                'name': '40',
            },
            '50': {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l2': {
                        'eth': {
                            'destination_mac_address': 'any',
                            'ether_type': 'aarp',
                            'source_mac_address': 'aaaa.aaff.5555 ffff.ffff.0000',
                        },
                    },
                },
                'name': '50',
            },
        },
        'name': 'mac_acl',
        'type': 'eth-acl-type',
    },
    'test22': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'destination_network': {
                                '10.4.1.1/32': {
                                    'destination_network': '10.4.1.1/32',
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
            '20': {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'precedence': 'network',
                            'protocol': 'tcp',
                            'source_network': {
                                '10.16.2.2/32': {
                                    'source_network': '10.16.2.2/32',
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
            '30': {
                'actions': {
                    'forwarding': 'deny',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
        'type': 'ipv4-acl-type',
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
            '10': {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
                'statistics': {
                    'matched_packets': 0,
                },
            },
            '20': {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
            '40': {
                'actions': {
                    'forwarding': 'permit',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
        'type': 'ipv4-acl-type',
    },
}

    device_output3 = {'execute.return_value': '''
    IPV4 ACL 1
    10 remark NTP Access
    20 permit ip 10.1.1.39/32 any
    30 permit ip 172.16.154.23/32 any
    '''}

    parsed_output3 = {
        '1': {
            'aces': {
                '30': {
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'ip',
                                'source_network': {
                                    '172.16.154.23/32': {
                                        'source_network': '172.16.154.23/32',
                                    },
                                },
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any',
                                    },
                                },
                            },
                        },
                    },
                    'name': '30',
                    'actions': {
                        'forwarding': 'permit',
                    },
                },
                '20': {
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'ip',
                                'source_network': {
                                    '10.1.1.39/32': {
                                        'source_network': '10.1.1.39/32',
                                    },
                                },
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any',
                                    },
                                },
                            },
                        },
                    },
                    'name': '20',
                    'actions': {
                        'forwarding': 'permit',
                    },
                },
            },
            'type': 'ipv4-acl-type',
            'name': '1',
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

    def test_golden3(self):
        self.maxDiff = None
        self.dev = Mock(**self.device_output3)
        obj = ShowAccessLists(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.parsed_output3)

class TestShowAccessListsSummary(unittest.TestCase):
    dev = Device(name='device')
    empty_output = {'execute.return_value': ''}

    device_output = {'execute.return_value': '''
    Device# show access-lists summary 
IPV4 ACL acl_name
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL ipv4_acl
        Total ACEs Configured: 3
        Configured on interfaces:
                Ethernet1/1 - egress (Router ACL)
        Active on interfaces:
                Ethernet1/1 - egress (Router ACL)
IPV4 ACL ipv4_ext
        Total ACEs Configured: 0
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL ipv6_acl
        Total ACEs Configured: 3
        Configured on interfaces:
                Ethernet1/1 - ingress (Router ACL)
        Active on interfaces:
                Ethernet1/1 - ingress (Router ACL)
IPV6 ACL ipv6_acl2
        Total ACEs Configured: 1
        Configured on interfaces:
                Ethernet1/1 - egress (Router ACL)
        Active on interfaces:
                Ethernet1/1 - egress (Router ACL)
MAC ACL mac_acl
        Total ACEs Configured: 5
        Configured on interfaces:
                Ethernet1/1 - ingress (Port ACL)
        Active on interfaces:
IPV4 ACL sl_def_acl

        Statistics enabled
        Total ACEs Configured: 4
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL test22
        Total ACEs Configured: 3
        Configured on interfaces:
                Ethernet1/1 - ingress (Router ACL)
        Active on interfaces:
                Ethernet1/1 - ingress (Router ACL)
    '''}

    parsed_output = {
    'acl': {
        'acl_name': {
            'total_aces_configured': 1,
        },
        'ipv4_ext': {
            'total_aces_configured': 0,
        },
    },
    'attachment_points': {
        'Ethernet1/1': {
            'egress': {
                'ipv4_acl': {
                    'total_aces_configured': 3,
                    'active': True,
                    'name': 'ipv4_acl',
                    'type': 'Router ACL',
                },
                'ipv6_acl2': {
                    'total_aces_configured': 1,
                    'active': True,
                    'name': 'ipv6_acl2',
                    'type': 'Router ACL',
                },
            },
            'ingress': {
                'ipv6_acl': {
                    'total_aces_configured': 3,
                    'active': True,
                    'name': 'ipv6_acl',
                    'type': 'Router ACL',
                },
                'mac_acl': {
                    'total_aces_configured': 5,
                    'active': True,
                    'name': 'mac_acl',
                    'type': 'Port ACL',
                },
                'test22': {
                    'total_aces_configured': 3,
                    'active': True,
                    'name': 'test22',
                    'type': 'Router ACL',
                },
            },
            'interface_id': 'Ethernet1/1',
        },
    },
}

    device_output2 = {'execute.return_value': '''
+++ executing command 'show access-lists summary' +++
show access-lists summary

IPV4 ACL 23
        Total ACEs Configured: 13
        Configured on interfaces:
                VTY         - ingress
        Active on interfaces:
                VTY         - ingress
IPV4 ACL Deny-any
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL FROM_AD_LAB_ESX
        Total ACEs Configured: 17
        Configured on interfaces:
                Vlan125 - ingress (Router ACL)
        Active on interfaces:
                Vlan125 - ingress (Router ACL)
IPV4 ACL TO_AD_LAB_ESX
        Total ACEs Configured: 17
        Configured on interfaces:
                Vlan125 - egress (Router ACL)
        Active on interfaces:
                Vlan125 - egress (Router ACL)
IPV4 ACL __urpf_v4_acl__
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL __urpf_v6_acl__
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-bgp
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-bgp6
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-cts
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-dhcp
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-dhcp-relay-response
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-dhcp6
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-dhcp6-relay-response
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-eigrp
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-eigrp6
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-ftp
        Total ACEs Configured: 4
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-glbp
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-hsrp
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-hsrp6
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-http-response
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-http6-response
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-icmp
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-icmp6
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-igmp
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-lisp
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-lisp6
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-cdp-udld-vtp
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-cfsoe
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-dot1x
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-fabricpath-isis
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-fcoe
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-flow-control
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-l2-tunnel
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-l2pt
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-l3-isis
        Total ACEs Configured: 3
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-lacp
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-lldp
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-mvrp
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-otv-isis
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-sdp-srp
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-stp
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
MAC ACL copp-system-p-acl-mac-undesirable
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-mld
        Total ACEs Configured: 4
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-mpls-ldp
        Total ACEs Configured: 3
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-mpls-oam
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-mpls-rsvp
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-msdp
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-ndp
        Total ACEs Configured: 5
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-ntp
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-ntp6
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-ospf
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-ospf6
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-otv-as
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-pim
        Total ACEs Configured: 3
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-pim-mdt-join
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-pim-reg
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-pim6
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-pim6-reg
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-radius
        Total ACEs Configured: 8
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-radius6
        Total ACEs Configured: 8
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-rip
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-rip6
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-rise
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-rise6
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-sftp
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-smtp-response
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-smtp6-response
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-snmp
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-ssh
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-ssh6
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-tacacs
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-tacacs6
        Total ACEs Configured: 2
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-telnet
        Total ACEs Configured: 4
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-telnet6
        Total ACEs Configured: 4
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-tftp
        Total ACEs Configured: 4
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-tftp6
        Total ACEs Configured: 4
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-traceroute
        Total ACEs Configured: 3
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-undesirable
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-vpc
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-vrrp
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV6 ACL copp-system-p-acl-vrrp6
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL copp-system-p-acl-wccp
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL ctrlNet
        Total ACEs Configured: 1
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL jtienm
        Total ACEs Configured: 3
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL jtinms
        Total ACEs Configured: 0
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL jtisnmp
        Total ACEs Configured: 11
        Configured on interfaces:
        Active on interfaces:
IPV4 ACL sl_def_acl

        Statistics enabled
        Total ACEs Configured: 4
        Configured on interfaces:
        Active on interfaces:
    '''}


    parsed_output2 = {
        "acl": {
            "Deny-any": {
                "total_aces_configured": 1
            },
            "__urpf_v4_acl__": {
                "total_aces_configured": 1
            },
            "__urpf_v6_acl__": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-bgp": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-bgp6": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-cts": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-dhcp": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-dhcp-relay-response": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-dhcp6": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-dhcp6-relay-response": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-eigrp": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-eigrp6": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-ftp": {
                "total_aces_configured": 4
            },
            "copp-system-p-acl-glbp": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-hsrp": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-hsrp6": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-http-response": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-http6-response": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-icmp": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-icmp6": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-igmp": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-lisp": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-lisp6": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-mac-cdp-udld-vtp": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-mac-cfsoe": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-mac-dot1x": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-mac-fabricpath-isis": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-mac-fcoe": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-mac-flow-control": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-mac-l2-tunnel": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-mac-l2pt": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-mac-l3-isis": {
                "total_aces_configured": 3
            },
            "copp-system-p-acl-mac-lacp": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-mac-lldp": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-mac-mvrp": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-mac-otv-isis": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-mac-sdp-srp": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-mac-stp": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-mac-undesirable": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-mld": {
                "total_aces_configured": 4
            },
            "copp-system-p-acl-mpls-ldp": {
                "total_aces_configured": 3
            },
            "copp-system-p-acl-mpls-oam": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-mpls-rsvp": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-msdp": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-ndp": {
                "total_aces_configured": 5
            },
            "copp-system-p-acl-ntp": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-ntp6": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-ospf": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-ospf6": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-otv-as": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-pim": {
                "total_aces_configured": 3
            },
            "copp-system-p-acl-pim-mdt-join": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-pim-reg": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-pim6": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-pim6-reg": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-radius": {
                "total_aces_configured": 8
            },
            "copp-system-p-acl-radius6": {
                "total_aces_configured": 8
            },
            "copp-system-p-acl-rip": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-rip6": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-rise": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-rise6": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-sftp": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-smtp-response": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-smtp6-response": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-snmp": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-ssh": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-ssh6": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-tacacs": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-tacacs6": {
                "total_aces_configured": 2
            },
            "copp-system-p-acl-telnet": {
                "total_aces_configured": 4
            },
            "copp-system-p-acl-telnet6": {
                "total_aces_configured": 4
            },
            "copp-system-p-acl-tftp": {
                "total_aces_configured": 4
            },
            "copp-system-p-acl-tftp6": {
                "total_aces_configured": 4
            },
            "copp-system-p-acl-traceroute": {
                "total_aces_configured": 3
            },
            "copp-system-p-acl-undesirable": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-vpc": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-vrrp": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-vrrp6": {
                "total_aces_configured": 1
            },
            "copp-system-p-acl-wccp": {
                "total_aces_configured": 1
            },
            "ctrlNet": {
                "total_aces_configured": 1
            },
            "jtienm": {
                "total_aces_configured": 3
            },
            "jtinms": {
                "total_aces_configured": 0
            },
            "jtisnmp": {
                "total_aces_configured": 11
            }
        },
        "attachment_points": {
            "VTY": {
                "ingress": {
                    "23": {
                        "active": True,
                        "name": "23",
                        "total_aces_configured": 13
                    }
                },
                "interface_id": "VTY"
            },
            "Vlan125": {
                "egress": {
                    "TO_AD_LAB_ESX": {
                        "active": True,
                        "name": "TO_AD_LAB_ESX",
                        "total_aces_configured": 17,
                        "type": "Router ACL"
                    }
                },
                "ingress": {
                    "FROM_AD_LAB_ESX": {
                        "active": True,
                        "name": "FROM_AD_LAB_ESX",
                        "total_aces_configured": 17,
                        "type": "Router ACL"
                    }
                },
                "interface_id": "Vlan125"
            }
        }
    }

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowAccessListsSummary(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.device_output)
        obj = ShowAccessListsSummary(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.parsed_output)

    def test_golden2(self):
        self.maxDiff = None
        self.dev = Mock(**self.device_output2)
        obj = ShowAccessListsSummary(device=self.dev)
        parsed_output2 = obj.parse()
        self.assertEqual(parsed_output2,self.parsed_output2)
