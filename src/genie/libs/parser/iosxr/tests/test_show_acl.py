#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxr.show_acl import ShowAclAfiAll, \
										ShowAclEthernetServices


class test_show_acl_afi_all(unittest.TestCase):
    dev = Device(name='device')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
		'acl_name': {
		    'name': 'acl_name',
		    'type': 'ipv4-acl-type',
		    'aces': {
		        10: {
		            'name': '10',
		            'matches': {
		                'l3': {
		                    'ipv4': {
		                        'source_ipv4_network': {
		                            'any': {
		                                'source_ipv4_network': 'any',
		                                },
		                            },
		                        'destination_ipv4_network': {
		                            'any': {
		                                'destination_ipv4_network': 'any',
		                                },
		                            },
		                        },
		                    },
		                },
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-none',
		                },
		            },
		        },
		    },
		'ipv4_acl': {
		    'name': 'ipv4_acl',
		    'type': 'ipv4-acl-type',
		    'aces': {
		        10: {
		            'name': '10',
		            'matches': {
		                'l3': {
		                    'ipv4': {
		                        'source_ipv4_network': {
		                            'any': {
		                                'source_ipv4_network': 'any',
		                                },
		                            },
		                        'destination_ipv4_network': {
		                            'any': {
		                                'destination_ipv4_network': 'any',
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
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-none',
		                },
		            },
		        20: {
		            'name': '20',
		            'matches': {
		                'l3': {
		                    'ipv4': {
		                        'source_ipv4_network': {
		                            'any': {
		                                'source_ipv4_network': 'any',
		                                },
		                            },
		                        'destination_ipv4_network': {
		                            'any': {
		                                'destination_ipv4_network': 'any',
		                                },
		                            },
		                        },
		                    },
		                'l4': {
		                    'tcp': {
		                        'destination_port': {
		                            'operator': {
		                                'operator': 'eq',
		                                'port': 'ssh',
		                                },
		                            },
		                        },
		                    },
		                },
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-none',
		                },
		            },
		        30: {
		            'name': '30',
		            'matches': {
		                'l3': {
		                    'ipv4': {
		                        'source_ipv4_network': {
		                            'any': {
		                                'source_ipv4_network': 'any',
		                                },
		                            },
		                        'destination_ipv4_network': {
		                            'any': {
		                                'destination_ipv4_network': 'any',
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
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-none',
		                },
		            },
		        },
		    },
		'test22': {
		    'name': 'test22',
		    'type': 'ipv4-acl-type',
		    'aces': {
		        10: {
		            'name': '10',
		            'matches': {
		                'l3': {
		                    'ipv4': {
		                        'source_ipv4_network': {
		                            '192.168.1.0 0.0.0.255': {
		                                'source_ipv4_network': '192.168.1.0 0.0.0.255',
		                                },
		                            },
		                        'destination_ipv4_network': {
		                            '192.168.1.0 0.0.0.255': {
		                                'destination_ipv4_network': 'host 10.4.1.1',
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
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-syslog',
		                },
		            },
		        20: {
		            'name': '20',
		            'matches': {
		                'l3': {
		                    'ipv4': {
		                        'source_ipv4_network': {
		                            'host 10.16.2.2': {
		                                'source_ipv4_network': 'host 10.16.2.2',
		                                },
		                            },
		                        'destination_ipv4_network': {
		                            'host 10.16.2.2': {
		                                'destination_ipv4_network': 'any',
		                                },
		                            },
		                        'precedence': 'network',
		                        'ttl': 255,
		                        'ttl_operator': 'eq',
		                        },
		                    },
		                'l4': {
		                    'tcp': {
		                        'source-port': {
		                            'operator': {
		                                'operator': 'eq',
		                                'port': 'www',
		                                },
		                            },
		                        },
		                    },
		                },
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-none',
		                },
		            },
		        30: {
		            'name': '30',
		            'matches': {
		                'l3': {
		                    'ipv4': {
		                        'source_ipv4_network': {
		                            'any': {
		                                'source_ipv4_network': 'any',
		                                },
		                            },
		                        'destination_ipv4_network': {
		                            'any': {
		                                'destination_ipv4_network': 'any',
		                                },
		                            },
		                        },
		                    },
		                },
		            'actions': {
		                'forwarding': 'deny',
		                'logging': 'log-none',
		                },
		            },
		        },
		    },
		'ipv6_acl': {
		    'name': 'ipv6_acl',
		    'type': 'ipv6-acl-type',
		    'aces': {
		        10: {
		            'name': '10',
		            'matches': {
		                'l3': {
		                    'ipv6': {
		                        'source_ipv6_network': {
		                            'any': {
		                                'source_ipv6_network': 'any',
		                                },
		                            },
		                        'destination_ipv6_network': {
		                            'any': {
		                                'destination_ipv6_network': 'any',
		                                },
		                            },
		                        },
		                    },
		                },
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-syslog',
		                },
		            },
		        20: {
		            'name': '20',
		            'matches': {
		                'l3': {
		                    'ipv6': {
		                        'source_ipv6_network': {
		                            'host 2001::1': {
		                                'source_ipv6_network': 'host 2001::1',
		                                },
		                            },
		                        'destination_ipv6_network': {
		                            'host 2001::1': {
		                                'destination_ipv6_network': 'host 2001:1::2',
		                                },
		                            },
		                        },
		                    },
		                },
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-none',
		                },
		            },
		        30: {
		            'name': '30',
		            'matches': {
		                'l3': {
		                    'ipv6': {
		                        'source_ipv6_network': {
		                            'any': {
		                                'source_ipv6_network': 'any',
		                                },
		                            },
		                        'destination_ipv6_network': {
		                            'any': {
		                                'destination_ipv6_network': 'host 2001:2::2',
		                                },
		                            },
		                        },
		                    },
		                'l4': {
		                    'tcp': {
		                        'source-port': {
		                            'operator': {
		                                'operator': 'eq',
		                                'port': '8443',
		                                },
		                            },
		                        },
		                    },
		                },
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-none',
		                },
		            },
		        },
		    },
		}

    golden_output = {'execute.return_value': '''\
    RP/0/0/CPU0:ios#show access-lists afi-all
	Wed Mar 28 04:03:46.345 UTC
	ipv4 access-list acl_name
	 10 permit ipv4 any any
	ipv4 access-list ipv4_acl
	 10 permit tcp any any eq www
	 20 permit tcp any any eq ssh
	 30 permit tcp any any eq 443
	ipv4 access-list test22
	 10 permit tcp 192.168.1.0 0.0.0.255 host 10.4.1.1 established log
	 20 permit tcp host 10.16.2.2 eq www any precedence network ttl eq 255
	 30 deny ipv4 any any
	ipv6 access-list ipv6_acl
	 10 permit ipv6 any any log
	 20 permit ipv6 host 2001::1 host 2001:1::2
	 30 permit tcp any eq 8443 host 2001:2::2
    '''
    }

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowAclAfiAll(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowAclAfiAll(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_acl_ethernet_services(unittest.TestCase):
    dev = Device(name='device')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
		'eth_acl': {
		    'name': 'eth_acl',
		    'type': 'eth-acl-type',
		    'aces': {
		        10: {
		            'name': '10',
		            'matches': {
		                'l2': {
		                    'eth': {
		                        'destination_mac_address': 'any',
		                        'source_mac_address': 'any',
		                        },
		                    },
		                },
		            'actions': {
		                'forwarding': 'permit',
		                },
		            },
		        },
		    },
		'mac_acl': {
		    'name': 'mac_acl',
		    'type': 'eth-acl-type',
		    'aces': {
		        10: {
		            'name': '10',
		            'matches': {
		                'l2': {
		                    'eth': {
		                        'destination_mac_address': 'host 0000.0000.0000',
		                        'source_mac_address': 'host 0000.0000.0000',
		                        },
		                    },
		                },
		            'actions': {
		                'forwarding': 'permit',
		                },
		            },
		        20: {
		            'name': '20',
		            'matches': {
		                'l2': {
		                    'eth': {
		                        'destination_mac_address': 'host 0000.0000.0000',
		                        'source_mac_address': 'host 0000.0000.0000',
		                        'ether_type': '8041',
		                        },
		                    },
		                },
		            'actions': {
		                'forwarding': 'deny',
		                },
		            },
		        30: {
		            'name': '30',
		            'matches': {
		                'l2': {
		                    'eth': {
		                        'destination_mac_address': 'host 0000.0000.0000',
		                        'source_mac_address': 'host 0000.0000.0000',
		                        'vlan': 10,
		                        },
		                    },
		                },
		            'actions': {
		                'forwarding': 'deny',
		                },
		            },
		        40: {
		            'name': '40',
		            'matches': {
		                'l2': {
		                    'eth': {
		                        'destination_mac_address': 'host bbbb.bbff.7777',
		                        'source_mac_address': 'host aaaa.aaff.5555',
		                        'ether_type': '80f3',
		                        },
		                    },
		                },
		            'actions': {
		                'forwarding': 'permit',
		                },
		            },
		        },
		    },
		}
    golden_output = {'execute.return_value': '''\
   RP/0/0/CPU0:ios#show access-lists ethernet-services 
Wed Mar 28 04:04:37.482 UTC
ethernet-services access-list eth_acl
 10 permit any any
ethernet-services access-list mac_acl
 10 permit host 0000.0000.0000 host 0000.0000.0000
 20 deny host 0000.0000.0000 host 0000.0000.0000 8041
 30 deny host 0000.0000.0000 host 0000.0000.0000 vlan 10
 40 permit host aaaa.aaff.5555 host bbbb.bbff.7777 80f3
    '''
    }
    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowAclEthernetServices(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowAclEthernetServices(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)
if __name__ == '__main__':
    unittest.main()