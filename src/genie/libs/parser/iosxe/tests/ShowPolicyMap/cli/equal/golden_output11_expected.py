expected_output = {
    "policy_map": {
        "pm_hier2_child_0_2": {
            "class": {
                "cm_0": {
                    "priority_levels": 1,
                    "police": {
                        "cir_percent": 5,
                        "bc_ms": 2,
                        "be_ms": 0,
                        "conform_action": ["transmit"],
                        "exceed_action": ["drop"],
                        "violate_action": ["drop"],
                    },
                    "queue_limit_packets": 77,
                },
                "cm_1": {
                    "average_rate_traffic_shaping": True,
                    "cir_percent": 80,
                    "bandwidth_remaining_ratio": 80,
                },
                "class-default": {
                    "average_rate_traffic_shaping": True,
                    "cir_percent": 50,
                    "bandwidth_remaining_ratio": 20,
                },
            }
        }
    }
}
