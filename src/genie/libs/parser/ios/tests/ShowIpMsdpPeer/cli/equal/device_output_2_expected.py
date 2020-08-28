expected_output = {
    "vrf": {
        "VRF1": {
            "peer": {
                "10.16.2.2": {
                    "peer_as": 65000,
                    "session_state": "Up",
                    "resets": "0",
                    "connect_source": "Loopback300",
                    "connect_source_address": "10.4.1.1",
                    "elapsed_time": "00:19:00",
                    "statistics": {
                        "sent": {
                            "data_message": 22,
                            "sa_message": 21,
                            "sa_response": 0,
                            "data_packets": 0,
                        },
                        "received": {
                            "data_message": 40,
                            "sa_message": 0,
                            "sa_request": 0,
                            "data_packets": 0,
                        },
                        "output_msg_discarded": 0,
                        "established_transitions": 1,
                        "queue": {"size_in": 0, "size_out": 0},
                        "error": {"rpf_failure": 0},
                    },
                    "conn_count_cleared": "00:27:47",
                    "sa_filter": {
                        "in": {
                            "(S,G)": {"filter": "none", "route_map": "none"},
                            "RP": {"filter": "none", "route_map": "none"},
                        },
                        "out": {
                            "(S,G)": {"filter": "none", "route_map": "none"},
                            "RP": {"filter": "none", "route_map": "none"},
                        },
                    },
                    "sa_request": {"input_filter": "none"},
                    "ttl_threshold": 0,
                    "sa_learned_from": 0,
                    "signature_protection": False,
                },
                "10.36.3.3": {
                    "peer_as": 65000,
                    "session_state": "Down",
                    "resets": "31",
                    "connect_source": "Loopback300",
                    "connect_source_address": "10.4.1.1",
                    "elapsed_time": "00:00:23",
                    "statistics": {
                        "sent": {
                            "data_message": 0,
                            "sa_message": 0,
                            "sa_response": 0,
                            "data_packets": 0,
                        },
                        "received": {
                            "data_message": 0,
                            "sa_message": 0,
                            "sa_request": 0,
                            "data_packets": 0,
                        },
                        "output_msg_discarded": 0,
                        "established_transitions": 31,
                        "queue": {"size_in": 0, "size_out": 0},
                        "error": {"rpf_failure": 0},
                    },
                    "conn_count_cleared": "00:27:56",
                    "sa_filter": {
                        "in": {
                            "(S,G)": {"filter": "none", "route_map": "none"},
                            "RP": {"filter": "none", "route_map": "none"},
                        },
                        "out": {
                            "(S,G)": {"filter": "none", "route_map": "none"},
                            "RP": {"filter": "none", "route_map": "none"},
                        },
                    },
                    "sa_request": {"input_filter": "none"},
                    "ttl_threshold": 0,
                    "sa_learned_from": 0,
                    "signature_protection": False,
                },
            }
        }
    }
}
