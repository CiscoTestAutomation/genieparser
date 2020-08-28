import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.iosxe.show_sdwan_appqoe import (
    ShowSdwanAppqoeTcpoptStatus,
    ShowSdwanAppqoeNatStatistics,
    ShowSdwanAppqoeRmResources)


# ============================================
# unittest for 'show sdwan appqoe tcpopt status'
# ============================================
class TestShowSdwanAppqoeTcpoptStatus(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        ==========================================================
                        TCP-OPT Status
        ==========================================================

        Status
        ------
        TCP OPT Operational State      : RUNNING
        TCP Proxy Operational State    : RUNNING
        '''
        }

    golden_parsed_output = {
        'status': {
            'tcp_opt_operational_state': 'RUNNING',
            'tcp_proxy_operational_state': 'RUNNING'
            }
        }
    
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanAppqoeTcpoptStatus(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanAppqoeTcpoptStatus(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ============================================
# unittest for 'show sdwan appqoe nat-statistics'
# ============================================
class TestShowSdwanAppqoeNatStatistics(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        ==========================================================
                    NAT Statistics
        ==========================================================
        Insert Success      : 518181
        Delete Success      : 518181
        Duplicate Entries   : 5
        Allocation Failures : 0
        Port Alloc Success  : 0
        Port Alloc Failures : 0
        Port Free Success   : 0
        Port Free Failures  : 0
        '''
        }

    golden_parsed_output = {
        'nat_statistics': {
            'insert_success': 518181,
            'delete_success': 518181,
            'duplicate_entries': 5,
            'allocation_failures': 0,
            'port_alloc_success': 0,
            'port_alloc_failures': 0,
            'port_free_success': 0,
            'port_free_failures': 0
            }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanAppqoeNatStatistics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanAppqoeNatStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ============================================
# unittest for 'show sdwan appqoe rm-resources'
# ============================================
class TestShowSdwanAppqoeRmResources(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        ==========================================================
                    RM Resources 
        ==========================================================
        RM Global Resources :
        Max Services Memory (KB)    : 6410098
        Available System Memory(KB) : 12820196
        Used Services Memory (KB)   : 0
        Used Services Memory (%)    : 0
        System Memory Status        : GREEN
        Num sessions Status         : GREEN
        Overall HTX health Status   : GREEN

        Registered Service Resources :
        TCP Resources:
        Max Sessions                : 11000
        Used Sessions               : 0
        Memory Per Session          : 128
        SSL Resources:
        Max Sessions                : 11000
        Used Sessions               : 0
        Memory Per Session          : 50
        '''
        }

    golden_parsed_output = {
        'rm_resources': {
            'rm_global_resources': {
                'max_services_memory_kb': 6410098,
                'available_system_memory_kb': 12820196,
                'used_services_memory_kb': 0,
                'used_services_memory_percentage': 0,
                'system_memory_status': 'GREEN',
                'num_sessions_status': 'GREEN',
                'overall_htx_health_status': 'GREEN'
                },
            'registered_service_resources': {
                'tcp_resources': {
                    'max_sessions': 11000,
                    'used_sessions': 0,
                    'memory_per_session': 128
                    },
                'ssl_resources': {
                    'max_sessions': 11000,
                    'used_sessions': 0,
                    'memory_per_session': 50
                    }
                }
             }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanAppqoeRmResources(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanAppqoeRmResources(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
		unittest.main()
