expected_output = {
    "policy_map": {
        "map1": {
            "class": {
                "cs1": {
                    "police": {
                        "rate": 10000000000,
                        "conform_action": ["transmit"],
                        "exceed_action": ["drop"],
                    }
                },
                "cs2": {
                    "police": {
                        "rate": 10000000000,
                        "conform_action": ["transmit"],
                        "exceed_action": ["drop"],
                    }
                }
            }
        }
    }
}
