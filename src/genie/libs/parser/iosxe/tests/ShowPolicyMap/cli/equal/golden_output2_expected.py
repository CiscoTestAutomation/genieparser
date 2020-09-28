expected_output = {
    "policy_map": {
        "police-in": {
            "class": {
                "class-default": {
                    "police": {
                        "rate_percent": 10,
                        "conform_action": ["transmit"],
                        "exceed_action": ["drop"],
                    }
                }
            }
        }
    }
}
