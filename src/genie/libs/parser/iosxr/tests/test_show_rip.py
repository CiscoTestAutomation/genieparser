# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.iosxr.show_rip import ShowRipDatabase

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

if __name__ == '__main__':
    unittest.main()
