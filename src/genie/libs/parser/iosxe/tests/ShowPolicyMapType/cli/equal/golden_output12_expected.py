expected_output = {
    "GigabitEthernet0/1/4": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "police-in": {
                        "class_map": {
                            "class-default": {
                                "bytes": 0,
                                "match": ["any"],
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "police": {
                                    "cir_bc_bytes": 83619,
                                    "cir_bps": 445500,
                                    "conformed": {
                                        "actions": {"transmit": True},
                                        "bps": 0,
                                        "bytes": 0,
                                        "packets": 0,
                                    },
                                    "exceeded": {
                                        "actions": {"drop": True},
                                        "bps": 0,
                                        "bytes": 0,
                                        "packets": 0,
                                    },
                                },
                                "rate": {
                                    "drop_rate_bps": 0,
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                },
                            }
                        }
                    }
                }
            }
        }
    }
}
