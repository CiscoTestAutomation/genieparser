# Python
import unittest
from unittest.mock import Mock

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,SchemaMissingKeyError

# ATS
from ats.topology import Device
from ats.topology import loader

# iosxe show_flow
from genie.libs.parser.iosxe.show_flow import (ShowFlowMonitor,
                                               ShowFlowMonitorCache,
                                               ShowFlowMonitorCacheRecord,
                                               ShowFlowExporterStatistics)

# ==============================================================
# Unit test for 'show flow monitor {name} cache format table'
# ==============================================================
class TestShowFlowMonitor(unittest.TestCase):
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
            '10.4.1.10': {
                'ipv4_dst_addr': {
                    '10.4.10.1': {
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
            '10.4.1.11': {
                'ipv4_dst_addr': {
                    '10.4.10.2': {
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
    10.4.1.10         10.4.10.1                    0              0  0xC0         89                   100                     1
    10.4.1.10         10.4.10.1                    1              1  0xC0         89                   100                     1
    10.4.1.11         10.4.10.2                    0              0  0xC0         89                   100                     1
    
    Device#
    '''}

    golden_parsed_output2 = {
        'cache_type': 'Normal (Platform cache)',
        'cache_size': 16,
        'current_entries': 1,
        'flows_added': 1,
        'flows_aged': 0,
    }

    golden_output2 = {'execute.return_value': '''
        Device#show flow monitor FLOW-MONITOR-1 cache format table
        Cache type:                               Normal (Platform cache)
        Cache size:                                   16
        Current entries:                               1

        Flows added:                                   1
        Flows aged:                                    0

        There are no cache entries to display.

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

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowFlowMonitor(device=self.device)
        parsed_output = obj.parse(name='FLOW-MONITOR-1')
        self.assertEqual(parsed_output, self.golden_parsed_output2)


class TestShowFlowMonitorCache(unittest.TestCase):
    '''Unit test for "show flow monitor {name} cache"
    '''
    maxDiff = None
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'cache_type': 'Normal (Platform cache)',
        'cache_size': 200000,
        'current_entries': 1,
        'high_water_mark': 3,
        'flows_added': 16,
        'flows_aged': {
            'total': 15,
            'inactive_timeout': 15,
            'inactive_timeout_secs': 15,
        },
        'entries': {
            1: {
                'ip_vrf_id_input': '0          (DEFAULT)',
                'ipv4_src_addr': '192.168.189.254',
                'ipv4_dst_addr': '192.168.189.253',
                'intf_input': 'Null',
                'intf_output': 'TenGigabitEthernet0/0/0.1003',
                'pkts': 2,
            },
            2: {
                'ip_vrf_id_input': '0          (DEFAULT)',
                'ipv4_src_addr': '192.168.16.254',
                'ipv4_dst_addr': '192.168.16.253',
                'intf_input': 'Null',
                'intf_output': 'TenGigabitEthernet0/0/0.1001',
                'pkts': 3,
            },
            3: {
                'ip_vrf_id_input': '0          (DEFAULT)',
                'ipv4_src_addr': '192.168.229.254',
                'ipv4_dst_addr': '192.168.229.253',
                'intf_input': 'Null',
                'intf_output': 'TenGigabitEthernet0/0/0.1002',
                'pkts': 3,
            },
        },
    }
    golden_output ={'execute.return_value':'''
        Device#show flow monitor mon_vrf_1 cache
        Load for five secs: 3%/0%; one minute: 2%; five minutes: 5%
        Time source is NTP, 16:04:38.706 UTC Wed Nov 6 2019

        Cache type:                               Normal (Platform cache)
        Cache size:                               200000
        Current entries:                               1
        High Watermark:                                3

        Flows added:                                  16
        Flows aged:                                   15
            - Inactive timeout    (    15 secs)         15

        IP VRF ID INPUT                IPV4 SRC ADDR    IPV4 DST ADDR    intf input            intf output                 pkts
        =============================  ===============  ===============  ====================  ====================  ==========
        0          (DEFAULT)           192.168.189.254    192.168.189.253    Null                  Te0/0/0.1003                   2
        0          (DEFAULT)           192.168.16.254    192.168.16.253    Null                  Te0/0/0.1001                   3
        0          (DEFAULT)           192.168.229.254    192.168.229.253    Null                  Te0/0/0.1002                   3
        
        Device#
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowFlowMonitorCache(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(name='mon_vrf_1')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowFlowMonitorCache(device=self.device)
        parsed_output = obj.parse(name='mon_vrf_1')
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowFlowMonitorCacheRecord(unittest.TestCase):
    '''Unit test for "show flow monitor {name} cache format record"
    '''
    maxDiff = None
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'cache_type': 'Normal (Platform cache)',
        'cache_size': 200000,
        'current_entries': 3,
        'high_water_mark': 3,
        'flows_added': 18,
        'flows_aged': {
            'total': 6,
            'active_timeout': 0,
            'active_timeout_secs': 100,
            'inactive_timeout': 0,
            'inactive_timeout_secs': 100,
            'event_aged': 0,
            'watermark_aged': 6,
            'emergency_aged': 0,
        },
        'entries': {
            1: {
                'ip_vrf_id_input': '0          (DEFAULT)',
                'ipv4_src_addr': '192.168.189.254',
                'ipv4_dst_addr': '192.168.189.253',
                'intf_input': 'Null',
                'intf_output': 'TenGigabitEthernet0/0/0.1003',
                'pkts': 3,
            },
            2: {
                'ip_vrf_id_input': '0          (DEFAULT)',
                'ipv4_src_addr': '192.168.16.254',
                'ipv4_dst_addr': '192.168.16.253',
                'intf_input': 'Null',
                'intf_output': 'TenGigabitEthernet0/0/0.1001',
                'pkts': 4,
            },
            3: {
                'ip_vrf_id_input': '0          (DEFAULT)',
                'ipv4_src_addr': '192.168.229.254',
                'ipv4_dst_addr': '192.168.229.253',
                'intf_input': 'Null',
                'intf_output': 'TenGigabitEthernet0/0/0.1002',
                'pkts': 4,
            },
        },
    }
    golden_output ={'execute.return_value':'''
        Device#show flow monitor mon_vrf_1 cache format record
        Load for five secs: 3%/0%; one minute: 2%; five minutes: 5%
        Time source is NTP, 16:04:45.275 UTC Wed Nov 6 2019

        Cache type:                               Normal (Platform cache)
        Cache size:                               200000
        Current entries:                               3
        High Watermark:                                3

        Flows added:                                  18
        Flows aged:                                    6
            - Active timeout      (   100 secs)        0
            - Inactive timeout    (   100 secs)        0
            - Event aged                               0
            - Watermark aged                           6
            - Emergency aged                           0

        IP VRF ID INPUT:           0          (DEFAULT)
        IPV4 SOURCE ADDRESS:       192.168.189.254
        IPV4 DESTINATION ADDRESS:  192.168.189.253
        interface input:           Null
        interface output:          Te0/0/0.1003
        counter packets:           3

        IP VRF ID INPUT:           0          (DEFAULT)
        IPV4 SOURCE ADDRESS:       192.168.16.254
        IPV4 DESTINATION ADDRESS:  192.168.16.253
        interface input:           Null
        interface output:          Te0/0/0.1001
        counter packets:           4

        IP VRF ID INPUT:           0          (DEFAULT)
        IPV4 SOURCE ADDRESS:       192.168.229.254
        IPV4 DESTINATION ADDRESS:  192.168.229.253
        interface input:           Null
        interface output:          Te0/0/0.1002
        counter packets:           4
        Device#
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowFlowMonitorCacheRecord(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(name='mon_vrf_1')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowFlowMonitorCacheRecord(device=self.device)
        parsed_output = obj.parse(name='mon_vrf_1')
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowFlowExporterStatistics(unittest.TestCase):
    """ Unit tests for:
            * show flow exporter statistics
            * show flow exporter {exporter} statistics
    """
    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_output = {"execute.return_value": """
        show flow exporter statistics
        Flow Exporter test:
          Packet send statistics (last cleared 00:10:17 ago):
            Successfully sent:         6                     (410 bytes)
            Reason not given:          163                   (7820 bytes)
            No destination address:     421                   (10423 bytes)
         
          Client send statistics:
            Client: Flow Monitor Test
              Records added:           21
                - sent:                8
                - failed to send:      13
              Bytes added:             1260
                - sent:                145
                - failed to send:      1115
    """}

    golden_parsed_output = {
        "flow_exporter": {
            "test": {
                "pkt_send_stats": {
                    "last_cleared": "00:10:17",
                    "successfully_sent": 6,
                    "successfully_sent_bytes": 410,
                    "reason_not_given": 163,
                    "reason_not_given_bytes": 7820,
                    "no_destination_address": 421,
                    "no_destination_address_bytes": 10423
                },
                "client_send_stats": {
                    "Flow Monitor Test": {
                        "records_added": {
                            "total": 21,
                            "sent": 8,
                            "failed": 13
                        },
                        "bytes_added": {
                            "total": 1260,
                            "sent": 145,
                            "failed": 1115
                        }
                    }
                }
            }
        }
    }

    golden_output_exporter = {"execute.return_value": """
        show flow exporter rest statistics
        Flow Exporter rest:
          Packet send statistics (last cleared 00:10:17 ago):
            Successfully sent:         6                     (410 bytes)
            Reason not given:          163                   (7820 bytes)

          Client send statistics:
            Client: Flow Monitor Test
              Records added:           21
                - sent:                8
                - failed to send:      13
              Bytes added:             1260
                - sent:                145
                - failed to send:      1115
    """}

    golden_parsed_output_exporter = {
        "flow_exporter": {
            "rest": {
                "pkt_send_stats": {
                    "last_cleared": "00:10:17",
                    "successfully_sent": 6,
                    "successfully_sent_bytes": 410,
                    "reason_not_given": 163,
                    "reason_not_given_bytes": 7820
                },
                "client_send_stats": {
                    "Flow Monitor Test": {
                        "records_added": {
                            "total": 21,
                            "sent": 8,
                            "failed": 13
                        },
                        "bytes_added": {
                            "total": 1260,
                            "sent": 145,
                            "failed": 1115
                        }
                    }
                }
            }
        }
    }

    golden_output_partial = {"execute.return_value": """
        flow exporter statistics
        Flow Exporter test:
          Packet send statistics (last cleared 00:12:12 ago):
            Successfully sent:         0                     (0 bytes)
         
          Client send statistics:
            Client: Flow Monitor Test
              Records added:           0
              Bytes added:             0
    """}

    golden_parsed_output_partial = {
        "flow_exporter": {
            "test": {
                "pkt_send_stats": {
                    "last_cleared": "00:12:12",
                    "successfully_sent": 0,
                    "successfully_sent_bytes": 0
                },
                "client_send_stats": {
                    "Flow Monitor Test": {
                        "records_added": {
                            "total": 0
                        },
                        "bytes_added": {
                            "total": 0
                        }
                    }
                }
            }
        }
    }


    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowFlowExporterStatistics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowFlowExporterStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_exporter(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_exporter)
        obj = ShowFlowExporterStatistics(device=self.device)
        parsed_output = obj.parse(exporter='rest')
        self.assertEqual(parsed_output, self.golden_parsed_output_exporter)

    def test_golden_partial(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_partial)
        obj = ShowFlowExporterStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_partial)


if __name__ == '__main__':
    unittest.main()
