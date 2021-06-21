expected_output = {
    "configuration": {
        "trusted_port": "yes",
        "security_level": "guard",
        "device_role": "node",
        "data_glean": "log-only",
        "prefix_glean": "only",
        "limit_address_count": {
            "ipv4": 5,
            "ipv6": 1
        },
        "cache_guard": "ipv4"
    },
    "device": {
        1: {
            "target": "Twe1/0/42",
            "policy_type": "PORT",
            "policy_name": "test",
            "feature": "Device-tracking",
            "tgt_range": "vlan all"
        }
    }
}