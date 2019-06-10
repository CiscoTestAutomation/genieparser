import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.asa.show_arp import ShowArp

# =============================================
# Parser for 'show arp'
# =============================================
class test_show_arp(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'arp': {
        	1: {
        		'name': 'pod100',
       			'mac_address': '0000.0c9f.f00b',
	        	'entry': '318',
	        	'ipv4': {
	                '172.16.100.254': { 
	                    'ip': '172.16.100.254'
	               	}
	            }	        	
        	},
        	2: {
        		'name': 'pod100',
       			'mac_address': '7cad.7491.65c0',
	        	'entry': '348',
	        	'ipv4': {
	                '172.16.100.252': { 
	                    'ip': '172.16.100.252'
	               	}
	            }	        	
        	},
        	3: {
        		'name': 'pod100',
       			'mac_address': 'f0f7.55bd.b480',
	        	'entry': '1017',
	        	'ipv4': {
	                '172.16.100.253': { 
	                    'ip': '172.16.100.253'
	               	}
	            }	        	
        	},
        	4: {
        		'name': 'pod101',
       			'mac_address': 'f0f7.55bd.b480',
	        	'entry': '858',
	        	'ipv4': {
	                '172.16.101.253': { 
	                    'ip': '172.16.101.253'
	               	}
	            }	        	
        	},
        	5: {
        		'name': 'pod101',
       			'mac_address': '0000.0c9f.f00b',
	        	'entry': '2211',
	        	'ipv4': {
	                '172.16.101.10': { 
	                    'ip': '172.16.101.10'
	               	}
	            }	        	
        	},
        	6: {
        		'name': 'pod101',
       			'mac_address': '0000.0c9f.f00b',
	        	'entry': '2217',
	        	'ipv4': {
	                '172.16.101.11': { 
	                    'ip': '172.16.101.11'
	               	}
	            }	        	
        	},
        	7: {
        		'name': 'pod101',
       			'mac_address': '0000.0c9f.f00b',
	        	'entry': '2372',
	        	'ipv4': {
	                '172.16.101.12': { 
	                    'ip': '172.16.101.12'
	               	}
	            }	        	
        	},
        	8: {
        		'name': 'pod101',
       			'mac_address': '0000.0c9f.f00b',
	        	'entry': '2375',
	        	'ipv4': {
	                '172.16.101.13': { 
	                    'ip': '172.16.101.13'
	               	}
	            }	        	
        	},
        	9: {
        		'name': 'pod101',
       			'mac_address': '0000.0c9f.f00b',
	        	'entry': '2393',
	        	'ipv4': {
	                '172.16.101.14': { 
	                    'ip': '172.16.101.14'
	               	}
	            }	        	
        	},
        	10: {
        		'name': 'pod101',
       			'mac_address': '0000.0c9f.f00b',
	        	'entry': '2402',
	        	'ipv4': {
	                '172.16.101.19': { 
	                    'ip': '172.16.101.19'
	               	}
	            }	        	
        	},
        	11: {
        		'name': 'pod101',
       			'mac_address': '0000.0c9f.f00b',
	        	'entry': '2444',
	        	'ipv4': {
	                '172.16.101.18': { 
	                    'ip': '172.16.101.18'
	               	}
	            }	        	
        	},
        	12: {
        		'name': 'pod101',
       			'mac_address': '0000.0c9f.f00b',
	        	'entry': '2450',
	        	'ipv4': {
	                '172.16.101.17': { 
	                    'ip': '172.16.101.17'
	               	}
	            }	        	
        	},
        	13: {
        		'name': 'devadmin-in',
       			'mac_address': '0050.56ac.f1ce',
	        	'entry': '4',
	        	'ipv4': {
	                '10.10.2.20': { 
	                    'ip': '10.10.2.20'
	               	}
	            }	        	
        	},
        	14: {
        		'name': 'devadmin-in',
       			'mac_address': '0050.56ac.7871',
	        	'entry': '12',
	        	'ipv4': {
	                '10.10.2.65': { 
	                    'ip': '10.10.2.65'
	               	}
	            }	        	
        	},
        	15: {
        		'name': 'devadmin-in',
       			'mac_address': '0050.56ac.6d00',
	        	'entry': '12',
	        	'ipv4': {
	                '10.10.2.29': { 
	                    'ip': '10.10.2.29'
	               	}
	            }	        	
        	},
        	16: {
        		'name': 'outside',
       			'mac_address': '0011.2094.1d2b',
	        	'entry': '2',
	        	'ipv4': {
	                '10.86.194.61': { 
	                    'ip': '10.86.194.61'
	               	}
	            }	        	
        	},
        	17: {
        		'name': 'outside',
       			'mac_address': '001a.300c.8000',
	        	'entry': '-',
	        	'ipv4': {
	                '10.86.194.1': { 
	                    'ip': '10.86.194.1'
	               	}
	            }	        	
        	},
        	18: {
        		'name': 'outside',
       			'mac_address': '00d0.02a8.440a',
	        	'entry': 'alias',
	        	'ipv4': {
	                '10.86.195.2': { 
	                    'ip': '10.86.195.2'
	               	}
	            }	        	
        	}
        }
    }

    golden_output = {'execute.return_value': '''
		DevNet-asa-sm-1/admin# show arp
			pod100 172.16.100.254 0000.0c9f.f00b 318
			pod100 172.16.100.252 7cad.7491.65c0 348
			pod100 172.16.100.253 f0f7.55bd.b480 1017
			pod101 172.16.101.253 f0f7.55bd.b480 858
			pod101 172.16.101.10 0000.0c9f.f00b 2211
			pod101 172.16.101.11 0000.0c9f.f00b 2217
			pod101 172.16.101.12 0000.0c9f.f00b 2372
			pod101 172.16.101.13 0000.0c9f.f00b 2375
			pod101 172.16.101.14 0000.0c9f.f00b 2393
			pod101 172.16.101.19 0000.0c9f.f00b 2402
			pod101 172.16.101.18 0000.0c9f.f00b 2444
			pod101 172.16.101.17 0000.0c9f.f00b 2450
			devadmin-in 10.10.2.20 0050.56ac.f1ce 4
			devadmin-in 10.10.2.65 0050.56ac.7871 12
			devadmin-in 10.10.2.29 0050.56ac.6d00 12
			outside 10.86.194.61 0011.2094.1d2b 2
			outside 10.86.194.1 001a.300c.8000 -
			outside 10.86.195.2 00d0.02a8.440a alias
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowArp(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowArp(device=self.device)
        parsed_output = interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()