expected_output={
    "zone_pair": {
        "CU_107->DEFAULT": {
            "service_policy_inspect": {
                "TEST": {
                    "class_map": {
                        "TEST": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "access-group name HBN2"
                            ],
                            "class_map_action": {
                                "Inspect": {
                                    "packet_type": {
                                        "udp": {
                                            "switch1_type": "process switch",
                                            "switch2_type": "fast switch",
                                            "packets_in_switch1": 0,
                                            "packets_in_switch2": 84014582
                                        }
                                    },
                                    "sessions_since_startup_or_reset": 30,
                                    "current_session_counts_estab": 10,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 10,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "16:42:32",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "ICMP": {
                            "class_map_type": "match-all",
                            "class_map_match": [
                                "protocol icmp"
                            ],
                            "class_map_action": {
                                "Pass": {
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
                                    "total_packets": 6986043,
                                    "total_bytes": 3423161070
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}