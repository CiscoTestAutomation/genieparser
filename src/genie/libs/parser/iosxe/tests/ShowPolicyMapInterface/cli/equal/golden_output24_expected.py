expected_output = {
    "GigabitEthernet0/0/0.2": {
        "service_policy": {
            "output": {
                "policy_name": {
                    "ABC-DEF-GHI-JKL-MNO123123123": {
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
                                "queue_limit_packets": "68",
                                "queueing": True,
                                "rate": {
                                    "drop_rate_bps": 0,
                                    "interval": 30,
                                    "offered_rate_bps": 0,
                                },
                                "shape_bc_bps": 399488,
                                "shape_be_bps": 399488,
                                "shape_cir_bps": 99872000,
                                "shape_type": "average",
                                "target_shape_rate": 99872000,
                                "total_drops": 0,
                                "child_policy_name": {
                                    "ABC-DEF-OPQ-RST-DYNAMIC5-XYZ123123123": {
                                        "class_map": {
                                            "network-control-XYZ123123123": {
                                                "match_evaluation": "match-any",
                                                "packets": 0,
                                                "bytes": 0,
                                                "rate": {
                                                    "interval": 30,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": [
                                                    "access-group name NETWORK-CONTROL-XYZ123123123"
                                                ],
                                                "queueing": True,
                                                "queue_limit_packets": "64",
                                                "queue_depth": 0,
                                                "total_drops": 0,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 0,
                                                "bytes_output": 0,
                                                "bandwidth_percent": 1,
                                                "bandwidth_kbps": 998,
                                                "random_detect": {
                                                    "exp_weight_constant": "9 (1/512)",
                                                    "mean_queue_depth": 0,
                                                    "class": {
                                                        "cs3": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "24",
                                                            "maximum_thresh": "40",
                                                            "mark_prob": "1/10",
                                                        }
                                                    },
                                                },
                                                "qos_set": {
                                                    "cos": {"5": {"packets_marked": 0}}
                                                },
                                            },
                                            "realtime-XYZ123123123": {
                                                "match_evaluation": "match-any",
                                                "packets": 0,
                                                "bytes": 0,
                                                "rate": {
                                                    "interval": 30,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": [
                                                    "ip dscp cs4 (32) af41 (34) af42 (36) af43 (38) cs5 (40) ef"
                                                ],
                                                "qos_set": {
                                                    "cos": {"5": {"packets_marked": 0}}
                                                },
                                            },
                                            "interactive3-XYZ123123123": {
                                                "match_evaluation": "match-any",
                                                "packets": 0,
                                                "bytes": 0,
                                                "rate": {
                                                    "interval": 30,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": [
                                                    "ip dscp cs3 (24) af31 (26) af32 (28) af33 (30)"
                                                ],
                                                "queueing": True,
                                                "queue_limit_packets": "64",
                                                "queue_depth": 0,
                                                "total_drops": 0,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 0,
                                                "bytes_output": 0,
                                                "bandwidth_percent": 5,
                                                "bandwidth_kbps": 4993,
                                                "random_detect": {
                                                    "exp_weight_constant": "9 (1/512)",
                                                    "mean_queue_depth": 0,
                                                    "class": {
                                                        "cs3": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "24",
                                                            "maximum_thresh": "40",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "af31": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "24",
                                                            "maximum_thresh": "40",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "af32": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "24",
                                                            "maximum_thresh": "40",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "af33": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "24",
                                                            "maximum_thresh": "40",
                                                            "mark_prob": "1/10",
                                                        },
                                                    },
                                                },
                                                "qos_set": {
                                                    "cos": {"5": {"packets_marked": 0}}
                                                },
                                            },
                                            "interactive21-XYZ123123123": {
                                                "match_evaluation": "match-any",
                                                "packets": 0,
                                                "bytes": 0,
                                                "rate": {
                                                    "interval": 30,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": [
                                                    "ip dscp cs2 (16) af21 (18) af22 (20) af23 (22)"
                                                ],
                                                "queueing": True,
                                                "queue_limit_packets": "64",
                                                "queue_depth": 0,
                                                "total_drops": 0,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 0,
                                                "bytes_output": 0,
                                                "bandwidth_percent": 5,
                                                "bandwidth_kbps": 4993,
                                                "random_detect": {
                                                    "exp_weight_constant": "9 (1/512)",
                                                    "mean_queue_depth": 0,
                                                    "class": {
                                                        "cs2": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "24",
                                                            "maximum_thresh": "40",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "af21": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "24",
                                                            "maximum_thresh": "40",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "af22": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "24",
                                                            "maximum_thresh": "40",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "af23": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "24",
                                                            "maximum_thresh": "40",
                                                            "mark_prob": "1/10",
                                                        },
                                                    },
                                                },
                                                "qos_set": {
                                                    "cos": {"5": {"packets_marked": 0}}
                                                },
                                            },
                                            "besteffort-XYZ123123123": {
                                                "match_evaluation": "match-any",
                                                "packets": 0,
                                                "bytes": 0,
                                                "rate": {
                                                    "interval": 30,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": ["ip dscp cs1 (8)"],
                                                "queueing": True,
                                                "queue_limit_packets": "64",
                                                "queue_depth": 0,
                                                "total_drops": 0,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 0,
                                                "bytes_output": 0,
                                                "bandwidth_percent": 1,
                                                "bandwidth_kbps": 998,
                                                "random_detect": {
                                                    "exp_weight_constant": "9 (1/512)",
                                                    "mean_queue_depth": 0,
                                                },
                                                "qos_set": {
                                                    "cos": {"5": {"packets_marked": 0}}
                                                },
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
                                                "queueing": True,
                                                "queue_limit_packets": "64",
                                                "pkts_output": 0,
                                                "bytes_output": 0,
                                                "bandwidth_percent": 58,
                                                "bandwidth_kbps": 57925,
                                                "random_detect": {
                                                    "exp_weight_constant": "9 (1/512)",
                                                    "mean_queue_depth": 0,
                                                    "class": {
                                                        "default": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "24",
                                                            "maximum_thresh": "40",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "af11": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "24",
                                                            "maximum_thresh": "40",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "af12": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "24",
                                                            "maximum_thresh": "40",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "af13": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "24",
                                                            "maximum_thresh": "40",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "cs6": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "24",
                                                            "maximum_thresh": "40",
                                                            "mark_prob": "1/10",
                                                        },
                                                        "cs7": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "24",
                                                            "maximum_thresh": "40",
                                                            "mark_prob": "1/10",
                                                        },
                                                    },
                                                },
                                                "qos_set": {
                                                    "cos": {"5": {"packets_marked": 0}}
                                                },
                                                "fair_queue_limit_per_flow": 16,
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
