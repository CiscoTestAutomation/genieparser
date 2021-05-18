# Import the Python mock functionality
import unittest
from unittest.mock import Mock
# pyATS
from pyats.topology import Device
from pyats.topology import loader
# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError
# sros show_router_arp_dynamic
from genie.libs.parser.sros.show_router_arp_dynamic import ShowRouterArpDynamic

# =================================
# Unit test for 'show router arp dynamic'
# =================================

class test_show_router_arp_dynamic(unittest.TestCase):

	'''Unit test for "show router arp dynamic"'''

	empty_output = {'execute.return_value': ''}

	golden_parsed_output1 = {

	"router": {
		"Base": {
			"ip_address": {
				"1.1.1.1": {
					"interface": "To-ASR5.5K",
					"mac_add": "00:fe:c8:34:a7:39",
					"expiry": "02h34m12s",
					"type": "Dyn[I]"
				},
				"2.2.2.2": {
					"interface": "To-ASR5.5K_2",
					"mac_add": "00:fe:c8:34:a9:39",
					"expiry": "03h46m20s",
					"type": "Dyn[I]"
				},
				"3.3.3.3": {
					"interface": "To-CENTRAL",
					"mac_add": "10:e8:78:a8:4e:a5",
					"expiry": "02h29m13s",
					"type": "Dyn[I]"
				},
				"4.4.4.4": {
					"interface": "To-MANAG",
					"mac_add": "00:04:96:98:7c:2e",
					"expiry": "03h57m43s",
					"type": "Dyn[I]"
				}
			},
			"entries": 4
			}
		}
	}

	golden_output1 = {'execute.return_value': '''
===============================================================================
ARP Table Router: (Base)
===============================================================================
IP Address      MAC Address       Expiry    Type   Interface
-------------------------------------------------------------------------------
1.1.1.1         00:fe:c8:34:a7:39 02h34m12s Dyn[I] To-ASR5.5K
2.2.2.2         00:fe:c8:34:a9:39 03h46m20s Dyn[I] To-ASR5.5K_2
3.3.3.3         10:e8:78:a8:4e:a5 02h29m13s Dyn[I] To-CENTRAL
4.4.4.4         00:04:96:98:7c:2e 03h57m43s Dyn[I] To-MANAG
-------------------------------------------------------------------------------
No. of ARP Entries: 4
===============================================================================
'''}

	def test_show_service_router_arp_dynamic_full1(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output1)
		obj = ShowRouterArpDynamic(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output1)

	def test_show_service_router_arp_dynamic_empty(self):
		self.maxDiff = None
		self.device = Mock(**self.empty_output)
		obj = ShowRouterArpDynamic(device=self.device)
		with self.assertRaises(SchemaEmptyParserError):
			parsed_output = obj.parse()

if __name__ == '__main__':
	unittest.main()