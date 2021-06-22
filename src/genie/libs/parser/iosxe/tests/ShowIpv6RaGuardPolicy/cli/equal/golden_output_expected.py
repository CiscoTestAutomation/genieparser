expected_output = {
    "configuration": {
        "trusted_port": "yes",
        "device_role": "router",
        "min_hop_limit": 1,
        "max_hop_limit": 3,
        "managed_config_flag": "on",
        "other_config_flag": "on",
        "max_router_preference": "high",
        "match_ra_prefix": "bar",
        "match_ipv6_access_list": "foo"
    },
    "device": {
        1: {
            "target": "Twe1/0/42",
            "policy_type": "PORT",
            "policy_name": "asdf",
            "feature": "RA guard",
            "tgt_range": "vlan all"
        }
    }
}