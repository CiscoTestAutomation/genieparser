expected_output = {
    "our_address": {
        "10.169.197.93": {
            "neighbor_address": {
                "10.169.197.94": {
                    "ld_rd": "4097/4097",
                    'ld': 4097,
                    'rd': 4097,
                    "rh_rs": "Up",
                    "state": "Up",
                    "interface": "GigabitEthernet0/0/0",
                    "session": {
                        "state": "UP",
                        "echo_function": True,
                        "echo_interval_ms": 500,
                    },
                    "session_host": "Software",
                    "handle": 1,
                    "local_diag": 0,
                    "demand_mode": 0,
                    "poll_bit": 0,
                    "min_tx_int": 1000000,
                    "min_rx_int": 1000000,
                    "multiplier": 6,
                    "received_min_rx_int": 1000000,
                    "received_multiplier": 6,
                    "holddown": 0,
                    "holddown_hits": 0,
                    "hello": 1000,
                    "hello_hits": 1912,
                    "rx": {
                        "count": 1914,
                        "min_int_ms": 1,
                        "max_int_ms": 1017,
                        "avg_int_ms": 878,
                        "last_ms_ago": 668,
                    },
                    "tx": {
                        "count": 1914,
                        "min_int_ms": 1,
                        "max_int_ms": 1003,
                        "avg_int_ms": 878,
                        "last_ms_ago": 69,
                    },
                    "elapsed_time_watermarks": "0 0",
                    "elapsed_time_watermarks_last": 0,
                    "registered_protocols": ["OSPF", "CEF"],
                    "up_time": "00:28:01",
                    "last_packet": {
                        "version": 1,
                        "diagnostic": 0,
                        "state_bit": "Up",
                        "demand_bit": 0,
                        "poll_bit": 0,
                        "final_bit": 0,
                        "c_bit": 0,
                        "multiplier": 6,
                        "length": 24,
                        "my_discr": 4097,
                        "your_discr": 4097,
                        "min_tx_int": 1000000,
                        "min_rx_int": 1000000,
                        "min_echo_int": 300000,
                    },
                }
            }
        }
    }
}
