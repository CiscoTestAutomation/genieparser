expected_output = {
    "traceroute": {
        "172.31.165.220/32": {
            "address": "172.31.165.220",
            "mask": "32",
            "timeout_seconds": 2,
            "hops": {
                "1": {
                    "paths": {
                        1: {
                            "address": "192.168.197.93",
                            "label_info": {"label_name": "implicit-null", "exp": 0},
                            "probe_msec": ["1"],
                            "mru": 1552,
                        }
                    },
                    "code": "L",
                },
                "2": {
                    "paths": {1: {"address": "192.168.197.102", "probe_msec": ["1"]}},
                    "code": "!",
                },
                "0": {
                    "paths": {
                        1: {
                            "address": "192.168.197.94",
                            "label_info": {"label_name": "1015", "exp": 0},
                            "mru": 1552,
                        }
                    }
                },
            },
        }
    }
}
