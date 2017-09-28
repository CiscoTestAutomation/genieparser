# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from parser.iosxe.show_archive import ShowArchive


# ============================================
# Parser for 'show archive'
# ============================================
class test_show_archive(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'archive': {
            'maximum': 10,
            'total': 1,
            'most_recent_file': 'bootflash:uncfgIntfgigabitethernet0_0_0-Sep-27-15-04-18.414-PDT-0',
            '1': {
                'file': 'bootflash:uncfgIntfgigabitethernet0_0_0-Sep-27-15-04-18.414-PDT-0',
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        The maximum archive configurations allowed is 10.
        There are currently 1 archive configurations saved.
        The next archive file will be named bootflash:uncfgIntfgigabitethernet0_0_0-<timestamp>-1
        Archive #  Name
        1        bootflash:uncfgIntfgigabitethernet0_0_0-Sep-27-15-04-18.414-PDT-0 <- Most Recent
        2        
        3        
        4        
        5        
        6        
        7        
        8        
        9        
        10 
    '''}


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowArchive(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowArchive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()