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
                                               ShowFlowExporterStatistics)

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


class test_show_flow_exporter_statistics(unittest.TestCase):
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
                    "pkts_sent": 6,
                    "bytes_sent": 410,
                    "pkts_failed": 163,
                    "bytes_failed": 7820
                },
                "client_send_stats": {
                    "Flow Monitor Test": {
                        "client": "Flow Monitor Test",
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
                    "pkts_sent": 6,
                    "bytes_sent": 410,
                    "pkts_failed": 163,
                    "bytes_failed": 7820
                },
                "client_send_stats": {
                    "Flow Monitor Test": {
                        "client": "Flow Monitor Test",
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
                    "pkts_sent": 0,
                    "bytes_sent": 0
                },
                "client_send_stats": {
                    "Flow Monitor Test": {
                        "client": "Flow Monitor Test",
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
