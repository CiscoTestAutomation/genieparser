expected_output = {
    "vrf": {
        "default": {
            "num_of_sa_cache": 1,
            "sa_cache": {
                "225.1.1.1 10.1.4.15": {
                    "group": "225.1.1.1",
                    "source_addr": "10.1.4.15",
                    "up_time": "00:19:29",
                    "expire": "00:05:14",
                    "peer": "10.1.100.1",
                    "origin_rp": {"10.1.100.1": {"rp_address": "10.1.100.1"}},
                    "peer_learned_from": "10.1.100.1",
                    "rpf_peer": "10.1.100.1",
                    "statistics": {
                        "received": {"sa": 14, "encapsulated_data_received": 0}
                    },
                }
            },
        }
    }
}
