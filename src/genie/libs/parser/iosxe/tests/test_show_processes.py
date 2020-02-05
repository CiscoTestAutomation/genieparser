# Python
import unittest
from unittest.mock import Mock
 
# ATS
from ats.topology import Device
from ats.topology import loader
 
# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

from genie.libs.parser.iosxe.show_processes import ShowProcessesMemoryPlatformSorted

# =====================================================
# Unit test for "show processes memory platform sorted"
# =====================================================
class test_show_processes_memory_platform_sorted(unittest.TestCase):

	device = Device(name='aDevice')
	empty_output = {'execute.return_value': ''}


	golden_parsed_output = {
		'system_memory':
			{'lowest': '3707912K',
			'per_process_memory':
				{'linux_iosd-imag' :
					{'pid': 16994,
					'text': 233305,
					'data': 887872,
					'stack': 136,
					'dynamic': 388,
					'RSS': 887872},
				'fed':
					{'pid': 16590,
					'text': 165,
					'data': 249336,
					'stack': 136,
					'dynamic': 90100,
					'RSS': 249336},
				'dbm':
					{'pid': 1582,
					'text': 275,
					'data': 205248,
					'stack': 136,
					'dynamic': 3628,
					'RSS': 205248},
				'pubd':
					{'pid': 6558,
					'text': 76,
					'data': 170928,
					'stack': 136,
					'dynamic': 3216,
					'RSS': 170928}},
			'total': '7703908K',
			'free': '3840132K',
			'used': '3863776K'}
		}


	golden_output = {'execute.return_value': '''
		System memory: 7703908K total, 3863776K used, 3840132K free,
		Lowest: 3707912K
		   Pid    Text      Data   Stack   Dynamic       RSS              Name
		----------------------------------------------------------------------
		 16994  233305    887872     136       388    887872   linux_iosd-imag
		 16590     165    249336     136     90100    249336    fed main event
		  1582     275    205248     136      3628    205248               dbm
		  6558      76    170928     136      3216    170928              pubd
		'''}

	def test_empty(self):
		self.device = Mock(**self.empty_output)
		obj = ShowProcessesMemoryPlatformSorted(device=self.device)
		with self.assertRaises(SchemaEmptyParserError):
			parsed_output = obj.parse()

	def test_show_processes_memory_platform_sorted_full(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output)
		obj = ShowProcessesMemoryPlatformSorted(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output)




if __name__ == '__main__':
	unittest.main()









