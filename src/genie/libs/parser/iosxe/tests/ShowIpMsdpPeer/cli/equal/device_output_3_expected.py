expected_output = {
    "vrf": {
        "default": {
            "peer": {
                "10.4.1.2": {
                    "conn_count_cleared": "2w5d",
                    "connect_source": "Loopback0",
                    "connect_source_address": "10.4.1.1",
                    "elapsed_time": "2w2d",
                    "resets": "1",
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
                    "sa_learned_from": 0,
                    "sa_request": {"input_filter": "none"},
                    "session_state": "Up",
                    "signature_protection": False,
                    "statistics": {
                        "error": {"rpf_failure": 0},
                        "established_transitions": 2,
                        "output_msg_discarded": 0,
                        "queue": {"size_in": 0, "size_out": 0},
                        "received": {
                            "data_message": 23498,
                            "data_packets": 32,
                            "sa_message": 135,
                            "sa_request": 0,
                        },
                        "sent": {
                            "data_message": 23466,
                            "data_packets": 0,
                            "sa_message": 31,
                            "sa_response": 0,
                        },
                    },
                    "ttl_threshold": 0,
                }
            }
        }
    }
}
