expected_output = {
    "traceroute": {
        "127.0.0.1": {
            "address": "127.0.0.1",
            "hops": {
                "1": {
                    "paths": {
                        1: {
                            "address": "127.0.0.2",
                            "probe_msec": ["4", "8", "0"]
                        }
                    }
                },
                "2": {
                    "paths": {
                        1: {
                            "address": "127.0.0.3",
                            "probe_msec": ["8", "*", "0"]
                        }
                    }
                }
            }
        }
    }
}

