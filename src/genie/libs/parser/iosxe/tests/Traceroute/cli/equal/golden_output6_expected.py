expected_output = {
    "traceroute": {
        "10.151.22.22": {
            "address": "10.151.22.22",
            "hops": {
                "1": {
                    "paths": {
                        1: {
                            "address": "10.0.0.5",
                            "probe_msec": ["307", "10", "2"],
                            "label_info": {"MPLS": {"label": "16022", "exp": 0}},
                        }
                    }
                },
                "2": {
                    "paths": {
                        1: {"address": "10.0.0.18", "probe_msec": ["351", "*", "8"]}
                    }
                },
            },
        }
    }
}
