expected_output = {
    "vrf": {
        "default": {
            "num_of_sa_cache": 1,
            "sa_cache": {
                "225.1.1.1 10.3.3.18": {
                    "group": "225.1.1.1",
                    "source_addr": "10.3.3.18",
                    "up_time": "00:00:10",
                    "expire": "00:05:49",
                    "peer_as": 3,
                    "peer": "10.1.100.4",
                    "origin_rp": {"10.3.100.8": {"rp_address": "10.3.100.8"}},
                    "peer_learned_from": "10.1.100.4",
                    "rpf_peer": "10.1.100.4",
                    "statistics": {
                        "received": {"sa": 1, "encapsulated_data_received": 1}
                    },
                }
            },
        }
    }
}
