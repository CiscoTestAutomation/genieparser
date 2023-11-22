expected_output = {
    "GigabitEthernet0/0/3.3001": {
        "service_policy": {
            "output": {
                "policy_name": {
                    "policy1": {
                        "class_map": {
                            "class-default": {
                                "match_evaluation": "match-any",
                                "packets": 3275598,
                                "bytes": 362268259,
                                "rate": {
                                    "interval": 60,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["any"],
                                "queueing": True,
                                "queue_limit_packets": "208",
                                "queue_depth": 0,
                                "total_drops": 0,
                                "no_buffer_drops": 0,
                                "pkts_output": 3022920,
                                "bytes_output": 263471161,
                                "bandwidth_remaining_ratio": 1,
                                "overhead_accounting": "Enabled",
                                "shape_type": "average",
                                "shape_cir_bps": 50000000,
                                "shape_bc_bps": 200000,
                                "shape_be_bps": 200000,
                                "target_shape_rate": 50000000,
                                "child_policy_name": {
                                    "policy2": {
                                        "class_map": {
                                            "cm1": {
                                                "match_evaluation": "match-any",
                                                "packets": 3000453,
                                                "bytes": 262033259,
                                                "rate": {
                                                    "interval": 60,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": [
                                                    "access-group name accssgroup1"
                                                ],
                                                "queueing": True,
                                                "queue_limit_bytes": 525000,
                                                "queue_depth": 0,
                                                "total_drops": 0,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 3000454,
                                                "bytes_output": 262033337,
                                                "bandwidth_remaining_percent": 1,
                                                "overhead_accounting": "enabled",
                                                "random_detect": {
                                                    "exp_weight_constant": "9 (1/512)",
                                                    "mean_queue_depth": 94,
                                                    "class": {
                                                        "cs6": {
                                                            "transmitted_packets": "3000454",
                                                            "transmitted_bytes": "262033337",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "225750",
                                                            "maximum_thresh": "262500",
                                                            "mark_prob": "1/10",
                                                        }
                                                    },
                                                },
                                                "qos_set": {
                                                    "dscp": {
                                                        "cs6": {
                                                            "marker_statistics": "Disabled"
                                                        }
                                                    }
                                                },
                                            },
                                            "cm2": {
                                                "match_evaluation": "match-any",
                                                "packets": 0,
                                                "bytes": 0,
                                                "rate": {
                                                    "interval": 60,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": ["dscp af41 (34) af42 (36)"],
                                                "queueing": True,
                                                "queue_limit_bytes": 312500,
                                                "queue_depth": 0,
                                                "total_drops": 0,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 0,
                                                "bytes_output": 0,
                                                "bandwidth_remaining_percent": 25,
                                                "overhead_accounting": "enabled",
                                                "qos_set": {
                                                    "dscp": {
                                                        "af41": {
                                                            "marker_statistics": "Disabled"
                                                        }
                                                    }
                                                },
                                            },
                                            "cm3": {
                                                "match_evaluation": "match-any",
                                                "packets": 0,
                                                "bytes": 0,
                                                "rate": {
                                                    "interval": 60,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": [
                                                    "ip dscp af31 (26) af32 (28)",
                                                    "dscp af31 (26) af32 (28)",
                                                ],
                                                "queueing": True,
                                                "queue_limit_bytes": 312500,
                                                "queue_depth": 0,
                                                "total_drops": 0,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 0,
                                                "bytes_output": 0,
                                                "bandwidth_remaining_percent": 10,
                                                "overhead_accounting": "enabled",
                                                "random_detect": {
                                                    "exp_weight_constant": "9 (1/512)",
                                                    "mean_queue_depth": 0,
                                                    "class": {
                                                        "af31": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "134375",
                                                            "maximum_thresh": "156250",
                                                            "mark_prob": "1/10",
                                                        }
                                                    },
                                                },
                                                "qos_set": {
                                                    "dscp": {
                                                        "af31": {
                                                            "marker_statistics": "Disabled"
                                                        }
                                                    }
                                                },
                                            },
                                            "cm4": {
                                                "match_evaluation": "match-any",
                                                "packets": 0,
                                                "bytes": 0,
                                                "rate": {
                                                    "interval": 60,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": [
                                                    "ip dscp af21 (18) af22 (20)",
                                                    "dscp af21 (18) af22 (20)",
                                                ],
                                                "queueing": True,
                                                "queue_limit_bytes": 312500,
                                                "queue_depth": 0,
                                                "total_drops": 0,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 0,
                                                "bytes_output": 0,
                                                "bandwidth_remaining_percent": 40,
                                                "overhead_accounting": "enabled",
                                                "random_detect": {
                                                    "exp_weight_constant": "9 (1/512)",
                                                    "mean_queue_depth": 0,
                                                    "class": {
                                                        "af21": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "134375",
                                                            "maximum_thresh": "156250",
                                                            "mark_prob": "1/10",
                                                        }
                                                    },
                                                },
                                                "qos_set": {
                                                    "dscp": {
                                                        "af21": {
                                                            "marker_statistics": "Disabled"
                                                        }
                                                    }
                                                },
                                            },
                                            "cm5": {
                                                "match_evaluation": "match-any",
                                                "packets": 0,
                                                "bytes": 0,
                                                "rate": {
                                                    "interval": 60,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": ["dscp af11 (10) af12 (12)"],
                                                "queueing": True,
                                                "queue_limit_bytes": 312500,
                                                "queue_depth": 0,
                                                "total_drops": 0,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 0,
                                                "bytes_output": 0,
                                                "bandwidth_remaining_percent": 5,
                                                "overhead_accounting": "enabled",
                                                "random_detect": {
                                                    "exp_weight_constant": "9 (1/512)",
                                                    "mean_queue_depth": 0,
                                                    "class": {
                                                        "af11": {
                                                            "transmitted_packets": "0",
                                                            "transmitted_bytes": "0",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "78125",
                                                            "maximum_thresh": "156250",
                                                            "mark_prob": "1/10",
                                                        }
                                                    },
                                                },
                                                "qos_set": {
                                                    "dscp": {
                                                        "af11": {
                                                            "marker_statistics": "Disabled"
                                                        }
                                                    }
                                                },
                                            },
                                            "class-default": {
                                                "match_evaluation": "match-any",
                                                "packets": 275144,
                                                "bytes": 100234922,
                                                "rate": {
                                                    "interval": 60,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": ["any"],
                                                "queueing": True,
                                                "queue_limit_bytes": 312500,
                                                "queue_depth": 0,
                                                "total_drops": 0,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 22466,
                                                "bytes_output": 1437824,
                                                "bandwidth_remaining_percent": 19,
                                                "overhead_accounting": "enabled",
                                                "random_detect": {
                                                    "exp_weight_constant": "9 (1/512)",
                                                    "mean_queue_depth": 64,
                                                    "class": {
                                                        "default": {
                                                            "transmitted_packets": "22466",
                                                            "transmitted_bytes": "1437824",
                                                            "random_drop_packets": "0",
                                                            "random_drop_bytes": "0",
                                                            "tail_drop_packets": "0",
                                                            "tail_drop_bytes": "0",
                                                            "minimum_thresh": "115625",
                                                            "maximum_thresh": "156250",
                                                            "mark_prob": "1/10",
                                                        }
                                                    },
                                                },
                                                "qos_set": {
                                                    "dscp": {
                                                        "default": {
                                                            "marker_statistics": "Disabled"
                                                        }
                                                    }
                                                },
                                            },
                                        }
                                    }
                                },
                            }
                        }
                    }
                }
            }
        }
    }
}
