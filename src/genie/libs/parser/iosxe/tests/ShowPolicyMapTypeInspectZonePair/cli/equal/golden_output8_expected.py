expected_output={
    "zone_pair": {
        "in-out": {
            "service_policy_inspect": {
                "pmap1": {
                    "class_map": {
                        "cmap1": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol tcp",
                            ],
                            "class_map_action": {
                                "Inspect": {
                                    "total_packets": 0,
                                    "total_bytes": 0,
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
                                "any"
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
