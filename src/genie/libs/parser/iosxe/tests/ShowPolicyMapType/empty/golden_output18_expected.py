expected_output = {
    "TenGigabitEthernet0/0/0.101": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "L3VPN_in": {
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
                                    "cir_bps": 400000,
                                    "cir_bc_bytes": 400000,
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
                        },
                        "child_policy_name": {
                            "STD_in_child": {
                                "class_map": {
                                    "IPP567": {
                                        "match_evaluation": "match-all",
                                        "packets": 0,
                                        "bytes": 0,
                                        "rate": {
                                            "interval": 300,
                                            "offered_rate_bps": 0,
                                            "drop_rate_bps": 0,
                                        },
                                        "match": ["ip precedence 3  4  5"],
                                        "qos_set": {
                                            "ip precedence": {
                                                "1": {"marker_statistics": "Disabled"}
                                            },
                                            "qos-group": {
                                                "1": {"marker_statistics": "Disabled"}
                                            },
                                        },
                                    }
                                }
                            }
                        },
                    }
                }
            },
            "output": {
                "policy_name": {
                    "L3VPN_out": {
                        "class_map": {
                            "class-default": {
                                "match_evaluation": "match-any",
                                "packets": 2121212,
                                "bytes": 121212,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 11111171,
                                    "drop_rate_bps": 1118111,
                                },
                                "match": ["any"],
                                "queueing": True,
                                "queue_limit_packets": "64",
                                "queue_depth": 0,
                                "total_drops": 11111,
                                "no_buffer_drops": 0,
                                "pkts_output": 11511,
                                "bytes_output": 111611,
                                "shape_type": "average",
                                "shape_cir_bps": 111222,
                                "shape_bc_bps": 2323,
                                "shape_be_bps": 3434,
                                "target_shape_rate": 454545,
                            }
                        },
                        "child_policy_name": {
                            "leeaf": {
                                "queue_stats_for_all_priority_classes": {
                                    "priority_level": {
                                        "1": {
                                            "queueing": True,
                                            "queue_limit_packets": "512",
                                            "queue_depth": 0,
                                            "total_drops": 0,
                                            "no_buffer_drops": 0,
                                            "pkts_output": 123456,
                                            "bytes_output": 7890123,
                                        }
                                    }
                                },
                                "class_map": {
                                    "IPP67": {
                                        "match_evaluation": "match-all",
                                        "bandwidth_kbps": 234,
                                        "bandwidth_percent": 50,
                                        "packets": 123,
                                        "bytes": 4567,
                                        "rate": {
                                            "interval": 300,
                                            "offered_rate_bps": 123123123,
                                            "drop_rate_bps": 456456456,
                                        },
                                        "match": ["ip precedence 6  7"],
                                        "queueing": True,
                                        "queue_limit_packets": "64",
                                        "queue_depth": 63,
                                        "total_drops": 2655550,
                                        "no_buffer_drops": 0,
                                        "pkts_output": 6612304,
                                        "bytes_output": 819909328,
                                    }
                                },
                            }
                        },
                    }
                }
            },
        }
    }
}
