expected_output = {
    "traceroute": {
        "192.168.1.1": {
            "address": "192.168.1.1",
            "hops": {
                "1": {"paths": {1: {"address": "*  *  *"}}},
                "2": {"paths": {1: {"address": "*  *  *"}}},
                "3": {
                    "paths": {
                        1: {
                            "probe_msec": ["*", "*", "3"],
                            "address": "10.169.14.121",
                            "label_info": {"MPLS": {"label": "16063/459", "exp": 0}},
                        }
                    }
                },
                "4": {
                    "paths": {
                        1: {
                            "address": "10.169.14.158",
                            "probe_msec": ["2", "3", "3"],
                            "label_info": {"MPLS": {"label": "16063/459", "exp": 0}},
                        }
                    }
                },
                "5": {
                    "paths": {
                        1: {"address": "192.168.1.1", "probe_msec": ["3", "*", "3"]}
                    }
                },
            },
        }
    }
}
