expected_output = {
    "Port-channel1": {
        "service_group": 1,
        "service_policy": {
            "output": {
                "policy_name": {
                    "VLAN51_QoS": {
                        "class_map": {
                            "VLAN51_QoS": {
                                "match_evaluation": "match-all",
                                "packets": 30,
                                "bytes": 13638,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 1000,
                                    "drop_rate_bps": 1000,
                                },
                                "match": ["access-group name VLAN51_QoS"],
                                "police": {
                                    "cir_bps": 8000,
                                    "cir_bc_bytes": 1000,
                                    "conformed": {
                                        "packets": 22,
                                        "bytes": 1494,
                                        "actions": {"transmit": True},
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 8,
                                        "bytes": 12144,
                                        "actions": {"drop": True},
                                        "bps": 1000,
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
        },
    }
}
