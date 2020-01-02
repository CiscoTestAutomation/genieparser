# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.nxos.show_mld import ShowIpv6MldInterface, \
                                  ShowIpv6MldGroups, \
                                  ShowIpv6MldLocalGroups


# ==============================================
# Unit test for 'show ipv6 mld interface vrf all'
# Unit test for 'show ipv6 mld interface'
# Unit test for 'show ipv6 mld interface vrf <WORD>'
# ==============================================
class test_show_ipv6_mld_interface(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrfs": {
            "VRF1": {
                 "interface": {
                      "Ethernet2/2": {
                           "query_max_response_time": 16,
                           "querier": "fe80::5054:ff:fed7:c01f",
                           "group_policy": "test",
                           "group_timeout": 2578,
                           "enable_refcount": 4,
                           "version": 2,
                           "link_status": "up",
                           "immediate_leave": True,
                           "startup_query": {
                                "interval": 91,
                                "configured_interval": 31,
                                "count": 7
                           },
                           "last_member": {
                                "query_count": 7,
                                "mrt": 1
                           },
                           "robustness_variable": 7,
                           "oper_status": "up",
                           "host_version": 2,
                           "available_groups": 6400,
                           "membership_count": 2,
                           "query_interval": 366,
                           "configured_robustness_variable": 7,
                           "statistics": {
                                "sent": {
                                     "v1_queries": 0,
                                     "v2_reports": 102,
                                     "v1_leaves": 0,
                                     "v1_reports": 0,
                                     "v2_queries": 82
                                },
                                "received": {
                                     "v1_queries": 0,
                                     "v2_reports": 416,
                                     "v1_leaves": 0,
                                     "v1_reports": 0,
                                     "v2_queries": 82
                                }
                           },
                           "configured_querier_timeout": 255,
                           "link_local_groups_reporting": False,
                           "max_groups": 6400,
                           "enable": True,
                           "next_query_sent_in": "00:05:18",
                           "querier_timeout": 2570,
                           "ipv6": {
                                "2001:db8:8404:751c::1/64": {
                                     "ip": "2001:db8:8404:751c::1",
                                     "prefix_length": "64",
                                     "status": "valid"
                                }
                           },
                           "configured_query_max_response_time": 16,
                           "link_local": {
                                "ipv6_address": "fe80::5054:ff:fed7:c01f",
                                "address": "fe80::5054:ff:fed7:c01f",
                                "status": "valid"
                           },
                           "unsolicited_report_interval": 1,
                           "querier_version": 2,
                           "configured_query_interval": 366,
                           "configured_group_timeout": 260
                      }
                 }
            },
            "default": {
                 "interface": {
                      "Ethernet2/1": {
                           "query_max_response_time": 16,
                           "querier": "fe80::5054:ff:fed7:c01f",
                           "group_policy": "test",
                           "group_timeout": 2578,
                           "enable_refcount": 5,
                           "version": 2,
                           "link_status": "up",
                           "immediate_leave": True,
                           "startup_query": {
                                "interval": 91,
                                "configured_interval": 31,
                                "count": 7
                           },
                           "last_member": {
                                "query_count": 7,
                                "mrt": 1
                           },
                           "robustness_variable": 7,
                           "oper_status": "up",
                           "host_version": 2,
                           "available_groups": 6400,
                           "membership_count": 2,
                           "query_interval": 366,
                           "configured_robustness_variable": 7,
                           "statistics": {
                                "sent": {
                                     "v1_queries": 0,
                                     "v2_reports": 191,
                                     "v1_leaves": 0,
                                     "v1_reports": 0,
                                     "v2_queries": 792
                                },
                                "received": {
                                     "v1_queries": 0,
                                     "v2_reports": 1775,
                                     "v1_leaves": 0,
                                     "v1_reports": 0,
                                     "v2_queries": 792
                                }
                           },
                           "configured_querier_timeout": 255,
                           "link_local_groups_reporting": False,
                           "max_groups": 6400,
                           "enable": True,
                           "next_query_sent_in": "00:03:01",
                           "querier_timeout": 2570,
                           "ipv6": {
                                "2001:db8:8404:907f::1/64": {
                                     "ip": "2001:db8:8404:907f::1",
                                     "prefix_length": "64",
                                     "status": "valid"
                                }
                           },
                           "configured_query_max_response_time": 16,
                           "link_local": {
                                "ipv6_address": "fe80::5054:ff:fed7:c01f",
                                "address": "fe80::5054:ff:fed7:c01f",
                                "status": "valid"
                           },
                           "unsolicited_report_interval": 1,
                           "querier_version": 2,
                           "configured_query_interval": 366,
                           "configured_group_timeout": 260
                      }
                 }
            }
       }
    }

    golden_output = {'execute.return_value': '''\
        ICMPv6 MLD Interfaces for VRF "VRF1"
        Ethernet2/2, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:db8:8404:751c::1/64 [VALID]
          Link Local Address : fe80::5054:ff:fed7:c01f(VALID)
          IPv6 Link-local Address: fe80::5054:ff:fed7:c01f
          ICMPv6 MLD parameters:
              Active Querier: fe80::5054:ff:fed7:c01f
              Querier version: 2, next query sent in: 00:05:18
              MLD Membership count: 2
              MLD version: 2, host version: 2
              MLD query interval: 366 secs, configured value: 366 secs
              MLD max response time: 16 secs, configured value: 16 secs
              MLD startup query interval: 91 secs, configured value: 31 secs
              MLD startup query count: 7
              MLD last member mrt: 1 secs
              MLD last member query count: 7
              MLD group timeout: 2578 secs, configured value: 260 secs
              MLD querier timeout: 2570 secs, configured value: 255 secs
              MLD unsolicited report interval: 1 secs
              MLD robustness variable: 7, configured value: 7
              MLD reporting for link-local groups: disabled
              MLD immediate leave: enabled
              MLD interface enable refcount: 4
              MLD Report Policy: test
              MLD State Limit: 6400,  Available States: 6400
          ICMPv6 MLD Statistics (sent/received):
          V1 Queries:          0/0         
          V2 Queries:         82/82        
          V1 Reports:          0/0         
          V2 Reports:        102/416       
          V1 Leaves :          0/0         
        ICMPv6 MLD Interfaces for VRF "default"
        Ethernet2/1, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:db8:8404:907f::1/64 [VALID]
          Link Local Address : fe80::5054:ff:fed7:c01f(VALID)
          IPv6 Link-local Address: fe80::5054:ff:fed7:c01f
          ICMPv6 MLD parameters:
              Active Querier: fe80::5054:ff:fed7:c01f
              Querier version: 2, next query sent in: 00:03:01
              MLD Membership count: 2
              MLD version: 2, host version: 2
              MLD query interval: 366 secs, configured value: 366 secs
              MLD max response time: 16 secs, configured value: 16 secs
              MLD startup query interval: 91 secs, configured value: 31 secs
              MLD startup query count: 7
              MLD last member mrt: 1 secs
              MLD last member query count: 7
              MLD group timeout: 2578 secs, configured value: 260 secs
              MLD querier timeout: 2570 secs, configured value: 255 secs
              MLD unsolicited report interval: 1 secs
              MLD robustness variable: 7, configured value: 7
              MLD reporting for link-local groups: disabled
              MLD immediate leave: enabled
              MLD interface enable refcount: 5
              MLD Report Policy: test
              MLD State Limit: 6400,  Available States: 6400
          ICMPv6 MLD Statistics (sent/received):
          V1 Queries:          0/0         
          V2 Queries:        792/792       
          V1 Reports:          0/0         
          V2 Reports:        191/1775      
          V1 Leaves :          0/0         
        ICMPv6 MLD Interfaces for VRF "management"

    '''}

    golden_parsed_output_1 = {
        "vrfs": {
            "default": {
                 "interface": {
                      "Ethernet2/1": {
                           "query_max_response_time": 16,
                           "querier": "fe80::5054:ff:fed7:c01f",
                           "group_policy": "test",
                           "group_timeout": 2578,
                           "enable_refcount": 5,
                           "version": 2,
                           "link_status": "up",
                           "immediate_leave": True,
                           "startup_query": {
                                "interval": 91,
                                "configured_interval": 31,
                                "count": 7
                           },
                           "last_member": {
                                "query_count": 7,
                                "mrt": 1
                           },
                           "robustness_variable": 7,
                           "oper_status": "up",
                           "host_version": 2,
                           "available_groups": 6400,
                           "membership_count": 2,
                           "query_interval": 366,
                           "configured_robustness_variable": 7,
                           "statistics": {
                                "sent": {
                                     "v1_queries": 0,
                                     "v2_reports": 191,
                                     "v1_leaves": 0,
                                     "v1_reports": 0,
                                     "v2_queries": 792
                                },
                                "received": {
                                     "v1_queries": 0,
                                     "v2_reports": 1775,
                                     "v1_leaves": 0,
                                     "v1_reports": 0,
                                     "v2_queries": 792
                                }
                           },
                           "configured_querier_timeout": 255,
                           "link_local_groups_reporting": False,
                           "max_groups": 6400,
                           "enable": True,
                           "next_query_sent_in": "00:03:01",
                           "querier_timeout": 2570,
                           "ipv6": {
                                "2001:db8:8404:907f::1/64": {
                                     "ip": "2001:db8:8404:907f::1",
                                     "prefix_length": "64",
                                     "status": "valid"
                                }
                           },
                           "configured_query_max_response_time": 16,
                           "link_local": {
                                "ipv6_address": "fe80::5054:ff:fed7:c01f",
                                "address": "fe80::5054:ff:fed7:c01f",
                                "status": "valid"
                           },
                           "unsolicited_report_interval": 1,
                           "querier_version": 2,
                           "configured_query_interval": 366,
                           "configured_group_timeout": 260
                      }
                 }
            }
       }
    }

    golden_output_1 = {'execute.return_value': '''\
        ICMPv6 MLD Interfaces for VRF "default"
        Ethernet2/1, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:db8:8404:907f::1/64 [VALID]
          Link Local Address : fe80::5054:ff:fed7:c01f(VALID)
          IPv6 Link-local Address: fe80::5054:ff:fed7:c01f
          ICMPv6 MLD parameters:
              Active Querier: fe80::5054:ff:fed7:c01f
              Querier version: 2, next query sent in: 00:03:01
              MLD Membership count: 2
              MLD version: 2, host version: 2
              MLD query interval: 366 secs, configured value: 366 secs
              MLD max response time: 16 secs, configured value: 16 secs
              MLD startup query interval: 91 secs, configured value: 31 secs
              MLD startup query count: 7
              MLD last member mrt: 1 secs
              MLD last member query count: 7
              MLD group timeout: 2578 secs, configured value: 260 secs
              MLD querier timeout: 2570 secs, configured value: 255 secs
              MLD unsolicited report interval: 1 secs
              MLD robustness variable: 7, configured value: 7
              MLD reporting for link-local groups: disabled
              MLD immediate leave: enabled
              MLD interface enable refcount: 5
              MLD Report Policy: test
              MLD State Limit: 6400,  Available States: 6400
          ICMPv6 MLD Statistics (sent/received):
          V1 Queries:          0/0         
          V2 Queries:        792/792       
          V1 Reports:          0/0         
          V2 Reports:        191/1775      
          V1 Leaves :          0/0
    '''}

    golden_parsed_output_2 = {
        'vrfs': {
            'VRF1': {
                'count': 4,
                'interface': {
                    'Ethernet1/1.11': {'configured_group_timeout': 260,
                                        'configured_querier_timeout': 255,
                                        'configured_query_interval': 125,
                                        'configured_query_max_response_time': 10,
                                        'configured_robustness_variable': 2,
                                        'enable': True,
                                        'enable_refcount': 1,
                                        'group_timeout': 260,
                                        'host_version': 2,
                                        'ipv6': {'2001:10:3:5::5/64': {'ip': '2001:10:3:5::5',
                                                                       'prefix_length': '64',
                                                                       'status': 'valid'}},
                                        'last_member': {'mrt': 1,
                                                        'query_count': 2},
                                        'link_local_groups_reporting': False,
                                        'link_status': 'up',
                                        'oper_status': 'up',
                                        'querier_timeout': 255,
                                        'query_interval': 125,
                                        'query_max_response_time': 10,
                                        'robustness_variable': 2,
                                        'startup_query': {'configured_interval': 31,
                                                          'count': 2,
                                                          'interval': 31},
                                        'unsolicited_report_interval': 10,
                                        'version': 2},
                    'Ethernet1/2.11': {'configured_group_timeout': 260,
                                        'configured_querier_timeout': 255,
                                        'configured_query_interval': 125,
                                        'configured_query_max_response_time': 10,
                                        'configured_robustness_variable': 2,
                                        'enable': True,
                                        'enable_refcount': 1,
                                        'group_timeout': 260,
                                        'host_version': 2,
                                        'ipv6': {'2001:20:5:5::5/64': {'ip': '2001:20:5:5::5',
                                                                       'prefix_length': '64',
                                                                       'status': 'valid'}},
                                        'last_member': {'mrt': 1,
                                                        'query_count': 2},
                                        'link_local_groups_reporting': False,
                                        'link_status': 'up',
                                        'oper_status': 'up',
                                        'querier_timeout': 255,
                                        'query_interval': 125,
                                        'query_max_response_time': 10,
                                        'robustness_variable': 2,
                                        'startup_query': {'configured_interval': 31,
                                                          'count': 2,
                                                          'interval': 31},
                                        'unsolicited_report_interval': 10,
                                        'version': 2}
                }
            },
            'default': {
                'count': 6,
                'interface': {
                    'Ethernet1/1.10': {'configured_group_timeout': 260,
                                       'configured_querier_timeout': 255,
                                       'configured_query_interval': 125,
                                       'configured_query_max_response_time': 10,
                                       'configured_robustness_variable': 2,
                                       'enable': True,
                                       'enable_refcount': 1,
                                       'group_timeout': 260,
                                       'host_version': 2,
                                       'ipv6': {'2001:10:3:5::5/64': {'ip': '2001:10:3:5::5',
                                                                      'prefix_length': '64',
                                                                      'status': 'valid'}},
                                       'last_member': {'mrt': 1,
                                                       'query_count': 2},
                                       'link_local_groups_reporting': False,
                                       'link_status': 'up',
                                       'oper_status': 'up',
                                       'querier_timeout': 255,
                                       'query_interval': 125,
                                       'query_max_response_time': 10,
                                       'robustness_variable': 2,
                                       'startup_query': {'configured_interval': 31,
                                                         'count': 2,
                                                         'interval': 31},
                                       'unsolicited_report_interval': 10,
                                       'version': 2},
                    'Ethernet1/2.10': {'configured_group_timeout': 260,
                                       'configured_querier_timeout': 255,
                                       'configured_query_interval': 125,
                                       'configured_query_max_response_time': 10,
                                       'configured_robustness_variable': 2,
                                       'enable': True,
                                       'enable_refcount': 1,
                                       'group_timeout': 260,
                                       'host_version': 2,
                                       'ipv6': {'2001:20:5:5::5/64': {'ip': '2001:20:5:5::5',
                                                                      'prefix_length': '64',
                                                                      'status': 'valid'}},
                                       'last_member': {'mrt': 1,
                                                       'query_count': 2},
                                       'link_local_groups_reporting': False,
                                       'link_status': 'up',
                                       'oper_status': 'up',
                                       'querier_timeout': 255,
                                       'query_interval': 125,
                                       'query_max_response_time': 10,
                                       'robustness_variable': 2,
                                       'startup_query': {'configured_interval': 31,
                                                         'count': 2,
                                                         'interval': 31},
                                       'unsolicited_report_interval': 10,
                                       'version': 2}
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''\
MLD Interfaces for VRF "default", count: 6
Ethernet1/1.10, Interface status: protocol-up/link-up/admin-up
  IPv6 address: 
    2001:10:3:5::5/64 [VALID]
  Active querier: fe80::282:49ff:fe9d:1b08, version: 2, next query sent in: 00:01:33
  Membership count: 0
  Old Membership count 0
  MLD version: 2, host version: 2
  MLD query interval: 125 secs, configured value: 125 secs
  MLD max response time: 10 secs, configured value: 10 secs
  MLD startup query interval: 31 secs, configured value: 31 secs
  MLD startup query count: 2
  MLD last member mrt: 1 secs
  MLD last member query count: 2
  MLD group timeout: 260 secs, configured value: 260 secs
  MLD querier timeout: 255 secs, configured value: 255 secs
  MLD unsolicited report interval: 10 secs
  MLD robustness variable: 2, configured value: 2
  MLD reporting for link-local groups: disabled
  MLD interface enable refcount: 1
  MLD interface immediate leave: disabled
  MLD interface suppress v2-gsq: disabled
  MLD VRF name default (id 1)
  MLD Report Policy: None
  MLD Host Proxy: Disabled
  MLD State Limit: None
  MLD interface statistics: (only non-zero values displayed)
    General (sent/received):
      v1-queries: 0/0, v1-reports: 0/0, v1-leaves: 0/0
      v2-queries: 12/12, v2-reports: 0/6
    Errors:
      General Queries received with invalid destination address; v1: 0, v2: 0
      Checksum errors: 0, Packet length errors: 0
      Packets with Local IP as source: 0, Source subnet check failures: 0 
      Query from non-querier:1
      Report version mismatch: 0, Query version mismatch: 0
      Unknown MLD message type: 0
      Invalid v1 reports: 0, Invalid v2 reports: 0
      v2 reports with invalid auxillary length: 0
      Packets dropped due to router-alert check: 0
      Packets dropped due to invalid TTL: 0
  Interface PIM DR: No
  Interface vPC SVI: No
  Interface vPC CFS statistics:
    DR queries sent: 0
    DR queries rcvd: 0
    DR queries fail: 0
    DR updates sent: 0
    DR updates rcvd: 0
    DR updates fail: 0
Ethernet1/2.10, Interface status: protocol-up/link-up/admin-up
  IPv6 address: 
    2001:20:5:5::5/64 [VALID]
  Active querier: fe80::282:49ff:fe9d:1b08, version: 2, next query sent in: 00:01:11
  Membership count: 2
  Old Membership count 0
  MLD version: 2, host version: 2
  MLD query interval: 125 secs, configured value: 125 secs
  MLD max response time: 10 secs, configured value: 10 secs
  MLD startup query interval: 31 secs, configured value: 31 secs
  MLD startup query count: 2
  MLD last member mrt: 1 secs
  MLD last member query count: 2
  MLD group timeout: 260 secs, configured value: 260 secs
  MLD querier timeout: 255 secs, configured value: 255 secs
  MLD unsolicited report interval: 10 secs
  MLD robustness variable: 2, configured value: 2
  MLD reporting for link-local groups: disabled
  MLD interface enable refcount: 1
  MLD interface immediate leave: disabled
  MLD interface suppress v2-gsq: disabled
  MLD VRF name default (id 1)
  MLD Report Policy: None
  MLD Host Proxy: Disabled
  MLD State Limit: None
  MLD interface statistics: (only non-zero values displayed)
    General (sent/received):
      v1-queries: 0/0, v1-reports: 0/0, v1-leaves: 0/0
      v2-queries: 12/12, v2-reports: 0/36
    Errors:
      General Queries received with invalid destination address; v1: 0, v2: 0
      Checksum errors: 0, Packet length errors: 0
      Packets with Local IP as source: 0, Source subnet check failures: 0 
      Query from non-querier:0
      Report version mismatch: 0, Query version mismatch: 0
      Unknown MLD message type: 0
      Invalid v1 reports: 0, Invalid v2 reports: 0
      v2 reports with invalid auxillary length: 0
      Packets dropped due to router-alert check: 0
      Packets dropped due to invalid TTL: 0
  Interface PIM DR: Yes
  Interface vPC SVI: No
  Interface vPC CFS statistics:
    DR queries sent: 0
    DR queries rcvd: 0
    DR queries fail: 0
    DR updates sent: 0
    DR updates rcvd: 0
    DR updates fail: 0
MLD Interfaces for VRF "VRF1", count: 4
Ethernet1/1.11, Interface status: protocol-up/link-up/admin-up
  IPv6 address: 
    2001:10:3:5::5/64 [VALID]
  Active querier: fe80::282:49ff:fe9d:1b08, version: 2, next query sent in: 00:01:24
  Membership count: 0
  Old Membership count 0
  MLD version: 2, host version: 2
  MLD query interval: 125 secs, configured value: 125 secs
  MLD max response time: 10 secs, configured value: 10 secs
  MLD startup query interval: 31 secs, configured value: 31 secs
  MLD startup query count: 2
  MLD last member mrt: 1 secs
  MLD last member query count: 2
  MLD group timeout: 260 secs, configured value: 260 secs
  MLD querier timeout: 255 secs, configured value: 255 secs
  MLD unsolicited report interval: 10 secs
  MLD robustness variable: 2, configured value: 2
  MLD reporting for link-local groups: disabled
  MLD interface enable refcount: 1
  MLD interface immediate leave: disabled
  MLD interface suppress v2-gsq: disabled
  MLD VRF name VRF1 (id 3)
  MLD Report Policy: None
  MLD Host Proxy: Disabled
  MLD State Limit: None
  MLD interface statistics: (only non-zero values displayed)
    General (sent/received):
      v1-queries: 0/0, v1-reports: 0/0, v1-leaves: 0/0
      v2-queries: 12/12, v2-reports: 0/6
    Errors:
      General Queries received with invalid destination address; v1: 0, v2: 0
      Checksum errors: 0, Packet length errors: 0
      Packets with Local IP as source: 0, Source subnet check failures: 0 
      Query from non-querier:1
      Report version mismatch: 0, Query version mismatch: 0
      Unknown MLD message type: 0
      Invalid v1 reports: 0, Invalid v2 reports: 0
      v2 reports with invalid auxillary length: 0
      Packets dropped due to router-alert check: 0
      Packets dropped due to invalid TTL: 0
  Interface PIM DR: No
  Interface vPC SVI: No
  Interface vPC CFS statistics:
    DR queries sent: 0
    DR queries rcvd: 0
    DR queries fail: 0
    DR updates sent: 0
    DR updates rcvd: 0
    DR updates fail: 0
Ethernet1/2.11, Interface status: protocol-up/link-up/admin-up
  IPv6 address: 
    2001:20:5:5::5/64 [VALID]
  Active querier: fe80::282:49ff:fe9d:1b08, version: 2, next query sent in: 00:01:20
  Membership count: 2
  Old Membership count 0
  MLD version: 2, host version: 2
  MLD query interval: 125 secs, configured value: 125 secs
  MLD max response time: 10 secs, configured value: 10 secs
  MLD startup query interval: 31 secs, configured value: 31 secs
  MLD startup query count: 2
  MLD last member mrt: 1 secs
  MLD last member query count: 2
  MLD group timeout: 260 secs, configured value: 260 secs
  MLD querier timeout: 255 secs, configured value: 255 secs
  MLD unsolicited report interval: 10 secs
  MLD robustness variable: 2, configured value: 2
  MLD reporting for link-local groups: disabled
  MLD interface enable refcount: 1
  MLD interface immediate leave: disabled
  MLD interface suppress v2-gsq: disabled
  MLD VRF name VRF1 (id 3)
  MLD Report Policy: None
  MLD Host Proxy: Disabled
  MLD State Limit: None
  MLD interface statistics: (only non-zero values displayed)
    General (sent/received):
      v1-queries: 0/0, v1-reports: 0/0, v1-leaves: 0/0
      v2-queries: 12/12, v2-reports: 0/36
    Errors:
      General Queries received with invalid destination address; v1: 0, v2: 0
      Checksum errors: 0, Packet length errors: 0
      Packets with Local IP as source: 0, Source subnet check failures: 0 
      Query from non-querier:0
      Report version mismatch: 0, Query version mismatch: 0
      Unknown MLD message type: 0
      Invalid v1 reports: 0, Invalid v2 reports: 0
      v2 reports with invalid auxillary length: 0
      Packets dropped due to router-alert check: 0
      Packets dropped due to invalid TTL: 0
  Interface PIM DR: Yes
  Interface vPC SVI: No
  Interface vPC CFS statistics:
    DR queries sent: 0
    DR queries rcvd: 0
    DR queries fail: 0
    DR updates sent: 0
    DR updates rcvd: 0
    DR updates fail: 0
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6MldInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6MldInterface(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6MldInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpv6MldInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

# ==============================================
# Unit test for 'show ipv6 mld groups'
# Unit test for 'show ipv6 mld groups vrf all'
# Unit test for 'show ipv6 mld groups vrf <WORD>'
# ==============================================
class test_show_ip_igmp_groups(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrfs": {
            "default": {
                 "groups_count": 2,
                 "interface": {
                      "Ethernet2/1": {
                           "group": {
                                "ff30::2": {
                                     "source": {
                                          "2001:db8:0:abcd::2": {
                                               "last_reporter": "2001:db8:8404:907f::1",
                                               "expire": "never",
                                               "type": "static",
                                               "up_time": "00:26:28"
                                          }
                                     }
                                },
                                "fffe::2": {
                                     "last_reporter": "2001:db8:8404:907f::1",
                                     "expire": "never",
                                     "type": "static",
                                     "up_time": "00:26:05"
                                }
                           }
                      }
                 }
            },
            "VRF1": {
                 "groups_count": 2,
                 "interface": {
                      "Ethernet2/2": {
                           "group": {
                                "ff30::2": {
                                     "source": {
                                          "2001:db8:0:abcd::2": {
                                               "last_reporter": "2001:db8:8404:751c::1",
                                               "expire": "never",
                                               "type": "static",
                                               "up_time": "00:25:49"
                                          }
                                     }
                                },
                                "fffe::2": {
                                     "last_reporter": "2001:db8:8404:751c::1",
                                     "expire": "never",
                                     "type": "static",
                                     "up_time": "00:25:49"
                                }
                           }
                      }
                 }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        MLD Connected Group Membership for VRF "default" - 2 total entries
        (2001:db8:0:abcd::2, ff30::2)
          Type: Static, Interface: Ethernet2/1
          Uptime/Expires: 00:26:28/never, Last Reporter: 2001:db8:8404:907f::1

        (*, fffe::2)
          Type: Static, Interface: Ethernet2/1
          Uptime/Expires: 00:26:05/never, Last Reporter: 2001:db8:8404:907f::1

        MLD Connected Group Membership for VRF "VRF1" - 2 total entries
        (2001:db8:0:abcd::2, ff30::2)
          Type: Static, Interface: Ethernet2/2
          Uptime/Expires: 00:25:49/never, Last Reporter: 2001:db8:8404:751c::1

        (*, fffe::2)
          Type: Static, Interface: Ethernet2/2
          Uptime/Expires: 00:25:49/never, Last Reporter: 2001:db8:8404:751c::1
    '''}

    golden_parsed_output_1 = {
        "vrfs": {
            "default": {
                 "groups_count": 2,
                 "interface": {
                      "Ethernet2/1": {
                           "group": {
                                "ff30::2": {
                                     "source": {
                                          "2001:db8:0:abcd::2": {
                                               "last_reporter": "2001:db8:8404:907f::1",
                                               "expire": "never",
                                               "type": "static",
                                               "up_time": "00:26:28"
                                          }
                                     }
                                },
                                "fffe::2": {
                                     "last_reporter": "2001:db8:8404:907f::1",
                                     "expire": "never",
                                     "type": "static",
                                     "up_time": "00:26:05"
                                }
                           }
                      }
                 }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        MLD Connected Group Membership for VRF "default" - 2 total entries
        (2001:db8:0:abcd::2, ff30::2)
          Type: Static, Interface: Ethernet2/1
          Uptime/Expires: 00:26:28/never, Last Reporter: 2001:db8:8404:907f::1

        (*, fffe::2)
          Type: Static, Interface: Ethernet2/1
          Uptime/Expires: 00:26:05/never, Last Reporter: 2001:db8:8404:907f::1
    '''}

    golden_parsed_output_2 = {
    "vrfs": {
        "default": {
            "groups_count": 3,
            "interface": {
                "Ethernet1/2.10": {
                    "group": {
                        "ff38::1": {
                            "source": {
                                "2001:20:1:1::254": {
                                    "type": "d",
                                    "expire": "00:03:31",
                                    "up_time": "00:13:56",
                                    "last_reporter": "fe80::200:7cff:fe06:af79"
                                }
                            }
                        },
                        "fffe::1": {
                            "type": "d",
                            "expire": "00:03:31",
                            "up_time": "00:13:56",
                            "last_reporter": "fe80::200:7cff:fe06:af79"
                        }
                    }
                },
                "Ethernet1/2.12": {
                    "group": {
                        "fffe::4": {
                            "type": "s",
                            "expire": "never",
                            "up_time": "00:21:20",
                            "last_reporter": "fe80::282:49ff:fe9d:1b08"
                        }
                    }
                }
            }
        },
        "VRF1": {
            "groups_count": 2,
            "interface": {
                "Ethernet1/2.11": {
                    "group": {
                        "ff38::1": {
                            "source": {
                                "2001:20:1:1::254": {
                                    "type": "d",
                                    "expire": "00:03:09",
                                    "up_time": "00:13:56",
                                    "last_reporter": "fe80::200:7cff:fe0c:2a3f"
                                }
                            }
                        },
                        "fffe::1": {
                            "type": "d",
                            "expire": "00:03:09",
                            "up_time": "00:13:56",
                            "last_reporter": "fe80::200:7cff:fe0c:2a3f"
                        }
                    }
                }
            }
        }
    }
}

    golden_output_2 = {'execute.return_value': '''\
show ipv6 mld groups vrf all

MLD Connected Group Membership for VRF "default" - 3 total entries
Type: S - Static, D - Dynamic, L - Local, T - SSM Translated, H - Host Proxy
      * - Cache Only
Group Address      Type Interface              Uptime    Expires   Last Reporter
ff38::1
  2001:20:1:1::254 D    Ethernet1/2.10         00:13:56  00:03:31  fe80::200:7cff:fe06:af79
fffe::1            D   Ethernet1/2.10         00:13:56  00:03:31  fe80::200:7cff:fe06:af79
fffe::4            S   Ethernet1/2.12         00:21:20  never     fe80::282:49ff:fe9d:1b08

MLD Connected Group Membership for VRF "VRF1" - 2 total entries
Type: S - Static, D - Dynamic, L - Local, T - SSM Translated, H - Host Proxy
      * - Cache Only
Group Address      Type Interface              Uptime    Expires   Last Reporter
ff38::1
  2001:20:1:1::254 D    Ethernet1/2.11         00:13:56  00:03:09  fe80::200:7cff:fe0c:2a3f
fffe::1            D   Ethernet1/2.11         00:13:56  00:03:09  fe80::200:7cff:fe0c:2a3f
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6MldGroups(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6MldGroups(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6MldGroups(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpv6MldGroups(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


# ==============================================
# Unit test for 'show ipv6 mld local-groups'
# Unit test for 'show ipv6 mld local-groups vrf all'
# Unit test for 'show ipv6 mld local-groups vrf <WORD>'
# ==============================================
class test_show_ipv6_mld_local_groups(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrfs": {
            "VRF1": {
                 "interface": {
                      "Ethernet2/2": {
                           "static_group": {
                                "fffe::2 *": {
                                     "group": "fffe::2",
                                     "source": "*"
                                },
                                "ff30::2 2001:db8:0:abcd::2": {
                                     "group": "ff30::2",
                                     "source": "2001:db8:0:abcd::2"
                                }
                           },
                           "group": {
                                "ff30::2": {
                                     "source": {
                                          "2001:db8:0:abcd::2": {
                                               "last_reported": "1d07h",
                                               "type": "static"
                                          }
                                     }
                                },
                                "fffe::2": {
                                     "last_reported": "1d07h",
                                     "type": "static"
                                },
                                "fffe::1": {
                                     "last_reported": "00:01:04",
                                     "type": "local"
                                },
                                "ff30::1": {
                                     "source": {
                                          "2001:db8:0:abcd::1": {
                                               "last_reported": "00:01:01",
                                               "type": "local"
                                          }
                                     }
                                }
                           },
                           "join_group": {
                                "ff30::1 2001:db8:0:abcd::1": {
                                     "group": "ff30::1",
                                     "source": "2001:db8:0:abcd::1"
                                },
                                "fffe::1 *": {
                                     "group": "fffe::1",
                                     "source": "*"
                                }
                           }
                      }
                 }
            },
            "default": {
                 "interface": {
                      "Ethernet2/1": {
                           "static_group": {
                                "fffe::2 *": {
                                     "group": "fffe::2",
                                     "source": "*"
                                },
                                "ff30::2 2001:db8:0:abcd::2": {
                                     "group": "ff30::2",
                                     "source": "2001:db8:0:abcd::2"
                                }
                           },
                           "group": {
                                "ff30::2": {
                                     "source": {
                                          "2001:db8:0:abcd::2": {
                                               "last_reported": "1d07h",
                                               "type": "static"
                                          }
                                     }
                                },
                                "fffe::2": {
                                     "last_reported": "1d07h",
                                     "type": "static"
                                },
                                "fffe::1": {
                                     "last_reported": "00:03:07",
                                     "type": "local"
                                },
                                "ff30::1": {
                                     "source": {
                                          "2001:db8:0:abcd::1": {
                                               "last_reported": "00:03:19",
                                               "type": "local"
                                          }
                                     }
                                }
                           },
                           "join_group": {
                                "ff30::1 2001:db8:0:abcd::1": {
                                     "group": "ff30::1",
                                     "source": "2001:db8:0:abcd::1"
                                },
                                "fffe::1 *": {
                                     "group": "fffe::1",
                                     "source": "*"
                                }
                           }
                      }
                 }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        MLD Locally Joined Group Membership for VRF "default"
        Group   Type     Interface   Last Reported 
        (*, fffe::1)
                Local    Eth2/1      00:03:07  
        (2001:db8:0:abcd::1, ff30::1)
                Local    Eth2/1      00:03:19  
        (2001:db8:0:abcd::2, ff30::2)
                Static   Eth2/1      1d07h     
        (*, fffe::2)
                Static   Eth2/1      1d07h     
        MLD Locally Joined Group Membership for VRF "VRF1"
        Group   Type     Interface   Last Reported 
        (*, fffe::1)
                Local    Eth2/2      00:01:04  
        (2001:db8:0:abcd::1, ff30::1)
                Local    Eth2/2      00:01:01  
        (2001:db8:0:abcd::2, ff30::2)
                Static   Eth2/2      1d07h     
        (*, fffe::2)
                Static   Eth2/2      1d07h  
    '''}

    golden_parsed_output_1 = {
        "vrfs": {
            "VRF1": {
                 "interface": {
                      "Ethernet2/2": {
                           "static_group": {
                                "fffe::2 *": {
                                     "group": "fffe::2",
                                     "source": "*"
                                },
                                "ff30::2 2001:db8:0:abcd::2": {
                                     "group": "ff30::2",
                                     "source": "2001:db8:0:abcd::2"
                                }
                           },
                           "group": {
                                "ff30::2": {
                                     "source": {
                                          "2001:db8:0:abcd::2": {
                                               "last_reported": "1d07h",
                                               "type": "static"
                                          }
                                     }
                                },
                                "fffe::2": {
                                     "last_reported": "1d07h",
                                     "type": "static"
                                },
                                "fffe::1": {
                                     "last_reported": "00:01:04",
                                     "type": "local"
                                },
                                "ff30::1": {
                                     "source": {
                                          "2001:db8:0:abcd::1": {
                                               "last_reported": "00:01:01",
                                               "type": "local"
                                          }
                                     }
                                }
                           },
                           "join_group": {
                                "ff30::1 2001:db8:0:abcd::1": {
                                     "group": "ff30::1",
                                     "source": "2001:db8:0:abcd::1"
                                },
                                "fffe::1 *": {
                                     "group": "fffe::1",
                                     "source": "*"
                                }
                           }
                      }
                 }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        MLD Locally Joined Group Membership for VRF "VRF1"
        Group   Type     Interface   Last Reported 
        (*, fffe::1)
                Local    Eth2/2      00:01:04  
        (2001:db8:0:abcd::1, ff30::1)
                Local    Eth2/2      00:01:01  
        (2001:db8:0:abcd::2, ff30::2)
                Static   Eth2/2      1d07h     
        (*, fffe::2)
                Static   Eth2/2      1d07h  
    '''}

    golden_parsed_output_2 = {
    "vrfs": {
        "default": {
            "interface": {
                "Ethernet1/2.12": {
                    "group": {
                        "fffe::2": {
                            "source": {
                                "*": {
                                    "last_reported": "00:27:31",
                                    "type": "local"
                                }
                            },
                            "last_reported": "00:27:31",
                            "type": "local"
                        },
                        "fffe::3": {
                            "source": {
                                "*": {
                                    "last_reported": "00:27:31",
                                    "type": "local"
                                }
                            },
                            "last_reported": "00:27:31",
                            "type": "local"
                        },
                        "fffe::4": {
                            "source": {
                                "*": {
                                    "last_reported": "00:27:31",
                                    "type": "static"
                                }
                            },
                            "last_reported": "00:27:31",
                            "type": "static"
                        }
                    },
                    "join_group": {
                        "fffe::2 *": {
                            "group": "fffe::2",
                            "source": "*"
                        },
                        "fffe::3 *": {
                            "group": "fffe::3",
                            "source": "*"
                        }
                    },
                    "static_group": {
                        "fffe::4 *": {
                            "group": "fffe::4",
                            "source": "*"
                        }
                    }
                }
            }
        },
        "VRF1": {}
    }
}

    golden_output_2 = {'execute.return_value': '''\
show ipv6 mld local-groups vrf all

MLD Locally Joined Group Membership for VRF "default"
Group Address    Source Address   Type     Interface   Last Reported 
fffe::2          *                Local    Eth1/2.12   00:27:31  
fffe::3          *                Local    Eth1/2.12   00:27:31  
fffe::4          *                Static   Eth1/2.12   00:27:31  

MLD Locally Joined Group Membership for VRF "VRF1"
Group Address    Source Address   Type     Interface   Last Reported  
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6MldLocalGroups(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6MldLocalGroups(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6MldLocalGroups(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpv6MldLocalGroups(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

if __name__ == '__main__':
    unittest.main()