expected_output = {
    "GigabitEthernet0/0/0.2": {
        "service_policy": {
            "output": {
                "policy_name": {
                    "ABC-DEF-GHI-JKL-MNO123123123": {
                        "child_policy_name": {
                            "ABC-DEF-OPQ-RST-DYNAMIC5-XYZ123123123": {
                                "class_map": {
                                    "besteffort-XYZ123123123": {
                                        "bandwidth_kbps": 998,
                                        "bandwidth_percent": 1,
                                        "bytes": 0,
                                        "bytes_output": 0,
                                        "match": ["ip dscp cs1 (8)"],
                                        "match_evaluation": "match-any",
                                        "no_buffer_drops": 0,
                                        "packets": 0,
                                        "pkts_output": 0,
                                        "qos_set": {
                                            "cos": {"5": {"packets_marked": 0}}
                                        },
                                        "queue_depth": 0,
                                        "queue_limit_packets": "64",
                                        "queueing": True,
                                        "random_detect": {
                                            "exp_weight_constant": "9 (1/512)",
                                            "mean_queue_depth": 0,
                                        },
                                        "rate": {
                                            "drop_rate_bps": 0,
                                            "interval": 30,
                                            "offered_rate_bps": 0,
                                        },
                                        "total_drops": 0,
                                    },
                                    "class-default": {
                                        "bandwidth_kbps": 57925,
                                        "bandwidth_percent": 58,
                                        "bytes": 0,
                                        "bytes_output": 0,
                                        "match": ["any"],
                                        "match_evaluation": "match-any",
                                        "packets": 0,
                                        "pkts_output": 0,
                                        "qos_set": {
                                            "cos": {"5": {"packets_marked": 0}}
                                        },
                                        "queue_limit_packets": "64",
                                        "queueing": True,
                                        "random_detect": {
                                            "exp_weight_constant": "9 (1/512)",
                                            "mean_queue_depth": 0,
                                        },
                                        "rate": {
                                            "drop_rate_bps": 0,
                                            "interval": 30,
                                            "offered_rate_bps": 0,
                                        },
                                    },
                                    "interactive21-XYZ123123123": {
                                        "bandwidth_kbps": 4993,
                                        "bandwidth_percent": 5,
                                        "bytes": 0,
                                        "bytes_output": 0,
                                        "match": [
                                            "ip dscp cs2 (16) af21 (18) af22 (20) af23 (22)"
                                        ],
                                        "match_evaluation": "match-any",
                                        "no_buffer_drops": 0,
                                        "packets": 0,
                                        "pkts_output": 0,
                                        "qos_set": {
                                            "cos": {"5": {"packets_marked": 0}}
                                        },
                                        "queue_depth": 0,
                                        "queue_limit_packets": "64",
                                        "queueing": True,
                                        "random_detect": {
                                            "exp_weight_constant": "9 (1/512)",
                                            "mean_queue_depth": 0,
                                        },
                                        "rate": {
                                            "drop_rate_bps": 0,
                                            "interval": 30,
                                            "offered_rate_bps": 0,
                                        },
                                        "total_drops": 0,
                                    },
                                    "interactive3-XYZ123123123": {
                                        "bandwidth_kbps": 4993,
                                        "bandwidth_percent": 5,
                                        "bytes": 0,
                                        "bytes_output": 0,
                                        "match": [
                                            "ip dscp cs3 (24) af31 (26) af32 (28) af33 (30)"
                                        ],
                                        "match_evaluation": "match-any",
                                        "no_buffer_drops": 0,
                                        "packets": 0,
                                        "pkts_output": 0,
                                        "qos_set": {
                                            "cos": {"5": {"packets_marked": 0}}
                                        },
                                        "queue_depth": 0,
                                        "queue_limit_packets": "64",
                                        "queueing": True,
                                        "random_detect": {
                                            "exp_weight_constant": "9 (1/512)",
                                            "mean_queue_depth": 0,
                                        },
                                        "rate": {
                                            "drop_rate_bps": 0,
                                            "interval": 30,
                                            "offered_rate_bps": 0,
                                        },
                                        "total_drops": 0,
                                    },
                                    "network-control-XYZ123123123": {
                                        "bandwidth_kbps": 998,
                                        "bandwidth_percent": 1,
                                        "bytes": 0,
                                        "bytes_output": 0,
                                        "match": [
                                            "access-group name NETWORK-CONTROL-XYZ123123123"
                                        ],
                                        "match_evaluation": "match-any",
                                        "no_buffer_drops": 0,
                                        "packets": 0,
                                        "pkts_output": 0,
                                        "qos_set": {
                                            "cos": {"5": {"packets_marked": 0}}
                                        },
                                        "queue_depth": 0,
                                        "queue_limit_packets": "64",
                                        "queueing": True,
                                        "random_detect": {
                                            "exp_weight_constant": "9 (1/512)",
                                            "mean_queue_depth": 0,
                                        },
                                        "rate": {
                                            "drop_rate_bps": 0,
                                            "interval": 30,
                                            "offered_rate_bps": 0,
                                        },
                                        "total_drops": 0,
                                    },
                                    "realtime-XYZ123123123": {
                                        "bytes": 0,
                                        "match": [
                                            "ip dscp cs4 (32) af41 (34) af42 (36) af43 (38) cs5 (40) ef"
                                        ],
                                        "match_evaluation": "match-any",
                                        "packets": 0,
                                        "qos_set": {
                                            "cos": {"5": {"packets_marked": 0}}
                                        },
                                        "rate": {
                                            "drop_rate_bps": 0,
                                            "interval": 30,
                                            "offered_rate_bps": 0,
                                        },
                                    },
                                },
                                "queue_stats_for_all_priority_classes": {
                                    "priority_level": {
                                        "default": {
                                            "bytes_output": 0,
                                            "no_buffer_drops": 0,
                                            "pkts_output": 0,
                                            "queue_depth": 0,
                                            "queue_limit_packets": "512",
                                            "queueing": True,
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
                            }
                        },
                    }
                }
            }
        }
    }
}
