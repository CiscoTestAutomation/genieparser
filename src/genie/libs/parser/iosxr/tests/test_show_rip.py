# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.iosxr.show_rip import ShowRipStatistics

# ===============================
# Unit tests for:
#    show rip statistics
#    show rip vrf {vrf} statistics
# ===============================
class test_show_rip_statistics(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip': {
                                'statistics': {
                                    'total_messages_sent': 5294,
                                    'message_send_failures': 0,
                                    'regular_updates_sent': 2944,
                                    'queries_responsed_to': 0,
                                    'rib_updates': 4365,
                                    'total_packets_received': 4896,
                                    'packets_discarded': 0,
                                    'routes_discarded': 4760,
                                    'packets_received_at_standby': 0,
                                    'routes_allocated': 9,
                                    'paths_allocated': 6,
                                    'route_malloc_failures': 0,
                                    'path_malloc_failures': 0
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\  
        RP/0/RP0/CPU0:R1#show rip statistics                                            
        Wed Jan 30 18:50:57.778 UTC                                                     
                                                                                        
        RIP statistics:                                                                 
        Total messages sent:        5294                                                
        Message send failures:      0                                                   
        Regular updates sent:       2944                                                
        Queries responsed to:       0                                                   
        RIB updates:                4365                                                
        Total packets received:     4896                                                
        Discarded packets:          0                                                   
        Discarded routes:           4760                                                
        Packet received at standby: 0                                                   
        Number of routes allocated: 9                                                   
        Number of paths allocated:  6                                                   
        Route malloc failures:      0                                                   
        Path malloc failures:       0        
    '''}

    golden_parsed_output_2 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip': {
                                'statistics': {
                                    'total_messages_sent': 995,
                                    'message_send_failures': 0,
                                    'regular_updates_sent': 988,
                                    'queries_responsed_to': 0,
                                    'rib_updates': 6,
                                    'total_packets_received': 495,
                                    'packets_discarded': 0,
                                    'routes_discarded': 0,
                                    'packets_received_at_standby': 0,
                                    'routes_allocated': 11,
                                    'paths_allocated': 7,
                                    'route_malloc_failures': 0,
                                    'path_malloc_failures': 0
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''\  
        RP/0/RP0/CPU0:R1#show rip vrf VRF1 statistics                                   
        Wed Jan 30 18:51:24.635 UTC                                                     
                                                                                        
        RIP statistics:                                                                 
        Total messages sent:        995                                                 
        Message send failures:      0                                                   
        Regular updates sent:       988                                                 
        Queries responsed to:       0                                                   
        RIB updates:                6                                                   
        Total packets received:     495                                                 
        Discarded packets:          0                                                   
        Discarded routes:           0                                                   
        Packet received at standby: 0                                                   
        Number of routes allocated: 11                                                  
        Number of paths allocated:  7                                                   
        Route malloc failures:      0                                                   
        Path malloc failures:       0  
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRipStatistics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_statistics(self):
        self.device = Mock(**self.golden_output)
        obj = ShowRipStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_statistics(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowRipStatistics(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

if __name__ == '__main__':
    unittest.main()
