expected_output = {
    "GigabitEthernet0/0/0": {
        "service_policy": {
            "output": {
                "policy_name": {
                    "top": {
                        "class_map": {
                            "vlan100": {
                                "match_evaluation": "match-all",
                                "packets": 2619318,
                                "bytes": 1309658128,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 15632000,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["vlan  100"],
                                "queueing": True,
                                "queue_limit_packets": "64",
                                "queue_depth": 0,
                                "total_drops": 2582299,
                                "no_buffer_drops": 0,
                                "pkts_output": 36918,
                                "bytes_output": 18458128,
                                "shape_type": "average",
                                "shape_cir_bps": 8000000,
                                "shape_bc_bps": 32000,
                                "shape_be_bps": 32000,
                                "target_shape_rate": 8000000,
                                "bandwidth_remaining_ratio": 1000,
                                "child_policy_name": {
                                    "middle": {
                                        "class_map": {
                                            "sec": {
                                                "match_evaluation": "match-all",
                                                "packets": 1761255,
                                                "bytes": 880627500,
                                                "rate": {
                                                    "interval": 300,
                                                    "offered_rate_bps": 10622000,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": ["access-group name sec"],
                                                "queueing": True,
                                                "queue_limit_packets": "64",
                                                "queue_depth": 0,
                                                "total_drops": 1759330,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 1853,
                                                "bytes_output": 926500,
                                                "shape_type": "average",
                                                "shape_cir_bps": 8000000,
                                                "shape_bc_bps": 32000,
                                                "shape_be_bps": 32000,
                                                "target_shape_rate": 8000000,
                                                "bandwidth_remaining_percent": 3,
                                                "child_policy_name": {
                                                    "bottom": {
                                                        "class_map": {
                                                            "ef": {
                                                                "match_evaluation": "match-all",
                                                                "packets": 889238,
                                                                "bytes": 444619000,
                                                                "rate": {
                                                                    "interval": 300,
                                                                    "offered_rate_bps": 5425000,
                                                                    "drop_rate_bps": 5419000,
                                                                },
                                                                "match": [
                                                                    "dscp ef (46)"
                                                                ],
                                                                "queueing": True,
                                                                "queue_limit_packets": "64",
                                                                "queue_depth": 64,
                                                                "total_drops": 888685,
                                                                "no_buffer_drops": 0,
                                                                "pkts_output": 553,
                                                                "bytes_output": 276500,
                                                                "bandwidth_remaining_percent": 15,
                                                            },
                                                            "class-default": {
                                                                "match_evaluation": "match-any",
                                                                "packets": 871942,
                                                                "bytes": 435971000,
                                                                "rate": {
                                                                    "interval": 300,
                                                                    "offered_rate_bps": 5196000,
                                                                    "drop_rate_bps": 5185000,
                                                                },
                                                                "match": ["any"],
                                                                "queueing": True,
                                                                "queue_limit_packets": "512",
                                                                "pkts_output": 1300,
                                                                "bytes_output": 650000,
                                                                "fair_queue_limit_per_flow": 128,
                                                                "random_detect": {
                                                                    "exp_weight_constant": "4 (1/16)",
                                                                    "mean_queue_depth": 65,
                                                                    "class": {
                                                                        "default": {
                                                                            "transmitted_packets": "0",
                                                                            "transmitted_bytes": "0",
                                                                            "random_drop_packets": "0",
                                                                            "random_drop_bytes": "0",
                                                                            "tail_drop_packets": "0",
                                                                            "tail_drop_bytes": "0",
                                                                            "minimum_thresh": "34",
                                                                            "maximum_thresh": "62",
                                                                            "mark_prob": "1/10",
                                                                        },
                                                                        "af31": {
                                                                            "transmitted_packets": "1300",
                                                                            "transmitted_bytes": "650000",
                                                                            "random_drop_packets": "84",
                                                                            "random_drop_bytes": "42000",
                                                                            "tail_drop_packets": "870561",
                                                                            "tail_drop_bytes": "435280500",
                                                                            "minimum_thresh": "32",
                                                                            "maximum_thresh": "64",
                                                                            "mark_prob": "1/10",
                                                                        },
                                                                    },
                                                                },
                                                                "bandwidth_remaining_percent": 85,
                                                            },
                                                        }
                                                    }
                                                },
                                            },
                                            "class-default": {
                                                "match_evaluation": "match-any",
                                                "packets": 858034,
                                                "bytes": 429016128,
                                                "rate": {
                                                    "interval": 300,
                                                    "offered_rate_bps": 5011000,
                                                    "drop_rate_bps": 4803000,
                                                },
                                                "match": ["any"],
                                                "queueing": True,
                                                "queue_limit_packets": "64",
                                                "queue_depth": 64,
                                                "total_drops": 822969,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 35065,
                                                "bytes_output": 17531628,
                                                "shape_type": "average",
                                                "shape_cir_bps": 8000000,
                                                "shape_bc_bps": 32000,
                                                "shape_be_bps": 32000,
                                                "target_shape_rate": 8000000,
                                            },
                                        }
                                    }
                                },
                            },
                            "vlan101": {
                                "match_evaluation": "match-all",
                                "packets": 830718,
                                "bytes": 415358128,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 4648000,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["vlan  101"],
                                "queueing": True,
                                "queue_limit_packets": "64",
                                "queue_depth": 0,
                                "total_drops": 795129,
                                "no_buffer_drops": 0,
                                "pkts_output": 35549,
                                "bytes_output": 17773628,
                                "shape_type": "average",
                                "shape_cir_bps": 8000000,
                                "shape_bc_bps": 32000,
                                "shape_be_bps": 32000,
                                "target_shape_rate": 8000000,
                                "bandwidth_remaining_ratio": 1000,
                                "child_policy_name": {
                                    "middle": {
                                        "class_map": {
                                            "sec": {
                                                "match_evaluation": "match-all",
                                                "packets": 830706,
                                                "bytes": 415353000,
                                                "rate": {
                                                    "interval": 300,
                                                    "offered_rate_bps": 4648000,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": ["access-group name sec"],
                                                "queueing": True,
                                                "queue_limit_packets": "64",
                                                "queue_depth": 0,
                                                "total_drops": 795129,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 35547,
                                                "bytes_output": 17773500,
                                                "shape_type": "average",
                                                "shape_cir_bps": 8000000,
                                                "shape_bc_bps": 32000,
                                                "shape_be_bps": 32000,
                                                "target_shape_rate": 8000000,
                                                "bandwidth_remaining_percent": 3,
                                                "child_policy_name": {
                                                    "bottom": {
                                                        "class_map": {
                                                            "ef": {
                                                                "match_evaluation": "match-all",
                                                                "packets": 0,
                                                                "bytes": 0,
                                                                "rate": {
                                                                    "interval": 300,
                                                                    "offered_rate_bps": 0,
                                                                    "drop_rate_bps": 0,
                                                                },
                                                                "match": [
                                                                    "dscp ef (46)"
                                                                ],
                                                                "queueing": True,
                                                                "queue_limit_packets": "64",
                                                                "queue_depth": 0,
                                                                "total_drops": 0,
                                                                "no_buffer_drops": 0,
                                                                "pkts_output": 0,
                                                                "bytes_output": 0,
                                                                "bandwidth_remaining_percent": 15,
                                                            },
                                                            "class-default": {
                                                                "match_evaluation": "match-any",
                                                                "packets": 830676,
                                                                "bytes": 415338000,
                                                                "rate": {
                                                                    "interval": 300,
                                                                    "offered_rate_bps": 4648000,
                                                                    "drop_rate_bps": 4441000,
                                                                },
                                                                "match": ["any"],
                                                                "queueing": True,
                                                                "queue_limit_packets": "512",
                                                                "pkts_output": 35547,
                                                                "bytes_output": 17773500,
                                                                "fair_queue_limit_per_flow": 128,
                                                                "random_detect": {
                                                                    "exp_weight_constant": "4 (1/16)",
                                                                    "mean_queue_depth": 63,
                                                                    "class": {
                                                                        "default": {
                                                                            "transmitted_packets": "35547",
                                                                            "transmitted_bytes": "17773500",
                                                                            "random_drop_packets": "3561",
                                                                            "random_drop_bytes": "1780500",
                                                                            "tail_drop_packets": "791568",
                                                                            "tail_drop_bytes": "395784000",
                                                                            "minimum_thresh": "34",
                                                                            "maximum_thresh": "62",
                                                                            "mark_prob": "1/10",
                                                                        },
                                                                        "af31": {
                                                                            "transmitted_packets": "0",
                                                                            "transmitted_bytes": "0",
                                                                            "random_drop_packets": "0",
                                                                            "random_drop_bytes": "0",
                                                                            "tail_drop_packets": "0",
                                                                            "tail_drop_bytes": "0",
                                                                            "minimum_thresh": "32",
                                                                            "maximum_thresh": "64",
                                                                            "mark_prob": "1/10",
                                                                        },
                                                                    },
                                                                },
                                                                "bandwidth_remaining_percent": 85,
                                                            },
                                                        }
                                                    }
                                                },
                                            },
                                            "class-default": {
                                                "match_evaluation": "match-any",
                                                "packets": 2,
                                                "bytes": 128,
                                                "rate": {
                                                    "interval": 300,
                                                    "offered_rate_bps": 0,
                                                    "drop_rate_bps": 0,
                                                },
                                                "match": ["any"],
                                                "queueing": True,
                                                "queue_limit_packets": "64",
                                                "queue_depth": 0,
                                                "total_drops": 0,
                                                "no_buffer_drops": 0,
                                                "pkts_output": 2,
                                                "bytes_output": 128,
                                                "shape_type": "average",
                                                "shape_cir_bps": 8000000,
                                                "shape_bc_bps": 32000,
                                                "shape_be_bps": 32000,
                                                "target_shape_rate": 8000000,
                                            },
                                        }
                                    }
                                },
                            },
                            "class-default": {
                                "match_evaluation": "match-any",
                                "packets": 804701,
                                "bytes": 402349628,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 4303000,
                                    "drop_rate_bps": 4055000,
                                },
                                "match": ["any"],
                                "queueing": True,
                                "queue_limit_packets": "64",
                                "queue_depth": 64,
                                "total_drops": 761091,
                                "no_buffer_drops": 0,
                                "pkts_output": 43610,
                                "bytes_output": 21804128,
                                "bandwidth_remaining_ratio": 1,
                                "shape_type": "average",
                                "shape_cir_bps": 10000000,
                                "shape_bc_bps": 40000,
                                "shape_be_bps": 40000,
                                "target_shape_rate": 10000000,
                            },
                        }
                    }
                }
            }
        }
    }
}
