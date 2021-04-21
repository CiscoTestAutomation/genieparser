expected_output = {
    "TenGigabitEthernet0/0/0": {
        "service_policy": {
            "output": {
                "policy_name": {
                    "pm_queuing": {
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
                        "class_map": {
                            "cm_dscp_class1": {
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "bytes": 0,
                                "priority": {"exceed_drops": 0, "type": "Strict"},
                                "rate": {
                                    "interval": 60,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["ip dscp ef (46)"],
                            },
                            "cm_dscp_att_ncp": {
                                "match_evaluation": "match-any",
                                "packets": 50402030,
                                "bytes": 4960596805,
                                "rate": {
                                    "interval": 60,
                                    "offered_rate_bps": 1000,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["ip dscp cs6 (48) cs7 (56)"],
                                "queueing": True,
                                "queue_limit_packets": "41666",
                                "queue_depth": 0,
                                "total_drops": 0,
                                "no_buffer_drops": 0,
                                "pkts_output": 21791793,
                                "bytes_output": 1927911831,
                                "bandwidth_remaining_percent": 5,
                            },
                            "cm_dscp_class2": {
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 60,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["ip dscp af31 (26) af32 (28)"],
                                "queueing": True,
                                "queue_limit_packets": "41666",
                                "queue_depth": 0,
                                "total_drops": 0,
                                "no_buffer_drops": 0,
                                "pkts_output": 0,
                                "bytes_output": 0,
                                "bandwidth_remaining_percent": 25,
                            },
                            "cm_dscp_class3": {
                                "match_evaluation": "match-any",
                                "packets": 25610,
                                "bytes": 5013442,
                                "rate": {
                                    "interval": 60,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["ip dscp af21 (18) af22 (20)"],
                                "queueing": True,
                                "queue_limit_packets": "41666",
                                "queue_depth": 0,
                                "total_drops": 0,
                                "no_buffer_drops": 0,
                                "pkts_output": 25610,
                                "bytes_output": 5013442,
                                "bandwidth_remaining_percent": 25,
                            },
                            "class-default": {
                                "match_evaluation": "match-any",
                                "packets": 195800135,
                                "bytes": 14147555758,
                                "rate": {
                                    "interval": 60,
                                    "offered_rate_bps": 4000,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["any"],
                                "queueing": True,
                                "queue_limit_packets": "41666",
                                "queue_depth": 0,
                                "total_drops": 0,
                                "no_buffer_drops": 0,
                                "pkts_output": 183412932,
                                "bytes_output": 9203926787,
                                "bandwidth_remaining_percent": 25,
                            },
                        },
                    }
                }
            }
        }
    }
}
