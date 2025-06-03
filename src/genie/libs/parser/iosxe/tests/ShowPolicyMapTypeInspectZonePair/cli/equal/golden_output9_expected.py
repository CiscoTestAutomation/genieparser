expected_output= {
    "zone_pair": {
        "in-self": {
            "service_policy_inspect": {
                "pmap": {
                    "class_map": {
                        "cmap": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "access-group name OGACL"
                            ],
                            "class_map_action": {
                                "Inspect": {
                                    "packet_type": {
                                        "icmp": {
                                            "switch1_type": "process switch",
                                            "switch2_type": "fast switch",
                                            "packets_in_switch1": 0,
                                            "packets_in_switch2": 10
                                        }
                                    },
                                    "sessions_since_startup_or_reset": 1,
                                    "current_session_counts_estab": 1,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 1,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "00:00:20",
                                    "last_statistic_reset": "00:00:06",
                                    "last_session_creation_rate": 1,
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
