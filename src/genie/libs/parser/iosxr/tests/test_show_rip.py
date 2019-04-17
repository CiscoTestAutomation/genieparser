# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.iosxr.show_rip import ShowRip

# ===============================
# Unit tests for:
#   'show rip'
#   'show rip vrf all'
# ===============================
class test_show_rip(unittest.TestCase):
    device = Device(name="aDevice")
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip': {
                                'active': 'Yes',
                                'added_to_socket': 'Yes',
                                'out_of_memory_state': 'Normal',
                                'version': 2,
                                'default_metric': 3,
                                'maximum_paths': 4,
                                'auto_summarize': 'No',
                                'broadcast_for_v2': 'No',
                                'packet_source_validation': 'Yes',
                                'nsf': 'Disabled',
                                'timers': {
                                    'until_next_update': 7,
                                    'update_interval': 10,
                                    'invalid_interval': 31,
                                    'holddown_interval': 32,
                                    'flush_interval': 33
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\  
        RP/0/RP0/CPU0:R1#show rip                                                                                                      
        Wed Jan 30 18:47:49.312 UTC                                                     
                                                                                        
        RIP config:                                                                     
        Active:                    Yes                                                  
        Added to socket:           Yes                                                  
        Out-of-memory state:        Normal                                              
        Version:                    2                                                   
        Default metric:             3                                                   
        Maximum paths:              4                                                   
        Auto summarize:            No                                                   
        Broadcast for V2:          No                                                   
        Packet source validation:  Yes                                                  
        NSF:                        Disabled                                            
        Timers: Update:             10 seconds (7 seconds until next update)            
                Invalid:            31 seconds                                          
                Holddown:           32 seconds                                          
                Flush:              33 seconds  
    '''}

    golden_parsed_output_2 = {
        'vrf': {
            'all': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip': {
                                'active': 'Yes',
                                'added_to_socket': 'Yes',
                                'out_of_memory_state': 'Normal',
                                'version': 2,
                                'default_metric': 1,
                                'maximum_paths': 4,
                                'auto_summarize': 'No',
                                'broadcast_for_v2': 'No',
                                'packet_source_validation': 'No',
                                'nsf': 'Disabled',
                                'timers': {
                                    'until_next_update': 18,
                                    'update_interval': 30,
                                    'invalid_interval': 180,
                                    'holddown_interval': 180,
                                    'flush_interval': 240
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''\                                                    
        RP/0/RP0/CPU0:R1#show rip vrf all                                               
        Wed Jan 30 18:48:40.235 UTC                                                     
                                                                                
                                                                                
        VRF: VRF1                                                                       
        =======================================                                         
        RIP config:                                                                     
        Active:                    Yes                                                  
        Added to socket:           Yes                                                  
        Out-of-memory state:        Normal                                              
        Version:                    2                                                   
        Default metric:             1                                                   
        Maximum paths:              4                                                   
        Auto summarize:            No                                                   
        Broadcast for V2:          No                                                   
        Packet source validation:  No                                                   
        NSF:                        Disabled                                            
        Timers: Update:             30 seconds (18 seconds until next update)           
                Invalid:            180 seconds                                         
                Holddown:           180 seconds                                         
                Flush:              240 seconds
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRip(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowRip(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_all(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowRip(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

if __name__ == '__main__':
    unittest.main()
