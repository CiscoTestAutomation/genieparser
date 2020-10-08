expected_output = {
    "GigabitEthernet0/0/1": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "TEST": {
                        "class_map": {
                            "class-default": {
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["any"],
                            }
                        }
                    }
                }
            }
        }
    }
}
