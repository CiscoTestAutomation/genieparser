expected_output = {
    "Control Plane": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "TEST": {
                        "class_map": {
                            "TEST": {
                                "match_evaluation": "match-all",
                                "packets": 20,
                                "bytes": 11280,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["access-group 101"],
                                "police": {
                                    "police_bps": 8000,
                                    "police_limit": 1500,
                                    "extended_limit": 1500,
                                    "conformed": {
                                        "packets": 15,
                                        "bytes": 6210,
                                        "actions": {"transmit": True},
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 5,
                                        "bytes": 5070,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                    "violated": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                },
                            },
                            "class-default": {
                                "match_evaluation": "match-any",
                                "packets": 105325,
                                "bytes": 11415151,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["any"],
                            },
                        }
                    }
                }
            }
        }
    }
}
