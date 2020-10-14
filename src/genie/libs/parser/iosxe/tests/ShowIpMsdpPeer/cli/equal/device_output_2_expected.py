expected_output = {
    "vrf": {
        "VRF1": {
            "peer": {
                "10.1.100.2": {
                    "peer_as": 1,
                    "session_state": "Up",
                    "resets": "0",
                    "connect_source": "Loopback0",
                    "connect_source_address": "10.1.100.1",
                    "elapsed_time": "00:15:38",
                    "statistics": {
                        "queue": {"size_in": 0, "size_out": 0},
                        "sent": {
                            "data_message": 17,
                            "sa_message": 8,
                            "sa_response": 0,
                            "data_packets": 1,
                        },
                        "received": {
                            "data_message": 15,
                            "sa_message": 0,
                            "sa_request": 0,
                            "data_packets": 0,
                        },
                        "error": {"rpf_failure": 0},
                        "established_transitions": 1,
                        "output_msg_discarded": 0,
                    },
                    "conn_count_cleared": "00:15:38",
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
