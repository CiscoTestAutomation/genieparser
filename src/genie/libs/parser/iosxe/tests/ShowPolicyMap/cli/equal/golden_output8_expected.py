expected_output = {
    "policy_map": {
        "policy1": {
            "class": {
                "class1": {
                    "police": {
                        "cir_percent": 20,
                        "bc_ms": 300,
                        "pir_percent": 40,
                        "be_ms": 400,
                        "conform_action": ["transmit"],
                        "exceed_action": ["drop"],
                        "violate_action": ["drop"],
                    }
                }
            }
        }
    }
}
