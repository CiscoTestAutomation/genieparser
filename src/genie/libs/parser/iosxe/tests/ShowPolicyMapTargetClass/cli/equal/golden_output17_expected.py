expected_output = {
    "GigabitEthernet9/5": {
        "service_group": 1,
        "service_policy": {
            "input": {
                "policy_name": {
                    "policy1": {
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
                                "police": {
                                    "cir_bps": 200000,
                                    "cir_bc_bytes": 6250,
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"transmit": True},
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                },
                            }
                        }
                    }
                }
            },
            "output": {
                "policy_name": {
                    "policy2": {
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
                                "queueing": True,
                                "queue_limit_packets": "131072",
                                "queue_depth": 0,
                                "total_drops": 0,
                                "no_buffer_drops": 0,
                                "pkts_output": 0,
                                "bytes_output": 0,
                                "bandwidth_remaining_ratio": 2,
                            }
                        }
                    }
                }
            },
        },
    }
}
