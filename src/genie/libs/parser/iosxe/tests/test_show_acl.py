#!/bin/env python
import unittest

from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_acl import ShowAccessLists, \
                                             ShowIpAccessLists, \
                                             ShowIpv6AccessLists


class TestShowAccessLists(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
    'acl_name': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'ipv4',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv4': {
                            'established': False,
                        },
                    },
                },
                'name': '10',
                'statistics': {
                    'matched_packets': 10031,
                },
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
                    'logging': 'log-none',
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
                                    'port': 80,
                                },
                            },
                            'established': False,
                        },
                    },
                },
                'name': '10',
            },
            '20': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
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
                                    'port': 22,
                                },
                            },
                            'established': False,
                        },
                    },
                },
                'name': '20',
            },
        },
        'name': 'ipv4_acl',
        'type': 'ipv4-acl-type',
    },
    'test1': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-syslog',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'dscp': 'default',
                            'protocol': 'pim',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'pim': {
                            'established': False,
                        },
                    },
                },
                'name': '10',
            },
            '20': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'source_network': {
                                '0.1.1.1 255.0.0.0': {
                                    'source_network': '0.1.1.1 255.0.0.0',
                                },
                            },
                            'protocol': 'icmp',
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'icmp': {
                            'code': 66,
                            'established': False,
                            'type': 10,
                        },
                    },
                },
                'name': '20',
            },
        },
        'name': 'test1',
        'type': 'ipv4-acl-type',
    },
    'test22': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-syslog',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'source_network': {
                                '192.168.1.0 0.0.0.255': {
                                    'source_network': '192.168.1.0 0.0.0.255',
                                },
                            },
                            'protocol': 'tcp',
                            'destination_network': {
                                'host 10.4.1.1': {
                                    'destination_network': 'host 10.4.1.1',
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
                    'logging': 'log-none',
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
                                'host 10.16.2.2': {
                                    'source_network': 'host 10.16.2.2',
                                },
                            },
                            'ttl': 255,
                            'ttl_operator': 'eq',
                        },
                    },
                    'l4': {
                        'tcp': {
                            'established': False,
                            'source_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': 'www telnet 443',
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
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'ipv4',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv4': {
                            'established': False,
                        },
                    },
                },
                'name': '30',
            },
            '40': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
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
                            'established': False,
                            'source_port': {
                                'range': {
                                    'lower_port': 20,
                                    'upper_port': 179,
                                },
                            },
                        },
                    },
                },
                'name': '40',
            },
        },
        'name': 'test22',
        'type': 'ipv4-acl-type',
    },
    'ipv6_acl': {
        'aces': {
            '20': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'host 2001:1::2': {
                                    'destination_network': 'host 2001:1::2',
                                },
                            },
                            'protocol': 'ipv6',
                            'source_network': {
                                'host 2001::1': {
                                    'source_network': 'host 2001::1',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv6': {
                            'established': False,
                        },
                    },
                },
                'name': '20',
            },
            '30': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'host 2001:2::2': {
                                    'destination_network': 'host 2001:2::2',
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
                            'established': False,
                            'source_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': 'www 8443',
                                },
                            },
                        },
                    },
                },
                'name': '30',
            },
            '80': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-syslog',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                '2001:db8:1:1::1 2001:db8:24:24::6': {
                                    'destination_network': '2001:db8:1:1::1 2001:db8:24:24::6',
                                },
                            },
                            'protocol': 'ipv6',
                            'source_network': {
                                '2001:db8:9:9::3 2001:db8:10:10::4': {
                                    'source_network': '2001:db8:9:9::3 2001:db8:10:10::4',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv6': {
                            'established': False,
                        },
                    },
                },
                'name': '80',
            },
        },
        'name': 'ipv6_acl',
        'type': 'ipv6-acl-type',
    },
    'preauth_v6': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
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
                    'l4': {
                        'udp': {
                            'destination_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': 53,
                                },
                            },
                            'established': False,
                        },
                    },
                },
                'name': '10',
            },
            '20': {
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
                            'dscp': 'cs7',
                            'protocol': 'esp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'esp': {
                            'established': False,
                        },
                    },
                },
                'name': '20',
            },
            '30': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
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
                    'l4': {
                        'ipv6': {
                            'established': False,
                        },
                    },
                },
                'name': '30',
            },
        },
        'name': 'preauth_v6',
        'per_user': True,
        'type': 'ipv6-acl-type',
    },
    'mac_acl': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l2': {
                        'eth': {
                            'destination_mac_address': 'any',
                            'source_mac_address': 'any',
                        },
                    },
                },
                'name': '10',
            },
            '20': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l2': {
                        'eth': {
                            'destination_mac_address': 'any',
                            'ether_type': 'msdos',
                            'source_mac_address': 'any',
                        },
                    },
                },
                'name': '20',
            },
            '30': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
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
                'name': '30',
            },
            '40': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l2': {
                        'eth': {
                            'destination_mac_address': 'host 0003.0003.0003',
                            'lsap': '0x1 0xD8FE',
                            'source_mac_address': 'host 0001.0002.0033',
                        },
                    },
                },
                'name': '40',
            },
            '50': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l2': {
                        'eth': {
                            'cos': 4,
                            'destination_mac_address': 'any',
                            'ether_type': 'aarp',
                            'source_mac_address': 'any',
                            'vlan': 20,
                        },
                    },
                },
                'name': '50',
            },
        },
        'name': 'mac_acl',
        'type': 'eth-acl-type',
    },
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
            10 permit tcp 192.168.1.0 0.0.0.255 host 10.4.1.1 established log
            20 permit tcp host 10.16.2.2 eq www telnet 443 any precedence network ttl eq 255
            30 deny ip any any
            40 permit tcp any range ftp-data bgp any
        IPv6 access list ipv6_acl
            permit ipv6 host 2001::1 host 2001:1::2 sequence 20
            permit tcp any eq www 8443 host 2001:2::2 sequence 30
            permit ipv6 2001:db8:9:9::3 2001:db8:10:10::4 2001:db8:1:1::1 2001:db8:24:24::6 log sequence 80
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

    golden_ip_access_list_output = {'execute.return_value': '''\
    Router#show ip access-lists ACL_TEST
Load for five secs: 1%/0%; one minute: 2%; five minutes: 2%
Time source is NTP, 18:12:32.965 EST Mon Oct 17 2016

Extended IP access list ACL_TEST
    10 deny tcp 10.69.188.0 0.0.0.255 host 192.168.16.1 eq www
    20 deny tcp 10.4.1.0 0.0.0.255 host 192.168.16.1 eq www
    30 deny tcp 10.4.2.0 0.0.0.255 host 192.168.16.1 eq www
    40 deny tcp 10.4.3.0 0.0.0.255 host 192.168.16.1 eq www
    50 deny tcp 10.4.4.0 0.0.0.255 host 192.168.16.1 eq www
    60 deny tcp 10.4.5.0 0.0.0.255 host 192.168.16.1 eq www
    70 deny tcp 10.4.6.0 0.0.0.255 host 192.168.16.1 eq www
    80 deny tcp 10.4.7.0 0.0.0.255 host 192.168.16.1 eq www
    90 deny tcp 10.4.8.0 0.0.0.255 host 192.168.16.1 eq www
    100 deny tcp 10.4.9.0 0.0.0.255 host 192.168.16.1 eq www
    110 deny tcp 10.4.10.0 0.0.0.255 host 192.168.16.1 eq www
    120 deny tcp 10.4.11.0 0.0.0.255 host 192.168.16.1 eq www
    130 deny tcp 10.4.12.0 0.0.0.255 host 192.168.16.1 eq www
    140 deny tcp 10.4.13.0 0.0.0.255 host 192.168.16.1 eq www
    150 deny tcp 10.4.14.0 0.0.0.255 host 192.168.16.1 eq www
    160 deny tcp 10.4.15.0 0.0.0.255 host 192.168.16.1 eq www
    170 deny tcp 10.4.16.0 0.0.0.255 host 192.168.16.1 eq www

    '''}
    golden_parsed_ip_access_list_output = {
        "ACL_TEST": {
                "aces": {
                    "80": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.7.0 0.0.0.255": {
                                            "source_network": "10.4.7.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "80"
                    },
                    "50": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.4.0 0.0.0.255": {
                                            "source_network": "10.4.4.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "50"
                    },
                    "10": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.69.188.0 0.0.0.255": {
                                            "source_network": "10.69.188.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "10"
                    },
                    "130": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.12.0 0.0.0.255": {
                                            "source_network": "10.4.12.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "130"
                    },
                    "90": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.8.0 0.0.0.255": {
                                            "source_network": "10.4.8.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "90"
                    },
                    "40": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.3.0 0.0.0.255": {
                                            "source_network": "10.4.3.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "40"
                    },
                    "150": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.14.0 0.0.0.255": {
                                            "source_network": "10.4.14.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "150"
                    },
                    "30": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.2.0 0.0.0.255": {
                                            "source_network": "10.4.2.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "30"
                    },
                    "120": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.11.0 0.0.0.255": {
                                            "source_network": "10.4.11.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "120"
                    },
                    "100": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.9.0 0.0.0.255": {
                                            "source_network": "10.4.9.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "100"
                    },
                    "170": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.16.0 0.0.0.255": {
                                            "source_network": "10.4.16.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "170"
                    },
                    "160": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.15.0 0.0.0.255": {
                                            "source_network": "10.4.15.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "160"
                    },
                    "20": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.1.0 0.0.0.255": {
                                            "source_network": "10.4.1.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "20"
                    },
                    "70": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.6.0 0.0.0.255": {
                                            "source_network": "10.4.6.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "70"
                    },
                    "110": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.10.0 0.0.0.255": {
                                            "source_network": "10.4.10.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "110"
                    },
                    "140": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.13.0 0.0.0.255": {
                                            "source_network": "10.4.13.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "140"
                    },
                    "60": {
                        "actions": {
                            "forwarding": "deny",
                            "logging": "log-none"
                        },
                        "matches": {
                            "l3": {
                                "ipv4": {
                                    "source_network": {
                                        "10.4.5.0 0.0.0.255": {
                                            "source_network": "10.4.5.0 0.0.0.255"
                                        }
                                    },
                                    "protocol": "tcp",
                                    "destination_network": {
                                        "host 192.168.16.1": {
                                            "destination_network": "host 192.168.16.1"
                                        }
                                    }
                                }
                            },
                            "l4": {
                                "tcp": {
                                    "destination_port": {
                                        "operator": {
                                            "operator": "eq",
                                            "port": 80
                                        }
                                    },
                                    "established": False
                                }
                            }
                        },
                        "name": "60"
                    }
                },
                "type": "ipv4-acl-type",
                "name": "ACL_TEST"
            }
        }


    golden_ipv6_access_list_output = {'execute.return_value':'''\
    Router# show ipv6 access-list OutFilter_IPv6
IPv6 access list OutFilter_IPv6
    permit icmp any any mld-query sequence 30
    permit icmp any any router-advertisement sequence 40
    deny 103 any any sequence 50
    permit icmp any any packet-too-big sequence 60
    deny icmp any any sequence 70
    deny ipv6 2001:DB8:B30A:DC63::/64 any sequence 74
    deny ipv6 2001:DB8:B30A:F442::/64 any sequence 75
    permit ipv6 any 2001:db8:1d14::/16 log-input sequence 80
    deny ipv6 2001:DB8:B30A:FE9B::/64 any sequence 90
    deny ipv6 2001:DB8:B30A:213::/64 any sequence 100
    deny ipv6 2001:db8:5254:1000::/35 2001:db8:5254:1000::/35 dscp default sequence 110
    permit ipv6 any any (3974749339 matches) sequence 120
    '''}

    golden_parsed_ipv6_access_list_output = {
     "OutFilter_IPv6": {
          "aces": {
               "120": {
                    "statistics": {
                         "matched_packets": 3974749339
                    },
                    "matches": {
                         "l4": {
                              "ipv6": {
                                   "established": False
                              }
                         },
                         "l3": {
                              "ipv6": {
                                   "destination_network": {
                                        "any": {
                                             "destination_network": "any"
                                        }
                                   },
                                   "source_network": {
                                        "any": {
                                             "source_network": "any"
                                        }
                                   },
                                   "protocol": "ipv6"
                              }
                         }
                    },
                    "actions": {
                         "forwarding": "permit",
                         "logging": "log-none"
                    },
                    "name": "120"
               },
               "30": {
                    "matches": {
                         "l4": {
                              "icmp": {
                                   "established": False
                              }
                         },
                         "l3": {
                              "ipv6": {
                                   "destination_network": {
                                        "any": {
                                             "destination_network": "any"
                                        }
                                   },
                                   "source_network": {
                                        "any": {
                                             "source_network": "any"
                                        }
                                   },
                                   "protocol": "icmp"
                              }
                         }
                    },
                    "actions": {
                         "forwarding": "permit",
                         "logging": "log-none"
                    },
                    "name": "30"
               },
                '100': {
                    'actions': {
                        'forwarding': 'deny',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv6': {
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                },
                                'protocol': 'ipv6',
                                'source_network': {
                                    '2001:DB8:B30A:213::/64': {
                                        'source_network': '2001:DB8:B30A:213::/64'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'ipv6': {
                                'established': False
                            }
                        }
                    },
                    'name': '100'
                },
                '110': {
                    'actions': {
                        'forwarding': 'deny',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv6': {
                                'destination_network': {
                                    '2001:db8:5254:1000::/35': {
                                        'destination_network': '2001:db8:5254:1000::/35'
                                    }
                                },
                                'dscp': 'default',
                                'protocol': 'ipv6',
                                'source_network': {
                                    '2001:db8:5254:1000::/35': {
                                        'source_network': '2001:db8:5254:1000::/35'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'ipv6': {
                                'established': False
                            }
                        }
                    },
                    'name': '110'
                },
               "90": {
                    "matches": {
                         "l2": {
                              "eth": {
                                   "source_mac_address": "ipv6",
                                   "destination_mac_address": "2404",
                                   "ether_type": ":2001:DB8:F442:121::/64 any sequence 75"
                              }
                         }
                    },
                    "actions": {
                         "forwarding": "deny",
                         "logging": "log-none"
                    },
                    "name": "90"
               },
               "80": {
                    "matches": {
                         "l2": {
                              "eth": {
                                   "source_mac_address": "ipv6",
                                   "destination_mac_address": "2404",
                                   "ether_type": ":2001:DB8:DC63:121::/64 any sequence 74"
                              }
                         }
                    },
                    "actions": {
                         "forwarding": "deny",
                         "logging": "log-none"
                    },
                    "name": "80"
               },
               "70": {
                    "matches": {
                         "l4": {
                              "icmp": {
                                   "established": False
                              }
                         },
                         "l3": {
                              "ipv6": {
                                   "destination_network": {
                                        "any": {
                                             "destination_network": "any"
                                        }
                                   },
                                   "source_network": {
                                        "any": {
                                             "source_network": "any"
                                        }
                                   },
                                   "protocol": "icmp"
                              }
                         }
                    },
                    "actions": {
                         "forwarding": "deny",
                         "logging": "log-none"
                    },
                    "name": "70"
               },
               "50": {
                    "matches": {
                         "l2": {
                              "eth": {
                                   "source_mac_address": "103",
                                   "destination_mac_address": "any",
                                   "ether_type": "any sequence 50"
                              }
                         }
                    },
                    "actions": {
                         "forwarding": "deny",
                         "logging": "log-none"
                    },
                    "name": "50"
               },
               "60": {
                    "matches": {
                         "l4": {
                              "icmp": {
                                   "established": False
                              }
                         },
                         "l3": {
                              "ipv6": {
                                   "destination_network": {
                                        "any": {
                                             "destination_network": "any"
                                        }
                                   },
                                   "source_network": {
                                        "any": {
                                             "source_network": "any"
                                        }
                                   },
                                   "protocol": "icmp"
                              }
                         }
                    },
                    "actions": {
                         "forwarding": "permit",
                         "logging": "log-none"
                    },
                    "name": "60"
               },
               "40": {
                    "matches": {
                         "l4": {
                              "icmp": {
                                   "established": False
                              }
                         },
                         "l3": {
                              "ipv6": {
                                   "destination_network": {
                                        "any": {
                                             "destination_network": "any"
                                        }
                                   },
                                   "source_network": {
                                        "any": {
                                             "source_network": "any"
                                        }
                                   },
                                   "protocol": "icmp"
                              }
                         }
                    },
                    "actions": {
                         "forwarding": "permit",
                         "logging": "log-none"
                    },
                    "name": "40"
               },
               '75': {
                   'actions': {
                       'forwarding': 'deny',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv6': {
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                },
                                'protocol': 'ipv6',
                                'source_network': {
                                    '2001:DB8:B30A:F442::/64': {
                                        'source_network': '2001:DB8:B30A:F442::/64'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'ipv6': {
                                'established': False
                            }
                        }
                    },
                    'name': '75'
                },
                '74': {
                    'actions': {
                        'forwarding': 'deny',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv6': {
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                },
                                'protocol': 'ipv6',
                                'source_network': {
                                    '2001:DB8:B30A:DC63::/64': {
                                        'source_network': '2001:DB8:B30A:DC63::/64'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'ipv6': {
                                'established': False
                            }
                        }
                    },
                    'name': '74'
                },
                '80': {
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-syslog'
                    },
                    'matches': {
                        'l3': {
                            'ipv6': {
                                'destination_network': {
                                    '2001:db8:1d14::/16': {
                                        'destination_network': '2001:db8:1d14::/16'
                                    }
                                },
                                'protocol': 'ipv6',
                                'source_network': {
                                    'any': {
                                        'source_network': 'any'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'ipv6': {
                                'established': False
                            }
                        }
                    },
                    'name': '80'
                },
                '90': {
                    'actions': {
                        'forwarding': 'deny',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv6': {
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                },
                                'protocol': 'ipv6',
                                'source_network': {
                                    '2001:DB8:B30A:FE9B::/64': {
                                        'source_network': '2001:DB8:B30A:FE9B::/64'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'ipv6': {
                                'established': False
                            }
                        }
                    },
                    'name': '90'
                },
          },
          "name": "OutFilter_IPv6",
          "type": "ipv6-acl-type"
     }
}

    golden_ipv6_access_list_all_output = {'execute.return_value': '''\
        Device> show ipv6 access-list
            IPv6 access list inbound
                permit tcp any any eq bgp (8 matches) sequence 10
                permit tcp any any eq telnet (15 matches) sequence 20
                permit udp any any sequence 30
            IPv6 access list Virtual-Access2.1#427819008151 (per-user)
                permit tcp host 2001:DB8:1::32 eq bgp host 2001:DB8:2::32 eq 11000 sequence 1
                permit tcp host 2001:DB8:1::32 eq telnet host 2001:DB8:2::32 eq 11001 sequence 2
    '''
    }

    golden_parsed_ipv6_access_list_all_output = {
        "inbound": {
            "aces": {
                "10": {
                    "statistics": {
                        "matched_packets": 8
                    },
                    "matches": {
                        "l3": {
                            "ipv6": {
                                "destination_network": {
                                    "any": {
                                        "destination_network": "any"
                                    }
                                },
                                "protocol": "tcp",
                                "source_network": {
                                    "any": {
                                        "source_network": "any"
                                    }
                                }
                            }
                        },
                        "l4": {
                            "tcp": {
                                "destination_port": {
                                    "operator": {
                                        "operator": "eq",
                                        "port": 179
                                    }
                                },
                                "established": False
                            }
                        }
                    },
                    "actions": {
                        "logging": "log-none",
                        "forwarding": "permit"
                    },
                    "name": "10"
                },
                "30": {
                    "matches": {
                        "l3": {
                            "ipv6": {
                                "destination_network": {
                                    "any": {
                                        "destination_network": "any"
                                    }
                                },
                                "protocol": "udp",
                                "source_network": {
                                    "any": {
                                        "source_network": "any"
                                    }
                                }
                            }
                        },
                        "l4": {
                            "udp": {
                                "established": False
                            }
                        }
                    },
                    "actions": {
                        "logging": "log-none",
                        "forwarding": "permit"
                    },
                    "name": "30"
                },
                "20": {
                    "statistics": {
                        "matched_packets": 15
                    },
                    "matches": {
                        "l3": {
                            "ipv6": {
                                "destination_network": {
                                    "any": {
                                        "destination_network": "any"
                                    }
                                },
                                "protocol": "tcp",
                                "source_network": {
                                    "any": {
                                        "source_network": "any"
                                    }
                                }
                            }
                        },
                        "l4": {
                            "tcp": {
                                "destination_port": {
                                    "operator": {
                                        "operator": "eq",
                                        "port": 23
                                    }
                                },
                                "established": False
                            }
                        }
                    },
                    "actions": {
                        "logging": "log-none",
                        "forwarding": "permit"
                    },
                    "name": "20"
                }
            },
            "name": "inbound",
            "type": "ipv6-acl-type"
        },
        'Virtual-Access2.1#427819008151': {
            'aces': {
                '1': {
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv6': {
                                'destination_network': {
                                    'host 2001:DB8:2::32': {
                                        'destination_network': 'host 2001:DB8:2::32'
                                    }
                                },
                                'protocol': 'tcp',
                                'source_network': {
                                    'host 2001:DB8:1::32': {
                                        'source_network': 'host 2001:DB8:1::32'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'tcp': {
                                'destination_port': {
                                    'operator': {
                                        'operator': 'eq',
                                        'port': 11000
                                    }
                                },
                                'established': False,
                                'source_port': {
                                    'operator': {
                                        'operator': 'eq',
                                        'port': 'bgp'
                                    }
                                }
                            }
                        }
                    },
                    'name': '1'
                },
                '2': {
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv6': {
                                'destination_network': {
                                    'host 2001:DB8:2::32': {
                                        'destination_network': 'host 2001:DB8:2::32'
                                    }
                                },
                                'protocol': 'tcp',
                                'source_network': {
                                    'host 2001:DB8:1::32': {
                                        'source_network': 'host 2001:DB8:1::32'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'tcp': {
                                'destination_port': {
                                    'operator': {
                                        'operator': 'eq',
                                        'port': 11001
                                    }
                                },
                                'established': False,
                                'source_port': {
                                    'operator': {
                                        'operator': 'eq',
                                        'port': 'telnet'
                                    }
                                }
                            }
                        }
                    },
                    'name': '2'
                }
            },
            'name': 'Virtual-Access2.1#427819008151',
            'per_user': True,
            'type': 'ipv6-acl-type'
        }
    }


    golden_output_1 = {'execute.return_value': '''\
        show access-lists
        Standard IP access list NAT_ACL
          10 permit 10.2.0.0, wildcard bits 0.0.255.255
            20 permit 10.2.0.0
            30 deny   any
            40 permit 10.196.7.7
        Standard IP access list NAT_ACL2
          10 permit 10.2.0.0, wildcard bits 0.0.255.255
            20 permit 10.196.7.8
            30 deny   any
        Extended IP access list PYATS_ACL_TEST
          10 permit ip host 0.0.0.0 any
          20 permit ip 192.0.2.0 0.0.0.255 192.168.10.0 0.0.0.255
          30 deny tcp 10.55.0.0 0.0.0.255 192.168.220.0 0.0.0.255 eq www
        IPv6 access list PYATS_ACL_TEST_IPv6
          permit ipv6 2001:DB8::/64 any sequence 10
          permit esp host 2001:DB8:5::1 any sequence 20
         permit tcp host 2001:DB8:1::1 eq www any eq bgp sequence 30
          permit udp any host 2001:DB8:1::1 sequence 40
    '''    
    }

    golden_parsed_output_1 = {
        'NAT_ACL': {
            'aces': {
                '10': {
                    'actions': {
                        'forwarding': 'permit'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'ipv4',
                                'source_network': {
                                    '10.2.0.0 0.0.255.255': {
                                        'source_network': '10.2.0.0 0.0.255.255'
                                    }
                                }
                            }
                        }
                    },
                    'name': '10'
                },
                '20': {
                    'actions': {
                        'forwarding': 'permit'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'ipv4',
                                'source_network': {
                                    '10.2.0.0 0.0.0.0': {
                                        'source_network': '10.2.0.0 0.0.0.0'
                                    }
                                }
                            }
                        }
                    },
                    'name': '20'
                },
                '30': {
                    'actions': {
                        'forwarding': 'deny'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'ipv4',
                                'source_network': {
                                    'any': {
                                        'source_network': 'any'
                                    }
                                }
                            }
                        }
                    },
                    'name': '30'
                },
                '40': {
                    'actions': {
                        'forwarding': 'permit'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'ipv4',
                                'source_network': {
                                    '10.196.7.7 0.0.0.0': {
                                        'source_network': '10.196.7.7 0.0.0.0'
                                    }
                                }
                            }
                        }
                    },
                    'name': '40'
                }
            },
            'name': 'NAT_ACL',
            'type': 'ipv4-acl-type'
        },
        'NAT_ACL2': {
            'aces': {
                '10': {
                    'actions': {
                        'forwarding': 'permit'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'ipv4',
                                'source_network': {
                                    '10.2.0.0 0.0.255.255': {
                                        'source_network': '10.2.0.0 0.0.255.255'
                                    }
                                }
                            }
                        }
                    },
                    'name': '10'
                },
                '20': {
                    'actions': {
                        'forwarding': 'permit'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'ipv4',
                                'source_network': {
                                    '10.196.7.8 0.0.0.0': {
                                        'source_network': '10.196.7.8 0.0.0.0'
                                    }
                                }
                            }
                        }
                    },
                    'name': '20'
                },
                '30': {
                    'actions': {
                        'forwarding': 'deny'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'ipv4',
                                'source_network': {
                                    'any': {
                                        'source_network': 'any'
                                    }
                                }
                            }
                        }
                    },
                    'name': '30'
                }
            },
            'name': 'NAT_ACL2',
            'type': 'ipv4-acl-type'
        },
        'PYATS_ACL_TEST': {
            'aces': {
                '10': {
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                },
                                'protocol': 'ipv4',
                                'source_network': {
                                    'host 0.0.0.0': {
                                        'source_network': 'host 0.0.0.0'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'ipv4': {
                                'established': False
                            }
                        }
                    },
                    'name': '10'
                },
                '20': {
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'destination_network': {
                                    '192.168.10.0 0.0.0.255': {
                                        'destination_network': '192.168.10.0 0.0.0.255'
                                    }
                                },
                                'protocol': 'ipv4',
                                'source_network': {
                                    '192.0.2.0 0.0.0.255': {
                                        'source_network': '192.0.2.0 0.0.0.255'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'ipv4': {
                                'established': False
                            }
                        }
                    },
                    'name': '20'
                },
                '30': {
                    'actions': {
                        'forwarding': 'deny',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'destination_network': {
                                    '192.168.220.0 0.0.0.255': {
                                        'destination_network': '192.168.220.0 0.0.0.255'
                                    }
                                },
                                'protocol': 'tcp',
                                'source_network': {
                                    '10.55.0.0 0.0.0.255': {
                                        'source_network': '10.55.0.0 0.0.0.255'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'tcp': {
                                'destination_port': {
                                    'operator': {
                                        'operator': 'eq',
                                        'port': 80
                                    }
                                },
                                'established': False
                            }
                        }
                    },
                    'name': '30'
                }
            },
            'name': 'PYATS_ACL_TEST',
            'type': 'ipv4-acl-type'
        },
        'PYATS_ACL_TEST_IPv6': {
            'aces': {
                '10': {
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv6': {
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                },
                                'protocol': 'ipv6',
                                'source_network': {
                                    '2001:DB8::/64': {
                                        'source_network': '2001:DB8::/64'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'ipv6': {
                                'established': False
                            }
                        }
                    },
                    'name': '10'
                },
                '20': {
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv6': {
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                },
                                'protocol': 'esp',
                                'source_network': {
                                    'host 2001:DB8:5::1': {
                                        'source_network': 'host 2001:DB8:5::1'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'esp': {
                                'established': False
                            }
                        }
                    },
                    'name': '20'
                },
                '30': {
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv6': {
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                },
                                'protocol': 'tcp',
                                'source_network': {
                                    'host 2001:DB8:1::1': {
                                        'source_network': 'host 2001:DB8:1::1'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'tcp': {
                                'destination_port': {
                                    'operator': {
                                        'operator': 'eq',
                                        'port': 179
                                    }
                                },
                                'established': False,
                                'source_port': {
                                    'operator': {
                                        'operator': 'eq',
                                        'port': 'www'
                                    }
                                }
                            }
                        }
                    },
                    'name': '30'
                },
                '40': {
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv6': {
                                'destination_network': {
                                    'host 2001:DB8:1::1': {
                                        'destination_network': 'host 2001:DB8:1::1'
                                    }
                                },
                                'protocol': 'udp',
                                'source_network': {
                                    'any': {
                                        'source_network': 'any'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'udp': {
                                'established': False
                            }
                        }
                    },
                    'name': '40'
                }
            },
            'name': 'PYATS_ACL_TEST_IPv6',
            'type': 'ipv6-acl-type'
        }
    }

    golden_output_customer = {'execute.return_value': '''
        Standard IP access list 43
            10 permit 10.1.0.2 (1168716 matches)
            20 permit 10.144.0.9
            30 permit 10.70.10.0, wildcard bits 0.0.10.255
            40 permit 10.196.0.0, wildcard bits 0.0.255.255 (8353358 matches)
    '''
    }

    golden_parsed_output_customer = {
        '43': {
            'aces': {
                '10': {
                    'actions': {
                        'forwarding': 'permit'
                    },
                    'statistics': {
                        'matched_packets': 1168716
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'ipv4',
                                'source_network': {
                                    '10.1.0.2 0.0.0.0': {
                                        'source_network': '10.1.0.2 0.0.0.0'
                                    }
                                }
                            }
                        }
                    },
                    'name': '10'
                },
                '20': {
                    'actions': {
                        'forwarding': 'permit'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'ipv4',
                                'source_network': {
                                    '10.144.0.9 0.0.0.0': {
                                        'source_network': '10.144.0.9 0.0.0.0'
                                    }
                                }
                            }
                        }
                    },
                    'name': '20'
                },
                '30': {
                    'actions': {
                        'forwarding': 'permit'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'ipv4',
                                'source_network': {
                                    '10.70.10.0 0.0.10.255': {
                                        'source_network': '10.70.10.0 0.0.10.255'
                                    }
                                }
                            }
                        }
                    },
                    'name': '30'
                },
                '40': {
                    'actions': {
                        'forwarding': 'permit'
                    },
                    'statistics': {
                        'matched_packets': 8353358
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'ipv4',
                                'source_network': {
                                    '10.196.0.0 0.0.255.255': {
                                        'source_network': '10.196.0.0 0.0.255.255'
                                    }
                                }
                            }
                        }
                    },
                    'name': '40'
                }
            },
            'name': '43',
            'type': 'ipv4-acl-type'
        }
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

    def test_ip_access_list_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_ip_access_list_output)
        obj = ShowIpAccessLists(device=self.dev_c3850)
        parsed_output = obj.parse(acl="ACL_TEST")
        self.assertEqual(parsed_output,self.golden_parsed_ip_access_list_output)

    def test_ipv6_access_list_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_ipv6_access_list_output)
        obj = ShowIpv6AccessLists(device=self.dev_c3850)
        parsed_output = obj.parse(acl="OutFilter_IPv6")
        self.assertEqual(parsed_output,self.golden_parsed_ipv6_access_list_output)

    def test_ipv6_access_list_all_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_ipv6_access_list_all_output)
        obj = ShowIpv6AccessLists(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_ipv6_access_list_all_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_1)
        obj = ShowIpv6AccessLists(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)
    
    def test_golden_customer(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_customer)
        obj = ShowIpAccessLists(device=self.dev_c3850)
        parsed_output = obj.parse(acl='43')
        self.assertEqual(parsed_output, self.golden_parsed_output_customer)

if __name__ == '__main__':
    unittest.main()

