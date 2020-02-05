# Python
import unittest
from unittest.mock import Mock
 
# ATS
from pyats.topology import Device
from pyats.topology import loader
 
# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxe show_ip_parser
from genie.libs.parser.iosxr.show_mld import ShowMldSummaryInternal, \
                                             ShowMldInterface, \
                                             ShowMldGroupsDetail, \
                                             ShowMldGroupsGroupDetail

# ==============================================================================
# Unit test for 
#    * 'show mld summary internal'
#    * 'show mld vrf {vrf} summary internal'
# ==============================================================================
class test_show_mld_summary_internal(unittest.TestCase):
    ''' 
    Unit test for:
    show mld summary internal
    show mld vrf {vrf} summary internal
    '''

    device = Device(name = 'aDevice')
    empty_output = { 'execute.return_value' : '' }

    # show mld summary internal
    golden_parsed_output1 = {
        'vrf': {
            'default': {
                'disabled_intf': 0,
                'enabled_intf': 1,
                'interface': {
                    'GigabitEthernet0/0/0/0': {
                        'igmp_r_uptime': '1d06h',
                        'last_query': '00:29:26',
                        'last_report': '00:04:16',
                        'max_groups': 6400,
                        'num_groups': 13,
                        'on': True,
                        'parent': '0x0'
                    }
                },
                'max_num_groups_x_intfs': 75000,
                'mte_tuple_count': 0,
                'num_groups_x_intf': 13,
                'robustness_value': 10,
                'supported_intf': 1,
                'unsupported_intf': 0
            }
        }
    }

    golden_output1 = { 'execute.return_value': 
        '''
        RP/0/0/CPU0:ios#show mld summary internal

        Robustness Value 10
        No. of Group x Interfaces 13
        Maximum number of Group x Interfaces 75000

        Supported Interfaces   : 1
        Unsupported Interfaces : 0
        Enabled Interfaces     : 1
        Disabled Interfaces    : 0

        MTE tuple count        : 0

        Interface                       Number  Max #   On Parent     Last     Last     IGMP R
                                        Groups  Groups                query    Report   Uptime
        GigabitEthernet0/0/0/0          13      6400    Y  0x0        00:29:26 00:04:16    1d06h
        '''
    }

    # show mld vrf {vrf} summary internal
    golden_parsed_output2 = {
        'vrf': {
            'VRF1': {
                'disabled_intf': 0,
                'enabled_intf': 1,
                'interface': {
                    'GigabitEthernet0/0/0/1': {
                        'igmp_r_uptime': '1d06h',
                        'last_query': '00:00:03',
                        'last_report': '00:00:01',
                        'max_groups': 6400,
                        'num_groups': 10,
                        'on': True,
                        'parent': '0x0'
                    }
                },
                'max_num_groups_x_intfs': 75000,
                'mte_tuple_count': 0,
                'num_groups_x_intf': 10,
                'robustness_value': 10,
                'supported_intf': 1,
                'unsupported_intf': 0
            }
        }
    }

    golden_output2 = { 'execute.return_value': 
        '''
        RP/0/0/CPU0:ios#show mld vrf VRF1 summary internal 

        Robustness Value 10
        No. of Group x Interfaces 10
        Maximum number of Group x Interfaces 75000

        Supported Interfaces   : 1
        Unsupported Interfaces : 0
        Enabled Interfaces     : 1
        Disabled Interfaces    : 0

        MTE tuple count        : 0

        Interface                       Number  Max #   On Parent     Last     Last     IGMP R
                                        Groups  Groups                query    Report   Uptime
        GigabitEthernet0/0/0/1          10      6400    Y  0x0        00:00:03 00:00:01    1d06h
        '''
    }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowMldSummaryInternal(device = self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    # show mld summary internal
    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowMldSummaryInternal(device = self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)
    
    # show mld vrf {vrf} summary internal
    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowMldSummaryInternal(device = self.device)
        parsed_output = obj.parse(vrf = 'VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output2)


# ==============================================================================
# Unit test for 
#    * 'show mld interface'
#    * 'show mld vrf {vrf} interface'
# ==============================================================================
class test_show_mld_interface(unittest.TestCase):
    ''' 
    Unit test for:
    show mld interface
    show mld vrf {vrf} interface
    '''

    device = Device(name = 'aDevice')
    empty_output = { 'execute.return_value' : '' }

    # show mld interface
    golden_parsed_output1 = {
        'vrf': {
            'default': {
                'interface': {
                    'GigabitEthernet0/0/0/0': {
                        'counters': {
                            'joins': 18,
                            'leaves': 5
                        },
                        'enable': True,
                        'internet_address': 'fe80::5054:ff:fefa:9ad7',
                        'interface_status': 'up',
                        'last_member_query_interval': 1,
                        'oper_status': 'up',
                        'querier': 'fe80::5054:ff:fed7:c01f',
                        'querier_timeout': 3666,
                        'query_interval': 366,
                        'query_max_response_time': 12,
                        'time_elapsed_since_igmp_router_enabled': '1d06h',
                        'time_elapsed_since_last_query_sent': '00:30:16',
                        'time_elapsed_since_last_report_received': '00:05:05',
                        'version': 2
                    }
                }
            }
        }
    }

    golden_output1 = { 'execute.return_value': 
        '''
        RP/0/0/CPU0:ios#show mld interface

        GigabitEthernet0/0/0/0 is up, line protocol is up
          Internet address is fe80::5054:ff:fefa:9ad7
          MLD is enabled on interface
          Current MLD version is 2
          MLD query interval is 366 seconds
          MLD querier timeout is 3666 seconds
          MLD max query response time is 12 seconds
          Last member query response interval is 1 seconds
          MLD activity: 18 joins, 5 leaves
          MLD querying router is fe80::5054:ff:fed7:c01f 
          Time elapsed since last query sent 00:30:16
          Time elapsed since IGMP router enabled 1d06h
          Time elapsed since last report received 00:05:05
        '''
    }

    # show mld vrf {vrf} interface
    golden_parsed_output2 = {
        'vrf': {
            'VRF1': {
                'interface': {
                    'GigabitEthernet0/0/0/1': {
                        'counters': {
                            'joins': 12,
                            'leaves': 2
                        },
                        'enable': True,
                        'internet_address': 'fe80::5054:ff:fe35:f846',
                        'interface_status': 'up',
                        'last_member_query_interval': 1,
                        'oper_status': 'up',
                        'querier_timeout': 3666,
                        'query_interval': 366,
                        'query_max_response_time': 12,
                        'time_elapsed_since_igmp_router_enabled': '1d06h',
                        'time_elapsed_since_last_query_sent': '00:00:53',
                        'time_elapsed_since_last_report_received': '00:00:51',
                        'version': 2
                    }
                }
            }
        }
    }

    golden_output2 = { 'execute.return_value': 
        '''
        RP/0/0/CPU0:ios#show mld vrf VRF1 interface

        GigabitEthernet0/0/0/1 is up, line protocol is up
          Internet address is fe80::5054:ff:fe35:f846
          MLD is enabled on interface
          Current MLD version is 2
          MLD query interval is 366 seconds
          MLD querier timeout is 3666 seconds
          MLD max query response time is 12 seconds
          Last member query response interval is 1 seconds
          MLD activity: 12 joins, 2 leaves
          MLD querying router is fe80::5054:ff:fe35:f846 (this system)
          Time elapsed since last query sent 00:00:53
          Time elapsed since IGMP router enabled 1d06h
          Time elapsed since last report received 00:00:51
        '''
    }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowMldInterface(device = self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    # show mld interface
    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowMldInterface(device = self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)
    
    # show mld vrf {vrf} interface
    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowMldInterface(device = self.device)
        parsed_output = obj.parse(vrf = 'VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output2)



# ==============================================================================
# Unit test for 
#    * 'show mld groups detail'
#    * 'show mld vrf {vrf} groups detail'
#    * 'show mld groups {group} detail'
# ==============================================================================
class test_show_mld_groups_detail(unittest.TestCase):
    ''' 
    Unit test for:
    show mld groups detail
    show mld vrf {vrf} groups detail
    show mld groups {group} detail
    '''

    device = Device(name = 'aDevice')
    empty_output = { 'execute.return_value' : '' }

    # show mld groups detail
    golden_parsed_output1 = {
        'vrf': {
            'default': {
                'interface': {
                    'GigabitEthernet0/0/0/0': {
                        'group': {
                            'ff02::16': {
                                'expire': 'never',
                                'router_mode': 'exclude',
                                'host_mode': 'exclude',
                                'last_reporter': 'fe80::5054:ff:fefa:9ad7',
                                'up_time': '1d06h'
                            },
                            'ff02::1:ff28:cd4b': {
                                'expire': '01:00:01',
                                'router_mode': 'exclude',
                                'host_mode': 'include',
                                'last_reporter': 'fe80::eca7:a4ff:fe28:cd4b',
                                'up_time': '1d06h'
                            },
                            'ff02::1:ff60:50aa': {
                                'expire': '01:00:01',
                                'router_mode': 'exclude',
                                'host_mode': 'include',
                                'last_reporter': 'fe80::eca7:a4ff:fe28:cd4b',
                                'up_time': '1d06h'
                            },
                            'ff02::1:ffae:4aba': {
                                'expire': '01:00:01',
                                'router_mode': 'exclude',
                                'host_mode': 'include',
                                'last_reporter': 'fe80::eca7:a4ff:fe28:cd4b',
                                'up_time': '1d06h'
                            },
                            'ff02::1:ffd7:c01f': {
                                'expire': '00:29:15',
                                'router_mode': 'exclude',
                                'host_mode': 'include',
                                'last_reporter': 'fe80::5054:ff:fed7:c01f',
                                'up_time': '00:33:19'
                            },
                            'ff02::1:ffda:f428': {
                                'expire': '01:00:01',
                                'router_mode': 'exclude',
                                'host_mode': 'include',
                                'last_reporter': 'fe80::eca7:a4ff:fe28:cd4b',
                                'up_time': '06:27:46'
                            },
                            'ff02::2': {
                                'expire': 'never',
                                'router_mode': 'exclude',
                                'host_mode': 'exclude',
                                'last_reporter': 'fe80::5054:ff:fefa:9ad7',
                                'up_time': '1d06h'
                            },
                            'ff02::d': {
                                'expire': 'never',
                                'router_mode': 'exclude',
                                'host_mode': 'exclude',
                                'last_reporter': 'fe80::5054:ff:fefa:9ad7',
                                'up_time': '1d06h'
                            },
                            'ff15:1::1': {
                                'router_mode': 'include',
                                'host_mode': 'include',
                                'last_reporter': 'fe80::5054:ff:fefa:9ad7',
                                'source': {
                                    '2001:db8:2:2::2': {
                                        'expire': '01:00:00',
                                        'flags': 'Remote Local 2d',
                                        'forward': True,
                                        'up_time': '08:06:00'
                                    }
                                },
                                'up_time': '08:06:00'
                            },
                            'ff25:2::1': {
                                'expire': 'never',
                                'router_mode': 'exclude',
                                'host_mode': 'exclude',
                                'last_reporter': 'fe80::5054:ff:fefa:9ad7',
                                'up_time': '08:06:00'
                            },
                            'ff35:1::1': {
                                'router_mode': 'include',
                                'host_mode': 'include',
                                'last_reporter': 'fe80::5054:ff:fefa:9ad7',
                                'source': {
                                    '2001:db8:3:3::3': {
                                        'expire': '01:00:00',
                                        'flags': 'Remote Local e',
                                        'forward': True,
                                        'up_time': '00:33:28'
                                    }
                                },
                                'up_time': '00:33:28'
                            },
                            'ff45:1::1': {
                                'expire': 'never',
                                'router_mode': 'exclude',
                                'host_mode': 'exclude',
                                'last_reporter': 'fe80::5054:ff:fefa:9ad7',
                                'up_time': '00:33:28'
                            },
                            'fffe::1': {
                                'expire': '00:59:49',
                                'router_mode': 'exclude',
                                'host_mode': 'include',
                                'last_reporter': 'fe80::5054:ff:fed7:c01f',
                                'up_time': '07:59:31'
                            }
                        },
                        'join_group': {
                            'ff15:1::1 2001:db8:2:2::2': {
                                'group': 'ff15:1::1',
                                'source': '2001:db8:2:2::2'
                            }
                        },
                        'static_group': {
                            'ff35:1::1 2001:db8:3:3::3': {
                                'group': 'ff35:1::1',
                                'source': '2001:db8:3:3::3'
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output1 = { 'execute.return_value': 
        '''
        RP/0/0/CPU0:ios#show mld groups detail

        Interface:      GigabitEthernet0/0/0/0
        Group:          ff02::2
        Uptime:         1d06h
        Router mode:    EXCLUDE (Expires: never)
        Host mode:      EXCLUDE
        Last reporter:  fe80::5054:ff:fefa:9ad7
        Source list is empty
        Interface:      GigabitEthernet0/0/0/0
        Group:          ff02::d
        Uptime:         1d06h
        Router mode:    EXCLUDE (Expires: never)
        Host mode:      EXCLUDE
        Last reporter:  fe80::5054:ff:fefa:9ad7
        Source list is empty
        Interface:      GigabitEthernet0/0/0/0
        Group:          ff02::16
        Uptime:         1d06h
        Router mode:    EXCLUDE (Expires: never)
        Host mode:      EXCLUDE
        Last reporter:  fe80::5054:ff:fefa:9ad7
        Source list is empty
        Interface:      GigabitEthernet0/0/0/0
        Group:          ff02::1:ff28:cd4b
        Uptime:         1d06h
        Router mode:    EXCLUDE (Expires: 01:00:01)
        Host mode:      INCLUDE
        Last reporter:  fe80::eca7:a4ff:fe28:cd4b
        Source list is empty
        Interface:      GigabitEthernet0/0/0/0
        Group:          ff02::1:ff60:50aa
        Uptime:         1d06h
        Router mode:    EXCLUDE (Expires: 01:00:01)
        Host mode:      INCLUDE
        Last reporter:  fe80::eca7:a4ff:fe28:cd4b
        Source list is empty
        Interface:      GigabitEthernet0/0/0/0
        Group:          ff02::1:ffae:4aba
        Uptime:         1d06h
        Router mode:    EXCLUDE (Expires: 01:00:01)
        Host mode:      INCLUDE
        Last reporter:  fe80::eca7:a4ff:fe28:cd4b
        Source list is empty
        Interface:      GigabitEthernet0/0/0/0
        Group:          ff02::1:ffd7:c01f
        Uptime:         00:33:19
        Router mode:    EXCLUDE (Expires: 00:29:15)
        Host mode:      INCLUDE
        Last reporter:  fe80::5054:ff:fed7:c01f
        Source list is empty
        Interface:      GigabitEthernet0/0/0/0
        Group:          ff02::1:ffda:f428
        Uptime:         06:27:46
        Router mode:    EXCLUDE (Expires: 01:00:01)
        Host mode:      INCLUDE
        Last reporter:  fe80::eca7:a4ff:fe28:cd4b
        Source list is empty
        Interface:      GigabitEthernet0/0/0/0
        Group:          ff15:1::1
        Uptime:         08:06:00
        Router mode:    INCLUDE
        Host mode:      INCLUDE
        Last reporter:  fe80::5054:ff:fefa:9ad7
        Group source list:
          Source Address                          Uptime    Expires   Fwd  Flags
          2001:db8:2:2::2                       08:06:00  01:00:00  Yes  Remote Local 2d
        Interface:      GigabitEthernet0/0/0/0
        Group:          ff25:2::1
        Uptime:         08:06:00
        Router mode:    EXCLUDE (Expires: never)
        Host mode:      EXCLUDE
        Last reporter:  fe80::5054:ff:fefa:9ad7
        Source list is empty
        Interface:      GigabitEthernet0/0/0/0
        Group:          ff35:1::1
        Uptime:         00:33:28
        Router mode:    INCLUDE
        Host mode:      INCLUDE
        Last reporter:  fe80::5054:ff:fefa:9ad7
        Group source list:
          Source Address                          Uptime    Expires   Fwd  Flags
          2001:db8:3:3::3                       00:33:28  01:00:00  Yes  Remote Local e
        Interface:      GigabitEthernet0/0/0/0
        Group:          ff45:1::1
        Uptime:         00:33:28
        Router mode:    EXCLUDE (Expires: never)
        Host mode:      EXCLUDE
        Last reporter:  fe80::5054:ff:fefa:9ad7
        Source list is empty
        Interface:      GigabitEthernet0/0/0/0
        Group:          fffe::1
        Uptime:         07:59:31
        Router mode:    EXCLUDE (Expires: 00:59:49)
        Host mode:      INCLUDE
        Last reporter:  fe80::5054:ff:fed7:c01f
        Source list is empty
        '''
    }

    # show mld vrf {vrf} groups detail
    golden_parsed_output2 = {
        'vrf': {
            'VRF1': {
                'interface': {
                    'GigabitEthernet0/0/0/1': {
                        'group': {
                            'ff02::16': {
                                'expire': 'never',
                                'router_mode': 'exclude',
                                'host_mode': 'exclude',
                                'last_reporter': 'fe80::5054:ff:fe35:f846',
                                'up_time': '1d06h'
                            },
                            'ff02::1:ff00:1': {
                                'expire': '00:58:14',
                                'router_mode': 'exclude',
                                'host_mode': 'include',
                                'last_reporter': 'fe80::5054:ff:fe7c:dc70',
                                'up_time': '09:00:17'
                            },
                            'ff02::1:ff24:c88d': {
                                'expire': '00:58:30',
                                'router_mode': 'exclude',
                                'host_mode': 'include',
                                'last_reporter': 'fe80::7c2f:c2ff:fe24:c88d',
                                'up_time': '1d06h'
                            },
                            'ff02::1:ff7c:dc70': {
                                'expire': '00:58:14',
                                'router_mode': 'exclude',
                                'host_mode': 'include',
                                'last_reporter': 'fe80::5054:ff:fe7c:dc70',
                                'up_time': '09:00:17'
                            },
                            'ff02::2': {
                                'expire': 'never',
                                'router_mode': 'exclude',
                                'host_mode': 'exclude',
                                'last_reporter': 'fe80::5054:ff:fe35:f846',
                                'up_time': '1d06h'
                            },
                            'ff02::d': {
                                'expire': 'never',
                                'router_mode': 'exclude',
                                'host_mode': 'exclude',
                                'last_reporter': 'fe80::5054:ff:fe35:f846',
                                'up_time': '1d06h'
                            },
                            'ff15:1::1': {
                                'router_mode': 'include',
                                'host_mode': 'include',
                                'last_reporter': 'fe80::5054:ff:fe35:f846',
                                'source': {
                                    '2001:db8:2:2::2': {
                                        'expire': '00:58:30',
                                        'flags': 'Remote Local 2d',
                                        'forward': True,
                                        'up_time': '08:10:33'
                                    }
                                },
                                'up_time': '08:11:27'
                            },
                            'ff25:2::1': {
                                'expire': 'never',
                                'router_mode': 'exclude',
                                'host_mode': 'exclude',
                                'last_reporter': 'fe80::5054:ff:fe35:f846',
                                'up_time': '08:11:12'
                            },
                            'ff35:1::1': {
                                'router_mode': 'include',
                                'host_mode': 'include',
                                'last_reporter': 'fe80::5054:ff:fe35:f846',
                                'source': {
                                    '2001:db8:3:3::3': {
                                        'expire': '00:58:30',
                                        'flags': 'Remote Local e',
                                        'forward': True,
                                        'up_time': '00:39:52'
                                    }
                                },
                                'up_time': '00:39:52'
                            },
                            'ff45:1::1': {
                                'expire': 'never',
                                'router_mode': 'exclude',
                                'host_mode': 'exclude',
                                'last_reporter': 'fe80::5054:ff:fe35:f846',
                                'up_time': '00:39:44'
                            }
                        },
                        'join_group': {
                            'ff15:1::1 2001:db8:2:2::2': {
                                'group': 'ff15:1::1',
                                'source': '2001:db8:2:2::2'
                            }
                        },
                        'static_group': {
                            'ff35:1::1 2001:db8:3:3::3': {
                                'group': 'ff35:1::1',
                                'source': '2001:db8:3:3::3'
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output2 = { 'execute.return_value': 
        '''
        RP/0/0/CPU0:ios#show mld vrf VRF1 groups detail

        Interface:      GigabitEthernet0/0/0/1
        Group:          ff02::2
        Uptime:         1d06h
        Router mode:    EXCLUDE (Expires: never)
        Host mode:      EXCLUDE
        Last reporter:  fe80::5054:ff:fe35:f846
        Source list is empty
        Interface:      GigabitEthernet0/0/0/1
        Group:          ff02::d
        Uptime:         1d06h
        Router mode:    EXCLUDE (Expires: never)
        Host mode:      EXCLUDE
        Last reporter:  fe80::5054:ff:fe35:f846
        Source list is empty
        Interface:      GigabitEthernet0/0/0/1
        Group:          ff02::16
        Uptime:         1d06h
        Router mode:    EXCLUDE (Expires: never)
        Host mode:      EXCLUDE
        Last reporter:  fe80::5054:ff:fe35:f846
        Source list is empty
        Interface:      GigabitEthernet0/0/0/1
        Group:          ff02::1:ff00:1
        Uptime:         09:00:17
        Router mode:    EXCLUDE (Expires: 00:58:14)
        Host mode:      INCLUDE
        Last reporter:  fe80::5054:ff:fe7c:dc70
        Source list is empty
        Interface:      GigabitEthernet0/0/0/1
        Group:          ff02::1:ff24:c88d
        Uptime:         1d06h
        Router mode:    EXCLUDE (Expires: 00:58:30)
        Host mode:      INCLUDE
        Last reporter:  fe80::7c2f:c2ff:fe24:c88d
        Source list is empty
        Interface:      GigabitEthernet0/0/0/1
        Group:          ff02::1:ff7c:dc70
        Uptime:         09:00:17
        Router mode:    EXCLUDE (Expires: 00:58:14)
        Host mode:      INCLUDE
        Last reporter:  fe80::5054:ff:fe7c:dc70
        Source list is empty
        Interface:      GigabitEthernet0/0/0/1
        Group:          ff15:1::1
        Uptime:         08:11:27
        Router mode:    INCLUDE
        Host mode:      INCLUDE
        Last reporter:  fe80::5054:ff:fe35:f846
        Group source list:
          Source Address                          Uptime    Expires   Fwd  Flags
          2001:db8:2:2::2                       08:10:33  00:58:30  Yes  Remote Local 2d
        Interface:      GigabitEthernet0/0/0/1
        Group:          ff25:2::1
        Uptime:         08:11:12
        Router mode:    EXCLUDE (Expires: never)
        Host mode:      EXCLUDE
        Last reporter:  fe80::5054:ff:fe35:f846
        Source list is empty
        Interface:      GigabitEthernet0/0/0/1
        Group:          ff35:1::1
        Uptime:         00:39:52
        Router mode:    INCLUDE
        Host mode:      INCLUDE
        Last reporter:  fe80::5054:ff:fe35:f846
        Group source list:
          Source Address                          Uptime    Expires   Fwd  Flags
          2001:db8:3:3::3                       00:39:52  00:58:30  Yes  Remote Local e
        Interface:      GigabitEthernet0/0/0/1
        Group:          ff45:1::1
        Uptime:         00:39:44
        Router mode:    EXCLUDE (Expires: never)
        Host mode:      EXCLUDE
        Last reporter:  fe80::5054:ff:fe35:f846
        Source list is empty
        '''
    }

    # show mld groups {group} detail
    golden_parsed_output3 = {
        'vrf': {
            'default': {
                'interface': {
                    'GigabitEthernet0/0/0/0.115': {
                        'group': {
                            'ff35::232:2:2:2': {
                                'host_mode': 'include',
                                'last_reporter': '::',
                                'router_mode': 'include',
                                'source': {
                                    'fc00::10:255:134:44': {
                                        'expire': 'expired',
                                        'flags': 'Local 29',
                                        'forward': False,
                                        'up_time': '07:17:10'
                                    }
                                },
                                'suppress': 0,
                                'up_time': '07:17:10'
                            }
                        },
                        'join_group': {
                            'ff35::232:2:2:2 fc00::10:255:134:44': {
                                'group': 'ff35::232:2:2:2',
                                'source': 'fc00::10:255:134:44'
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output3 = { 'execute.return_value' : 
        '''
        RP/0/RP0/CPU0:R2_xr#show mld groups ff35::232:2:2:2 detail

        Interface:      GigabitEthernet0/0/0/0.115
        Group:          ff35::232:2:2:2
        Uptime:         07:17:10
        Router mode:    INCLUDE
        Host mode:      INCLUDE
        Last reporter:  ::
        Suppress:       0
        Group source list:
          Source Address                          Uptime    Expires   Fwd  Flags
          fc00::10:255:134:44                   07:17:10  expired   No   Local 29
        '''
    }

    golden_parsed_output4 = {
        'vrf': {
            'default': {
                'interface': {
                    'GigabitEthernet0/0/0/0.115': {
                        'group': {
                            'ff35::232:2:2:22': {
                                'host_mode': 'include',
                                'last_reporter': '::',
                                'router_mode': 'include',
                                'source': {
                                    'fc00::10:255:134:44': {
                                        'expire': 'expired',
                                        'flags': 'Local a',
                                        'forward': False,
                                        'up_time': '00:01:21'
                                    }
                                },
                                'suppress': 0,
                                'up_time': '00:01:21'
                            }
                        },
                        'static_group': {
                            'ff35::232:2:2:22 fc00::10:255:134:44': {
                                'group': 'ff35::232:2:2:22',
                                'source': 'fc00::10:255:134:44'
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output4 = { 'execute.return_value' : 
        '''
        RP/0/RP0/CPU0:R2_xr#show mld groups ff35::232:2:2:22 detail

        Interface:      GigabitEthernet0/0/0/0.115
        Group:          ff35::232:2:2:22
        Uptime:         00:01:21
        Router mode:    INCLUDE
        Host mode:      INCLUDE
        Last reporter:  ::
        Suppress:       0
        Group source list:
          Source Address                          Uptime    Expires   Fwd  Flags
          fc00::10:255:134:44                   00:01:21  expired   No   Local a
        '''
    }

    golden_parsed_output5 = {
        'vrf': {
            'default': {
                'interface': {
                    'GigabitEthernet0/0/0/0.115': {
                        'group': {
                            'ff35::232:2:2:2': {
                                'host_mode': 'include',
                                'last_reporter': '::',
                                'router_mode': 'include',
                                'source': {
                                    'fc00::10:255:134:44': {
                                        'expire': 'expired',
                                        'flags': 'Local 2b',
                                        'forward': False,
                                        'up_time': '1w1d'
                                    }
                                },
                                'suppress': 0,
                                'up_time': '1w1d'
                            }
                        },
                        'join_group': {
                            'ff35::232:2:2:2 fc00::10:255:134:44': {
                                'group': 'ff35::232:2:2:2',
                                'source': 'fc00::10:255:134:44'
                            }
                        },
                        'static_group': {
                            'ff35::232:2:2:2 fc00::10:255:134:44': {
                                'group': 'ff35::232:2:2:2',
                                'source': 'fc00::10:255:134:44'
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output5 = { 'execute.return_value' : 
        '''
        RP/0/RP0/CPU0:R2_xr#show mld groups ff35::232:2:2:2 detail

        Interface:      GigabitEthernet0/0/0/0.115
        Group:          ff35::232:2:2:2
        Uptime:         1w1d
        Router mode:    INCLUDE
        Host mode:      INCLUDE
        Last reporter:  ::
        Suppress:       0
        Group source list:
          Source Address                          Uptime    Expires   Fwd  Flags
          fc00::10:255:134:44                   1w1d      expired   No   Local 2b
        '''
    }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowMldGroupsDetail(device = self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    # show mld groups detail
    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowMldGroupsDetail(device = self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)
    
    # show mld vrf {vrf} groups detail
    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowMldGroupsDetail(device = self.device)
        parsed_output = obj.parse(vrf = 'VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    # show mld groups {group} detail
    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowMldGroupsGroupDetail(device = self.device)
        parsed_output = obj.parse(group = 'ff35::232:2:2:2')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_golden4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowMldGroupsGroupDetail(device = self.device)
        parsed_output = obj.parse(group = 'ff35::232:2:2:22')
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_golden5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        obj = ShowMldGroupsGroupDetail(device = self.device)
        parsed_output = obj.parse(group = 'ff35::232:2:2:2')
        self.assertEqual(parsed_output, self.golden_parsed_output5)

if __name__ == '__main__':
    unittest.main()
