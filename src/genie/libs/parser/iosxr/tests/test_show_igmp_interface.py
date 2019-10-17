
import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.iosxr.show_igmp_interface import ShowIgmpInterface

#############################################################################
# unitest For Show IGMP Interface
#############################################################################

class test_show_igmp_interface(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'GigabitEthernet0/0/0/0.110': {
            'enabled': True,
            'igmp_activity_joins': '7',
            'igmp_activity_leaves': '1',
            'igmp_max_query_response_time': '10',
            'igmp_querier_timeout': '125',
            'igmp_query_interval': '60',
            'igmp_query_response_interval': '1',
            'igmp_querying_router': '10.12.110.1',
            'igmp_state': 'enabled',
            'igmp_time_since_last_query_sent': '02:42:58',
            'igmp_time_since_last_report_received': '00:00:31',
            'igmp_time_since_router_enabled': '02:46:41',
            'igmp_version': '3',
            'ipv4': {
                '10.12.110.2/24': {
                    'ip': '10.12.110.2',
                    'prefix_length': '24'
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
                    'prefix_length': '24'
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
                    'prefix_length': '24'
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
                    'prefix_length': '24'
                }
            },
            'line_protocol': 'up',
            'oper_status': 'up'
        },
        'GigabitEthernet0/0/0/1.110': {
            'enabled': True,
            'igmp_activity_joins': '5',
            'igmp_activity_leaves': '0',
            'igmp_max_query_response_time': '10',
            'igmp_querier_timeout': '125',
            'igmp_query_interval': '60',
            'igmp_query_response_interval': '1',
            'igmp_querying_router': '10.23.110.2',
            'igmp_state': 'enabled',
            'igmp_time_since_last_query_sent': '00:00:55',
            'igmp_time_since_last_report_received': '00:00:55',
            'igmp_time_since_router_enabled': '02:46:41',
            'igmp_version': '3',
            'ipv4': {
                '10.23.110.2/24': {
                    'ip': '10.23.110.2',
                    'prefix_length': '24'
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
                    'prefix_length': '24'
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
                    'prefix_length': '24'
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
                    'prefix_length': '24'
                }
            },
            'line_protocol': 'up',
            'oper_status': 'up'
        },
        'Loopback0': {
            'enabled': True,
            'igmp_activity_joins': '6',
            'igmp_activity_leaves': '0',
            'igmp_max_query_response_time': '10',
            'igmp_querier_timeout': '125',
            'igmp_query_interval': '60',
            'igmp_query_response_interval': '1',
            'igmp_querying_router': '2.2.2.2',
            'igmp_state': 'enabled',
            'igmp_time_since_last_query_sent': '00:00:53',
            'igmp_time_since_last_report_received': '00:00:51',
            'igmp_time_since_router_enabled': '02:46:41',
            'igmp_version': '3',
            'ipv4': {
                '2.2.2.2/32': {
                    'ip': '2.2.2.2',
                    'prefix_length': '32'
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
                    'prefix_length': '24'
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

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_detail_obj = ShowIgmpInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_detail_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_detail_obj = ShowIgmpInterface(device=self.device)
        parsed_output = interface_detail_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_custom(self):
        self.device = Mock(**self.golden_interface_output)
        interface_detail_obj = ShowIgmpInterface(device=self.device)
        parsed_output = interface_detail_obj.parse(interface='GigabitEthernet0/0/0/1.115')
        self.assertEqual(parsed_output, self.golden_parsed_interface_output)


if __name__ == '__main__':
    unittest.main()
