
import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.iosxr.show_igmp import ShowIgmpInterface, ShowIgmpSummary

#############################################################################
# unitest For Show IGMP Interface
#############################################################################

class TestShowIgmpInterface(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
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

    golden_parsed_interface_output = {
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

    golden_parsed_interface_output1 = {
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
        parsed_output = interface_detail_obj.parse(vrf='default')
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
        'igmp': {
            'Disabled_Interfaces': 6,
            'Enabled_Interfaces': 3,
            'GroupxInterfaces': 16,
            'Interface': {
                'Loopback0': {
                    'Max_Groups': 25000,
                    'Number_Groups': 6 
                },
                'GigabitEthernet0/0/0/0.90': {
                    'Max_Groups': 25000,
                    'Number_Groups': 1
                },
                'GigabitEthernet0/0/0/1.90': {
                    'Max_Groups': 25000,
                    'Number_Groups': 1
                },
                'GigabitEthernet0/0/0/0.110': {
                    'Max_Groups': 25000,
                    'Number_Groups': 6
                },
                'GigabitEthernet0/0/0/0.115': {
                    'Max_Groups': 25000,
                    'Number_Groups': 4
                },
                'GigabitEthernet0/0/0/0.120': {
                    'Max_Groups': 25000,
                    'Number_Groups': 1
                },
                'GigabitEthernet0/0/0/1.110': {
                    'Max_Groups': 25000,
                    'Number_Groups': 5
                },
                'GigabitEthernet0/0/0/1.115': {
                    'Max_Groups': 25000,
                    'Number_Groups': 0
                },
                'GigabitEthernet0/0/0/1.120': {
                    'Max_Groups': 25000,
                    'Number_Groups': 1
                }
            },
            'MTE_tuple_count': 0,
            'NoOfGroupsForVrf': 50000,
            'Robustness_value': 2,
            'Supported_Interfaces': 9,
            'Unsupported_Interfaces': 0,

        }
    }

    golden_parsed_summary_output = {
        'igmp': {
            'Disabled_Interfaces': 6,
            'Enabled_Interfaces': 3,
            'GroupxInterfaces': 15,
            'Interface': {
                'Loopback300': {
                    'Max_Groups': 25000,
                    'Number_Groups': 4 
                },
                'GigabitEthernet0/0/0/0.390': {
                    'Max_Groups': 25000,
                    'Number_Groups': 1
                },
                'GigabitEthernet0/0/0/0.410': {
                    'Max_Groups': 25000,
                    'Number_Groups': 7
                },
                'GigabitEthernet0/0/0/0.415': {
                    'Max_Groups': 25000,
                    'Number_Groups': 4
                },
                'GigabitEthernet0/0/0/0.420': {
                    'Max_Groups': 25000,
                    'Number_Groups': 1
                },
                'GigabitEthernet0/0/0/1.390': {
                    'Max_Groups': 25000,
                    'Number_Groups': 1
                },
                'GigabitEthernet0/0/0/1.410': {
                    'Max_Groups': 25000,
                    'Number_Groups': 5
                },
                'GigabitEthernet0/0/0/1.415': {
                    'Max_Groups': 25000,
                    'Number_Groups': 0
                },
                'GigabitEthernet0/0/0/1.420': {
                    'Max_Groups': 25000,
                    'Number_Groups': 1
                }
            },
            'MTE_tuple_count': 0,
            'NoOfGroupsForVrf': 50000,
            'Robustness_value': 2,
            'Supported_Interfaces': 9,
            'Unsupported_Interfaces': 0,
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
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_custom(self):
        self.device = Mock(**self.golden_summary_output)
        summary_detail_obj = ShowIgmpSummary(device=self.device)
        parsed_output = summary_detail_obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_summary_output)
        
if __name__ == '__main__':
    unittest.main()
