# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.iosxr.show_rip import ShowRip, \
                                            ShowRipStatistics, \
                                            ShowRipDatabase, \
                                            ShowRipInterface
                  

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
                                'default_metric': '3',
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
                                'default_metric': '1',
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
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_vrf_all(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowRip(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


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
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_vrf_statistics(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowRipStatistics(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


# ===============================
# Unit tests for:
#    show rip database
#    show rip vrf {vrf} database
# ===============================
class test_show_rip_database(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip': {
                                'routes': {
                                    '10.1.2.0/24': {
                                        'index': {
                                            1: {
                                                'metric': 0,
                                                'route_type': 'connected',
                                                'interface': 'GigabitEthernet0/0/0/0.100'
                                            }
                                        }
                                    },
                                    '10.1.3.0/24': {
                                        'index': {
                                            1: {
                                                'metric': 0,
                                                'route_type': 'connected',
                                                'interface': 'GigabitEthernet0/0/0/1.100'
                                            }
                                        }
                                    },
                                    '10.0.0.0/8': {
                                        'index': {
                                            1: {
                                                'summary_type': 'auto-summary'
                                            }
                                        }
                                    },
                                    '172.16.1.0/24': {
                                        'index': {
                                            1: {
                                                'metric': 3,
                                                'distance': 0,
                                                'redistributed': True
                                            }
                                        }
                                    },
                                    '172.16.11.0/24': {
                                        'index': {
                                            1: {
                                                'metric': 3,
                                                'distance': 1,
                                                'redistributed': True
                                            }
                                        }
                                    },
                                    '172.16.22.0/24': {
                                        'index': {
                                            1: {
                                                'metric': 11,
                                                'next_hop': '10.1.2.2',
                                                'up_time': '15s',
                                                'interface': 'GigabitEthernet0/0/0/0.100'
                                            }
                                        }
                                    },
                                    '172.16.0.0/16': {
                                        'index': {
                                            1: {
                                                'summary_type': 'auto-summary'
                                            }
                                        }
                                    },
                                    '192.168.1.1/32': {
                                        'index': {
                                            1: {
                                                'metric': 3,
                                                'distance': 0,
                                                'redistributed': True
                                            }
                                        }
                                    },
                                    '192.168.1.0/24': {
                                        'index': {
                                            1: {
                                                'summary_type': 'auto-summary'
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
    }

    golden_output = {'execute.return_value': '''\  
        RP/0/RP0/CPU0:R1#show rip database
        Wed Jan 30 18:48:59.532 UTC                                                     
                                                                                
        Routes held in RIP's topology database:                                         
        10.1.2.0/24                                                                     
            [0]    directly connected, GigabitEthernet0/0/0/0.100                       
        10.1.3.0/24                                                                     
            [0]    directly connected, GigabitEthernet0/0/0/1.100                       
        10.0.0.0/8    auto-summary                                                      
        172.16.1.0/24                                                                   
            [3] distance: 0    redistributed                                            
        172.16.11.0/24                                                                  
            [3] distance: 1    redistributed                                            
        172.16.22.0/24                                                                  
            [11] via 10.1.2.2, next hop 10.1.2.2, Uptime: 15s, GigabitEthernet0/0/0/0.100                                                                               
        172.16.0.0/16    auto-summary                                                   
        192.168.1.1/32                                                                  
            [3] distance: 0    redistributed                                            
        192.168.1.0/24    auto-summary 
        '''}

    golden_parsed_output_2 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip': {
                                'routes': {
                                    '10.1.2.0/24': {
                                        'index': {
                                            1: {
                                                'metric': 0,
                                                'route_type': 'connected',
                                                'interface': 'GigabitEthernet0/0/0/0.200'
                                            }
                                        }
                                    },
                                    '10.1.3.0/24': {
                                        'index': {
                                            1: {
                                                'metric': 0,
                                                'route_type': 'connected',
                                                'interface': 'GigabitEthernet0/0/0/1.200'
                                            }
                                        }
                                    },
                                    '10.2.3.0/24': {
                                        'index': {
                                            1: {
                                                'metric': 1,
                                                'next_hop': '10.1.2.2',
                                                'up_time': '10s',
                                                'interface': 'GigabitEthernet0/0/0/0.200'
                                            }
                                        }
                                    },
                                    '10.0.0.0/8': {
                                        'index': {
                                            1: {
                                                'summary_type': 'auto-summary'
                                            }
                                        }
                                    },
                                    '172.16.11.0/24': {
                                        'index': {
                                            1: {
                                                'metric': 15,
                                                'distance': 1,
                                                'redistributed': True
                                            }
                                        }
                                    },
                                    '172.16.22.0/24': {
                                        'index': {
                                            1: {
                                                'metric': 1,
                                                'next_hop': '10.1.2.2',
                                                'up_time': '10s',
                                                'interface': 'GigabitEthernet0/0/0/0.200'
                                            }
                                        }
                                    },
                                    '172.16.0.0/16': {
                                        'index': {
                                            1: {
                                                'summary_type': 'auto-summary'
                                            }
                                        }
                                    },
                                    '192.168.1.1/32': {
                                        'index': {
                                            1: {
                                                'metric': 1,
                                                'distance': 0,
                                                'redistributed': True
                                            }
                                        }
                                    },
                                    '192.168.1.0/24': {
                                        'index': {
                                            1: {
                                                'summary_type': 'auto-summary'
                                            }
                                        }
                                    },
                                    '192.168.2.2/32': {
                                        'index': {
                                            1: {
                                                'metric': 1,
                                                'next_hop': '10.1.2.2',
                                                'up_time': '10s',
                                                'interface': 'GigabitEthernet0/0/0/0.200'
                                            }
                                        }
                                    },
                                    '192.168.2.0/24': {
                                        'index': {
                                            1: {
                                                'summary_type': 'auto-summary'
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
    }

    golden_output_2 = {'execute.return_value': '''\ 
        RP/0/RP0/CPU0:R1#show rip vrf VRF1 database  
        Wed Jan 30 18:49:22.086 UTC                                                     
                                                                                
        Routes held in RIP's topology database:                                         
        10.1.2.0/24                                                                     
            [0]    directly connected, GigabitEthernet0/0/0/0.200                       
        10.1.3.0/24                                                                     
            [0]    directly connected, GigabitEthernet0/0/0/1.200                       
        10.2.3.0/24                                                                     
            [1] via 10.1.2.2, next hop 10.1.2.2, Uptime: 10s, GigabitEthernet0/0/0/0.200
        10.0.0.0/8    auto-summary                                                      
        172.16.11.0/24                                                                  
            [15] distance: 1    redistributed                                           
        172.16.22.0/24                                                                  
            [1] via 10.1.2.2, next hop 10.1.2.2, Uptime: 10s, GigabitEthernet0/0/0/0.200
        172.16.0.0/16    auto-summary                                                   
        192.168.1.1/32                                                                  
            [1] distance: 0    redistributed                                            
        192.168.1.0/24    auto-summary                                                  
        192.168.2.2/32                                                                  
            [1] via 10.1.2.2, next hop 10.1.2.2, Uptime: 10s, GigabitEthernet0/0/0/0.200
        192.168.2.0/24    auto-summary  
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRipDatabase(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_database(self):
        self.device = Mock(**self.golden_output)
        obj = ShowRipDatabase(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_database(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowRipDatabase(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_2)


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
            'default': {
                'address_family': {
                    'ipv4': {
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
                                                'address': '10.1.2.2',
                                                'uptime': 2,
                                                'version': 2,
                                                'packets_discarded': 0,
                                                'routes_discarded': 4733
                                            }
                                        },
                                        'out_of_memory_state': 'Normal',
                                        'broadcast_for_v2': False,
                                        'accept_metric_0': False,
                                        'send_versions': 2,
                                        'receive_versions': 2,
                                        'oper_status': 'Up',
                                        'address': '10.1.2.1/24',
                                        'passive': True,
                                        'split_horizon': True,
                                        'poison_reverse': False,
                                        'socket_set': {
                                            'multicast_group': True,
                                            'lpts_filter': True
                                        },
                                        'statistics': {
                                            'total_packets_received': 4877
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
                                        'oper_status': 'Up',
                                        'address': '10.1.3.1/24',
                                        'passive': False,
                                        'split_horizon': True,
                                        'poison_reverse': False,
                                        'socket_set': {
                                            'multicast_group': True,
                                            'lpts_filter': True
                                        },
                                        'statistics': {
                                            'total_packets_received': 0
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
        RP/0/RP0/CPU0:R1#show rip interface  
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
                    'ipv4': {
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
                                                'address': '10.1.2.2',
                                                'uptime': 15,
                                                'version': 2,
                                                'packets_discarded': 0,
                                                'routes_discarded': 0
                                            }
                                        },
                                        'out_of_memory_state': 'Normal',
                                        'broadcast_for_v2': False,
                                        'accept_metric_0': False,
                                        'send_versions': 2,
                                        'receive_versions': 2,
                                        'oper_status': 'Up',
                                        'address': '10.1.2.1/24',
                                        'passive': False,
                                        'split_horizon': True,
                                        'poison_reverse': False,
                                        'socket_set': {
                                            'multicast_group': True,
                                            'lpts_filter': True
                                        },
                                        'statistics': {
                                            'total_packets_received': 493
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
                                        'oper_status': 'Up',
                                        'address': '10.1.3.1/24',
                                        'passive': False,
                                        'split_horizon': True,
                                        'poison_reverse': False,
                                        'socket_set': {
                                            'multicast_group': True,
                                            'lpts_filter': True
                                        },
                                        'statistics': {
                                            'total_packets_received': 0
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
        RP/0/RP0/CPU0:R1#show rip vrf VRF1 interface 
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

