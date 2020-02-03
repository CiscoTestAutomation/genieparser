#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.ios.show_acl import ShowAccessLists

from genie.libs.parser.iosxe.tests.test_show_acl import TestShowAccessLists as TestShowAccessListsIosxe

class TestShowAccessLists(TestShowAccessListsIosxe):
    maxDiff = None
    golden_output_standard = {'execute.return_value': '''\
        Switch# show ip access-lists
        Standard IP access list 1
            permit 172.20.10.10
        Standard IP access list 10
            permit 10.66.12.12
        Standard IP access list 12
            deny   10.16.3.2
        Standard IP access list 32
            permit 172.20.20.20
        Standard IP access list 34
            permit 10.24.35.56
            permit 10.34.56.34
    '''}

    golden_parsed_output_standard = {
        '1': {
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
                                    '172.20.10.10 0.0.0.0': {
                                        'source_network': '172.20.10.10 0.0.0.0'
                                    }
                                }
                            }
                        }
                    },
                    'name': '10'
                }
            },
            'name': '1',
            'type': 'ipv4-acl-type'
        },
        '10': {
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
                                    '10.66.12.12 0.0.0.0': {
                                        'source_network': '10.66.12.12 0.0.0.0'
                                    }
                                }
                            }
                        }
                    },
                    'name': '10'
                }
            },
            'name': '10',
            'type': 'ipv4-acl-type'
        },
        '12': {
            'aces': {
                '10': {
                    'actions': {
                        'forwarding': 'deny'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'ipv4',
                                'source_network': {
                                    '10.16.3.2 0.0.0.0': {
                                        'source_network': '10.16.3.2 0.0.0.0'
                                    }
                                }
                            }
                        }
                    },
                    'name': '10'
                }
            },
            'name': '12',
            'type': 'ipv4-acl-type'
        },
        '32': {
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
                                    '172.20.20.20 0.0.0.0': {
                                        'source_network': '172.20.20.20 0.0.0.0'
                                    }
                                }
                            }
                        }
                    },
                    'name': '10'
                }
            },
            'name': '32',
            'type': 'ipv4-acl-type'
        },
        '34': {
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
                                    '10.24.35.56 0.0.0.0': {
                                        'source_network': '10.24.35.56 0.0.0.0'
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
                                    '10.34.56.34 0.0.0.0': {
                                        'source_network': '10.34.56.34 0.0.0.0'
                                    }
                                }
                            }
                        }
                    },
                    'name': '20'
                }
            },
            'name': '34',
            'type': 'ipv4-acl-type'
        }
    }

    golden_output_ios = {'execute.return_value': '''\
        Router# show access-lists 101
        Extended IP access list 101
            10 permit ip host 10.3.3.3 host 10.5.5.34
            20 permit icmp any any
            30 permit ip host 10.34.2.2 host 10.2.54.2
            40 permit ip host 10.3.4.31 host 10.3.32.3 log
    '''}
    
    golden_parsed_output_ios = {
        "101": {
            "name": "101",
            "type": "ipv4-acl-type",
            "aces": {
                "10": {
                    "name": "10",
                    "actions": {
                        "forwarding": "permit",
                        "logging": "log-none"
                    },
                    "matches": {
                        "l3": {
                            "ipv4": {
                                "protocol": "ipv4",
                                "source_network": {
                                    "host 10.3.3.3": {
                                        "source_network": "host 10.3.3.3"
                                    }
                                },
                                "destination_network": {
                                    "host 10.5.5.34": {
                                        "destination_network": "host 10.5.5.34"
                                    }
                                }
                            }
                        },
                        "l4": {
                            "ipv4": {
                                "established": False
                            }
                        }
                    }
                },
                "20": {
                    "name": "20",
                    "actions": {
                        "forwarding": "permit",
                        "logging": "log-none"
                    },
                    "matches": {
                        "l3": {
                            "ipv4": {
                                "protocol": "icmp",
                                "source_network": {
                                    "any": {
                                        "source_network": "any"
                                    }
                                },
                                "destination_network": {
                                    "any": {
                                        "destination_network": "any"
                                    }
                                }
                            }
                        },
                        "l4": {
                            "icmp": {
                                "established": False
                            }
                        }
                    }
                },
                "30": {
                    "name": "30",
                    "actions": {
                        "forwarding": "permit",
                        "logging": "log-none"
                    },
                    "matches": {
                        "l3": {
                            "ipv4": {
                                "protocol": "ipv4",
                                "source_network": {
                                    "host 10.34.2.2": {
                                        "source_network": "host 10.34.2.2"
                                    }
                                },
                                "destination_network": {
                                    "host 10.2.54.2": {
                                        "destination_network": "host 10.2.54.2"
                                    }
                                }
                            }
                        },
                        "l4": {
                            "ipv4": {
                                "established": False
                            }
                        }
                    }
                },
                "40": {
                    "name": "40",
                    "actions": {
                        "forwarding": "permit",
                        "logging": "log-syslog"
                    },
                    "matches": {
                        "l3": {
                            "ipv4": {
                                "protocol": "ipv4",
                                "source_network": {
                                    "host 10.3.4.31": {
                                        "source_network": "host 10.3.4.31"
                                    }
                                },
                                "destination_network": {
                                    "host 10.3.32.3": {
                                        "destination_network": "host 10.3.32.3"
                                    }
                                }
                            }
                        },
                        "l4": {
                            "ipv4": {
                                "established": False
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_customer1 = {'execute.return_value': '''
        Extended IP access list acl1
        10 permit icmp any any echo
        20 permit icmp any any echo-reply (1195 matches)
        30 permit icmp any any ttl-exceeded
        40 permit icmp any any unreachable
        50 permit icmp any any packet-too-big
        60 deny icmp any any
        80 permit udp any host 10.4.1.1 eq 1985
    '''
    }
    
    golden_parsed_output_customer1 = {
        'acl1': {
            'name': 'acl1',
            'type': 'ipv4-acl-type',
            'aces': {
                '10': {
                    'name': '10',
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'icmp',
                                'source_network': {
                                    'any': {
                                        'source_network': 'any'
                                    }
                                },
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'icmp': {
                                'established': False,
                                'msg_type': 'echo'
                            }
                        }
                    }
                },
                '20': {
                    'name': '20',
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'statistics': {
                        'matched_packets': 1195
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'icmp',
                                'source_network': {
                                    'any': {
                                        'source_network': 'any'
                                    }
                                },
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'icmp': {
                                'established': False,
                                'msg_type': 'echo-reply'
                            }
                        }
                    }
                },
                '30': {
                    'name': '30',
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'icmp',
                                'source_network': {
                                    'any': {
                                        'source_network': 'any'
                                    }
                                },
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'icmp': {
                                'established': False,
                                'msg_type': 'ttl-exceeded'
                            }
                        }
                    }
                },
                '40': {
                    'name': '40',
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'icmp',
                                'source_network': {
                                    'any': {
                                        'source_network': 'any'
                                    }
                                },
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'icmp': {
                                'established': False,
                                'msg_type': 'unreachable'
                            }
                        }
                    }
                },
                '50': {
                    'name': '50',
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'icmp',
                                'source_network': {
                                    'any': {
                                        'source_network': 'any'
                                    }
                                },
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'icmp': {
                                'established': False,
                                'msg_type': 'packet-too-big'
                            }
                        }
                    }
                },
                '60': {
                    'name': '60',
                    'actions': {
                        'forwarding': 'deny',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'icmp',
                                'source_network': {
                                    'any': {
                                        'source_network': 'any'
                                    }
                                },
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'icmp': {
                                'established': False
                            }
                        }
                    }
                },
                '80': {
                    'name': '80',
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'udp',
                                'source_network': {
                                    'any': {
                                        'source_network': 'any'
                                    }
                                },
                                'destination_network': {
                                    'host 10.4.1.1': {
                                        'destination_network': 'host 10.4.1.1'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'udp': {
                                'established': False,
                                'destination_port': {
                                    'operator': {
                                        'operator': 'eq',
                                        'port': 1985
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
                                 
    golden_output_customer2 = {'execute.return_value': '''
    Extended IP access list acl1
        10 permit icmp any any
        20 permit udp any host 10.4.1.1 eq 1985 (67 matches)
        30 permit ip object-group dummydpd-local object-group dummydpd-remote
    '''
    }
    
    golden_parsed_output_customer2 = {
        'acl1': {
            'name': 'acl1',
            'type': 'ipv4-acl-type',
            'aces': {
                '10': {
                    'name': '10',
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'icmp',
                                'source_network': {
                                    'any': {
                                        'source_network': 'any'
                                    }
                                },
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'icmp': {
                                'established': False
                            }
                        }
                    }
                },
                '20': {
                    'name': '20',
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'statistics': {
                        'matched_packets': 67
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'udp',
                                'source_network': {
                                    'any': {
                                        'source_network': 'any'
                                    }
                                },
                                'destination_network': {
                                    'host 10.4.1.1': {
                                        'destination_network': 'host 10.4.1.1'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'udp': {
                                'established': False,
                                'destination_port': {
                                    'operator': {
                                        'operator': 'eq',
                                        'port': 1985
                                    }
                                }
                            }
                        }
                    }
                },
                '30': {
                    'name': '30',
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'ipv4',
                                'source_network': {
                                    'object-group dummydpd-local': {
                                        'source_network': 'object-group dummydpd-local'
                                    }
                                },
                                'destination_network': {
                                    'object-group dummydpd-remote': {
                                        'destination_network': 'object-group dummydpd-remote'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'ipv4': {
                                'established': False
                            }
                        }
                    }
                }                   
            }
        }
    }

    golden_output_customer3 = {'execute.return_value': '''
    Extended IP access list acl1
        10 permit icmp any any echo
        20 permit icmp any any echo-reply (198 matches)
        40 permit icmp any any unreachable
        50 permit icmp any any packet-too-big
        60 deny icmp any any
        70 permit ip object-group grt-interface-nets object-group grt-interface-nets
        80 permit udp any host 10.4.1.1 eq 1985
        90 permit esp object-group vpn-endpoints-dummydpd host 10.4.1.1 (14 matches)
        100 permit ahp object-group vpn-endpoints-dummydpd host 10.4.1.1
        110 permit udp object-group vpn-endpoints-dummydpd host 10.4.1.1 eq isakmp (122 matches)
    '''
    }
    
    golden_parsed_output_customer3 = {
        'acl1': {
            'name': 'acl1',
            'type': 'ipv4-acl-type',
            'aces': {
                '10': {
                    'name': '10',
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'icmp',
                                'source_network': {
                                    'any': {
                                        'source_network': 'any'
                                    }
                                },
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'icmp': {
                                'established': False,
                                'msg_type': 'echo'
                            }
                        }
                    }
                },
                '20': {
                    'name': '20',
                    'actions': {
                        'forwarding': 'permit',
                        'logging': 'log-none'
                    },
                    'statistics': {
                        'matched_packets': 198
                    },
                    'matches': {
                        'l3': {
                            'ipv4': {
                                'protocol': 'icmp',
                                'source_network': {
                                    'any': {
                                        'source_network': 'any'
                                    }
                                },
                                'destination_network': {
                                    'any': {
                                        'destination_network': 'any'
                                    }
                                }
                            }
                        },
                        'l4': {
                            'icmp': {
                                'established': False,
                                'msg_type': 'echo-reply'
                                    }
                                }
                            }
                        },
                        '40': {
                            'name': '40',
                            'actions': {
                                'forwarding': 'permit',
                                'logging': 'log-none'
                            },
                            'matches': {
                                'l3': {
                                    'ipv4': {
                                        'protocol': 'icmp',
                                        'source_network': {
                                            'any': {
                                                'source_network': 'any'
                                            }
                                        },
                                        'destination_network': {
                                            'any': {
                                                'destination_network': 'any'
                                            }
                                        }
                                    }
                                },
                                'l4': {
                                    'icmp': {
                                        'established': False,
                                        'msg_type': 'unreachable'
                                    }
                                }
                            }
                        },
                        '50': {
                            'name': '50',
                            'actions': {
                                'forwarding': 'permit',
                                'logging': 'log-none'
                            },
                            'matches': {
                                'l3': {
                                    'ipv4': {
                                        'protocol': 'icmp',
                                        'source_network': {
                                            'any': {
                                                'source_network': 'any'
                                            }
                                        },
                                        'destination_network': {
                                            'any': {
                                                'destination_network': 'any'
                                            }
                                        }
                                    }
                                },
                                'l4': {
                                    'icmp': {
                                        'established': False,
                                        'msg_type': 'packet-too-big'
                                    }
                                }
                            }
                        },
                        '60': {
                            'name': '60',
                            'actions': {
                                'forwarding': 'deny',
                                'logging': 'log-none'
                            },
                            'matches': {
                                'l3': {
                                    'ipv4': {
                                        'protocol': 'icmp',
                                        'source_network': {
                                            'any': {
                                                'source_network': 'any'
                                            }
                                        },
                                        'destination_network': {
                                            'any': {
                                                'destination_network': 'any'
                                            }
                                        }
                                    }
                                },
                                'l4': {
                                    'icmp': {
                                        'established': False
                                    }
                                }
                            }
                        },
                        '70': {
                            'name': '70',
                            'actions': {
                                'forwarding': 'permit',
                                'logging': 'log-none'
                            },
                            'matches': {
                                'l3': {
                                    'ipv4': {
                                        'protocol': 'ipv4',
                                        'source_network': {
                                            'object-group grt-interface-nets': {
                                                'source_network': 'object-group grt-interface-nets'
                                            }
                                        },
                                        'destination_network': {
                                            'object-group grt-interface-nets': {
                                                'destination_network': 'object-group grt-interface-nets'
                                            }
                                        }
                                    }
                                },
                                'l4': {
                                    'ipv4': {
                                        'established': False
                                    }
                                }
                            }
                        },
                        '80': {
                            'name': '80',
                            'actions': {
                                'forwarding': 'permit',
                                'logging': 'log-none'
                            },
                            'matches': {
                                'l3': {
                                    'ipv4': {
                                        'protocol': 'udp',
                                        'source_network': {
                                            'any': {
                                                'source_network': 'any'
                                            }
                                        },
                                        'destination_network': {
                                            'host 10.4.1.1': {
                                                'destination_network': 'host 10.4.1.1'
                                            }
                                        }
                                    }
                                },
                                'l4': {
                                    'udp': {
                                        'established': False,
                                        'destination_port': {
                                            'operator': {
                                                'operator': 'eq',
                                                'port': 1985
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        '90': {
                            'name': '90',
                            'actions': {
                                'forwarding': 'permit',
                                'logging': 'log-none'
                            },
                            'statistics': {
                                'matched_packets': 14
                            },
                            'matches': {
                                'l3': {
                                    'ipv4': {
                                        'protocol': 'esp',
                                        'source_network': {
                                            'object-group vpn-endpoints-dummydpd': {
                                                'source_network': 'object-group vpn-endpoints-dummydpd'
                                            }
                                        },
                                        'destination_network': {
                                            'host 10.4.1.1': {
                                                'destination_network': 'host 10.4.1.1'
                                            }
                                        }
                                    }
                                },
                                'l4': {
                                    'esp': {
                                        'established': False
                                    }
                                }
                            }
                        },
                        '100': {
                            'name': '100',
                            'actions': {
                                'forwarding': 'permit',
                                'logging': 'log-none'
                            },
                            'matches': {
                                'l3': {
                                    'ipv4': {
                                        'protocol': 'ahp',
                                        'source_network': {
                                            'object-group vpn-endpoints-dummydpd': {
                                                'source_network': 'object-group vpn-endpoints-dummydpd'
                                            }
                                        },
                                        'destination_network': {
                                            'host 10.4.1.1': {
                                                'destination_network': 'host 10.4.1.1'
                                            }
                                        }
                                    }
                                },
                                'l4': {
                                    'ahp': {
                                        'established': False
                                    }
                                }
                            }
                        },
                        '110': {
                            'name': '110',
                            'actions': {
                                'forwarding': 'permit',
                                'logging': 'log-none'
                            },
                            'statistics': {
                                'matched_packets': 122
                            },
                            'matches': {
                                'l3': {
                                    'ipv4': {
                                        'protocol': 'udp',
                                        'source_network': {
                                            'object-group vpn-endpoints-dummydpd': { 
                                                'source_network': 'object-group vpn-endpoints-dummydpd'
                                            }
                                        },
                                        'destination_network': {
                                            'host 10.4.1.1': {
                                                'destination_network': 'host 10.4.1.1'
                                            }
                                        }
                                    }
                                },
                                'l4': {
                                    'udp': {
                                        'established': False,
                                        'destination_port': {
                                            'operator': {
                                                'operator': 'eq',
                                                'port': 500
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

                                        
    
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowAccessLists(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_standard(self):
        self.dev1 = Mock(**self.golden_output_standard)
        obj = ShowAccessLists(device=self.dev1)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_standard)

    def test_golden_ios(self):
        self.dev1 = Mock(**self.golden_output_ios)
        obj = ShowAccessLists(device=self.dev1)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_ios)

    def test_golden_customer1(self):
        self.dev_c3850 = Mock(**self.golden_output_customer1)
        obj = ShowAccessLists(device=self.dev_c3850)
        parsed_output = obj.parse(acl='acl1')
        self.assertEqual(parsed_output, self.golden_parsed_output_customer1)
        
    def test_golden_customer2(self):
        self.dev_c3850 = Mock(**self.golden_output_customer2)
        obj = ShowAccessLists(device=self.dev_c3850)
        parsed_output = obj.parse(acl='acl1')
        self.assertEqual(parsed_output, self.golden_parsed_output_customer2)
        
    def test_golden_customer3(self):
        self.dev_c3850 = Mock(**self.golden_output_customer3)
        obj = ShowAccessLists(device=self.dev_c3850)
        parsed_output = obj.parse(acl='acl1')
        self.assertEqual(parsed_output, self.golden_parsed_output_customer3)
        
if __name__ == '__main__':
    unittest.main()

