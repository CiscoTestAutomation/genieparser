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
        			 '10.10.1.1': { 
	                    'ip': '10.10.1.1',
	                    'link_layer_address': 'aa11.bb22.cc33',
	                    'age': '2'
	               	},
	               	'10.10.1.1': { 
	                    'ip': '10.10.1.1',
	                    'link_layer_address': 'aa11.bb22.cc33',
	                    'age': '-'
	               	},
	               	'10.10.1.1': { 
	                    'ip': '10.10.1.1',
	                    'link_layer_address': 'aa11.bb22.cc33',
	                    'age': 'alias'
	               	},
	               	'10.10.1.1/1': { 
	                    'ip': '10.10.1.1',
	                    'prefix_length': '1',
	                    'link_layer_address': 'aa11.bb22.cc33',
	                    'age': '-'
	               	}
	            }
	        }
	    },
	    'pod100': {
    		'ipv4': {
    			'neighbors': {
        			 '10.10.1.1': { 
	                    'ip': '10.10.1.1',
	                    'link_layer_address': 'aa11.bb22.cc33',
	                    'age': '1111'
	               	},
	               	'10.10.1.1': { 
	                    'ip': '10.10.1.1',
	                    'link_layer_address': 'aa11.bb22.cc33',
	                    'age': '2222'
	               	}
	            }
	        }
	    }
    }

    golden_output = {'execute.return_value': '''
		ciscoasa# show arp
		outside 10.10.1.1 aa11.bb22.cc33 2
		outside 10.10.1.1 aa11.bb22.cc33 -
		outside 10.10.1.1 aa11.bb22.cc33 alias
		outside 10.10.1.1/1 aa11.bb22.cc33 -
		pod100 10.10.1.1 aa11.bb22.cc33 1111
		pod100 10.10.1.1 aa11.bb22.cc33 2222
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