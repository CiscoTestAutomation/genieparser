

expected_output = {
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
