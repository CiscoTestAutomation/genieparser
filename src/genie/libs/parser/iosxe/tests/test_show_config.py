# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# MetaParser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
        SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_config import ShowArchiveConfigDifferences

#=====================================================
# Parser for 'show archive config differences
#=====================================================

class test_show_archive_config_differences(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value' : ''}
    
    golden_parsed_output = {
            'contextual_config_diffs':{
                'index': {
                    1: {
                        'before': ['-hostname Router'],
                        'after': ['+hostname TEST4']
                    }
                }
        }
    }

    golden_parsed_output_optional = {
                'contextual_config_diffs':{
                    'index': { 
                        1: {
                            'before': ['-hostname Router'],
                            'after' : ['+hostname TEST4']
                        }
                    }
            }
    }
    
    golden_output = {'execute.return_value': '''\
            !Contextual Config Diffs:
            -hostname Router
            +hostname TEST4
            '''
    }

    golden_output_optional = {'execute.return_value': '''\
            !Contextual Config Diffs:
            -hostname Router
            +hostname TEST4
            '''
    }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowArchiveConfigDifferences(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowArchiveConfigDifferences(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
    
    def test_golden_one_file(self):
        self.device = Mock(**self.golden_output_optional)
        obj = ShowArchiveConfigDifferences(device=self.device)
        parsed_output = obj.parse(fileA='file1.txt')
        self.assertEqual(parsed_output, self.golden_parsed_output_optional)

    def test_golden_two_files(self):
        self.device = Mock(**self.golden_output_optional)
        obj = ShowArchiveConfigDifferences(device=self.device)
        parsed_output = obj.parse(fileA='file1.txt', fileB='file2.txt')
        self.assertEqual(parsed_output, self.golden_parsed_output_optional)

    
if __name__ == '__main__':
    unittest.main()
