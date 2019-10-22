
import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.iosxr.show_igmp import ShowIgmpInterface, ShowIgmpSummary, ShowIgmpGroupsDetail

#############################################################################
# unitest For Show IGMP Interface
#############################################################################

class TestShowIgmpInterface(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'vrf': {
            'default': {
                'GigabitEthernet0/0/0/0.110': {
                    'enabled': True,
                    'igmp_activity_joins': 7,
                    'igmp_activity_leaves': 1,
                    'igmp_max_query_response_time': 10,
                    'igmp_querier_timeout': 125,
                    'igmp_query_interval': 60,
                    'igmp_query_response_interval': 1,
                    'igmp_querying_router': '10.12.110.1',
                    'igmp_state': 'enabled',
                    'igmp_time_since_last_query_sent': '02:42:58',
                    'igmp_time_since_last_report_received': '00:00:31',
                    'igmp_time_since_router_enabled': '02:46:41',
                    'igmp_version': 3,
                    'ipv4': {
                        '10.12.110.2/24': {
                            'ip': '10.12.110.2',
                            'prefix_length': 24
                            }
                        },
                    'line_protocol': 'up',
                    'oper_status': 'up'
                },
                'GigabitEthernet0/0/0/0.115': {
                    'enabled': True,
                    'igmp_state': 'disabled',
                    'ipv4':{
                        '10.12.115.2/24': {
                            'ip': '10.12.115.2',
                            'prefix_length': 24
                            }
                        },
                    'line_protocol': 'up',
                    'oper_status': 'up'
                },
                'GigabitEthernet0/0/0/0.120': {
                    'enabled': True,
                    'igmp_state': 'disabled',
                    'ipv4': {
                        '10.12.120.2/24': {
                            'ip': '10.12.120.2',
                            'prefix_length': 24
                        }
                    },
                    'line_protocol': 'up',
                    'oper_status': 'up'
                },
                'GigabitEthernet0/0/0/0.90':{
                    'enabled': True,
                    'igmp_state': 'disabled',
                    'ipv4': {
                        '10.12.90.2/24': {
                            'ip': '10.12.90.2',
                            'prefix_length': 24
                        }
                    },
                    'line_protocol': 'up',
                    'oper_status': 'up'
                },
                'GigabitEthernet0/0/0/1.110': {
                    'enabled': True,
                    'igmp_activity_joins': 5,
                    'igmp_activity_leaves': 0,
                    'igmp_max_query_response_time': 10,
                    'igmp_querier_timeout': 125,
                    'igmp_query_interval': 60,
                    'igmp_query_response_interval': 1,
                    'igmp_querying_router': '10.23.110.2',
                    'igmp_state': 'enabled',
                    'igmp_time_since_last_query_sent': '00:00:55',
                    'igmp_time_since_last_report_received': '00:00:55',
                   'igmp_time_since_router_enabled': '02:46:41',
                   'igmp_version': 3,
                   'ipv4': {
                       '10.23.110.2/24': {
                           'ip': '10.23.110.2',
                           'prefix_length': 24
                       }
                   },
                   'line_protocol': 'up',
                   'oper_status': 'up'
               },
               'GigabitEthernet0/0/0/1.115': {
                   'enabled': True,
                   'igmp_state': 'disabled',
                   'ipv4': {
                       '10.23.115.2/24': {
                           'ip': '10.23.115.2',
                           'prefix_length': 24
                       }
                   },
                   'line_protocol': 'up',
                   'oper_status': 'up'
               },
               'GigabitEthernet0/0/0/1.120': {
                   'enabled': True,
                   'igmp_state': 'disabled',
                   'ipv4': {
                       '10.23.120.2/24': {
                           'ip': '10.23.120.2',
                           'prefix_length': 24
                       }
                   },
                    'line_protocol': 'up',
                    'oper_status': 'up'
                },
                'GigabitEthernet0/0/0/1.90': {
                    'enabled': True,
                    'igmp_state': 'disabled',
                    'ipv4': {
                        '10.23.90.2/24': {
                            'ip': '10.23.90.2',
                            'prefix_length': 24
                        }
                    },
                    'line_protocol': 'up',
                    'oper_status': 'up'
                },
                'Loopback0': {
                    'enabled': True,
                    'igmp_activity_joins': 6,
                    'igmp_activity_leaves': 0,
                    'igmp_max_query_response_time': 10,
                    'igmp_querier_timeout': 125,
                    'igmp_query_interval': 60,
                    'igmp_query_response_interval': 1,
                    'igmp_querying_router': '2.2.2.2',
                    'igmp_state': 'enabled',
                    'igmp_time_since_last_query_sent': '00:00:53',
                    'igmp_time_since_last_report_received': '00:00:51',
                    'igmp_time_since_router_enabled': '02:46:41',
                    'igmp_version': 3,
                    'ipv4': {
                        '2.2.2.2/32': {
                            'ip': '2.2.2.2',
                            'prefix_length': 32
                            }
                        },
                    'line_protocol': 'up',
                    'oper_status': 'up'
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''
      Loopback0 is up, line protocol is up
        Internet address is 2.2.2.2/32
        IGMP is enabled on interface
        Current IGMP version is 3
        IGMP query interval is 60 seconds
        IGMP querier timeout is 125 seconds
        IGMP max query response time is 10 seconds
        Last member query response interval is 1 seconds
        IGMP activity: 6 joins, 0 leaves
        IGMP querying router is 2.2.2.2 (this system)
        Time elapsed since last query sent 00:00:53
        Time elapsed since IGMP router enabled 02:46:41
        Time elapsed since last report received 00:00:51
      GigabitEthernet0/0/0/0.90 is up, line protocol is up
        Internet address is 10.12.90.2/24
        IGMP is disabled on interface
      GigabitEthernet0/0/0/1.90 is up, line protocol is up
        Internet address is 10.23.90.2/24
        IGMP is disabled on interface
      GigabitEthernet0/0/0/0.110 is up, line protocol is up
        Internet address is 10.12.110.2/24
        IGMP is enabled on interface
        Current IGMP version is 3
        IGMP query interval is 60 seconds
        IGMP querier timeout is 125 seconds
        IGMP max query response time is 10 seconds
        Last member query response interval is 1 seconds
        IGMP activity: 7 joins, 1 leaves
        IGMP querying router is 10.12.110.1
        Time elapsed since last query sent 02:42:58
        Time elapsed since IGMP router enabled 02:46:41
        Time elapsed since last report received 00:00:31
      GigabitEthernet0/0/0/0.115 is up, line protocol is up
        Internet address is 10.12.115.2/24
        IGMP is disabled on interface
      GigabitEthernet0/0/0/0.120 is up, line protocol is up
        Internet address is 10.12.120.2/24
        IGMP is disabled on interface
      GigabitEthernet0/0/0/1.110 is up, line protocol is up
        Internet address is 10.23.110.2/24
        IGMP is enabled on interface
        Current IGMP version is 3
        IGMP query interval is 60 seconds
        IGMP querier timeout is 125 seconds
        IGMP max query response time is 10 seconds
        Last member query response interval is 1 seconds
        IGMP activity: 5 joins, 0 leaves
        IGMP querying router is 10.23.110.2 (this system)
        Time elapsed since last query sent 00:00:55
        Time elapsed since IGMP router enabled 02:46:41
        Time elapsed since last report received 00:00:55
      GigabitEthernet0/0/0/1.115 is up, line protocol is up
        Internet address is 10.23.115.2/24
        IGMP is disabled on interface
      GigabitEthernet0/0/0/1.120 is up, line protocol is up
        Internet address is 10.23.120.2/24
        IGMP is disabled on interface
    
    '''}
    
    golden_parsed_interface_output = {
        'vrf': {
            'default': {
                'GigabitEthernet0/0/0/1.115': {
                    'enabled': True,
                    'igmp_state': 'disabled',
                    'ipv4': {
                        '10.23.115.2/24': {
                            'ip': '10.23.115.2',
                            'prefix_length': 24
                        }
                    },
                    'line_protocol': 'up',
                    'oper_status': 'up'
                }
            }
        }
    }

    golden_parsed_interface_output1 = {
        'vrf': {
            'VRF1': {
                'Loopback0': {
                    'enabled': True,
                    'igmp_activity_joins': 6,
                    'igmp_activity_leaves': 0,
                    'igmp_max_query_response_time': 10,
                    'igmp_querier_timeout': 125,
                    'igmp_query_interval': 60,
                    'igmp_query_response_interval': 1,
                    'igmp_querying_router': '2.2.2.2',
                    'igmp_state': 'enabled',
                    'igmp_time_since_last_query_sent': '00:00:53',
                    'igmp_time_since_last_report_received': '00:00:51',
                    'igmp_time_since_router_enabled': '02:46:41',
                    'igmp_version': 3,
                    'ipv4': {
                        '2.2.2.2/32': {
                            'ip': '2.2.2.2',
                            'prefix_length': 32
                            }
                        },
                    'line_protocol': 'up',
                    'oper_status': 'up'
                }
            }
        }
    }

    golden_interface_output={'execute.return_value':'''
      GigabitEthernet0/0/0/1.115 is up, line protocol is up
        Internet address is 10.23.115.2/24
        IGMP is disabled on interface

    '''}

    golden_interface_output1={'execute.return_value':'''
      Loopback0 is up, line protocol is up
        Internet address is 2.2.2.2/32
        IGMP is enabled on interface
        Current IGMP version is 3
        IGMP query interval is 60 seconds
        IGMP querier timeout is 125 seconds
        IGMP max query response time is 10 seconds
        Last member query response interval is 1 seconds
        IGMP activity: 6 joins, 0 leaves
        IGMP querying router is 2.2.2.2 (this system)
        Time elapsed since last query sent 00:00:53
        Time elapsed since IGMP router enabled 02:46:41
        Time elapsed since last report received 00:00:51

    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_detail_obj = ShowIgmpInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_detail_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_detail_obj = ShowIgmpInterface(device=self.device)
        parsed_output = interface_detail_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_custom_interface(self):
        self.device = Mock(**self.golden_interface_output)
        interface_detail_obj = ShowIgmpInterface(device=self.device)
        parsed_output = interface_detail_obj.parse(interface='GigabitEthernet0/0/0/1.115')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_interface_output)
        
    def test_golden_custom_vrf(self):
        self.device = Mock(**self.golden_interface_output1)
        interface_detail_obj = ShowIgmpInterface(device=self.device)
        parsed_output = interface_detail_obj.parse(vrf='VRF1')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_interface_output1)

#############################################################################
# unitest For Show IGMP Summary
#############################################################################

class test_show_igmp_summary(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'vrf': {
            'default': {
                'igmp': {
                    'disabled_interfaces': 6,
                    'enabled_interfaces': 3,
                    'groupxInterfaces': 16,
                    'interface': {
                        'Loopback0': {
                            'max_groups': 25000,
                            'number_groups': 6 
                        },
                        'GigabitEthernet0/0/0/0.90': {
                            'max_groups': 25000,
                            'number_groups': 1
                        },
                        'GigabitEthernet0/0/0/1.90': {
                            'max_groups': 25000,
                            'number_groups': 1
                        },
                        'GigabitEthernet0/0/0/0.110': {
                            'max_groups': 25000,
                            'number_groups': 6
                        },
                        'GigabitEthernet0/0/0/0.115': {
                            'max_groups': 25000,
                            'number_groups': 4
                        },
                        'GigabitEthernet0/0/0/0.120': {
                            'max_groups': 25000,
                            'number_groups': 1
                        },
                        'GigabitEthernet0/0/0/1.110': {
                            'max_groups': 25000,
                            'number_groups': 5
                        },
                        'GigabitEthernet0/0/0/1.115': {
                            'max_groups': 25000,
                            'number_groups': 0
                        },
                        'GigabitEthernet0/0/0/1.120': {
                            'max_groups': 25000,
                            'number_groups': 1
                        }
                    },
                    'mte_tuple_count': 0,
                    'noOfGroupsForVrf': 50000,
                    'robustness_value': 2,
                    'supported_interfaces': 9,
                    'unsupported_interfaces': 0,

                }
            }
        }
    }

    golden_output = {'execute.return_value': '''
      Robustness Value 2
      No. of Group x Interfaces 16
      Maximum number of Groups for this VRF 50000
      
      Supported Interfaces   : 9
      Unsupported Interfaces : 0
      Enabled Interfaces     : 3
      Disabled Interfaces    : 6
      
      MTE tuple count        : 0
      
      Interface                       Number  Max #
                                      Groups  Groups
      Loopback0                       6       25000
      GigabitEthernet0/0/0/0.90       1       25000
      GigabitEthernet0/0/0/1.90       1       25000
      GigabitEthernet0/0/0/0.110      6       25000
      GigabitEthernet0/0/0/0.115      4       25000
      GigabitEthernet0/0/0/0.120      1       25000
      GigabitEthernet0/0/0/1.110      5       25000
      GigabitEthernet0/0/0/1.115      0       25000
      GigabitEthernet0/0/0/1.120      1       25000
    
    '''}
    
    golden_parsed_summary_output = {
        'vrf': {
            'VRF1': {
                'igmp': {
                    'disabled_interfaces': 6,
                    'enabled_interfaces': 3,
                    'groupxInterfaces': 15,
                    'interface': {
                        'Loopback300': {
                            'max_groups': 25000,
                            'number_groups': 4 
                        },
                        'GigabitEthernet0/0/0/0.390': {
                            'max_groups': 25000,
                            'number_groups': 1
                        },
                        'GigabitEthernet0/0/0/0.410': {
                            'max_groups': 25000,
                            'number_groups': 7
                        },
                        'GigabitEthernet0/0/0/0.415': {
                            'max_groups': 25000,
                            'number_groups': 4
                        },
                        'GigabitEthernet0/0/0/0.420': {
                            'max_groups': 25000,
                            'number_groups': 1
                        },
                        'GigabitEthernet0/0/0/1.390': {
                            'max_groups': 25000,
                            'number_groups': 1
                        },
                        'GigabitEthernet0/0/0/1.410': {
                            'max_groups': 25000,
                            'number_groups': 5
                        },
                        'GigabitEthernet0/0/0/1.415': {
                            'max_groups': 25000,
                            'number_groups': 0
                        },
                        'GigabitEthernet0/0/0/1.420': {
                            'max_groups': 25000,
                            'number_groups': 1
                        }
                    },
                    'mte_tuple_count': 0,
                    'noOfGroupsForVrf': 50000,
                    'robustness_value': 2,
                    'supported_interfaces': 9,
                    'unsupported_interfaces': 0,
                }
            }
        }
    }

    golden_summary_output={'execute.return_value':'''
      Robustness Value 2
      No. of Group x Interfaces 15
      Maximum number of Groups for this VRF 50000
      
      Supported Interfaces   : 9
      Unsupported Interfaces : 0
      Enabled Interfaces     : 3
      Disabled Interfaces    : 6
      
      MTE tuple count        : 0
      
      Interface                       Number  Max #
                                      Groups  Groups
      Loopback300                     4       25000
      GigabitEthernet0/0/0/0.390      1       25000
      GigabitEthernet0/0/0/0.410      7       25000
      GigabitEthernet0/0/0/0.415      4       25000
      GigabitEthernet0/0/0/0.420      1       25000
      GigabitEthernet0/0/0/1.390      1       25000
      GigabitEthernet0/0/0/1.410      5       25000
      GigabitEthernet0/0/0/1.415      0       25000
      GigabitEthernet0/0/0/1.420      1       25000

    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        summary_detail_obj = ShowIgmpSummary(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = summary_detail_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        summary_detail_obj = ShowIgmpSummary(device=self.device)
        parsed_output = summary_detail_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_custom(self):
        self.device = Mock(**self.golden_summary_output)
        summary_detail_obj = ShowIgmpSummary(device=self.device)
        parsed_output = summary_detail_obj.parse(vrf='VRF1')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_summary_output)
  
#############################################################################
# unitest For Show IGMP Groups Detail
#############################################################################
 
class test_show_igmp_groups_detail(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        "vrf": {
            "default": {
		        "interface": {
		        	"Loopback0": {
		                "group": {
		                	"224.0.0.2": {
		        				"host_mode": "exclude",
		        				"last_reporter": "2.2.2.2",
		        				"router_mode": "EXCLUDE (Expires: never)",
		        				"source_list": "empty",
		        				"suppress": 0,
		                		"up_time": "02:44:55"
		                		},
		                	"224.0.0.9": {
		        				"host_mode": "exclude",
			        			"last_reporter": "2.2.2.2",
			        			"router_mode": "EXCLUDE (Expires: never)",
			        			"source_list": "empty",
			        			"suppress": 0,
		                		"up_time": "09:47:23"
		                		},
		                    "224.0.0.13": {
			        			"host_mode": "exclude",
			        			"last_reporter": "2.2.2.2",
			        			"router_mode": "EXCLUDE (Expires: never)",
			        			"source_list": "empty",
			        			"suppress": 0,
		                    	"up_time": "02:44:55"
		                    },
		                    "224.0.0.22": {
			        			"host_mode": "exclude",
			        			"last_reporter": "2.2.2.2",
			        			"router_mode": "EXCLUDE (Expires: never)",
			        			"source_list": "empty",
			        			"suppress": 0,
		                    	"up_time": "02:44:55"
		                	},
		                	"224.0.1.39": {
			        			"host_mode": "exclude",
			        			"last_reporter": "2.2.2.2",
			        			"router_mode": "EXCLUDE (Expires: never)",
			        			"source_list": "empty",
			        			"suppress": 0,
		                		"up_time": "02:19:56"
		                	},
		                	"224.0.1.40": {
			        			"host_mode": "exclude",
			        			"last_reporter": "2.2.2.2",
			        			"router_mode": "EXCLUDE (Expires: never)",
			        			"source_list": "empty",
		        				"suppress": 0,
		                		"up_time": "02:44:55"
		                	}	
		                }
                    },
                    "GigabitEthernet0/0/0/0.90": {
                    	"group": {
                    		"224.0.0.10": {
		        				"host_mode": "exclude",
		        				"last_reporter": "0.0.0.0",
		        				"router_mode": "INCLUDE",
		        				"source_list": "empty",
		        				"suppress": 0,
                    			"up_time": "01:53:32"
                    		}
                    	}
                    },
                    "GigabitEthernet0/0/0/1.90": {
	                	"group": {
	                		"224.0.0.10": {
		        				"host_mode": "exclude",
		        				"last_reporter": "0.0.0.0",
		        				"router_mode": "INCLUDE",
		        				"source_list": "empty",
		        				"suppress": 0,
	                			"up_time": "01:53:32"
	                		}
	                	}
	                },
	                "GigabitEthernet0/0/0/0.110": {
	                	"group": {
	                		"224.0.0.2": {
				        		"host_mode": "exclude",
				        		"last_reporter": "10.12.110.2",
				        		"router_mode": "EXCLUDE (Expires: never)",
				        		"source_list": "empty",
				        		"suppress": 0,
	        	        		"up_time": "02:44:55"
	        	        	},
	        	        	"224.0.0.5": {
				        		"host_mode": "exclude",
				        		"last_reporter": "10.12.110.2",
				        		"router_mode": "EXCLUDE (Expires: never)",
				        		"source_list": "empty",
				        		"suppress": 0,
	        	        		"up_time": "10:36:57"
				        	},
		                	"224.0.0.6": {
				        		"host_mode": "exclude",
				        		"last_reporter": "10.12.110.2",
				        		"router_mode": "EXCLUDE (Expires: never)",
				        		"source_list": "empty",
				        		"suppress": 0,
		                		"up_time": "10:36:57"
		                	},
		                	"224.0.0.13": {
				        		"host_mode": "exclude",
				        		"last_reporter": "10.12.110.2",
				        		"router_mode": "EXCLUDE (Expires: never)",
				        		"source_list": "empty",
				        		"suppress": 0,
		                		"up_time": "02:44:55"
		                	},
		                	"224.0.0.22": {
				        		"host_mode": "exclude",
				        		"last_reporter": "10.12.110.2",
			        			"router_mode": "EXCLUDE (Expires: never)",
			        			"source_list": "empty",
			        			"suppress": 0,
		                		"up_time": "02:44:55"
		                	},
		                	"224.0.1.39": {
			        			"host_mode": "include",
			        			"last_reporter": "10.12.110.1",
			        			"router_mode": "EXCLUDE (Expires: 00:01:41)",
			        			"source_list": "empty",
			        			"suppress": 0,
		                		"up_time": "02:29:47",
		                	}
		                }
			        },
	              "GigabitEthernet0/0/0/0.115": {
                        "group": {
                            "239.2.2.1": {
		        				"host_mode": "exclude",
		        				"last_reporter": "0.0.0.0",
		        				"router_mode": "INCLUDE",
		        				"source_list": "empty",
		        				"suppress": 0,
                                "up_time": "01:53:32"
                            },
                            "239.2.2.2": {
		        				"host_mode": "exclude",
		        				"last_reporter": "0.0.0.0",
		        				"router_mode": "INCLUDE",
		        				"source_list": "empty",
		        				"suppress": 0,
                                "up_time": "01:53:32"
                            },
                            "239.2.2.3": {
                                "host_mode": "exclude",
                                "last_reporter": "0.0.0.0",
                                "router_mode": "INCLUDE",
                                "source_list": "empty",
                                "suppress": 0,
                                "up_time": "01:55:08"
		                	},	
                            "239.2.2.4": {
                                "host_mode": "exclude",
                                "last_reporter": "0.0.0.0",
                                "router_mode": "INCLUDE",
                                "source_list": "empty",
                                "suppress": 0,
                                "up_time": "01:55:08"
		                	}			
		                }
                    },
	                "GigabitEthernet0/0/0/0.120": {
	                	"group": {
	                		"224.0.0.9": {
			         			"host_mode": "exclude",
			         			"last_reporter": "0.0.0.0",
			         			"router_mode": "INCLUDE",
			         			"source_list": "empty",
			         			"suppress": 0,
	                			"up_time": "09:47:23"
	                		}
	                	}
	                },
	                "GigabitEthernet0/0/0/1.110": {
	                	"group": {
	                		"224.0.0.2": {
			         			"host_mode": "exclude",
			         			"last_reporter": "10.23.110.2",
			         			"router_mode": "EXCLUDE (Expires: never)",
			         			"source_list": "empty",
			         			"suppress": 0,
	                			"up_time": "02:44:55"
	                		},
	                		"224.0.0.5": {
			         			"host_mode": "exclude",
			         			"last_reporter": "10.23.110.2",
			         			"router_mode": "EXCLUDE (Expires: never)",
                                "source_list": "empty",
                                "suppress": 0,
                                "up_time": "10:36:57",
                            },
	                    	"224.0.0.6": {
			        			"host_mode": "exclude",
			        			"last_reporter": "10.23.110.2",
			        			"router_mode": "EXCLUDE (Expires: never)",
			        			"source_list": "empty",
			        			"suppress": 0,
	                    		"up_time": "10:36:57"
	                    	},
	                    	"224.0.0.13": {
			        			"host_mode": "exclude",
			        			"last_reporter": "10.23.110.2",
			        			"router_mode": "EXCLUDE (Expires: never)",
			        			"source_list": "empty",
                                "suppress": 0,
                                "up_time": "02:44:55"
                            },
                            "224.0.0.22": {
                                "host_mode": "exclude",
                                "last_reporter": "10.23.110.2",
                                "router_mode": "EXCLUDE (Expires: never)",
                                "source_list": "empty",
                                "suppress": 0,
                                "up_time": "02:44:55"				        
                            }
                        }
                    },
                    "GigabitEthernet0/0/0/1.120": {
                    	"group": {
                    		"224.0.0.9": {
			         			"host_mode": "exclude",
			         			"last_reporter": "0.0.0.0",
			         			"router_mode": "INCLUDE",
			         			"source_list": "empty",
			         			"suppress": 0,
                    			"up_time": "09:47:23"
                    			
                    		}			
                    	}
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''
      Interface:	Loopback0
      Group:		224.0.0.2
      Uptime:		02:44:55
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	2.2.2.2
      Suppress:	0
      Source list is empty
      Interface:	Loopback0
      Group:		224.0.0.9
      Uptime:		09:47:23
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	2.2.2.2
      Suppress:	0
      Source list is empty
      Interface:	Loopback0
      Group:		224.0.0.13
      Uptime:		02:44:55
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	2.2.2.2
      Suppress:	0
      Source list is empty
      Interface:	Loopback0
      Group:		224.0.0.22
      Uptime:		02:44:55
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	2.2.2.2
      Suppress:	0
      Source list is empty
      Interface:	Loopback0
      Group:		224.0.1.39
      Uptime:		02:19:56
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	2.2.2.2
      Suppress:	0
      Source list is empty
      Interface:	Loopback0
      Group:		224.0.1.40
      Uptime:		02:44:55
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	2.2.2.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.90
      Group:		224.0.0.10
      Uptime:		01:53:32
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/1.90
      Group:		224.0.0.10
      Uptime:		01:53:32
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.110
      Group:		224.0.0.2
      Uptime:		02:44:55
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.12.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.110
      Group:		224.0.0.5
      Uptime:		10:36:57
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.12.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.110
      Group:		224.0.0.6
      Uptime:		10:36:57
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.12.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.110
      Group:		224.0.0.13
      Uptime:		02:44:55
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.12.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.110
      Group:		224.0.0.22
      Uptime:		02:44:55
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.12.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.110
      Group:		224.0.1.39
      Uptime:		02:29:47
      Router mode:	EXCLUDE (Expires: 00:01:41)
      Host mode:	INCLUDE
      Last reporter:	10.12.110.1
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.115
      Group:		239.2.2.1
      Uptime:		01:53:32
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.115
      Group:		239.2.2.2
      Uptime:		01:53:32
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.115
      Group:		239.2.2.3
      Uptime:		01:55:08
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.115
      Group:		239.2.2.4
      Uptime:		01:55:08
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.120
      Group:		224.0.0.9
      Uptime:		09:47:23
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/1.110
      Group:		224.0.0.2
      Uptime:		02:44:55
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.23.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/1.110
      Group:		224.0.0.5
      Uptime:		10:36:57
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.23.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/1.110
      Group:		224.0.0.6
      Uptime:		10:36:57
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.23.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/1.110
      Group:		224.0.0.13
      Uptime:		02:44:55
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.23.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/1.110
      Group:		224.0.0.22
      Uptime:		02:44:55
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.23.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/1.120
      Group:		224.0.0.9
      Uptime:		09:47:23
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty
    
    '''}
    
    golden_parsed_igmp_groups_output = {
        "vrf": {
            "VRF1": {
		        "interface": {
		        	"Loopback300": {
		                "group": {
		                	"224.0.0.2": {
		        				"host_mode": "exclude",
		        				"last_reporter": "2.2.2.2",
		        				"router_mode": "EXCLUDE (Expires: never)",
		        				"source_list": "empty",
		        				"suppress": 0,
		                		"up_time": "02:43:30"
		                		},
		                	"224.0.0.9": {
		        				"host_mode": "exclude",
			        			"last_reporter": "2.2.2.2",
			        			"router_mode": "EXCLUDE (Expires: never)",
			        			"source_list": "empty",
			        			"suppress": 0,
		                		"up_time": "09:48:07"
		                		},
		                    "224.0.0.13": {
			        			"host_mode": "exclude",
			        			"last_reporter": "2.2.2.2",
			        			"router_mode": "EXCLUDE (Expires: never)",
			        			"source_list": "empty",
			        			"suppress": 0,
		                    	"up_time": "02:43:30"
		                    },
		                    "224.0.0.22": {
			        			"host_mode": "exclude",
			        			"last_reporter": "2.2.2.2",
			        			"router_mode": "EXCLUDE (Expires: never)",
			        			"source_list": "empty",
			        			"suppress": 0,
		                    	"up_time": "02:43:30"
		                	}
		                }
                    },
                    "GigabitEthernet0/0/0/0.390": {
                    	"group": {
                    		"224.0.0.10": {
		        				"host_mode": "exclude",
		        				"last_reporter": "0.0.0.0",
		        				"router_mode": "INCLUDE",
		        				"source_list": "empty",
		        				"suppress": 0,
                    			"up_time": "01:54:16"
                    		}
                    	}
                    },
                    "GigabitEthernet0/0/0/0.410": {
	                	"group": {
	                		"224.0.0.2": {
		        				"host_mode": "exclude",
		        				"last_reporter": "10.12.110.2",
		        				"router_mode": "EXCLUDE (Expires: never)",
		        				"source_list": "empty",
		        				"suppress": 0,
	                			"up_time": "02:43:30"
	                		},
                            "224.0.0.5": {
		        				"host_mode": "exclude",
		        				"last_reporter": "10.12.110.2",
		        				"router_mode": "EXCLUDE (Expires: never)",
		        				"source_list": "empty",
		        				"suppress": 0,
	                			"up_time": "10:37:41"
                            },
                            "224.0.0.6": {
		        				"host_mode": "exclude",
		        				"last_reporter": "10.12.110.2",
		        				"router_mode": "EXCLUDE (Expires: never)",
		        				"source_list": "empty",
		        				"suppress": 0,
	                			"up_time": "10:37:41"
                            },
                            "224.0.0.13": {
		        				"host_mode": "exclude",
		        				"last_reporter": "10.12.110.2",
		        				"router_mode": "EXCLUDE (Expires: never)",
		        				"source_list": "empty",
		        				"suppress": 0,
	                			"up_time": "02:43:30"
                            },
                            "224.0.0.22": {
		        				"host_mode": "exclude",
		        				"last_reporter": "10.12.110.2",
		        				"router_mode": "EXCLUDE (Expires: never)",
		        				"source_list": "empty",
		        				"suppress": 0,
	                			"up_time": "02:43:30"
                            },
                            "224.0.1.39": {
		        				"host_mode": "include",
		        				"last_reporter": "10.12.110.1",
		        				"router_mode": "EXCLUDE (Expires: 00:01:21)",
		        				"source_list": "empty",
		        				"suppress": 0,
	                			"up_time": "02:30:06"
                            },
                            "224.0.1.40": {
		        				"host_mode": "exclude",
		        				"last_reporter": "10.12.110.2",
		        				"router_mode": "EXCLUDE (Expires: never)",
		        				"source_list": "empty",
		        				"suppress": 0,
	                			"up_time": "02:43:30"
                            }
                                
	                	}
	                },
	                "GigabitEthernet0/0/0/0.415": {
	                	"group": {
	                		"239.2.2.1": {
				        		"host_mode": "exclude",
				        		"last_reporter": "0.0.0.0",
				        		"router_mode": "INCLUDE",
				        		"source_list": "empty",
				        		"suppress": 0,
	        	        		"up_time": "01:54:16"
	        	        	},
	        	        	"239.2.2.2": {
				        		"host_mode": "exclude",
				        		"last_reporter": "0.0.0.0",
				        		"router_mode": "INCLUDE",
				        		"source_list": "empty",
				        		"suppress": 0,
	        	        		"up_time": "01:54:16"
				        	},
		                	"239.2.2.3": {
				        		"host_mode": "exclude",
				        		"last_reporter": "0.0.0.0",
				        		"router_mode": "INCLUDE",
				        		"source_list": "empty",
				        		"suppress": 0,
		                		"up_time": "01:55:17"
		                	},
		                	"239.2.2.4": {
				        		"host_mode": "exclude",
				        		"last_reporter": "0.0.0.0",
				        		"router_mode": "INCLUDE",
				        		"source_list": "empty",
				        		"suppress": 0,
		                		"up_time": "01:55:17"
		                	}
                        }
                    },
	              "GigabitEthernet0/0/0/0.420": {
                        "group": {
                            "224.0.0.9": {
		        				"host_mode": "exclude",
		        				"last_reporter": "0.0.0.0",
		        				"router_mode": "INCLUDE",
		        				"source_list": "empty",
		        				"suppress": 0,
                                "up_time": "09:48:07"
                            }
                        }
                    },
	                "GigabitEthernet0/0/0/1.390": {
	                	"group": {
	                		"224.0.0.10": {
			         			"host_mode": "exclude",
			         			"last_reporter": "0.0.0.0",
			         			"router_mode": "INCLUDE",
			         			"source_list": "empty",
			         			"suppress": 0,
	                			"up_time": "01:54:16"
	                		}
	                	}
	                },
                    "GigabitEthernet0/0/0/1.410": {
                        "group": {
	                		"224.0.0.2": {
			         			"host_mode": "exclude",
			         			"last_reporter": "10.23.110.2",
			         			"router_mode": "EXCLUDE (Expires: never)",
                                "source_list": "empty",
                                "suppress": 0,
                                "up_time": "02:43:30",
                            },
	                    	"224.0.0.5": {
			        			"host_mode": "exclude",
			        			"last_reporter": "10.23.110.2",
			        			"router_mode": "EXCLUDE (Expires: never)",
			        			"source_list": "empty",
			        			"suppress": 0,
	                    		"up_time": "10:37:41"
	                    	},
	                    	"224.0.0.6": {
			        			"host_mode": "exclude",
			        			"last_reporter": "10.23.110.2",
			        			"router_mode": "EXCLUDE (Expires: never)",
			        			"source_list": "empty",
                                "suppress": 0,
                                "up_time": "10:37:41"
                            },
                            "224.0.0.13": {
                                "host_mode": "exclude",
                                "last_reporter": "10.23.110.2",
                                "router_mode": "EXCLUDE (Expires: never)",
                                "source_list": "empty",
                                "suppress": 0,
                                "up_time": "02:43:30"				        
                            },
                            "224.0.0.22": {
                                "host_mode": "exclude",
                                "last_reporter": "10.23.110.2",
                                "router_mode": "EXCLUDE (Expires: never)",
                                "source_list": "empty",
                                "suppress": 0,
                                "up_time": "02:43:30"
                            }
                        }
                    },
                    "GigabitEthernet0/0/0/1.420": {
                    	"group": {
                    		"224.0.0.9": {
			         			"host_mode": "exclude",
			         			"last_reporter": "0.0.0.0",
			         			"router_mode": "INCLUDE",
			         			"source_list": "empty",
			         			"suppress": 0,
                    			"up_time": "09:48:07"
                    		}			
                    	}
                    }
                }
            }
        }
    }

    golden_igmp_groups_output={'execute.return_value':'''
      Interface:	Loopback300
      Group:		224.0.0.2
      Uptime:		02:43:30
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	2.2.2.2
      Suppress:	0
      Source list is empty
      Interface:	Loopback300
      Group:		224.0.0.9
      Uptime:		09:48:07
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	2.2.2.2
      Suppress:	0
      Source list is empty
      Interface:	Loopback300
      Group:		224.0.0.13
      Uptime:		02:43:30
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	2.2.2.2
      Suppress:	0
      Source list is empty
      Interface:	Loopback300
      Group:		224.0.0.22
      Uptime:		02:43:30
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	2.2.2.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.390
      Group:		224.0.0.10
      Uptime:		01:54:16
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.410
      Group:		224.0.0.2
      Uptime:		02:43:30
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.12.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.410
      Group:		224.0.0.5
      Uptime:		10:37:41
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.12.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.410
      Group:		224.0.0.6
      Uptime:		10:37:41
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.12.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.410
      Group:		224.0.0.13
      Uptime:		02:43:30
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.12.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.410
      Group:		224.0.0.22
      Uptime:		02:43:30
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.12.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.410
      Group:		224.0.1.39
      Uptime:		02:30:06
      Router mode:	EXCLUDE (Expires: 00:01:21)
      Host mode:	INCLUDE
      Last reporter:	10.12.110.1
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.410
      Group:		224.0.1.40
      Uptime:		02:43:30
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.12.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.415
      Group:		239.2.2.1
      Uptime:		01:54:16
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.415
      Group:		239.2.2.2
      Uptime:		01:54:16
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.415
      Group:		239.2.2.3
      Uptime:		01:55:17
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.415
      Group:		239.2.2.4
      Uptime:		01:55:17
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/0.420
      Group:		224.0.0.9
      Uptime:		09:48:07
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/1.390
      Group:		224.0.0.10
      Uptime:		01:54:16
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/1.410
      Group:		224.0.0.2
      Uptime:		02:43:30
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.23.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/1.410
      Group:		224.0.0.5
      Uptime:		10:37:41
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.23.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/1.410
      Group:		224.0.0.6
      Uptime:		10:37:41
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.23.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/1.410
      Group:		224.0.0.13
      Uptime:		02:43:30
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.23.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/1.410
      Group:		224.0.0.22
      Uptime:		02:43:30
      Router mode:	EXCLUDE (Expires: never)
      Host mode:	EXCLUDE
      Last reporter:	10.23.110.2
      Suppress:	0
      Source list is empty
      Interface:	GigabitEthernet0/0/0/1.420
      Group:		224.0.0.9
      Uptime:		09:48:07
      Router mode:	INCLUDE
      Host mode:	EXCLUDE
      Last reporter:	0.0.0.0
      Suppress:	0
      Source list is empty

    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        igmp_groups_detail_obj = ShowIgmpGroupsDetail(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = igmp_groups_detail_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        igmp_groups_detail_obj = ShowIgmpGroupsDetail(device=self.device)
        parsed_output = igmp_groups_detail_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_custom(self):
        self.device = Mock(**self.golden_igmp_groups_output)
        igmp_groups_detail_obj = ShowIgmpGroupsDetail(device=self.device)
        parsed_output = igmp_groups_detail_obj.parse(vrf='VRF1')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_igmp_groups_output)
      
if __name__ == '__main__':
    unittest.main()
