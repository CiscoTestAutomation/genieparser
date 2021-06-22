expected_output = {
    "configuration": {
        "trusted": "yes",
        "validate_address": "yes",
        "validate_prefix": "yes",
        "permit": "link-local",
        "deny": "global-autoconf"
    },
    "device": {
        1: {
            "target": "Twe1/0/42",
            "policy_type": "PORT",
            "policy_name": "test1",
            "feature": "Source guard",
            "tgt_range": "vlan all"
        }
    }
}