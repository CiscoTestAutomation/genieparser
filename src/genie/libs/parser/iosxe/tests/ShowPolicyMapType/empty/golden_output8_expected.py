expected_output = {
    "TenGigabitEthernet0/0/2": {
        "service_policy": {
            "output": {
                "policy_name": {
                    "shape_priority": {
                        "queue_stats_for_all_priority_classes": {
                            "priority_level": {
                                "1": {
                                    "queueing": True,
                                    "queue_limit_us": 3932,
                                    "queue_limit_bytes": 49152,
                                    "queue_depth": 49476,
                                    "total_drops": 44577300,
                                    "no_buffer_drops": 0,
                                    "pkts_output": 2348138,
                                    "bytes_output": 1202246656,
                                },
                                "2": {
                                    "queueing": True,
                                    "queue_limit_us": 1966,
                                    "queue_limit_bytes": 49152,
                                    "queue_depth": 51072,
                                    "total_drops": 42228358,
                                    "no_buffer_drops": 0,
                                    "pkts_output": 4697080,
                                    "bytes_output": 2404904960,
                                },
                            }
                        },
                        "class_map": {
                            "class_priority": {
                                "match_evaluation": "match-any",
                                "packets": 46925438,
                                "bytes": 24025824256,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 1871849000,
                                    "drop_rate_bps": 1778171000,
                                },
                                "match": ["cos  1", "cos  2"],
                                "priority": {
                                    "percent": 10,
                                    "kbps": 100000,
                                    "burst_bytes": 2500000,
                                    "exceed_drops": 44577300,
                                },
                                "priority_level": 1,
                            },
                            "class_priority_level2": {
                                "match_evaluation": "match-any",
                                "packets": 46925438,
                                "bytes": 24025824256,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 1871849000,
                                    "drop_rate_bps": 1684485000,
                                },
                                "match": ["cos  3", "cos  4"],
                                "priority": {
                                    "percent": 20,
                                    "kbps": 200000,
                                    "burst_bytes": 5000000,
                                    "exceed_drops": 42228358,
                                },
                                "priority_level": 2,
                            },
                            "class_bw": {
                                "match_evaluation": "match-any",
                                "packets": 23462719,
                                "bytes": 12012912128,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 935925000,
                                    "drop_rate_bps": 281045000,
                                },
                                "match": ["cos  5"],
                                "queueing": True,
                                "queue_limit_us": 393,
                                "queue_limit_bytes": 49152,
                                "queue_depth": 49476,
                                "total_drops": 7045085,
                                "no_buffer_drops": 0,
                                "pkts_output": 16417634,
                                "bytes_output": 8405828608,
                                "bandwidth_remaining_percent": 70,
                            },
                            "class-default": {
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["any"],
                                "queue_limit_us": 393,
                                "queue_limit_bytes": 49152,
                                "queue_depth": 0,
                                "total_drops": 0,
                                "no_buffer_drops": 0,
                                "pkts_output": 0,
                                "bytes_output": 0,
                            },
                        },
                    }
                }
            }
        }
    }
}
