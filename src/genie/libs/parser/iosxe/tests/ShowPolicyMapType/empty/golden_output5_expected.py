expected_output = {
    "GigabitEthernet0/0/0": {
        "service_policy": {
            "output": {
                "policy_name": {
                    "CORE-Out": {
                        "class_map": {
                            "EXP0": {
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {"interval": 300, "offered_rate_bps": 0},
                                "match": ["mpls experimental topmost 0"],
                            },
                            "EXP1": {
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {"interval": 300, "offered_rate_bps": 0},
                                "match": ["mpls experimental topmost 1"],
                            },
                            "EXP2": {
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {"interval": 300, "offered_rate_bps": 0},
                                "match": ["mpls experimental topmost 2"],
                            },
                            "EXP3": {
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {"interval": 300, "offered_rate_bps": 0},
                                "match": ["mpls experimental topmost 3"],
                            },
                            "EXP4": {
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {"interval": 300, "offered_rate_bps": 0},
                                "match": ["mpls experimental topmost 4"],
                            },
                            "EXP5": {
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {"interval": 300, "offered_rate_bps": 0},
                                "match": ["mpls experimental topmost 5"],
                            },
                            "EXP6": {
                                "match_evaluation": "match-all",
                                "packets": 27,
                                "bytes": 1869,
                                "rate": {"interval": 300, "offered_rate_bps": 0},
                                "match": ["mpls experimental topmost 6"],
                            },
                            "EXP7": {
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {"interval": 300, "offered_rate_bps": 0},
                                "match": ["mpls experimental topmost 7"],
                            },
                            "class-default": {
                                "match_evaluation": "match-any",
                                "packets": 193,
                                "bytes": 19600,
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
