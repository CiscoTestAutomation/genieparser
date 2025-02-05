expected_output = {
    "global_configuration": {
        "enabled": "enabled",
        "v1v2_report_suppression": "enabled",
        "v3_report_suppression": "disabled",
        "link_local_groups_suppression": "enabled"
    },
    "vlans": {
        "461": {
            "ip_igmp_snooping": "enabled",
            "report_flooding": "disabled",
            "report_flooding_interfaces": "n/a",
            "group_address_for_proxy_leaves": "no",
            "v1v2_report_suppression": "enabled",
            "link_local_groups_suppression": "enabled",
            "v3_report_suppression": "disabled",
            "lookup_mode": "ip",
            "igmp_querier": {
                "address": "1.2.3.100",
                "version": 3,
                "interval": 125,
                "last_member_query_interval": 1,
                "robustness": 2
            },
            "switch_querier": {
                "type": "enabled",
                "ip_address": "1.2.3.100",
                "state": "running"
            },
            "v2_fast_leave": "disabled",
            "router_ports_count": 2,
            "groups_count": 1,
            "vlan_vpc_function": "enabled"
        }
    }
}