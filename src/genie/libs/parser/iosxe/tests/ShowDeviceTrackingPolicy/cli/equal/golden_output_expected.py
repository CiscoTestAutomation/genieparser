expected_output = {
    "configuration": {
        "trusted_port": "yes",
        "security_level": "guard",
        "device_role": "node",
        "data_glean": "log-only",
        "destination_glean": "log-only",
        "prefix_glean": "only",
        "nd": {
            "is_gleaning": "gleaning",
            "protecting_prefix_list": "qux"
        },
        "dhcp6": {
            "is_gleaning": "gleaning",
            "protecting_prefix_list": "baz"
        },
        "arp": {
            "is_gleaning": "gleaning",
            "protecting_prefix_list": "foo"
        },
        "dhcp4": {
            "is_gleaning": "gleaning",
            "protecting_prefix_list": "bar"
        },
        "protocol_unkn": {
            "is_gleaning": "gleaning",
            "protecting_prefix_list": "quux"
        },
        "limit_address_count": {
            "ipv4": 5,
            "ipv6": 1
        },
        "cache_guard": "ipv4",
        "origin": "fabric",
        "tracking": "enable"
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