# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_mld import ShowIpv6MldInterface, \
                                   ShowIpv6MldGroupsDetail, \
                                   ShowIpv6MldSsmMap


# ==================================================
# Unit test for 'show ipv6 mld interface'
# Unit test for 'show ipv6 mld vrf <WORD> interface'
# ==================================================
class test_show_ipv6_mld_interface(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrf": {
            "default": {
                 "interface": {
                      "Tunnel0": {
                           "oper_status": "up",
                           "interface_adress": "FE80::21E:BDFF:FEBA:D000/10",
                           "enable": False,
                           "interface_status": "up"
                      },
                      "VoIP-Null0": {
                           "oper_status": "up",
                           "interface_adress": "::/0",
                           "enable": False,
                           "interface_status": "up"
                      },
                      "LIIN0": {
                           "oper_status": "up",
                           "interface_adress": "::/0",
                           "enable": False,
                           "interface_status": "up"
                      },
                      "GigabitEthernet1": {
                           "oper_status": "up",
                           "querier_timeout": 740,
                           "active_groups": 0,
                           "group_policy": "test",
                           "query_interval": 366,
                           "version": 2,
                           "query_this_system": True,
                           "querier": "FE80::5054:FF:FE7C:DC70",
                           "interface_status": "up",
                           "last_member_query_interval": 1,
                           "counters": {
                                "leaves": 2,
                                "joins": 11
                           },
                           "max_groups": 6400,
                           "query_max_response_time": 16,
                           "enable": True,
                           "interface_adress": "FE80::5054:FF:FE7C:DC70/10"
                      },
                      "GigabitEthernet3": {
                           "oper_status": "down",
                           "interface_adress": "::/0",
                           "enable": False,
                           "interface_status": "administratively down"
                      },
                      "Null0": {
                           "oper_status": "up",
                           "interface_adress": "FE80::1/10",
                           "enable": False,
                           "interface_status": "up"
                      }
                 },
                 "max_groups": 64000,
                 "active_groups": 0
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Global State Limit : 0 active out of 64000 max
        GigabitEthernet1 is up, line protocol is up
          Internet address is FE80::5054:FF:FE7C:DC70/10
          MLD is enabled on interface
          Current MLD version is 2
          MLD query interval is 366 seconds
          MLD querier timeout is 740 seconds
          MLD max query response time is 16 seconds
          Last member query response interval is 1 seconds
          Inbound MLD access group is: test
          Interface State Limit : 0 active out of 6400 max
          MLD activity: 11 joins, 2 leaves
          MLD querying router is FE80::5054:FF:FE7C:DC70 (this system)
        GigabitEthernet3 is administratively down, line protocol is down
          Internet address is ::/0
          MLD is disabled on interface
        Null0 is up, line protocol is up
          Internet address is FE80::1/10
          MLD is disabled on interface
        VoIP-Null0 is up, line protocol is up
          Internet address is ::/0
          MLD is disabled on interface
        LIIN0 is up, line protocol is up
          Internet address is ::/0
          MLD is disabled on interface
        Tunnel0 is up, line protocol is up
          Internet address is FE80::21E:BDFF:FEBA:D000/10
          MLD is disabled on interface
    '''}
    
    golden_parsed_output_1 = {
        "vrf": {
            "VRF1": {
                 "interface": {
                      "GigabitEthernet2": {
                           "query_max_response_time": 16,
                           "enable": True,
                           "query_interval": 366,
                           "querier": "FE80::5054:FF:FEDD:BB49",
                           "interface_status": "up",
                           "query_this_system": True,
                           "version": 2,
                           "interface_adress": "FE80::5054:FF:FEDD:BB49/10",
                           "active_groups": 0,
                           "querier_timeout": 740,
                           "last_member_query_interval": 1,
                           "counters": {
                                "joins": 9,
                                "leaves": 0
                           },
                           "oper_status": "up",
                           "max_groups": 6400
                      },
                      "Tunnel1": {
                           "interface_status": "up",
                           "interface_adress": "FE80::21E:BDFF:FEBA:D000/10",
                           "oper_status": "up",
                           "enable": False
                      }
                 },
                 "max_groups": 64000,
                 "active_groups": 0
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        Global State Limit : 0 active out of 64000 max
        GigabitEthernet2 is up, line protocol is up
          Internet address is FE80::5054:FF:FEDD:BB49/10
          MLD is enabled on interface
          Current MLD version is 2
          MLD query interval is 366 seconds
          MLD querier timeout is 740 seconds
          MLD max query response time is 16 seconds
          Last member query response interval is 1 seconds
          Interface State Limit : 0 active out of 6400 max
          MLD activity: 9 joins, 0 leaves
          MLD querying router is FE80::5054:FF:FEDD:BB49 (this system)
        Tunnel1 is up, line protocol is up
          Internet address is FE80::21E:BDFF:FEBA:D000/10
          MLD is disabled on interface
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6MldInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_default_vrf(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6MldInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_non_default_vrf(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6MldInterface(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


# =====================================================
# Unit test for 'show ipv6 mld groups detail'
# Unit test for 'show ipv6 mld vrf <WORD> groups detail'
# =====================================================
class test_show_ipv6_mld_groups_detail(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrf": {
            "default": {
                 "interface": {
                      "GigabitEthernet1": {
                           "group": {
                                "FF15:1::1": {
                                     "up_time": "08:14:15",
                                     "source": {
                                          "2001:DB8:2:2::2": {
                                               "forward": True,
                                               "up_time": "08:13:22",
                                               "flags": "Remote Local 2D",
                                               "expire": "00:06:42"
                                          }
                                     },
                                     "filter_mode": "include",
                                     "host_mode": "include",
                                     "last_reporter": "FE80::5054:FF:FE7C:DC70"
                                },
                                "FF25:2::1": {
                                     "up_time": "08:14:01",
                                     "filter_mode": "exclude",
                                     "last_reporter": "FE80::5054:FF:FE7C:DC70",
                                     "host_mode": "exclude",
                                     "expire": "never"
                                },
                                "FF35:1::1": {
                                     "up_time": "00:42:41",
                                     "source": {
                                          "2001:DB8:3:3::3": {
                                               "forward": True,
                                               "up_time": "00:42:41",
                                               "flags": "Remote Local E",
                                               "expire": "00:06:42"
                                          }
                                     },
                                     "filter_mode": "include",
                                     "host_mode": "include",
                                     "last_reporter": "FE80::5054:FF:FE7C:DC70"
                                },
                                "FF45:1::1": {
                                     "up_time": "00:42:32",
                                     "filter_mode": "exclude",
                                     "last_reporter": "FE80::5054:FF:FE7C:DC70",
                                     "host_mode": "exclude",
                                     "expire": "never"
                                }
                           },
                           "join_group": {
                                "FF15:1::1 2001:DB8:2:2::2": {
                                     "group": "FF15:1::1",
                                     "source": "2001:DB8:2:2::2"
                                },
                           },
                           "static_group": {
                                "FF35:1::1 2001:DB8:3:3::3": {
                                     "group": "FF35:1::1",
                                     "source": "2001:DB8:3:3::3"
                                }
                           }
                      }
                 }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Interface:        GigabitEthernet1
        Group:                FF15:1::1
        Uptime:                08:14:15
        Router mode:        INCLUDE
        Host mode:        INCLUDE
        Last reporter:        FE80::5054:FF:FE7C:DC70
        Group source list:
        Source Address                          Uptime    Expires   Fwd  Flags
        2001:DB8:2:2::2                         08:13:22  00:06:42  Yes  Remote Local 2D
        Interface:        GigabitEthernet1
        Group:                FF25:2::1
        Uptime:                08:14:01
        Router mode:        EXCLUDE (Expires: never)
        Host mode:        EXCLUDE
        Last reporter:        FE80::5054:FF:FE7C:DC70
        Source list is empty
        Interface:        GigabitEthernet1
        Group:                FF35:1::1
        Uptime:                00:42:41
        Router mode:        INCLUDE
        Host mode:        INCLUDE
        Last reporter:        FE80::5054:FF:FE7C:DC70
        Group source list:
        Source Address                          Uptime    Expires   Fwd  Flags
        2001:DB8:3:3::3                         00:42:41  00:06:42  Yes  Remote Local E
        Interface:        GigabitEthernet1
        Group:                FF45:1::1
        Uptime:                00:42:32
        Router mode:        EXCLUDE (Expires: never)
        Host mode:        EXCLUDE
        Last reporter:        FE80::5054:FF:FE7C:DC70
        Source list is empty
    '''}
    
    golden_parsed_output_1 = {
        "vrf": {
            "VRF1": {
                 "interface": {
                      "GigabitEthernet2": {
                           "group": {
                                "FF15:1::1": {
                                     "up_time": "08:14:20",
                                     "source": {
                                          "2001:DB8:2:2::2": {
                                               "forward": True,
                                               "up_time": "08:13:56",
                                               "flags": "Remote Local 2D",
                                               "expire": "00:12:23"
                                          }
                                     },
                                     "filter_mode": "include",
                                     "host_mode": "include",
                                     "last_reporter": "FE80::5054:FF:FEDD:BB49"
                                },
                                "FF25:2::1": {
                                     "up_time": "08:14:18",
                                     "filter_mode": "exclude",
                                     "last_reporter": "FE80::5054:FF:FEDD:BB49",
                                     "host_mode": "exclude",
                                     "expire": "never"
                                },
                                "FF35:1::1": {
                                     "up_time": "00:42:30",
                                     "source": {
                                          "2001:DB8:3:3::3": {
                                               "forward": True,
                                               "up_time": "00:42:30",
                                               "flags": "Remote Local E",
                                               "expire": "00:12:23"
                                          }
                                     },
                                     "filter_mode": "include",
                                     "host_mode": "include",
                                     "last_reporter": "FE80::5054:FF:FEDD:BB49"
                                },
                                "FF45:1::1": {
                                     "up_time": "00:42:30",
                                     "filter_mode": "exclude",
                                     "last_reporter": "FE80::5054:FF:FEDD:BB49",
                                     "host_mode": "exclude",
                                     "expire": "never"
                                }
                           },
                           "join_group": {
                                "FF15:1::1 2001:DB8:2:2::2": {
                                     "group": "FF15:1::1",
                                     "source": "2001:DB8:2:2::2"
                                }
                           },
                           "static_group": {
                                "FF35:1::1 2001:DB8:3:3::3": {
                                     "group": "FF35:1::1",
                                     "source": "2001:DB8:3:3::3"
                                }
                           }
                      }
                 }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        Interface:        GigabitEthernet2
        Group:                FF15:1::1
        Uptime:                08:14:20
        Router mode:        INCLUDE
        Host mode:        INCLUDE
        Last reporter:        FE80::5054:FF:FEDD:BB49
        Group source list:
        Source Address                          Uptime    Expires   Fwd  Flags
        2001:DB8:2:2::2                         08:13:56  00:12:23  Yes  Remote Local 2D
        Interface:        GigabitEthernet2
        Group:                FF25:2::1
        Uptime:                08:14:18
        Router mode:        EXCLUDE (Expires: never)
        Host mode:        EXCLUDE
        Last reporter:        FE80::5054:FF:FEDD:BB49
        Source list is empty
        Interface:        GigabitEthernet2
        Group:                FF35:1::1
        Uptime:                00:42:30
        Router mode:        INCLUDE
        Host mode:        INCLUDE
        Last reporter:        FE80::5054:FF:FEDD:BB49
        Group source list:
        Source Address                          Uptime    Expires   Fwd  Flags
        2001:DB8:3:3::3                         00:42:30  00:12:23  Yes  Remote Local E
        Interface:        GigabitEthernet2
        Group:                FF45:1::1
        Uptime:                00:42:30
        Router mode:        EXCLUDE (Expires: never)
        Host mode:        EXCLUDE
        Last reporter:        FE80::5054:FF:FEDD:BB49
        Source list is empty
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6MldGroupsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_default_vrf(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6MldGroupsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_non_default_vrf(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6MldGroupsDetail(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


# ===========================================================
# Unit test for 'show ipv6 mld ssm-mapping <WROD>'
# Unit test for 'show ipv6 mld vrf <WORD> ssm-mapping <WORD>'
# ============================================================
class test_show_ipv6_mld_ssm_mapping(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrf": {
            "default": {
                 "ssm_map": {
                      "2001:DB8:1:1::1 FF35:1::1": {
                           "source_addr": "2001:DB8:1:1::1",
                           "group_address": "FF35:1::1",
                           "database": "static",
                           "group_mode_ssm": False
                      }
                 }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Group address  : FF35:1::1
        Group mode ssm : FALSE
        Database       : STATIC
        Source list    : 2001:DB8:1:1::1
    '''}
    
    golden_parsed_output_1 = {
        "vrf": {
            "VRF1": {
                 "ssm_map": {
                      "2001:DB8:1:1::1 FF35:1::1": {
                           "source_addr": "2001:DB8:1:1::1",
                           "group_address": "FF35:1::1",
                           "database": "static",
                           "group_mode_ssm": False
                      },
                      "2001:DB8::3 FF35:1::1": {
                           "source_addr": "2001:DB8::3",
                           "group_address": "FF35:1::1",
                           "database": "static",
                           "group_mode_ssm": False
                      }
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        Group address  : FF35:1::1
        Group mode ssm : FALSE
        Database       : STATIC
        Source list    : 2001:DB8:1:1::1
                         2001:DB8::3
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6MldSsmMap(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(group='ff35:1::1')

    def test_golden_default_vrf(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6MldSsmMap(device=self.device)
        parsed_output = obj.parse(group='ff35:1::1')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_non_default_vrf(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6MldSsmMap(device=self.device)
        parsed_output = obj.parse(vrf='VRF1', group='ff35:1::1')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()