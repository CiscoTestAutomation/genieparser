expected_output = {
    "indexes":{
        1:{
            "policy_name":"default",
            "policy_groups": ["DEFAULT_DENY_v6"]
        },
        2:{
            "src_grp_name":"Unknown",
            "dst_group_id":100,
            "policy_groups": ["SGACL_PERMIT_IPv6"]
        },
        3:{
            "src_grp_name":"Unknown",
            "dst_group_id":200,
            "policy_groups": ["SGACL_PERMIT_IPv6"]
        },
        4:{
            "src_grp_id":100,
            "dst_group_id":200,
            "policy_groups": ["SGACL_PERMIT_IPv6"]
        },
        "monitor_dynamic":False,
        "monitor_configured":False
    }
}