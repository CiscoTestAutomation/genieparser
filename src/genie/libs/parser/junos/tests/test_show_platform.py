# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Gennie
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.junos.show_platform import FileList


#==========================
# Unit test for 'file list'
#==========================
class test_file_list(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'dir': 
            {'root': 
                {'files': 
                    {'.cshrc@': 
                        {'path': '/packages/mnt/os-runtime/root/.cshrc'},
                    '.history': {},
                    '.login@': 
                        {'path': '/packages/mnt/os-runtime/root/.login'},
                    '.profile@': 
                        {'path': '/packages/mnt/os-runtime/root/.profile'},
                    'filename': {},
                    'my_file1': {},
                    'golden_config': {}}}}}

    golden_output1 = {'execute.return_value': '''
        root@junos_vmx1> file list
        /root/:
        .cshrc@ -> /packages/mnt/os-runtime/root/.cshrc
        .history
        .login@ -> /packages/mnt/os-runtime/root/.login
        .profile@ -> /packages/mnt/os-runtime/root/.profile
        filename
        my_file1
        golden_config
        '''}

    golden_parsed_output2 = {
        'dir': 
            {'root': 
                {'files': 
                    {'filename999': {}}}}}

    golden_output2 = {'execute.return_value': '''
        root@junos_vmx1> file list filename999
        /root/filename999
        '''}

    golden_parsed_output3 = {
        'dir': 
            {'root': {}}}

    golden_output3 = {'execute.return_value': '''
        root@junos_vmx1> file list filename999
        /root/filename999: No such file or directory
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = FileList(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = FileList(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = FileList(device=self.device)
        parsed_output = obj.parse(filename='filename999')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = FileList(device=self.device)
        parsed_output = obj.parse(filename='filename999')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

if __name__ == '__main__':
    unittest.main()
