
import re
import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.iosxr.show_igmp import (ShowIgmpInterface,
                                               ShowIgmpSummary,
                                               ShowIgmpGroupsDetail,
                                               ShowIgmpGroupsSummary)


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
                'interfaces': {
                    'GigabitEthernet0/0/0/0.110': {
                        'interface_status': 'up',
                        'igmp_activity': {
                            'joins': 7,
                            'leaves': 1
                        },
                        'igmp_max_query_response_time': 10,
                        'igmp_querier_timeout': 125,
                        'igmp_query_interval': 60,
                        'last_member_query_response_interval': 1,
                        'igmp_querying_router': '10.12.110.1',
                        'igmp_state': 'enabled',
                        'time_elapsed_since_last_query_sent': '02:42:58',
                        'time_elapsed_since_last_report_received': '00:00:31',
                        'time_elapsed_since_router_enabled': '02:46:41',
                        'igmp_version': 3,
                        'ip_address': '10.12.110.2/24',
                        'line_protocol': 'up',
                        'oper_status': 'up'
                    },
                    'GigabitEthernet0/0/0/0.115': {
                        'interface_status': 'up',
                        'igmp_state': 'disabled',
                        'ip_address': '10.12.115.2/24',
                        'line_protocol': 'up',
                        'oper_status': 'up'
                    },
                    'GigabitEthernet0/0/0/0.120': {
                        'interface_status': 'up',
                        'igmp_state': 'disabled',
                        'ip_address': '10.12.120.2/24',
                        'line_protocol': 'up',
                        'oper_status': 'up'
                    },
                    'GigabitEthernet0/0/0/0.90':{
                        'interface_status': 'up',
                        'igmp_state': 'disabled',
                        'ip_address': '10.12.90.2/24',
                        'line_protocol': 'up',
                        'oper_status': 'up'
                    },
                    'GigabitEthernet0/0/0/1.110': {
                        'interface_status': 'up',
                        'igmp_activity': {
                            'joins': 5,
                            'leaves': 0
                        },
                        'igmp_max_query_response_time': 10,
                        'igmp_querier_timeout': 125,
                        'igmp_query_interval': 60,
                        'last_member_query_response_interval': 1,
                        'igmp_querying_router': '10.23.110.2',
                        'igmp_querying_router_info': 'this system',
                        'igmp_state': 'enabled',
                        'time_elapsed_since_last_query_sent': '00:00:55',
                        'time_elapsed_since_last_report_received': '00:00:55',
                        'time_elapsed_since_router_enabled': '02:46:41',
                        'igmp_version': 3,
                        'ip_address': '10.23.110.2/24',
                        'line_protocol': 'up',
                        'oper_status': 'up'
                    },
                    'GigabitEthernet0/0/0/1.115': {
                        'interface_status': 'up',
                        'igmp_state': 'disabled',
                        'ip_address': '10.23.115.2/24',
                        'line_protocol': 'up',
                        'oper_status': 'up'
                    },
                    'GigabitEthernet0/0/0/1.120': {
                        'interface_status': 'up',
                        'igmp_state': 'disabled',
                        'ip_address': '10.23.120.2/24',
                        'line_protocol': 'up',
                        'oper_status': 'up'
                    },
                    'GigabitEthernet0/0/0/1.90': {
                        'interface_status': 'up',
                        'igmp_state': 'disabled',
                        'ip_address': '10.23.90.2/24',
                        'line_protocol': 'up',
                        'oper_status': 'up'
                    },
                    'Loopback0': {
                        'interface_status': 'up',
                        'igmp_activity': {
                            'joins': 6,
                            'leaves': 0
                        },
                        'igmp_max_query_response_time': 10,
                        'igmp_querier_timeout': 125,
                        'igmp_query_interval': 60,
                        'last_member_query_response_interval': 1,
                        'igmp_querying_router': '10.16.2.2',
                        'igmp_querying_router_info': 'this system',
                        'igmp_state': 'enabled',
                        'time_elapsed_since_last_query_sent': '00:00:53',
                        'time_elapsed_since_last_report_received': '00:00:51',
                        'time_elapsed_since_router_enabled': '02:46:41',
                        'igmp_version': 3,
                        'ip_address': '10.16.2.2/32',
                        'line_protocol': 'up',
                        'oper_status': 'up'
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''
        R2_xr# show igmp interface
        Loopback0 is up, line protocol is up
            Internet address is 10.16.2.2/32
            IGMP is enabled on interface
            Current IGMP version is 3
            IGMP query interval is 60 seconds
            IGMP querier timeout is 125 seconds
            IGMP max query response time is 10 seconds
            Last member query response interval is 1 seconds
            IGMP activity: 6 joins, 0 leaves
            IGMP querying router is 10.16.2.2 (this system)
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
                'interfaces': {
                    'GigabitEthernet0/0/0/1.115': {
                        'interface_status': 'up',
                        'igmp_state': 'disabled',
                        'ip_address': '10.23.115.2/24',
                        'line_protocol': 'up',
                        'oper_status': 'up'
                    }
                }
            }
        }
    }

    golden_parsed_interface_output1 = {
        'vrf': {
            'VRF1': {
                'interfaces': {
                    'Loopback0': {
                        'interface_status': 'up',
                        'igmp_activity': {
                            'joins': 6,
                            'leaves': 0
                        },
                        'igmp_max_query_response_time': 10,
                        'igmp_querier_timeout': 125,
                        'igmp_query_interval': 60,
                        'last_member_query_response_interval': 1,
                        'igmp_querying_router': '10.16.2.2',
                        'igmp_querying_router_info': 'this system',
                        'igmp_state': 'enabled',
                        'time_elapsed_since_last_query_sent': '00:00:53',
                        'time_elapsed_since_last_report_received': '00:00:51',
                        'time_elapsed_since_router_enabled': '02:46:41',
                        'igmp_version': 3,
                        'ip_address': '10.16.2.2/32',
                        'line_protocol': 'up',
                        'oper_status': 'up'
                    }
                }
            }
        }
    }

    golden_interface_output={'execute.return_value':'''
        R2_xr# show igmp interface GigabitEthernet0/0/0/1.115
        GigabitEthernet0/0/0/1.115 is up, line protocol is up
            Internet address is 10.23.115.2/24
            IGMP is disabled on interface
    '''}

    golden_interface_output1={'execute.return_value':'''
        R2_xr# show igmp vrf VRF1 interface
        Loopback0 is up, line protocol is up
            Internet address is 10.16.2.2/32
            IGMP is enabled on interface
            Current IGMP version is 3
            IGMP query interval is 60 seconds
            IGMP querier timeout is 125 seconds
            IGMP max query response time is 10 seconds
            Last member query response interval is 1 seconds
            IGMP activity: 6 joins, 0 leaves
            IGMP querying router is 10.16.2.2 (this system)
            Time elapsed since last query sent 00:00:53
            Time elapsed since IGMP router enabled 02:46:41
            Time elapsed since last report received 00:00:51
    '''}

    golden_parsed_interface_output2 = {
        'vrf': {
            'VRF1': {
                'interfaces': {
                    'Loopback0': {
                        'interface_status': 'up',
                        'igmp_activity': {
                            'joins': 6,
                            'leaves': 0
                        },
                        'igmp_max_query_response_time': 10,
                        'igmp_querier_timeout': 125,
                        'igmp_query_interval': 60,
                        'last_member_query_response_interval': 1,
                        'igmp_querying_router': '10.16.2.2',
                        'igmp_querying_router_info': 'this system',
                        'igmp_state': 'enabled',
                        'time_elapsed_since_last_query_sent': '00:00:53',
                        'time_elapsed_since_last_report_received': '00:00:51',
                        'time_elapsed_since_router_enabled': '02:46:41',
                        'igmp_version': 3,
                        'ip_address': '10.16.2.2/32',
                        'line_protocol': 'up',
                        'oper_status': 'up'
                    }
                }
            }
        }
    }
    
    golden_interface_output2={'execute.return_value':'''
        R2_xr# show igmp vrf VRF1 interface Loopback0
        Loopback0 is up, line protocol is up
            Internet address is 10.16.2.2/32
            IGMP is enabled on interface
            Current IGMP version is 3
            IGMP query interval is 60 seconds
            IGMP querier timeout is 125 seconds
            IGMP max query response time is 10 seconds
            Last member query response interval is 1 seconds
            IGMP activity: 6 joins, 0 leaves
            IGMP querying router is 10.16.2.2 (this system)
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
        
    def test_golden_custom_vrf_interface(self):
        self.device = Mock(**self.golden_interface_output2)
        interface_detail_obj = ShowIgmpInterface(device=self.device)
        parsed_output = interface_detail_obj.parse(vrf='VRF1', interface='Loopback0')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_interface_output2)

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
                'disabled_interfaces': 6,
                'enabled_interfaces': 3,
                'no_of_group_x_interface': 16,
                'interfaces': {
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
                'maximum_number_of_groups_for_vrf': 50000,
                'robustness_value': 2,
                'supported_interfaces': 9,
                'unsupported_interfaces': 0,
                }
            }
        }

    golden_output = {'execute.return_value': '''
        R2_xr#show igmp summary
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
                'disabled_interfaces': 6,
                'enabled_interfaces': 3,
                'no_of_group_x_interface': 15,
                'interfaces': {
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
                'maximum_number_of_groups_for_vrf': 50000,
                'robustness_value': 2,
                'supported_interfaces': 9,
                'unsupported_interfaces': 0,
                }
            }
        }

    golden_summary_output={'execute.return_value':'''
        R2_xr#show igmp vrf VRF1 summary
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
                "interfaces": {
                    "Loopback0": {
                        "group": {
                            "224.0.0.2": {
                                "host_mode": "exclude",
                                "last_reporter": "10.16.2.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "02:44:55"
                            },
                            "224.0.0.9": {
                                "host_mode": "exclude",
                                "last_reporter": "10.16.2.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "09:47:23"
                            },
                            "224.0.0.13": {
                                "host_mode": "exclude",
                                "last_reporter": "10.16.2.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "02:44:55"
                            },
                            "224.0.0.22": {
                                "host_mode": "exclude",
                                "last_reporter": "10.16.2.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "02:44:55"
                            },
                            "224.0.1.39": {
                                "host_mode": "exclude",
                                "last_reporter": "10.16.2.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "02:19:56"
                            },
                            "224.0.1.40": {
                                "host_mode": "exclude",
                                "last_reporter": "10.16.2.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
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
                                "router_mode_expires": "None",
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
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "02:44:55"
                            },
                            "224.0.0.5": {
                                "host_mode": "exclude",
                                "last_reporter": "10.12.110.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "10:36:57"
                            },
                            "224.0.0.6": {
                                "host_mode": "exclude",
                                "last_reporter": "10.12.110.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "10:36:57"
                            },
                            "224.0.0.13": {
                                "host_mode": "exclude",
                                "last_reporter": "10.12.110.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "02:44:55"
                            },
                            "224.0.0.22": {
                                "host_mode": "exclude",
                                "last_reporter": "10.12.110.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "02:44:55"
                            },
                            "224.0.1.39": {
                                "host_mode": "include",
                                "last_reporter": "10.12.110.1",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "00:01:41",
                                "suppress": 0,
                                "up_time": "02:29:47",
                            }
                        }
                    },
                    "GigabitEthernet0/0/0/0.120": {
                        "group": {
                            "224.0.0.9": {
                                "host_mode": "exclude",
                                "last_reporter": "0.0.0.0",
                                "router_mode": "INCLUDE",
                                "router_mode_expires": "None",
                                "suppress": 0,
                                "up_time": "09:47:23"
                            }
                        }
                    },
                    "GigabitEthernet0/0/0/1.120": {
                        "group": {
                            "224.0.0.9": {
                                "host_mode": "exclude",
                                "last_reporter": "0.0.0.0",
                                "router_mode": "INCLUDE",
                                "router_mode_expires": "None",
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
        R2_xr#show igmp groups detail
        Interface:	Loopback0
        Group:		224.0.0.2
        Uptime:		02:44:55
        Router mode:	EXCLUDE (Expires: never)
        Host mode:	EXCLUDE
        Last reporter:	10.16.2.2
        Suppress:	0
        Source list is empty
        Interface:	Loopback0
        Group:		224.0.0.9
        Uptime:		09:47:23
        Router mode:	EXCLUDE (Expires: never)
        Host mode:	EXCLUDE
        Last reporter:	10.16.2.2
        Suppress:	0
        Source list is empty
        Interface:	Loopback0
        Group:		224.0.0.13
        Uptime:		02:44:55
        Router mode:	EXCLUDE (Expires: never)
        Host mode:	EXCLUDE
        Last reporter:	10.16.2.2
        Suppress:	0
        Source list is empty
        Interface:	Loopback0
        Group:		224.0.0.22
        Uptime:		02:44:55
        Router mode:	EXCLUDE (Expires: never)
        Host mode:	EXCLUDE
        Last reporter:	10.16.2.2
        Suppress:	0
        Source list is empty
        Interface:	Loopback0
        Group:		224.0.1.39
        Uptime:		02:19:56
        Router mode:	EXCLUDE (Expires: never)
        Host mode:	EXCLUDE
        Last reporter:	10.16.2.2
        Suppress:	0
        Source list is empty
        Interface:	Loopback0
        Group:		224.0.1.40
        Uptime:		02:44:55
        Router mode:	EXCLUDE (Expires: never)
        Host mode:	EXCLUDE
        Last reporter:	10.16.2.2
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
        Interface:	GigabitEthernet0/0/0/0.120
        Group:		224.0.0.9
        Uptime:		09:47:23
        Router mode:	INCLUDE
        Host mode:	EXCLUDE
        Last reporter:	0.0.0.0
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
                "interfaces": {
                    "Loopback300": {
                        "group": {
                            "224.0.0.2": {
                                "host_mode": "exclude",
                                "last_reporter": "10.16.2.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "02:43:30"
                            },
                            "224.0.0.9": {
                                "host_mode": "exclude",
                                "last_reporter": "10.16.2.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "09:48:07"
                            },
                            "224.0.0.13": {
                                "host_mode": "exclude",
                                "last_reporter": "10.16.2.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "02:43:30"
                            },
                            "224.0.0.22": {
                                "host_mode": "exclude",
                                "last_reporter": "10.16.2.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
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
                                "router_mode_expires": "None",
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
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "02:43:30"
                            },
                            "224.0.0.5": {
                                "host_mode": "exclude",
                                "last_reporter": "10.12.110.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "10:37:41"
                            },
                            "224.0.0.6": {
                                "host_mode": "exclude",
                                "last_reporter": "10.12.110.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "10:37:41"
                            },
                            "224.0.0.13": {
                                "host_mode": "exclude",
                                "last_reporter": "10.12.110.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "02:43:30"
                            },
                            "224.0.0.22": {
                                "host_mode": "exclude",
                                "last_reporter": "10.12.110.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "02:43:30"
                            },
                            "224.0.1.39": {
                                "host_mode": "include",
                                "last_reporter": "10.12.110.1",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "00:01:21",
                                "suppress": 0,
                                "up_time": "02:30:06"
                            },
                            "224.0.1.40": {
                                "host_mode": "exclude",
                                "last_reporter": "10.12.110.2",
                                "router_mode": "EXCLUDE",
                                "router_mode_expires": "never",
                                "suppress": 0,
                                "up_time": "02:43:30"
                            }        
                        }
                    },
                    "GigabitEthernet0/0/0/0.420": {
                        "group": {
                            "224.0.0.9": {
                                "host_mode": "exclude",
                                "last_reporter": "0.0.0.0",
                                "router_mode": "INCLUDE",
                                "router_mode_expires": "None",
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
                                "router_mode_expires": "None",
                                "suppress": 0,
                                "up_time": "01:54:16"
                            }
                        }
                    },
                    "GigabitEthernet0/0/0/1.420": {
                        "group": {
                            "224.0.0.9": {
                                "host_mode": "exclude",
                                "last_reporter": "0.0.0.0",
                                "router_mode": "INCLUDE",
                                "router_mode_expires": "None",
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
        R2_xr#show igmp vrf VRF1 groups detail
        Interface:	Loopback300
        Group:		224.0.0.2
        Uptime:		02:43:30
        Router mode:	EXCLUDE (Expires: never)
        Host mode:	EXCLUDE
        Last reporter:	10.16.2.2
        Suppress:	0
        Source list is empty
        Interface:	Loopback300
        Group:		224.0.0.9
        Uptime:		09:48:07
        Router mode:	EXCLUDE (Expires: never)
        Host mode:	EXCLUDE
        Last reporter:	10.16.2.2
        Suppress:	0
        Source list is empty
        Interface:	Loopback300
        Group:		224.0.0.13
        Uptime:		02:43:30
        Router mode:	EXCLUDE (Expires: never)
        Host mode:	EXCLUDE
        Last reporter:	10.16.2.2
        Suppress:	0
        Source list is empty
        Interface:	Loopback300
        Group:		224.0.0.22
        Uptime:		02:43:30
        Router mode:	EXCLUDE (Expires: never)
        Host mode:	EXCLUDE
        Last reporter:	10.16.2.2
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
        Interface:	GigabitEthernet0/0/0/1.420
        Group:		224.0.0.9
        Uptime:		09:48:07
        Router mode:	INCLUDE
        Host mode:	EXCLUDE
        Last reporter:	0.0.0.0
        Suppress:	0
        Source list is empty
    '''}

    golden_output1 = {'execute.return_value': '''
        R2_xr#show igmp groups detail
            Interface:      GigabitEthernet0/0/0/2
            Group:          232.1.1.1
            Uptime:         00:04:55
            Router mode:    INCLUDE
            Host mode:      INCLUDE
            Last reporter:  192.168.1.42
            Group source list:
              Source Address   Uptime    Expires   Fwd  Flags
              192.168.1.18     00:04:55  00:01:28  Yes  Remote
    '''}
    
    golden_parsed_output1 = {
        "vrf": {
            "default": {
                "interfaces": {
                    "GigabitEthernet0/0/0/2": {
                        "group": {
                            "232.1.1.1": {
                                "host_mode": "include",
                                "last_reporter": "192.168.1.42",
                                "router_mode": "INCLUDE",
                                "router_mode_expires": "None",
                                "up_time": "00:04:55",
                                "source": {
                                    "192.168.1.18": {
                                        "up_time": "00:04:55",
                                        "expire": "00:01:28",
                                        "forward": "Yes",
                                        "flags": "Remote"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

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
        
    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        igmp_groups_detail_obj = ShowIgmpGroupsDetail(device=self.device)
        parsed_output = igmp_groups_detail_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output1)


# ==========================================================================
# Unittest for 'show igmp groups summary'
# ==========================================================================
class test_show_igmp_groups_summary(unittest.TestCase):
    """ Unit test for show igmp groups summary. """

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': """
        RP/0/RP0/CPU0:leaf-3#show igmp groups summ
        Mon Jul 13 15:45:02.517 PDT
        IGMP Route Summary for vrf default
          No. of (*,G) routes = 4
          No. of (S,G) routes = 0
          No. of Group x Interfaces = 19"""}

    golden_parsed_output_1 = {
        'vrf':
            {'default':
                {'no_g_routes': 4,
                 'no_group_x_intfs': 19,
                 'no_sg_routes': 0
                 }
             }
        }

    golden_output_2 = {'execute.return_value': """
        RP/0/RSP0/CPU0:leaf-5#show igmp vrf vpn1 groups summary 
        Thu Jul  9 17:02:32.516 PDT
        IGMP Route Summary for vrf vpn1
          No. of (*,G) routes = 4
          No. of (S,G) routes = 22
          No. of Group x Interfaces = 29"""}

    golden_parsed_output_2 = {
        'vrf':
            {'vpn1':
                {'no_g_routes': 4,
                 'no_group_x_intfs': 29,
                 'no_sg_routes': 22
                 }
             }
        }

    def test_show_igmp_groups_summary_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIgmpGroupsSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_igmp_groups_summary_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIgmpGroupsSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_show_igmp_groups_summary_full_custom_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIgmpGroupsSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


if __name__ == '__main__':
    unittest.main()
