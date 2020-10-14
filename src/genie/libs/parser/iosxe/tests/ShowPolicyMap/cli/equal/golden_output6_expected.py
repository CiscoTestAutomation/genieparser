expected_output = {
    "policy_map": {
        "child": {
            "class": {
                "voice": {
                    "priority": True,
                    "police": {
                        "cir_bps": 8000,
                        "cir_bc_bytes": 9216,
                        "cir_be_bytes": 0,
                        "conform_action": ["transmit"],
                        "exceed_action": ["drop"],
                        "violate_action": ["drop"],
                    },
                },
                "video": {"bandwidth_remaining_percent": 80},
            }
        }
    }
}
