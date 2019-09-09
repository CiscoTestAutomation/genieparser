# Python
import unittest
from unittest.mock import Mock

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,SchemaMissingKeyError

# ATS
from ats.topology import Device
from ats.topology import loader

# iosxe show_flow
from genie.libs.parser.iosxe.show_flow import ShowFlowMonitor

# ==============================================================
# Unit test for 'show flow monitor {name} cache format table'
# ==============================================================
class test_show_monitor(unittest.TestCase):
    '''Unit test for "show flow monitor {name} cache format table"
    '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
        'cache_type': 'Normal (Platform cache)',
        'cache_size': 16,
        'current_entries': 1,
        'high_water_mark': 1,
        'flows_added': 1,
        'flows_aged': 0,
        'ipv4_src_addr': {
            '1.1.1.10': {
                'ipv4_dst_addr': {
                    '22.10.10.1': {
                        'index': {
                            1: {
                                'trns_src_port': 0,
                                'trns_dst_port': 0,
                                'ip_tos': '0xC0',
                                'ip_port': 89,
                                'bytes_long': 100,
                                'pkts_long': 1,
                            },
                            2: {
                                'trns_src_port': 1,
                                'trns_dst_port': 1,
                                'ip_tos': '0xC0',
                                'ip_port': 89,
                                'bytes_long': 100,
                                'pkts_long': 1,
                            },
                        }
                    },
                },
            },
            '1.1.1.11': {
                'ipv4_dst_addr': {
                    '22.10.10.2': {
                        'index': {
                            1: {
                                'trns_src_port': 0,
                                'trns_dst_port': 0,
                                'ip_tos': '0xC0',
                                'ip_port': 89,
                                'bytes_long': 100,
                                'pkts_long': 1,
                            }
                        }
                    },
                },
            },
        },
    }

    golden_output1 ={'execute.return_value':'''
    Device#show flow monitor FLOW-MONITOR-1 cache format table
    Cache type:                               Normal (Platform cache)
    Cache size:                                   16
    Current entries:                               1
    High Watermark:                                1
    
    Flows added:                                   1
    Flows aged:                                    0
    
    IPV4 SRC ADDR    IPV4 DST ADDR    TRNS SRC PORT  TRNS DST PORT  IP TOS  IP PROT            bytes long             pkts long
    ===============  ===============  =============  =============  ======  =======  ====================  ====================
    1.1.1.10         22.10.10.1                    0              0  0xC0         89                   100                     1
    1.1.1.10         22.10.10.1                    1              1  0xC0         89                   100                     1
    1.1.1.11         22.10.10.2                    0              0  0xC0         89                   100                     1
    
    Device#
    '''}

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowFlowMonitor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(name='FLOW-MONITOR-1')

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowFlowMonitor(device=self.device)
        parsed_output = obj.parse(name='FLOW-MONITOR-1')
        self.assertEqual(parsed_output, self.golden_parsed_output1)
    
if __name__ == '__main__':
    unittest.main()