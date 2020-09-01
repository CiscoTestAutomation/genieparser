expected_output = {
    "traceroute": {
        "192.168.100.252": {
            "address": "192.168.100.252",
            "hops": {
                "1": {
                    "paths": {
                        1: {
                            "address": "10.169.196.213",
                            "label_info": {"MPLS": {"exp": 0, "label": "16051/67207"}},
                            "probe_msec": ["45", "46", "46"],
                        }
                    }
                },
                "2": {
                    "paths": {
                        1: {
                            "address": "10.169.14.157",
                            "label_info": {"MPLS": {"exp": 0, "label": "67207"}},
                            "probe_msec": ["*", "*", "40"],
                        }
                    }
                },
                "3": {
                    "paths": {
                        1: {
                            "address": "10.169.14.217",
                            "label_info": {"MPLS": {"exp": 0, "label": "24003"}},
                            "probe_msec": ["45", "46", "55"],
                        }
                    }
                },
                "4": {
                    "paths": {
                        1: {"address": "10.174.135.94", "probe_msec": ["36", "7", "2"]}
                    }
                },
                "5": {
                    "paths": {
                        1: {
                            "address": "192.168.100.18",
                            "asn": 2516,
                            "probe_msec": ["*", "*", "2"],
                        }
                    }
                },
            },
        }
    }
}
