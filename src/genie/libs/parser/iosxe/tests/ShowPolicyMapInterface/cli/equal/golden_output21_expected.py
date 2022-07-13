expected_output = {
    "GigabitEthernet4.1": {
        "service_policy": {
            "output": {
                "policy_name": {
                    "parent-policy": {
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
                                "child_policy_name": {
                                    "child-policy": {
                                        "class_map": {
                                            "high-priority": {
                                                "match_evaluation": "match-all",
                                                "packets": 0,
                                                "bytes": 0,
                                                "rate": {
                                                    "interval": 300,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": ["none"],
                                            },
                                            "low-priority": {
                                                "match_evaluation": "match-all",
                                                "packets": 0,
                                                "bytes": 0,
                                                "rate": {
                                                    "interval": 300,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": ["none"],
                                            },
                                            "band-policy": {
                                                "match_evaluation": "match-all",
                                                "packets": 0,
                                                "bytes": 0,
                                                "rate": {
                                                    "interval": 300,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": ["none"],
                                                "queueing": True,
                                                "queue_limit_packets": "64",
                                                "queue_depth": 0,
                                                "total_drops": 0,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 0,
                                                "bytes_output": 0,
                                                "bandwidth_kbps": 110000,
                                            },
                                            "test-cir": {
                                                "match_evaluation": "match-all",
                                                "packets": 0,
                                                "bytes": 0,
                                                "rate": {
                                                    "interval": 300,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": ["none"],
                                                "queueing": True,
                                                "queue_limit_packets": "64",
                                                "queue_depth": 0,
                                                "total_drops": 0,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 0,
                                                "bytes_output": 0,
                                                "bandwidth_kbps": 600000,
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
                                                "queue_limit_packets": "100",
                                                "queue_depth": 0,
                                                "total_drops": 0,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 0,
                                                "bytes_output": 0,
                                                "random_detect": {
                                                    "exp_weight_constant": "4 (1/16)",
                                                    "mean_queue_depth": 0,
                                                    "class": {
                                                        "0": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "25",
                                                            "maximum_thresh": "50",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "1": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "50",
                                                            "maximum_thresh": "70",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "2": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "80",
                                                            "maximum_thresh": "100",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "3": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "80",
                                                            "maximum_thresh": "100",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "4": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "80",
                                                            "maximum_thresh": "100",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "5": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "80",
                                                            "maximum_thresh": "100",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "6": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "80",
                                                            "maximum_thresh": "100",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "7": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "25",
                                                            "maximum_thresh": "50",
                                                            "mark_prob": "1/10",
                                                        },
                                                    },
                                                },
                                            },
                                        }
                                    }
                                },
                            }
                        },
                        "queue_stats_for_all_priority_classes": {
                            "priority_level": {
                                "default": {
                                    "queueing": True,
                                    "queue_limit_packets": "512",
                                    "queue_depth": 0,
                                    "total_drops": 0,
                                    "no_buffer_drops": 0,
                                    "pkts_output": 0,
                                    "bytes_output": 0,
                                }
                            }
                        },
                    }
                }
            }
        }
    }
}
