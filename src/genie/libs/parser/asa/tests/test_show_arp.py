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
     'outside': {
    		'ipv4': {
    			'neighbors': {
        			 '10.86.194.61': { 
	                    'ip': '10.86.194.61',
	                    'link_layer_address': '0011.2094.1d2b',
	                    'age': '2'
	               	},
	               	'10.86.194.1': { 
	                    'ip': '10.86.194.1',
	                    'link_layer_address': '001a.300c.8000',
	                    'age': '-'
	               	},
	               	'10.86.195.2': { 
	                    'ip': '10.86.195.2',
	                    'link_layer_address': '00d0.02a8.440a',
	                    'age': 'alias'
	               	},
	               	'10.86.195.3/24': { 
	                    'ip': '10.86.195.3',
	                    'prefix_length': '24',
	                    'link_layer_address': '00d0.02a8.440a',
	                    'age': '-'
	               	}
	            }
	        }
	    },
	    'pod100': {
    		'ipv4': {
    			'neighbors': {
        			 '168.32.24.251': { 
	                    'ip': '168.32.24.251',
	                    'link_layer_address': 'f0f7.asb2.421a',
	                    'age': '1017'
	               	},
	               	'168.32.25.251': { 
	                    'ip': '168.32.25.251',
	                    'link_layer_address': 'f0f7.asb2.421a',
	                    'age': '5211'
	               	}
	            }
	        }
	    }
    }

    golden_output = {'execute.return_value': '''
		ciscoasa# show arp
		outside 10.86.194.61 0011.2094.1d2b 2
		outside 10.86.194.1 001a.300c.8000 -
		outside 10.86.195.2 00d0.02a8.440a alias
		outside 10.86.195.3/24 00d0.02a8.440a -
		pod100 168.32.24.251 f0f7.asb2.421a 1017
		pod100 168.32.25.251 f0f7.asb2.421a 5211
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowArp(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowArp(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()