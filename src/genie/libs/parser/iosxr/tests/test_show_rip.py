# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.iosxr.show_rip import ShowRipInterface

# ===============================
# Unit tests for:
#    show rip interface
#    show rip vrf {vrf} interface
# ===============================
class test_show_rip_interface(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            None: {
                'address_family': {
                    None: {
                        'instance': {
                            'rip': {
                                'interfaces': {
                                    'GigabitEthernet0/0/0/0.100': {
                                        'authentication': {
                                            'auth_key_chain': {
                                                'key_chain': 'Not set'
                                            },
                                            'auth_key': {
                                                'crypto_algorithm': 'None'
                                            }
                                        },
                                        'cost': 0,
                                        'neighbors': {
                                            '10.1.2.2': {
                                                'address': '10.1.2.2'
                                            }
                                        },
                                        'out_of_memory_state': 'Normal',
                                        'broadcast_for_v2': False,
                                        'accept_metric_0': False,
                                        'send_versions': 2,
                                        'receive_versions': 2,
                                        'interface_state': 'Up',
                                        'address': '10.1.2.1/24',
                                        'passive': True,
                                        'split_horizon': True,
                                        'poison_reverse': False,
                                        'socket_set': {
                                            'multicast_group': True,
                                            'lpts_filter': True
                                        },
                                        'statistics': {
                                            'discontinuity_time': 2,
                                            'bad_packets_rcvd': 0,
                                            'bad_routes_rcvd': 4733,
                                            'updates_sent': 4877
                                        }
                                    },
                                    'GigabitEthernet0/0/0/1.100': {
                                        'authentication': {
                                            'auth_key_chain': {
                                                'key_chain': 'Not set'
                                            },
                                            'auth_key': {
                                                'crypto_algorithm': 'None'
                                            }
                                        },
                                        'cost': 0,
                                        'out_of_memory_state': 'Normal',
                                        'broadcast_for_v2': False,
                                        'accept_metric_0': False,
                                        'send_versions': 2,
                                        'receive_versions': 2,
                                        'interface_state': 'Up',
                                        'address': '10.1.3.1/24',
                                        'passive': True,
                                        'split_horizon': True,
                                        'poison_reverse': False,
                                        'socket_set': {
                                            'multicast_group': True,
                                            'lpts_filter': True
                                        },
                                        'statistics': {
                                            'updates_sent': 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\  
        Wed Jan 30 18:49:59.943 UTC                                                     
                                                                                
        GigabitEthernet0/0/0/0.100                                                      
        Rip enabled?:               Passive                                             
        Out-of-memory state:        Normal                                              
        Broadcast for V2:           No                                                  
        Accept Metric 0:           No                                                   
        Send versions:              2                                                   
        Receive versions:           2                                                   
        Interface state:            Up                                                  
        IP address:                 10.1.2.1/24                                         
        Metric Cost:                0                                                   
        Split horizon:              Enabled                                             
        Poison Reverse:             Disabled                                            
        Socket set options:                                                             
            Joined multicast group:    Yes                                              
            LPTS filter set:           Yes                                              
        Authentication mode:        None                                                
        Authentication keychain:    Not set                                             
                                                                                        
        Total packets received: 4877                                                  
        Authentication mode is not set                                                
        RIP peers attached to this interface:                                           
            10.1.2.2                                                                    
                uptime (sec): 2    version: 2                                           
                packets discarded: 0    routes discarded: 4733                          
                                                                                        
        GigabitEthernet0/0/0/1.100                                                      
        Rip enabled?:               Yes                                                 
        Out-of-memory state:        Normal                                              
        Broadcast for V2:           No                                                  
        Accept Metric 0:           No                                                   
        Send versions:              2                                                   
        Receive versions:           2                                                   
        Interface state:            Up                                                  
        IP address:                 10.1.3.1/24                                         
        Metric Cost:                0                                                   
        Split horizon:              Enabled                                             
        Poison Reverse:             Disabled                                            
        Socket set options:                                                             
            Joined multicast group:    Yes                                              
            LPTS filter set:           Yes                                              
        Authentication mode:        None                                                
        Authentication keychain:    Not set                                             
                                                                                        
        Total packets received: 0                                                     
        Authentication mode is not set
    '''}

    golden_parsed_output_2 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    None: {
                        'instance': {
                            'rip': {
                                'interfaces': {
                                    'GigabitEthernet0/0/0/0.200': {
                                        'authentication': {
                                            'auth_key_chain': {
                                                'key_chain': 'Not set'
                                            },
                                            'auth_key': {
                                                'crypto_algorithm': 'None'
                                            }
                                        },
                                        'cost': 0,
                                        'neighbors': {
                                            '10.1.2.2': {
                                                'address': '10.1.2.2'
                                            }
                                        },
                                        'out_of_memory_state': 'Normal',
                                        'broadcast_for_v2': False,
                                        'accept_metric_0': False,
                                        'send_versions': 2,
                                        'receive_versions': 2,
                                        'interface_state': 'Up',
                                        'address': '10.1.2.1/24',
                                        'passive': True,
                                        'split_horizon': True,
                                        'poison_reverse': False,
                                        'socket_set': {
                                            'multicast_group': True,
                                            'lpts_filter': True
                                        },
                                        'statistics': {
                                            'discontinuity_time': 15,
                                            'bad_packets_rcvd': 0,
                                            'bad_routes_rcvd': 0,
                                            'updates_sent': 493
                                        }
                                    },
                                    'GigabitEthernet0/0/0/1.200': {
                                        'authentication': {
                                            'auth_key_chain': {
                                                'key_chain': 'Not set'
                                            },
                                            'auth_key': {
                                                'crypto_algorithm': 'None'
                                            }
                                        },
                                        'cost': 0,
                                        'out_of_memory_state': 'Normal',
                                        'broadcast_for_v2': False,
                                        'accept_metric_0': False,
                                        'send_versions': 2,
                                        'receive_versions': 2,
                                        'interface_state': 'Up',
                                        'address': '10.1.3.1/24',
                                        'passive': True,
                                        'split_horizon': True,
                                        'poison_reverse': False,
                                        'socket_set': {
                                            'multicast_group': True,
                                            'lpts_filter': True
                                        },
                                        'statistics': {
                                            'updates_sent': 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''\  
        Wed Jan 30 18:50:24.640 UTC                                                     
                                                                                
        GigabitEthernet0/0/0/0.200                                                      
        Rip enabled?:               Yes                                                 
        Out-of-memory state:        Normal                                              
        Broadcast for V2:           No                                                  
        Accept Metric 0:           No                                                   
        Send versions:              2                                                   
        Receive versions:           2                                                   
        Interface state:            Up                                                  
        IP address:                 10.1.2.1/24                                         
        Metric Cost:                0                                                   
        Split horizon:              Enabled                                             
        Poison Reverse:             Disabled                                            
        Socket set options:                                                             
            Joined multicast group:    Yes                                              
            LPTS filter set:           Yes                                              
        Authentication mode:        None                                                
        Authentication keychain:    Not set                                             
                                                                                        
        Total packets received: 493                                                   
        Authentication mode is not set                                                
        RIP peers attached to this interface:                                           
            10.1.2.2                                                                    
                uptime (sec): 15    version: 2                                          
                packets discarded: 0    routes discarded: 0                             
                                                                                        
        GigabitEthernet0/0/0/1.200                                                      
        Rip enabled?:               Yes                                                 
        Out-of-memory state:        Normal                                              
        Broadcast for V2:           No                                                  
        Accept Metric 0:           No                                                   
        Send versions:              2                                                   
        Receive versions:           2                                                   
        Interface state:            Up                                                  
        IP address:                 10.1.3.1/24                                         
        Metric Cost:                0                                                   
        Split horizon:              Enabled                                             
        Poison Reverse:             Disabled                                            
        Socket set options:                                                             
            Joined multicast group:    Yes                                              
            LPTS filter set:           Yes                                              
        Authentication mode:        None                                                
        Authentication keychain:    Not set                                             
                                                                                        
        Total packets received: 0                                                     
        Authentication mode is not set  
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRipInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_interface(self):
        self.device = Mock(**self.golden_output)
        obj = ShowRipInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_interface(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowRipInterface(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

if __name__ == '__main__':
    unittest.main()
