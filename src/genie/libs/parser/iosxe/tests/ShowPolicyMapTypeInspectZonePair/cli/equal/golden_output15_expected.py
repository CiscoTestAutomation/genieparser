expected_output={
    "zone_pair": {
        "in-out": {
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
                                        "tcp": {
                                            "switch1_type": "process switch",
                                            "switch2_type": "fast switch",
                                            "packets_in_switch1": 0,
                                            "packets_in_switch2": 70
                                        },
                                        "udp": {
                                            "switch1_type": "process switch",
                                            "switch2_type": "fast switch",
                                            "packets_in_switch1": 0,
                                            "packets_in_switch2": 55
                                        },
                                        "icmp": {
                                            "switch1_type": "process switch",
                                            "switch2_type": "fast switch",
                                            "packets_in_switch1": 0,
                                            "packets_in_switch2": 100
                                        }
                                    },
                                    "sessions_since_startup_or_reset": 30,
                                    "current_session_counts_estab": 20,
                                    "current_session_counts_half_open": 10,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 20,
                                    "maxever_session_counts_half_open": 15,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "00:00:14",
                                    "last_statistic_reset": "00:00:08",
                                    "last_session_creation_rate": 30,
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
