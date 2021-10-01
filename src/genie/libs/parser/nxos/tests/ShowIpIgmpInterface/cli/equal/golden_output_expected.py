

expected_output = {
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
