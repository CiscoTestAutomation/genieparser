# Python
import unittest
from unittest.mock import Mock

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_traffic_collector
from genie.libs.parser.iosxr.show_traffic_collector import (
    ShowTrafficCollecterExternalInterface,
    ShowTrafficCollecterIpv4CountersPrefixDetail
)

# ==========================================================
#  Unit test for 'show traffic-collector external-interface'
# ==========================================================

class TestShowTrafficCollectorExternalInterface(unittest.TestCase):

    empty_output = {'execute.return_value': ''}

    maxDiff = None

    golden_parsed_output = {
        'interface':{
            'TenGigabitEthernet0/1/0/3':{
                'status': 'Enabled'
            },
            'TenGigabitEthernet0/1/0/4':{
                'status': 'Enabled'
            },
        },
    }

    golden_output = {'execute.return_value': '''
    RP/0/RSP0/CPU0:router# show traffic-collector external-interface 
         Interface             Status          
         --------------------  ----------------
         Te0/1/0/3             Enabled 
         Te0/1/0/4             Enabled

    '''}

    def test_show_traffic_collector_external_interface_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowTrafficCollecterExternalInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_traffic_collector_external_interface_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowTrafficCollecterExternalInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

# =============================================================================
#  Unit test for 'show traffic-collector ipv4 counters prefix <prefix> detail'
# =============================================================================

class TestShowTrafficCollecterIpv4CountersPrefixDetail(unittest.TestCase):

    empty_output = {'execute.return_value': ''}

    maxDiff = None

    golden_parsed_output = {
        'ipv4_counters':{
            'prefix':{
                '10.4.1.10/32':{
                    'label': 16010,
                    'state': 'Active',
                    'counters':{
                        'base':{
                            'average':{
                                'last_collection_intervals': 5,
                                'packet_rate':9496937,
                                'byte_rate':9363979882,
                            },
                            'history_of_counters':{
                                '23:01 - 23:02':{
                                    'packets': 9379529,
                                    'bytes': 9248215594,
                                },
                                '23:00 - 23:01':{
                                    'packets': 9687124,
                                    'bytes': 9551504264,
                                },
                                '22:59 - 23:00':{
                                    'packets': 9539200,
                                    'bytes': 9405651200,
                                },
                                '22:58 - 22:59':{
                                    'packets': 9845278,
                                    'bytes': 9707444108,
                                },
                                '22:57 - 22:58':{
                                    'packets': 9033554,
                                    'bytes': 8907084244,
                                },
                            },
                        },    
                        'tm_counters':{
                            'average':{
                                'last_collection_intervals': 5,
                                'packet_rate':9528754,
                                'byte_rate':9357236821,
                            },
                            'history_of_counters':{
                                '23:01 - 23:02':{
                                    'packets': 9400815,
                                    'bytes': 9231600330,
                                },
                                '23:00 - 23:01':{
                                    'packets': 9699455,
                                    'bytes': 9524864810,
                                },
                                '22:59 - 23:00':{
                                    'packets': 9579889,
                                    'bytes': 9407450998,
                                },
                                '22:58 - 22:59':{
                                    'packets': 9911734,
                                    'bytes': 9733322788,
                                },
                                '22:57 - 22:58':{
                                    'packets': 9051879,
                                    'bytes': 8888945178,
                                },
                            },
                        },
                    },    
                },    
            },
        },
    }


    golden_output = {'execute.return_value': '''
    
    RP/0/RSP0/CPU0:router# show traffic-collector ipv4 counters prefix 10.4.1.10/32 detail
    Prefix: 10.4.1.10/32  Label: 16010 State: Active
    Base:
    Average over the last 5 collection intervals:
        Packet rate: 9496937 pps, Byte rate: 9363979882 Bps

        History of counters:
            23:01 - 23:02: Packets 9379529, Bytes: 9248215594 
            23:00 - 23:01: Packets 9687124, Bytes: 9551504264 
            22:59 - 23:00: Packets 9539200, Bytes: 9405651200 
            22:58 - 22:59: Packets 9845278, Bytes: 9707444108 
            22:57 - 22:58: Packets 9033554, Bytes: 8907084244 
    TM Counters:
        Average over the last 5 collection intervals:
            Packet rate: 9528754 pps, Byte rate: 9357236821 Bps

        History of counters:
            23:01 - 23:02: Packets 9400815, Bytes: 9231600330 
            23:00 - 23:01: Packets 9699455, Bytes: 9524864810 
            22:59 - 23:00: Packets 9579889, Bytes: 9407450998 
            22:58 - 22:59: Packets 9911734, Bytes: 9733322788 
            22:57 - 22:58: Packets 9051879, Bytes: 8888945178
            
    '''}

    def test_show_traffic_collector_ipv4_counter_prefix_detail_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowTrafficCollecterExternalInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_traffic_collector_ipv4_counter_prefix_detail_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowTrafficCollecterIpv4CountersPrefixDetail(device=self.device)
        parsed_output = obj.parse(prefix='10.4.1.10/32')
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()