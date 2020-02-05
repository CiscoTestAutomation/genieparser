# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.nxos.show_igmp import ShowIpIgmpInterface, \
                                  ShowIpIgmpGroups, \
                                  ShowIpIgmpLocalGroups, \
                                  ShowIpIgmpSnooping


#=========================================================
# Unit test for show ip igmp snooping
#
#=========================================================
class test_show_ip_igmp_snooping(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_snooping_1 = \
        {
        'global_configuration': {
            'enabled': 'enabled',
            'v1v2_report_suppression': 'enabled',
            'v3_report_suppression': 'disabled',
            'link_local_groups_suppression': 'enabled',
            'vpc_multicast_optimization': 'disabled',
        },
        'vlans': {
            '1': {  # configuration_vlan_id
                'ip_igmp_snooping': 'enabled',
                'v1v2_report_suppression': 'enabled',
                'v3_report_suppression': 'disabled',
                'link_local_groups_suppression': 'enabled',
                'lookup_mode': 'ip',
                'switch_querier': 'disabled',
                'igmp_explicit_tracking': 'enabled',
                'v2_fast_leave': 'disabled',
                'router_ports_count': 1,
                'groups_count': 0,
                'vlan_vpc_function': 'enabled',
                'active_ports': ['Po20','Po30'],
                'report_flooding': 'disabled',
                'report_flooding_interfaces': 'n/a',
                'group_address_for_proxy_leaves': 'no',
                },
            '100': {  # configuration_vlan_id
                'ip_igmp_snooping': 'enabled',
                'v1v2_report_suppression': 'enabled',
                'v3_report_suppression': 'disabled',
                'link_local_groups_suppression': 'enabled',
                'lookup_mode': 'ip',
                'igmp_querier': {
                    'address': '10.51.1.1',
                    'version': 2,
                    'interval': 125,
                    'last_member_query_interval': 1,
                    'robustness': 2,
                },
                'switch_querier': 'disabled',
                'igmp_explicit_tracking': 'enabled',
                'v2_fast_leave': 'disabled',
                'router_ports_count': 2,
                'groups_count': 0,
                'vlan_vpc_function': 'enabled',
                'active_ports': ['Po20', 'Po30'],
                'report_flooding': 'disabled',
                'report_flooding_interfaces': 'n/a',
                'group_address_for_proxy_leaves': 'no',
                },
            '101': {  # configuration_vlan_id
                'ip_igmp_snooping': 'enabled',
                'v1v2_report_suppression': 'enabled',
                'v3_report_suppression': 'disabled',
                'link_local_groups_suppression': 'enabled',
                'lookup_mode': 'ip',
                'switch_querier': 'disabled',
                'igmp_explicit_tracking': 'enabled',
                'v2_fast_leave': 'disabled',
                'router_ports_count': 1,
                'groups_count': 0,
                'vlan_vpc_function': 'enabled',
                'active_ports': ['Po20', 'Po30'],
                'report_flooding': 'disabled',
                'report_flooding_interfaces': 'n/a',
                'group_address_for_proxy_leaves': 'no',
            },
        },
    }

    golden_output_snooping_1 = {'execute.return_value': '''
N95_1# show ip igmp snooping
Global IGMP Snooping Information:
  IGMP Snooping enabled
  IGMPv1/v2 Report Suppression enabled
  IGMPv3 Report Suppression disabled
  Link Local Groups Suppression enabled
  VPC Multicast optimization disabled

IGMP Snooping information for vlan 1
  IGMP snooping enabled
  Lookup mode: IP
  IGMP querier none
  Switch-querier disabled
  IGMP Explicit tracking enabled
  IGMPv2 Fast leave disabled
  IGMPv1/v2 Report suppression enabled
  IGMPv3 Report suppression disabled
  Link Local Groups suppression enabled
  Router port detection using PIM Hellos, IGMP Queries
  Number of router-ports: 1
  Number of groups: 0
  VLAN vPC function enabled
  Active ports:
    Po20        Po30
  Report Flooding: Disabled
  Interfaces for Report Flooding: n/a
  Use Group Address for Proxy Leaves: no

IGMP Snooping information for vlan 100
  IGMP snooping enabled
  Lookup mode: IP
  IGMP querier present, address: 10.51.1.1, version: 2, i/f Vlan100
  Querier interval: 125 secs
  Querier last member query interval: 1 secs
  Querier robustness: 2
  Switch-querier disabled
  IGMP Explicit tracking enabled
  IGMPv2 Fast leave disabled
  IGMPv1/v2 Report suppression enabled
  IGMPv3 Report suppression disabled
  Link Local Groups suppression enabled
  Router port detection using PIM Hellos, IGMP Queries
  Number of router-ports: 2
  Number of groups: 0
  VLAN vPC function enabled
  Active ports:
    Po20        Po30
  Report Flooding: Disabled
  Interfaces for Report Flooding: n/a
  Use Group Address for Proxy Leaves: no

IGMP Snooping information for vlan 101
  IGMP snooping enabled
  Lookup mode: IP
  IGMP querier none
  Switch-querier disabled
  IGMP Explicit tracking enabled
  IGMPv2 Fast leave disabled
  IGMPv1/v2 Report suppression enabled
  IGMPv3 Report suppression disabled
  Link Local Groups suppression enabled
  Router port detection using PIM Hellos, IGMP Queries
  Number of router-ports: 1
  Number of groups: 0
  VLAN vPC function enabled
  Active ports:
    Po20        Po30
  Report Flooding: Disabled
  Interfaces for Report Flooding: n/a
  Use Group Address for Proxy Leaves: no


    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpIgmpSnooping(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_snooping_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_snooping_1)
        obj = ShowIpIgmpSnooping(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_snooping_1)


# ==============================================
# Unit test for 'show ip igmp interface vrf all'
# Unit test for 'show ip igmp interface'
# Unit test for 'show ip igmp interface vrf <WORD>'
# ==============================================
class test_show_ip_igmp_interface(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrfs": {
            "default": {
                 "groups_count": 2,
                 "interface": {
                      "Ethernet2/2": {
                           "query_max_response_time": 10,
                           "vrf_name": "default",
                           "statistics": {
                                "general": {
                                     "sent": {
                                          "v2_reports": 0,
                                          "v2_queries": 16,
                                          "v2_leaves": 0
                                     },
                                     "received": {
                                          "v2_reports": 0,
                                          "v2_queries": 16,
                                          "v2_leaves": 0
                                     }
                                }
                           },
                           "configured_query_max_response_time": 10,
                           "pim_dr": True,
                           "vrf_id": 1,
                           "querier": "10.1.3.1",
                           "membership_count": 0,
                           "last_member": {
                               "query_count": 2,
                               "mrt": 1,
                           },
                           "startup_query": {
                               "interval": 31,
                               "configured_interval": 31,
                               "count": 2,
                           },
                           "link_status": "up",
                           "subnet": "10.1.3.0/24",
                           "address": "10.1.3.1",
                           "link_local_groups_reporting": False,
                           "unsolicited_report_interval": 10,
                           "enable_refcount": 1,
                           "enable": True,
                           "next_query_sent_in": "00:00:55",
                           "configured_query_interval": 125,
                           "old_membership_count": 0,
                           "group_timeout": 260,
                           "configured_robustness_variable": 2,
                           "vpc_svi": False,
                           "querier_version": 2,
                           "version": 2,
                           "query_interval": 125,
                           "querier_timeout": 255,
                           "immediate_leave": False,
                           "configured_group_timeout": 260,
                           "host_version": 2,
                           "configured_querier_timeout": 255,
                           "robustness_variable": 2,
                           "oper_status": "up"
                      },
                      "Ethernet2/1": {
                           "query_max_response_time": 15,
                           "vrf_name": "default",
                           "statistics": {
                                "errors": {
                                     "router_alert_check": 19,
                                },
                                "general": {
                                     "sent": {
                                          "v2_reports": 0,
                                          "v3_queries": 11,
                                          "v2_leaves": 0,
                                          "v3_reports": 56,
                                          "v2_queries": 5
                                     },
                                     "received": {
                                          "v2_reports": 0,
                                          "v3_queries": 11,
                                          "v2_leaves": 0,
                                          "v3_reports": 56,
                                          "v2_queries": 5
                                     }
                                }
                           },
                           "configured_query_max_response_time": 15,
                           "max_groups": 10,
                           "vrf_id": 1,
                           "querier": "10.1.2.1",
                           "membership_count": 4,
                           "last_member": {
                               "query_count": 5,
                               "mrt": 1,
                           },
                           "startup_query": {
                               "interval": 33,
                               "configured_interval": 31,
                               "count": 5,
                           },
                           "pim_dr": True,
                           "link_status": "up",
                           "subnet": "10.1.2.0/24",
                           "address": "10.1.2.1",
                           "link_local_groups_reporting": False,
                           "unsolicited_report_interval": 10,
                           "enable_refcount": 9,
                           "enable": True,
                           "group_policy": "access-group-filter",
                           "next_query_sent_in": "00:00:47",
                           "configured_query_interval": 133,
                           "old_membership_count": 0,
                           "group_timeout": 680,
                           "configured_robustness_variable": 5,
                           "vpc_svi": False,
                           "querier_version": 3,
                           "available_groups": 10,
                           "version": 3,
                           "query_interval": 133,
                           "querier_timeout": 672,
                           "immediate_leave": True,
                           "configured_group_timeout": 260,
                           "host_version": 3,
                           "configured_querier_timeout": 255,
                           "robustness_variable": 5,
                           "oper_status": "up"
                      }
                 }
            },
            "VRF1": {
                 "groups_count": 2,
                 "interface": {
                      "Ethernet2/4": {
                           "query_max_response_time": 15,
                           "vrf_name": "VRF1",
                           "statistics": {
                                "general": {
                                     "sent": {
                                          "v2_reports": 0,
                                          "v3_queries": 8,
                                          "v2_leaves": 0,
                                          "v3_reports": 44,
                                          "v2_queries": 8
                                     },
                                     "received": {
                                          "v2_reports": 0,
                                          "v3_queries": 8,
                                          "v2_leaves": 0,
                                          "v3_reports": 44,
                                          "v2_queries": 8
                                     }
                                }
                           },
                           "configured_query_max_response_time": 15,
                           "max_groups": 10,
                           "vrf_id": 3,
                           "querier": "10.186.2.1",
                           "membership_count": 4,
                           "last_member": {
                               "query_count": 5,
                               "mrt": 1,
                           },
                           "startup_query": {
                               "interval": 33,
                               "configured_interval": 31,
                               "count": 5,
                           },
                           "pim_dr": True,
                           "link_status": "up",
                           "subnet": "10.186.2.0/24",
                           "address": "10.186.2.1",
                           "link_local_groups_reporting": False,
                           "unsolicited_report_interval": 10,
                           "enable_refcount": 9,
                           "enable": True,
                           "group_policy": "access-group-filter",
                           "next_query_sent_in": "00:00:06",
                           "configured_query_interval": 133,
                           "old_membership_count": 0,
                           "group_timeout": 680,
                           "configured_robustness_variable": 5,
                           "vpc_svi": False,
                           "querier_version": 3,
                           "available_groups": 10,
                           "version": 3,
                           "query_interval": 133,
                           "querier_timeout": 672,
                           "immediate_leave": True,
                           "configured_group_timeout": 260,
                           "host_version": 3,
                           "configured_querier_timeout": 255,
                           "robustness_variable": 5,
                           "oper_status": "up"
                      },
                      "Ethernet2/3": {
                           "query_max_response_time": 10,
                           "vrf_name": "VRF1",
                           "statistics": {
                                "general": {
                                     "sent": {
                                          "v2_reports": 0,
                                          "v2_queries": 16,
                                          "v2_leaves": 0
                                     },
                                     "received": {
                                          "v2_reports": 0,
                                          "v2_queries": 16,
                                          "v2_leaves": 0
                                     }
                                }
                           },
                           "configured_query_max_response_time": 10,
                           "pim_dr": True,
                           "vrf_id": 3,
                           "querier": "10.186.3.1",
                           "membership_count": 0,
                           "last_member": {
                               "query_count": 2,
                               "mrt": 1,
                           },
                           "startup_query": {
                               "interval": 31,
                               "configured_interval": 31,
                               "count": 2,
                           },
                           "link_status": "up",
                           "subnet": "10.186.3.0/24",
                           "address": "10.186.3.1",
                           "link_local_groups_reporting": False,
                           "unsolicited_report_interval": 10,
                           "enable_refcount": 1,
                           "enable": True,
                           "next_query_sent_in": "00:00:47",
                           "configured_query_interval": 125,
                           "old_membership_count": 0,
                           "group_timeout": 260,
                           "configured_robustness_variable": 2,
                           "vpc_svi": False,
                           "querier_version": 2,
                           "version": 2,
                           "query_interval": 125,
                           "querier_timeout": 255,
                           "immediate_leave": False,
                           "configured_group_timeout": 260,
                           "host_version": 2,
                           "configured_querier_timeout": 255,
                           "robustness_variable": 2,
                           "oper_status": "up"
                      }
                 }
            },
            "tenant1": {
                 "groups_count": 0,
            },
            "manegement": {
                 "groups_count": 0,
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        IGMP Interfaces for VRF "default", count: 2
        Ethernet2/1, Interface status: protocol-up/link-up/admin-up
          IP address: 10.1.2.1, IP subnet: 10.1.2.0/24
          Active querier: 10.1.2.1, version: 3, next query sent in: 00:00:47
          Membership count: 4
          Old Membership count 0
          IGMP version: 3, host version: 3
          IGMP query interval: 133 secs, configured value: 133 secs
          IGMP max response time: 15 secs, configured value: 15 secs
          IGMP startup query interval: 33 secs, configured value: 31 secs
          IGMP startup query count: 5
          IGMP last member mrt: 1 secs
          IGMP last member query count: 5
          IGMP group timeout: 680 secs, configured value: 260 secs
          IGMP querier timeout: 672 secs, configured value: 255 secs
          IGMP unsolicited report interval: 10 secs
          IGMP robustness variable: 5, configured value: 5
          IGMP reporting for link-local groups: disabled
          IGMP interface enable refcount: 9
          IGMP interface immediate leave: enabled
          IGMP VRF name default (id 1)
          IGMP Report Policy: access-group-filter
          IGMP State Limit: 10,  Available States: 10
          IGMP interface statistics: (only non-zero values displayed)
            General (sent/received):
              v2-queries: 5/5, v2-reports: 0/0, v2-leaves: 0/0
              v3-queries: 11/11, v3-reports: 56/56
            Errors:
              Packets dropped due to router-alert check: 19
          Interface PIM DR: Yes
          Interface vPC SVI: No
          Interface vPC CFS statistics:
        Ethernet2/2, Interface status: protocol-up/link-up/admin-up
          IP address: 10.1.3.1, IP subnet: 10.1.3.0/24
          Active querier: 10.1.3.1, version: 2, next query sent in: 00:00:55
          Membership count: 0
          Old Membership count 0
          IGMP version: 2, host version: 2
          IGMP query interval: 125 secs, configured value: 125 secs
          IGMP max response time: 10 secs, configured value: 10 secs
          IGMP startup query interval: 31 secs, configured value: 31 secs
          IGMP startup query count: 2
          IGMP last member mrt: 1 secs
          IGMP last member query count: 2
          IGMP group timeout: 260 secs, configured value: 260 secs
          IGMP querier timeout: 255 secs, configured value: 255 secs
          IGMP unsolicited report interval: 10 secs
          IGMP robustness variable: 2, configured value: 2
          IGMP reporting for link-local groups: disabled
          IGMP interface enable refcount: 1
          IGMP interface immediate leave: disabled
          IGMP VRF name default (id 1)
          IGMP Report Policy: None
          IGMP State Limit: None
          IGMP interface statistics: (only non-zero values displayed)
            General (sent/received):
              v2-queries: 16/16, v2-reports: 0/0, v2-leaves: 0/0
            Errors:
          Interface PIM DR: Yes
          Interface vPC SVI: No
          Interface vPC CFS statistics:

        IGMP Interfaces for VRF "VRF1", count: 2
        Ethernet2/3, Interface status: protocol-up/link-up/admin-up
          IP address: 10.186.3.1, IP subnet: 10.186.3.0/24
          Active querier: 10.186.3.1, version: 2, next query sent in: 00:00:47
          Membership count: 0
          Old Membership count 0
          IGMP version: 2, host version: 2
          IGMP query interval: 125 secs, configured value: 125 secs
          IGMP max response time: 10 secs, configured value: 10 secs
          IGMP startup query interval: 31 secs, configured value: 31 secs
          IGMP startup query count: 2
          IGMP last member mrt: 1 secs
          IGMP last member query count: 2
          IGMP group timeout: 260 secs, configured value: 260 secs
          IGMP querier timeout: 255 secs, configured value: 255 secs
          IGMP unsolicited report interval: 10 secs
          IGMP robustness variable: 2, configured value: 2
          IGMP reporting for link-local groups: disabled
          IGMP interface enable refcount: 1
          IGMP interface immediate leave: disabled
          IGMP VRF name VRF1 (id 3)
          IGMP Report Policy: None
          IGMP State Limit: None
          IGMP interface statistics: (only non-zero values displayed)
            General (sent/received):
              v2-queries: 16/16, v2-reports: 0/0, v2-leaves: 0/0
            Errors:
          Interface PIM DR: Yes
          Interface vPC SVI: No
          Interface vPC CFS statistics:
        Ethernet2/4, Interface status: protocol-up/link-up/admin-up
          IP address: 10.186.2.1, IP subnet: 10.186.2.0/24
          Active querier: 10.186.2.1, version: 3, next query sent in: 00:00:06
          Membership count: 4
          Old Membership count 0
          IGMP version: 3, host version: 3
          IGMP query interval: 133 secs, configured value: 133 secs
          IGMP max response time: 15 secs, configured value: 15 secs
          IGMP startup query interval: 33 secs, configured value: 31 secs
          IGMP startup query count: 5
          IGMP last member mrt: 1 secs
          IGMP last member query count: 5
          IGMP group timeout: 680 secs, configured value: 260 secs
          IGMP querier timeout: 672 secs, configured value: 255 secs
          IGMP unsolicited report interval: 10 secs
          IGMP robustness variable: 5, configured value: 5
          IGMP reporting for link-local groups: disabled
          IGMP interface enable refcount: 9
          IGMP interface immediate leave: enabled
          IGMP VRF name VRF1 (id 3)
          IGMP Report Policy: access-group-filter
          IGMP State Limit: 10,  Available States: 10
          IGMP interface statistics: (only non-zero values displayed)
            General (sent/received):
              v2-queries: 8/8, v2-reports: 0/0, v2-leaves: 0/0
              v3-queries: 8/8, v3-reports: 44/44
            Errors:
          Interface PIM DR: Yes
          Interface vPC SVI: No
          Interface vPC CFS statistics:

        IGMP Interfaces for VRF "tenant1", count: 0
        IGMP Interfaces for VRF "manegement", count: 0

    '''}

    golden_parsed_output_1 = {
        "vrfs": {
            "tenant1": {
                 "groups_count": 0,
            },
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        IGMP Interfaces for VRF "tenant1", count: 0

    '''}
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpIgmpInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpIgmpInterface(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpIgmpInterface(device=self.device)
        parsed_output = obj.parse(vrf='tenant1')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


# ==============================================
# Unit test for 'show ip igmp groups'
# Unit test for 'show ip igmp groups vrf all'
# Unit test for 'show ip igmp groups vrf <WORD>'
# ==============================================
class test_show_ip_igmp_groups(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrfs": {
            "VRF1": {
                 "interface": {
                      "Ethernet2/4": {
                           "group": {
                                "239.6.6.6": {
                                     "expire": "never",
                                     "type": "S",
                                     "last_reporter": "10.186.2.1",
                                     "up_time": "00:15:27"
                                },
                                "239.8.8.8": {
                                     "source": {
                                          "10.16.2.2": {
                                               "expire": "never",
                                               "type": "S",
                                               "last_reporter": "10.186.2.1",
                                               "up_time": "00:15:27"
                                          }
                                     },
                                },
                                "239.5.5.5": {
                                     "expire": "never",
                                     "type": "S",
                                     "last_reporter": "10.186.2.1",
                                     "up_time": "00:15:27"
                                },
                                "239.7.7.7": {
                                     "source": {
                                          "10.16.2.1": {
                                               "expire": "never",
                                               "type": "S",
                                               "last_reporter": "10.186.2.1",
                                               "up_time": "00:15:27"
                                          }
                                     },
                                }
                           }
                      }
                 },
                 "total_entries": 4
            },
            "default": {
                 "interface": {
                      "Ethernet2/1": {
                           "group": {
                                "239.6.6.6": {
                                     "expire": "never",
                                     "type": "S",
                                     "last_reporter": "10.1.2.1",
                                     "up_time": "00:20:53"
                                },
                                "239.8.8.8": {
                                     "source": {
                                          "10.16.2.2": {
                                               "expire": "never",
                                               "type": "S",
                                               "last_reporter": "10.1.2.1",
                                               "up_time": "00:20:34"
                                          }
                                     },
                                },
                                "239.5.5.5": {
                                     "expire": "never",
                                     "type": "S",
                                     "last_reporter": "10.1.2.1",
                                     "up_time": "00:21:00"
                                },
                                "239.7.7.7": {
                                     "source": {
                                          "10.16.2.1": {
                                               "expire": "never",
                                               "type": "S",
                                               "last_reporter": "10.1.2.1",
                                               "up_time": "00:20:42"
                                          }
                                     },
                                }
                           }
                      }
                 },
                 "total_entries": 4
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        IGMP Connected Group Membership for VRF "default" - 4 total entries
        Type: S - Static, D - Dynamic, L - Local, T - SSM Translated
        Group Address      Type Interface           Uptime    Expires   Last Reporter
        239.5.5.5          S    Ethernet2/1         00:21:00  never     10.1.2.1
        239.6.6.6          S    Ethernet2/1         00:20:53  never     10.1.2.1
        239.7.7.7
          10.16.2.1          S    Ethernet2/1         00:20:42  never     10.1.2.1
        239.8.8.8
          10.16.2.2          S    Ethernet2/1         00:20:34  never     10.1.2.1

        IGMP Connected Group Membership for VRF "VRF1" - 4 total entries
        Type: S - Static, D - Dynamic, L - Local, T - SSM Translated
        Group Address      Type Interface           Uptime    Expires   Last Reporter
        239.5.5.5          S    Ethernet2/4         00:15:27  never     10.186.2.1
        239.6.6.6          S    Ethernet2/4         00:15:27  never     10.186.2.1
        239.7.7.7
          10.16.2.1          S    Ethernet2/4         00:15:27  never     10.186.2.1
        239.8.8.8
          10.16.2.2          S    Ethernet2/4         00:15:27  never     10.186.2.1
    '''}

    golden_parsed_output_1 = {
        "vrfs": {
            "default": {
                 "interface": {
                      "Ethernet2/1": {
                           "group": {
                                "239.6.6.6": {
                                     "expire": "never",
                                     "type": "S",
                                     "last_reporter": "10.1.2.1",
                                     "up_time": "00:20:53"
                                },
                                "239.8.8.8": {
                                     "source": {
                                          "10.16.2.2": {
                                               "expire": "never",
                                               "type": "S",
                                               "last_reporter": "10.1.2.1",
                                               "up_time": "00:20:34"
                                          }
                                     },
                                },
                                "239.5.5.5": {
                                     "expire": "never",
                                     "type": "S",
                                     "last_reporter": "10.1.2.1",
                                     "up_time": "00:21:00"
                                },
                                "239.7.7.7": {
                                     "source": {
                                          "10.16.2.1": {
                                               "expire": "never",
                                               "type": "S",
                                               "last_reporter": "10.1.2.1",
                                               "up_time": "00:20:42"
                                          }
                                     },
                                }
                           }
                      }
                 },
                 "total_entries": 4
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        IGMP Connected Group Membership for VRF "default" - 4 total entries
        Type: S - Static, D - Dynamic, L - Local, T - SSM Translated
        Group Address      Type Interface           Uptime    Expires   Last Reporter
        239.5.5.5          S    Ethernet2/1         00:21:00  never     10.1.2.1
        239.6.6.6          S    Ethernet2/1         00:20:53  never     10.1.2.1
        239.7.7.7
          10.16.2.1          S    Ethernet2/1         00:20:42  never     10.1.2.1
        239.8.8.8
          10.16.2.2          S    Ethernet2/1         00:20:34  never     10.1.2.1
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpIgmpGroups(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpIgmpGroups(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpIgmpGroups(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# ==============================================
# Unit test for 'show ip igmp local-groups'
# Unit test for 'show ip igmp local-groups vrf all'
# Unit test for 'show ip igmp local-groups vrf <WORD>'
# ==============================================
class test_show_ip_igmp_local_groups(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrfs": {
            "default": {
                 "interface": {
                      "Ethernet2/1": {
                           "join_group": {
                                "239.1.1.1 *": {
                                     "source": "*",
                                     "group": "239.1.1.1"
                                },
                                "239.3.3.3 10.4.1.1": {
                                     "source": "10.4.1.1",
                                     "group": "239.3.3.3"
                                },
                                "239.2.2.2 *": {
                                     "source": "*",
                                     "group": "239.2.2.2"
                                },
                                "239.4.4.4 10.4.1.2": {
                                     "source": "10.4.1.2",
                                     "group": "239.4.4.4"
                                }
                           },
                           "static_group": {
                                "239.5.5.5 *": {
                                     "source": "*",
                                     "group": "239.5.5.5"
                                },
                                "239.8.8.8 10.16.2.2": {
                                     "source": "10.16.2.2",
                                     "group": "239.8.8.8"
                                },
                                "239.6.6.6 *": {
                                     "source": "*",
                                     "group": "239.6.6.6"
                                },
                                "239.7.7.7 10.16.2.1": {
                                     "source": "10.16.2.1",
                                     "group": "239.7.7.7"
                                }
                           },
                           "group": {
                                "239.1.1.1": {
                                     "last_reporter": "00:00:13",
                                     "type": "local"
                                },
                                "239.8.8.8": {
                                     "source": {
                                          "10.16.2.2": {
                                               "last_reporter": "01:06:47",
                                               "type": "static"
                                          }
                                     },
                                },
                                "239.2.2.2": {
                                     "last_reporter": "00:00:18",
                                     "type": "local"
                                },
                                "239.4.4.4": {
                                     "source": {
                                          "10.4.1.2": {
                                               "last_reporter": "00:00:06",
                                               "type": "local"
                                          }
                                     },
                                },
                                "239.6.6.6": {
                                     "last_reporter": "01:06:47",
                                     "type": "static"
                                },
                                "239.5.5.5": {
                                     "last_reporter": "01:06:47",
                                     "type": "static"
                                },
                                "239.3.3.3": {
                                     "source": {
                                          "10.4.1.1": {
                                               "last_reporter": "00:00:11",
                                               "type": "local"
                                          }
                                     },
                                },
                                "239.7.7.7": {
                                     "source": {
                                          "10.16.2.1": {
                                               "last_reporter": "01:06:47",
                                               "type": "static"
                                          }
                                     },
                                }
                           }
                      }
                 }
            },
            "VRF1": {
                 "interface": {
                      "Ethernet2/4": {
                           "join_group": {
                                "239.1.1.1 *": {
                                     "source": "*",
                                     "group": "239.1.1.1"
                                },
                                "239.3.3.3 10.4.1.1": {
                                     "source": "10.4.1.1",
                                     "group": "239.3.3.3"
                                },
                                "239.2.2.2 *": {
                                     "source": "*",
                                     "group": "239.2.2.2"
                                },
                                "239.4.4.4 10.4.1.2": {
                                     "source": "10.4.1.2",
                                     "group": "239.4.4.4"
                                }
                           },
                           "static_group": {
                                "239.5.5.5 *": {
                                     "source": "*",
                                     "group": "239.5.5.5"
                                },
                                "239.8.8.8 10.16.2.2": {
                                     "source": "10.16.2.2",
                                     "group": "239.8.8.8"
                                },
                                "239.6.6.6 *": {
                                     "source": "*",
                                     "group": "239.6.6.6"
                                },
                                "239.7.7.7 10.16.2.1": {
                                     "source": "10.16.2.1",
                                     "group": "239.7.7.7"
                                }
                           },
                           "group": {
                                "239.1.1.1": {
                                     "last_reporter": "00:00:50",
                                     "type": "local"
                                },
                                "239.8.8.8": {
                                     "source": {
                                          "10.16.2.2": {
                                               "last_reporter": "01:06:47",
                                               "type": "static"
                                          }
                                     },
                                },
                                "239.2.2.2": {
                                     "last_reporter": "00:00:54",
                                     "type": "local"
                                },
                                "239.4.4.4": {
                                     "source": {
                                          "10.4.1.2": {
                                               "last_reporter": "00:00:55",
                                               "type": "local"
                                          }
                                     },
                                },
                                "239.6.6.6": {
                                     "last_reporter": "01:06:47",
                                     "type": "static"
                                },
                                "239.5.5.5": {
                                     "last_reporter": "01:06:47",
                                     "type": "static"
                                },
                                "239.3.3.3": {
                                     "source": {
                                          "10.4.1.1": {
                                               "last_reporter": "00:01:01",
                                               "type": "local"
                                          }
                                     },
                                },
                                "239.7.7.7": {
                                     "source": {
                                          "10.16.2.1": {
                                               "last_reporter": "01:06:47",
                                               "type": "static"
                                          }
                                     },
                                }}}}}}
    }

    golden_output = {'execute.return_value': '''\
        IGMP Locally Joined Group Membership for VRF "default"
        Group Address    Source Address   Type     Interface   Last Reported 
        239.1.1.1        *                Local    Eth2/1      00:00:13  
        239.2.2.2        *                Local    Eth2/1      00:00:18  
        239.3.3.3        10.4.1.1          Local    Eth2/1      00:00:11  
        239.4.4.4        10.4.1.2          Local    Eth2/1      00:00:06  
        239.5.5.5        *                Static   Eth2/1      01:06:47  
        239.6.6.6        *                Static   Eth2/1      01:06:47  
        239.7.7.7        10.16.2.1          Static   Eth2/1      01:06:47  
        239.8.8.8        10.16.2.2          Static   Eth2/1      01:06:47  

        IGMP Locally Joined Group Membership for VRF "VRF1"
        Group Address    Source Address   Type     Interface   Last Reported 
        239.1.1.1        *                Local    Eth2/4      00:00:50  
        239.2.2.2        *                Local    Eth2/4      00:00:54  
        239.3.3.3        10.4.1.1          Local    Eth2/4      00:01:01  
        239.4.4.4        10.4.1.2          Local    Eth2/4      00:00:55  
        239.5.5.5        *                Static   Eth2/4      01:06:47  
        239.6.6.6        *                Static   Eth2/4      01:06:47  
        239.7.7.7        10.16.2.1          Static   Eth2/4      01:06:47  
        239.8.8.8        10.16.2.2          Static   Eth2/4      01:06:47  
    '''}

    golden_parsed_output_1 = {
        "vrfs": {
            "VRF1": {
                 "interface": {
                      "Ethernet2/4": {
                           "join_group": {
                                "239.1.1.1 *": {
                                     "source": "*",
                                     "group": "239.1.1.1"
                                },
                                "239.3.3.3 10.4.1.1": {
                                     "source": "10.4.1.1",
                                     "group": "239.3.3.3"
                                },
                                "239.2.2.2 *": {
                                     "source": "*",
                                     "group": "239.2.2.2"
                                },
                                "239.4.4.4 10.4.1.2": {
                                     "source": "10.4.1.2",
                                     "group": "239.4.4.4"
                                }
                           },
                           "static_group": {
                                "239.5.5.5 *": {
                                     "source": "*",
                                     "group": "239.5.5.5"
                                },
                                "239.8.8.8 10.16.2.2": {
                                     "source": "10.16.2.2",
                                     "group": "239.8.8.8"
                                },
                                "239.6.6.6 *": {
                                     "source": "*",
                                     "group": "239.6.6.6"
                                },
                                "239.7.7.7 10.16.2.1": {
                                     "source": "10.16.2.1",
                                     "group": "239.7.7.7"
                                }
                           },
                           "group": {
                                "239.1.1.1": {
                                     "last_reporter": "00:00:50",
                                     "type": "local"
                                },
                                "239.8.8.8": {
                                     "source": {
                                          "10.16.2.2": {
                                               "last_reporter": "01:06:47",
                                               "type": "static"
                                          }
                                     },
                                },
                                "239.2.2.2": {
                                     "last_reporter": "00:00:54",
                                     "type": "local"
                                },
                                "239.4.4.4": {
                                     "source": {
                                          "10.4.1.2": {
                                               "last_reporter": "00:00:55",
                                               "type": "local"
                                          }
                                     },
                                },
                                "239.6.6.6": {
                                     "last_reporter": "01:06:47",
                                     "type": "static"
                                },
                                "239.5.5.5": {
                                     "last_reporter": "01:06:47",
                                     "type": "static"
                                },
                                "239.3.3.3": {
                                     "source": {
                                          "10.4.1.1": {
                                               "last_reporter": "00:01:01",
                                               "type": "local"
                                          }
                                     },
                                },
                                "239.7.7.7": {
                                     "source": {
                                          "10.16.2.1": {
                                               "last_reporter": "01:06:47",
                                               "type": "static"
                                          }
                                     },
                                }}}}}}
    }

    golden_output_1 = {'execute.return_value': '''\
        IGMP Locally Joined Group Membership for VRF "VRF1"
        Group Address    Source Address   Type     Interface   Last Reported 
        239.1.1.1        *                Local    Eth2/4      00:00:50  
        239.2.2.2        *                Local    Eth2/4      00:00:54  
        239.3.3.3        10.4.1.1          Local    Eth2/4      00:01:01  
        239.4.4.4        10.4.1.2          Local    Eth2/4      00:00:55  
        239.5.5.5        *                Static   Eth2/4      01:06:47  
        239.6.6.6        *                Static   Eth2/4      01:06:47  
        239.7.7.7        10.16.2.1          Static   Eth2/4      01:06:47  
        239.8.8.8        10.16.2.2          Static   Eth2/4      01:06:47
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpIgmpLocalGroups(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpIgmpLocalGroups(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpIgmpLocalGroups(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()