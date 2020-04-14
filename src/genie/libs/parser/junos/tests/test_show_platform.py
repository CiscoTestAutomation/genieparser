# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Gennie
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.junos.show_platform import FileList
from genie.libs.parser.junos.show_platform import ShowVersion


# ==========================
# Unit test for 'file list'
# ==========================
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


# ==========================
# Unit test for 'show version'
# ==========================
class test_show_version(unittest.TestCase):
    device = Device(name='aDevice')

    golden_parsed_output = {'hostname': "JunosHostname-1",
                             'operating_system': "Junos",
                             'software_version': "18.2R2-S1",
                             'model': "ex4200-24p",
                             }

    golden_output = {'execute.return_value': '''
        user2@JunosHostname-1> show version 
        fpc0:
        --------------------------------------------------------------------------
        Hostname: JunosHostname-1
        Model: ex4200-24p
        Junos: 18.2R2-S1
        JUNOS EX  Software Suite [18.2R2-S1]
        JUNOS FIPS mode utilities [18.2R2-S1]
        JUNOS Crypto Software Suite [18.2R2-S1]
        JUNOS Online Documentation [18.2R2-S1]
        JUNOS Phone-Home Software Suite [18.2R2-S1]
        
        {master:0}
        user1@JunosHostname-1> 
        '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowVersion(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)



if __name__ == '__main__':
    unittest.main()
