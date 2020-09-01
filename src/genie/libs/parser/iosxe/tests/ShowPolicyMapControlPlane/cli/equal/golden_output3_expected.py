expected_output = {
    "Control Plane": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "control-plane-in": {
                        "class_map": {
                            "telnet-class": {
                                "match_evaluation": "match-all",
                                "packets": 10521,
                                "bytes": 673344,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 18000,
                                    "drop_rate_bps": 15000,
                                },
                                "match": ["access-group 102"],
                                "police": {
                                    "cir_bps": 64000,
                                    "cir_bc_bytes": 8000,
                                    "conformed": {
                                        "packets": 1430,
                                        "bytes": 91520,
                                        "actions": {"transmit": True},
                                        "bps": 2000,
                                    },
                                    "exceeded": {
                                        "packets": 9091,
                                        "bytes": 581824,
                                        "actions": {"drop": True},
                                        "bps": 15000,
                                    },
                                },
                            },
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
                            },
                        }
                    }
                }
            }
        }
    }
}
