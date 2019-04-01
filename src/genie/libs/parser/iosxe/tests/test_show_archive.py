# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_archive import ShowArchive, \
                                            ShowArchiveConfigDifferences, \
                                            ShowArchiveConfigIncrementalDiffs

import json
# ============================================
# Parser for 'show archive'
# ============================================
class test_show_archive(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'archive': {
            'max_archive_configurations': 10,
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

#=====================================================
# Unit test for the following commands:
# * show archive config differences
# * show archive config differences {fileA} {fileB}
# * show archive config differences {fileA}
# * show archive config incremental-diff {fileA}
#=====================================================
class test_show_archive_config_differences(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value' : ''}
    
    golden_parsed_output = {
        'diff': [
            '+hostname Router',
            '-hostname Test4', 
            '-archive', 
            '-path bootflash:config', 
            '-maximum 14', 
            '-time-period 2'
        ]
    }
    
    golden_output = {'execute.return_value': '''\
        Load for five secs: 14%/0%; one minute: 13%; five minutes: 19%
        Time source is NTP, 11:58:48.301 EST Fri Oct 14 2016
        !Contextual Config Diffs:
        +hostname Router
        -hostname Test4
        -archive
        -path bootflash:config
        -maximum 14
        -time-period 2
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowArchiveConfigDifferences(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    # Test case for 'show archive config differences'
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowArchiveConfigDifferences(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
    
    # Test case for 'show archive config differences {fileA}'
    def test_golden_one_file(self):
        self.device = Mock(**self.golden_output)
        obj = ShowArchiveConfigDifferences(device=self.device)
        parsed_output = obj.parse(fileA='file1.txt')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    # Test case for 'show archive config differences {fileA} {fileB}'
    def test_golden_two_files(self):
        self.device = Mock(**self.golden_output)
        obj = ShowArchiveConfigDifferences(device=self.device)
        parsed_output = obj.parse(fileA='file1.txt', fileB='file2.txt')
        self.assertEqual(parsed_output, self.golden_parsed_output)

#=====================================================
# Unit test for the following commands:
# * show archive config incremental-diff {fileA}
#=====================================================
class test_show_archive_config_incremental_diff(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value' : ''}

    golden_parsed_output_incremental_diff = {
        'list_of_commands': [
            'ip subnet-zero', 
            'ip cef', 
            'ip name-server 10.4.4.4', 
            'voice dnis-map1', 
            'dnis 111', 
            'interface FastEthernet1/0',
            'no ip address', 
            'no ip route-cache', 
            'no ip mroute-cache',
            'shutdown', 
            'duplex half',
            'ip default-gateway 10.5.5.5',
            'ip classless', 
            'access-list 110 deny    ip any host 10.1.1.1',
            'access-list 110 deny    ip any host 10.1.1.2',
            'access-list 110 deny    ip any host 10.1.1.3',
            'snmp-server community private RW'
        ]
    }

    golden_output_incremental_diff = {'execute.return_value': '''\
        !List of Commands:
        ip subnet-zero
        ip cef
        ip name-server 10.4.4.4
        voice dnis-map1
            dnis 111
        interface FastEthernet1/0
            no ip address
            no ip route-cache
            no ip mroute-cache
            shutdown
            duplex half
    ip default-gateway 10.5.5.5
        ip classless
        access-list 110 deny    ip any host 10.1.1.1
        access-list 110 deny    ip any host 10.1.1.2
        access-list 110 deny    ip any host 10.1.1.3
        snmp-server community private RW
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowArchiveConfigIncrementalDiffs(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(fileA='file1.txt')

    def test_golden_incremental_diffs(self):
        self.device = Mock(**self.golden_output_incremental_diff)
        obj = ShowArchiveConfigIncrementalDiffs(device=self.device)
        parsed_output = obj.parse(fileA='file1.txt')
        self.assertEqual(parsed_output,self.golden_parsed_output_incremental_diff)

if __name__ == '__main__':
    unittest.main()
