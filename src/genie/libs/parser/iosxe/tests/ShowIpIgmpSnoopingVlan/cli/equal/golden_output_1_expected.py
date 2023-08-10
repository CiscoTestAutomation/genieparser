expected_output = {
    "igmp_snooping": "Enabled",
    "global_pim_snooping": "Disabled",
    "igmpv3_snooping": "Enabled",
    "report_supression": "Enabled",
    "tcn_solicit_query": "Disabled",
    "tcn_flood_query_count": 2,
    "robustness_variable": 2,
    "last_member_query_count": 2,
    "last_member_query_interval": 1000,
    "vlan": {
        "666": {
            "igmp_snooping": "Enabled",
            "pim_snooping": "Disabled",
            "igmpv2_immediate_leave": "Disabled",
            "explicit_host_tracking": "Enabled",
            "multicast_router_learning_mode": "pim-dvmrp",
            "cgmp_inter_mode": "IGMP_ONLY",
            "robustness_variable": 2,
            "last_member_query_count": 2,
            "last_member_query_interval": 1000,
        }
    },
}
