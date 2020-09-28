expected_output = {
    "policy_map": {
        "parent": {
            "class": {
                "class-default": {
                    "average_rate_traffic_shaping": True,
                    "cir_bps": 10000000,
                    "service_policy": "child",
                }
            }
        }
    }
}
