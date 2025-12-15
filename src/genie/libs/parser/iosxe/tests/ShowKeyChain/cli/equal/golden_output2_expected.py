expected_output = {
    "key_chains": {
        "test1": {
            "is_tcp": True,
            "preferred_mkt_id": 1,
            "keys": {
                "1": {
                    "key_string": "C!$c0123-1",
                    "cryptographic_algo": "hmac-sha-1",
                    "accept_lifetime": {
                        "start": "10:30:00 UTC Oct 3 2025",
                        "end": "infinite",
                        "is_valid": True
                    },
                    "send_lifetime": {
                        "start": "10:30:00 UTC Oct 3 2025",
                        "end": "infinite",
                        "is_valid": True
                    },
                    "send_id": 1,
                    "recv_id": 1,
                    "include_tcp_options": True,
                    "accept_ao_mismatch": True,
                    "mkt_ready": True,
                    "mkt_preferred": True,
                    "mkt_in_use": False,
                    "mkt_id": 1,
                    "mkt_send_id": 1,
                    "mkt_recv_id": 1,
                    "mkt_alive_send": True,
                    "mkt_alive_recv": True,
                    "mkt_include_tcp_options": True,
                    "mkt_accept_ao_mismatch": True
                }
            }
        }
    }
}