expected_output = {
    "GigabitEthernet4.1": {
        "service_policy": {
            "output": {
                "policy_name": {
                    "parent-policy": {
                        "child_policy_name": {
                            "child-policy": {
                                "class_map": {
                                    "band-policy": {
                                        "bandwidth_kbps": 110000,
                                        "bytes": 0,
                                        "bytes_output": 0,
                                        "match": ["none"],
                                        "match_evaluation": "match-all",
                                        "no_buffer_drops": 0,
                                        "packets": 0,
                                        "pkts_output": 0,
                                        "queue_depth": 0,
                                        "queue_limit_packets": "64",
                                        "queueing": True,
                                        "rate": {
                                            "drop_rate_bps": 0,
                                            "interval": 300,
                                            "offered_rate_bps": 0,
                                        },
                                        "total_drops": 0,
                                    },
                                    "class-default": {
                                        "bytes": 0,
                                        "bytes_output": 0,
                                        "match": ["any"],
                                        "match_evaluation": "match-any",
                                        "no_buffer_drops": 0,
                                        "packets": 0,
                                        "pkts_output": 0,
                                        "queue_depth": 0,
                                        "queue_limit_packets": "100",
                                        "random_detect": {
                                            "exp_weight_constant": "4 (1/16)",
                                            "mean_queue_depth": 0,
                                        },
                                        "rate": {
                                            "drop_rate_bps": 0,
                                            "interval": 300,
                                            "offered_rate_bps": 0,
                                        },
                                        "total_drops": 0,
                                    },
                                    "high-priority": {
                                        "bytes": 0,
                                        "match": ["none"],
                                        "match_evaluation": "match-all",
                                        "packets": 0,
                                        "rate": {
                                            "drop_rate_bps": 0,
                                            "interval": 300,
                                            "offered_rate_bps": 0,
                                        },
                                    },
                                    "low-priority": {
                                        "bytes": 0,
                                        "match": ["none"],
                                        "match_evaluation": "match-all",
                                        "packets": 0,
                                        "rate": {
                                            "drop_rate_bps": 0,
                                            "interval": 300,
                                            "offered_rate_bps": 0,
                                        },
                                    },
                                    "test-cir": {
                                        "bandwidth_kbps": 600000,
                                        "bytes": 0,
                                        "bytes_output": 0,
                                        "match": ["none"],
                                        "match_evaluation": "match-all",
                                        "no_buffer_drops": 0,
                                        "packets": 0,
                                        "pkts_output": 0,
                                        "queue_depth": 0,
                                        "queue_limit_packets": "64",
                                        "queueing": True,
                                        "rate": {
                                            "drop_rate_bps": 0,
                                            "interval": 300,
                                            "offered_rate_bps": 0,
                                        },
                                        "total_drops": 0,
                                    },
                                },
                                "queue_stats_for_all_priority_classes": {
                                    "priority_level": {
                                        "default": {
                                            "queueing": True,
                                            "queue_limit_packets": "512",
                                            "bytes_output": 0,
                                            "no_buffer_drops": 0,
                                            "pkts_output": 0,
                                            "queue_depth": 0,
                                            "total_drops": 0,
                                        }
                                    }
                                },
                            }
                        },
                        "class_map": {
                            "class-default": {
                                "bytes": 0,
                                "bytes_output": 0,
                                "match": ["any"],
                                "match_evaluation": "match-any",
                                "no_buffer_drops": 0,
                                "packets": 0,
                                "pkts_output": 0,
                                "queue_depth": 0,
                                "queue_limit_packets": "34",
                                "queueing": True,
                                "rate": {
                                    "drop_rate_bps": 0,
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                },
                                "shape_bc_bps": 21000000,
                                "shape_be_bps": 21000000,
                                "shape_cir_bps": 1000000000,
                                "shape_type": "average",
                                "target_shape_rate": 3000000000,
                                "total_drops": 0,
                            }
                        },
                    }
                }
            }
        }
    }
}
