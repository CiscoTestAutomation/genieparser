expected_output={
    "zone_pair": {
        "in-to-out": {
            "service_policy_inspect": {
                "in-to-out": {
                    "class_map": {
                        "in-to-out": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol http",
                                "protocol https"
                            ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class-default": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "any "
                            ],
                            "class_map_action": {
                                "Drop": {
                                    "total_packets": 0,
                                    "total_bytes": 0
                                }
                            }
                        }
                    }
                }
            }
        },
        "out-to-in": {
            "service_policy_inspect": {
                "p1": {
                    "class_map": {
                        "c1": {
                            "class_map_type": "match-all",
                            "class_map_match": [
                                "protocol http"
                            ],
                            "class_map_action": {
                                "Drop": {
                                    "total_packets": 0,
                                    "total_bytes": 0
                                }
                            }
                        },
                        "class-default": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "any "
                            ],
                            "class_map_action": {
                                "Drop": {
                                    "total_packets": 0,
                                    "total_bytes": 0
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}