import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.iosxe.show_utd import ShowUtdEngineStandardStatus, ShowSdwanUtdEngine


# ============================================
# unittest for 'show sdwan utd engine'
# ============================================
class TestShowSdwanUtdEngine(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        pm9010#show sdwan utd engine
        utd-oper-data utd-engine-status version 1.0.6_SV2.9.13.0_XE17.3
        utd-oper-data utd-engine-status profile Cloud-Medium
        utd-oper-data utd-engine-status status utd-oper-status-green
        utd-oper-data utd-engine-status reason ""
        utd-oper-data utd-engine-status memory-usage 11.3
        utd-oper-data utd-engine-status memory-status utd-oper-status-green
        ID  RUNNING  STATUS                 REASON  
        --------------------------------------------
        1   true     utd-oper-status-green       
        2   true     utd-oper-status-green      
        '''
        }

    golden_parsed_output = {
    'version': '1.0.6_SV2.9.13.0_XE17.3',
    'profile': 'Cloud-Medium',
    'status': 'utd-oper-status-green',
    'reason': '""',
    'memory_usage': 11.3,
    'memory_status': 'utd-oper-status-green',
    'engine_id': {
         1: {
            'running': 'true',
            'status': 'utd-oper-status-green',
            'reason': ''
            },
         2: {
            'running': 'true',
            'status': 'utd-oper-status-green',
            'reason': ''
            }
        }
    }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanUtdEngine(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanUtdEngine(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ============================================
# unittest for 'show utd engine standard status'
# ============================================
class TestShowUtdEngineStandardStatus(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        Engine version : 1.0.4_SV2.9.13.0_XE17.3
        Profile : Cloud-Medium
        System memory :
            Usage : 8.80 %
            Status : Green
        Number of engines : 2

        Engine Running Health Reason
        ===========================================
        Engine(#1): Yes Green None
        Engine(#2): Yes Green None
        =======================================================

        Overall system status: Green

        Signature update status:
        =========================
        Current signature package version: 29.0.c
        Last update status: None
        Last successful update time: None
        Last failed update time: None
        Last failed update reason: None
        Next update scheduled at: None
        Current status: Idle
        '''
        }

    golden_parsed_output = {
        'engine_version': '1.0.4_SV2.9.13.0_XE17.3',
        'profile': 'Cloud-Medium',
        'system_memory': {
            'usage_percentage': 8.8,
            'status': 'Green'
            },
        'number_of_engines': 2,
        'engine_id': {
            1: {
            'running_status': 'Yes',
            'health': 'Green',
            'reason': 'None'
            },
            2: {
            'running_status': 'Yes',
            'health': 'Green',
            'reason': 'None'
            }
        },
        'overall_system_status': 'Green',
        'signature_update_status': {
            'current_signature_package_version': '29.0.c',
            'last_update_status': 'None',
            'last_successful_update_time': 'None',
            'last_failed_update_time': 'None',
            'last_failed_update_reason': 'None',
            'next_update_scheduled_at': 'None',
            'current_status': 'Idle'
        }
    }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowUtdEngineStandardStatus(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowUtdEngineStandardStatus(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
		unittest.main()