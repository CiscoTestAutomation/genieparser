expected_output = {
    "policy_map": {
        "PHB": {
            "class": {
                "cos1": {
                    "police": {
                        "cir_bc_bytes": 8000,
                        "cir_bps": 200000,
                        "conform_action": ["transmit"],
                        "exceed_action": ["drop"],
                    },
                    "priority": True,
                },
                "cos2": {"bandwidth_kbps": 100, "bandwidth_remaining_percent": 40},
                "cos3": {"bandwidth_kbps": 200, "bandwidth_remaining_percent": 50},
            }
        },
        "ingress_policy": {"class": {"cos3": {"set": "cos 5"}}},
        "egress policy": {"class": {"cos5": {"shape_average_min": 30}}},
    }
}
