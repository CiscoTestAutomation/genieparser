#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxr.show_acl import ShowAclAfiAll


class test_show_acl_afi_all(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
		'acl_name': {
		    'name': 'acl_name',
		    'type': 'ipv4-acl-type',
		    'aces': {
		        '10': {
		            'name': '10',
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-none',
		                },
		            'matches': {
		                'l3': {
		                    'ipv4': {
		                        'protocol': 'ipv4',
		                        'source_network': {
		                            'any': {
		                                'source_network': 'any',
		                                },
		                            },
		                        'destination_network': {
		                            'any': {
		                                'destination_network': 'any',
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
		            },
		        },
		    },
		'ipv4_acl': {
		    'name': 'ipv4_acl',
		    'type': 'ipv4-acl-type',
		    'aces': {
		        '10': {
		            'name': '10',
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-none',
		                },
		            'matches': {
		                'l3': {
		                    'tcp': {
		                        'protocol': 'tcp',
		                        'source_network': {
		                            'any': {
		                                'source_network': 'any',
		                                },
		                            },
		                        'destination_network': {
		                            'any': {
		                                'destination_network': 'any',
		                                },
		                            },
		                        },
		                    },
		                'l4': {
		                    'tcp': {
		                        'established': False,
		                        'destination_port': {
		                            'operator': {
		                                'operator': 'eq',
		                                'port': 80,
		                                },
		                            },
		                        },
		                    },
		                },
		            },
		        '20': {
		            'name': '20',
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-none',
		                },
		            'matches': {
		                'l3': {
		                    'tcp': {
		                        'protocol': 'tcp',
		                        'source_network': {
		                            'any': {
		                                'source_network': 'any',
		                                },
		                            },
		                        'destination_network': {
		                            'any': {
		                                'destination_network': 'any',
		                                },
		                            },
		                        },
		                    },
		                'l4': {
		                    'tcp': {
		                        'established': False,
		                        'destination_port': {
		                            'operator': {
		                                'operator': 'eq',
		                                'port': 22,
		                                },
		                            },
		                        },
		                    },
		                },
		            },
		        '30': {
		            'name': '30',
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-none',
		                },
		            'matches': {
		                'l3': {
		                    'tcp': {
		                        'protocol': 'tcp',
		                        'source_network': {
		                            'any': {
		                                'source_network': 'any',
		                                },
		                            },
		                        'destination_network': {
		                            'any': {
		                                'destination_network': 'any',
		                                },
		                            },
		                        },
		                    },
		                'l4': {
		                    'tcp': {
		                        'established': False,
		                        'destination_port': {
		                            'operator': {
		                                'operator': 'eq',
		                                'port': 443,
		                                },
		                            },
		                        },
		                    },
		                },
		            },
		        },
		    },
		'test22': {
		    'name': 'test22',
		    'type': 'ipv4-acl-type',
		    'aces': {
		        '10': {
		            'name': '10',
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-syslog',
		                },
		            'matches': {
		                'l3': {
		                    'tcp': {
		                        'protocol': 'tcp',
		                        'source_network': {
		                            '192.168.1.0 0.0.0.255': {
		                                'source_network': '192.168.1.0 0.0.0.255',
		                                },
		                            },
		                        'destination_network': {
		                            'host 1.1.1.1': {
		                                'destination_network': 'host 1.1.1.1',
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
		            },
		        '20': {
		            'name': '20',
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-none',
		                },
		            'matches': {
		                'l3': {
		                    'tcp': {
		                        'protocol': 'tcp',
		                        'source_network': {
		                            'host 2.2.2.2': {
		                                'source_network': 'host 2.2.2.2',
		                                },
		                            },
		                        'destination_network': {
		                            'any': {
		                                'destination_network': 'any',
		                                },
		                            },
		                        'ttl_operator': 'eq',
		                        'ttl': 255,
		                        'precedence': 'network',
		                        },
		                    },
		                'l4': {
		                    'tcp': {
		                        'established': False,
		                        'source_port': {
		                            'operator': {
		                                'operator': 'eq',
		                                'port': 'www',
		                                },
		                            },
		                        },
		                    },
		                },
		            },
		        '30': {
		            'name': '30',
		            'actions': {
		                'forwarding': 'deny',
		                'logging': 'log-none',
		                },
		            'matches': {
		                'l3': {
		                    'ipv4': {
		                        'protocol': 'ipv4',
		                        'source_network': {
		                            'any': {
		                                'source_network': 'any',
		                                },
		                            },
		                        'destination_network': {
		                            'any': {
		                                'destination_network': 'any',
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
		            },
		        },
		    },
		'ipv6_acl': {
		    'name': 'ipv6_acl',
		    'type': 'ipv6-acl-type',
		    'aces': {
		        '10': {
		            'name': '10',
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-syslog',
		                },
		            'matches': {
		                'l3': {
		                    'ipv6': {
		                        'protocol': 'ipv6',
		                        'source_network': {
		                            'any': {
		                                'source_network': 'any',
		                                },
		                            },
		                        'destination_network': {
		                            'any': {
		                                'destination_network': 'any',
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
		            },
		        '20': {
		            'name': '20',
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-none',
		                },
		            'matches': {
		                'l3': {
		                    'ipv6': {
		                        'protocol': 'ipv6',
		                        'source_network': {
		                            'host 2001::1': {
		                                'source_network': 'host 2001::1',
		                                },
		                            },
		                        'destination_network': {
		                            'host 2001:1::2': {
		                                'destination_network': 'host 2001:1::2',
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
		            },
		        '30': {
		            'name': '30',
		            'actions': {
		                'forwarding': 'permit',
		                'logging': 'log-none',
		                },
		            'matches': {
		                'l3': {
		                    'tcp': {
		                        'protocol': 'tcp',
		                        'source_network': {
		                            'any': {
		                                'source_network': 'any',
		                                },
		                            },
		                        'destination_network': {
		                            'host 2001:2::2': {
		                                'destination_network': 'host 2001:2::2',
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
		                                'port': '8443',
		                                },
		                            },
		                        },
		                    },
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
	 10 permit tcp 192.168.1.0 0.0.0.255 host 1.1.1.1 established log
	 20 permit tcp host 2.2.2.2 eq www any precedence network ttl eq 255
	 30 deny ipv4 any any
	ipv6 access-list ipv6_acl
	 10 permit ipv6 any any log
	 20 permit ipv6 host 2001::1 host 2001:1::2
	 30 permit tcp any eq 8443 host 2001:2::2
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowAclAfiAll(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowAclAfiAll(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()