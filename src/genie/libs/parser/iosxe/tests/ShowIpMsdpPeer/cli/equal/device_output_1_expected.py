expected_output = {
    "vrf": {
        "default": {
            "peer": {
                "10.1.100.4": {
                    "session_state": "Up",
                    "peer_as": 1,
                    "resets": "0",
                    "connect_source": "Loopback0",
                    "connect_source_address": "10.1.100.2",
                    "elapsed_time": "00:41:18",
                    "statistics": {
                        "queue": {"size_in": 0, "size_out": 0},
                        "sent": {
                            "data_message": 42,
                            "sa_message": 0,
                            "sa_response": 0,
                            "data_packets": 0,
                        },
                        "received": {
                            "data_message": 50,
                            "sa_message": 27,
                            "sa_request": 0,
                            "data_packets": 6,
                        },
                        "established_transitions": 1,
                        "output_msg_discarded": 0,
                        "error": {"rpf_failure": 27},
                    },
                    "conn_count_cleared": "00:43:22",
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
                }
            }
        }
    }
}
