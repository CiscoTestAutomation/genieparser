expected_output = {
    "policy_map": {
        "parent-policy": {
            "class": {
                "class-default": {
                    "police": {
                        "cir_bps": 50000,
                        "cir_bc_bytes": 3000,
                        "cir_be_bytes": 3000,
                        "conform_color": "hipri-conform",
                        "conform_action": ["transmit"],
                        "exceed_action": ["transmit"],
                        "violate_action": ["drop"],
                        "service_policy": "child-policy",
                    }
                }
            }
        },
        "police": {
            "class": {
                "prec1": {"priority_level": {"1": {"kbps": 20000}}},
                "prec2": {"bandwidth_kbps": 20000},
                "class-default": {"bandwidth_kbps": 20000},
            }
        },
        "child-policy": {
            "class": {
                "user1-acl-child": {
                    "police": {
                        "cir_bps": 10000,
                        "cir_bc_bytes": 1500,
                        "conform_action": ["set-qos-transmit 5"],
                        "exceed_action": ["drop"],
                    }
                },
                "user2-acl-child": {
                    "police": {
                        "cir_bps": 20000,
                        "cir_bc_bytes": 1500,
                        "conform_action": ["set-qos-transmit 5"],
                        "exceed_action": ["drop"],
                    }
                },
                "class-default": {
                    "police": {
                        "cir_bps": 50000,
                        "cir_bc_bytes": 1500,
                        "conform_action": ["transmit"],
                        "exceed_action": ["drop"],
                    }
                },
            }
        },
    }
}
