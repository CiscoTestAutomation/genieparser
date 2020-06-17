# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Gennie
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.junos.show_platform import (FileList, ShowVersion,
                                                   FileListDetail)


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


# ==========================
# Unit test for 'show version'
# ==========================
class TestShowVersion(unittest.TestCase):
    maxDiff = None

    device = Device(name='aDevice')

    golden_parsed_output = {
        'software-information': {
            'package-information': [
                {
                    'comment': 'EX  Software Suite [18.2R2-S1]',
                    'name': 'ex-software-suite'
                },
                {
                    'comment': 'FIPS mode utilities [18.2R2-S1]',
                    'name': 'fips-mode-utilities'
                },
                {
                    'comment': 'Crypto Software Suite [18.2R2-S1]',
                    'name': 'crypto-software-suite'
                },
                {
                    'comment': 'Online Documentation [18.2R2-S1]',
                    'name': 'online-documentation'
                },
                {
                    'comment': 'Phone-Home Software Suite [18.2R2-S1]',
                    'name': 'phone-home-software-suite'
                }
            ],
            'host-name': 'JunosHostname-1',
            'product-model': 'ex4200-24p',
            'product-name': 'ex4200-24p',
            'junos-version': '18.2R2-S1'
        }
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

    empty_output = {'execute.return_value': ''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowVersion(device=self.device)

        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVersion(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

# =============================================
# Unit test for 'file list {directory} detail'
# =============================================
class TestFileListDetail(unittest.TestCase):
    maxDiff = None

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        "directory-list": {
            "directory": {
                "file-information": [
                    {
                        "file-date": {
                            "@junos:format": "May 22 02:40"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/log/trace-static",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r-----"
                        },
                        "file-size": "525672"
                    },
                    {
                        "file-date": {
                            "@junos:format": "May 22 02:40"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/log/trace-static.0.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r-----"
                        },
                        "file-size": "131497"
                    }
                ],
                "total-files": "2"
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
        file list /var/log/trace-static* detail 
        -rw-r-----  1 root  wheel     525672 May 22 02:40 /var/log/trace-static

        -rw-r-----  1 root  wheel     131497 May 22 02:40 /var/log/trace-static.0.gz

        total files: 2
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = FileListDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(root_path='/var/log/trace-static*')

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = FileListDetail(device=self.device)
        parsed_output = obj.parse(root_path='/var/log/trace-static*')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

if __name__ == '__main__':
    unittest.main()
