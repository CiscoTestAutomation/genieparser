expected_output = {
    "indexes":{
        1:{
            "policy_name":"default",
            "policy_groups": ["DEFAULT_DENY_v4"]
        },
        2:{
            "src_grp_name":"Unknown",
            "dst_group_id":100,
            "policy_groups": ["SGACL_PERMIT_IPv4"]
        },
        3:{
            "src_grp_name":"Unknown",
            "dst_group_id":200,
            "policy_groups": ["SGACL_PERMIT_IPv4"]
        },
        4:{
            "src_grp_id":100,
            "dst_group_id":200,
            "policy_groups": ["SGACL_PERMIT_IPv4"]
        },
        "monitor_dynamic":False,
        "monitor_configured":False
    }
}