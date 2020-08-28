expected_output = {
    "traceroute": {
        "192.168.1.1": {
            "address": "192.168.1.1",
            "hops": {
                "1": {
                    "paths": {
                        1: {
                            "address": "10.19.198.29",
                            "probe_msec": ["2", "2", "2"],
                            "label_info": {
                                "MPLS": {"label": "16052/16062/16063/39", "exp": 0}
                            },
                        }
                    }
                },
                "2": {
                    "paths": {
                        1: {
                            "address": "10.169.14.129",
                            "probe_msec": ["3", "1", "1"],
                            "label_info": {
                                "MPLS": {"label": "16062/16063/39", "exp": 0}
                            },
                        }
                    }
                },
                "3": {
                    "paths": {
                        1: {
                            "address": "10.169.14.34",
                            "probe_msec": ["3", "1", "2"],
                            "label_info": {"MPLS": {"label": "16063/39", "exp": 0}},
                        }
                    }
                },
                "4": {
                    "paths": {
                        1: {"address": "192.168.1.1", "probe_msec": ["2", "*", "2"]}
                    }
                },
            },
            "vrf": "MG501",
        }
    }
}
