expected_output = {
    "global_configuration": {
        "enabled": "enabled",
        "v1v2_report_suppression": "enabled",
        "v3_report_suppression": "disabled",
        "link_local_groups_suppression": "enabled"
    },
    "vlans": {
        "1": {
            "ip_igmp_snooping": "enabled",
            "v1v2_report_suppression": "enabled",
            "report_flooding": "disabled",
            "report_flooding_interfaces": "n/a",
            "group_address_for_proxy_leaves": "no",
            "link_local_groups_suppression": "enabled",
            "v3_report_suppression": "disabled",
            "lookup_mode": "ip",
            "switch_querier": {
                "type": "disabled"
            },
            "v2_fast_leave": "disabled",
            "router_ports_count": 1,
            "active_ports": [
                "Po700",
                "Po858"
            ],
            "groups_count": 0,
            "vlan_vpc_function": "enabled"
        },
        "2141": {
            "ip_igmp_snooping": "enabled",
            "v1v2_report_suppression": "enabled",
            "link_local_groups_suppression": "enabled",
            "v3_report_suppression": "disabled",
            "lookup_mode": "ip",
            "switch_querier": {
                "type": "enabled",
                "ip_address": "XXX.XXX.XXX.XXX",
                "state": "running"
            },
            "v2_fast_leave": "disabled",
            "router_ports_count": 1,
            "groups_count": 0,
            "vlan_vpc_function": "enabled",
            "active_ports": [
                "Po700",
                "Po702",
                "Po858"
            ],
            "report_flooding": "disabled",
            "report_flooding_interfaces": "n/a",
            "group_address_for_proxy_leaves": "no",
            "igmp_querier": {
                "address": "XXX.XXX.XXX.XXX",
                "version": 3,
                "interval": 125,
                "last_member_query_interval": 1,
                "robustness": 2
            }
        }
    }
}