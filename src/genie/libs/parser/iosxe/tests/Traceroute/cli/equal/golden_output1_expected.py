expected_output = {
    "traceroute": {
        "172.16.166.253": {
            "address": "172.16.166.253",
            "hops": {
                "9": {
                    "paths": {
                        1: {
                            "address": "10.2.1.2",
                            "vrf_out_id": "2001",
                            "vrf_out_name": "blue",
                            "vrf_in_id": "1001",
                            "vrf_in_name": "red",
                        }
                    }
                },
                "4": {
                    "paths": {
                        1: {
                            "address": "192.168.15.1",
                            "label_info": {"MPLS": {"label": "24133", "exp": 0}},
                            "probe_msec": ["6", "7", "64"],
                        }
                    }
                },
                "5": {
                    "paths": {
                        1: {
                            "address": "10.80.241.86",
                            "label_info": {"MPLS": {"label": "24147", "exp": 0}},
                            "probe_msec": ["69", "65", "111"],
                        }
                    }
                },
                "8": {
                    "paths": {
                        1: {
                            "address": "10.1.1.2",
                            "vrf_out_id": "2001",
                            "vrf_out_name": "blue",
                            "vrf_in_id": "1001",
                            "vrf_in_name": "red",
                        }
                    }
                },
                "2": {
                    "paths": {
                        1: {
                            "address": "10.0.9.1",
                            "label_info": {"MPLS": {"label": "300678", "exp": 0}},
                            "probe_msec": ["177", "150", "9"],
                        }
                    }
                },
                "1": {
                    "paths": {
                        1: {
                            "address": "172.31.255.125",
                            "label_info": {"MPLS": {"label": "624", "exp": 0}},
                            "probe_msec": ["70", "200", "19"],
                        }
                    }
                },
                "6": {
                    "paths": {
                        1: {
                            "address": "10.90.135.110",
                            "label_info": {"MPLS": {"label": "24140", "exp": 0}},
                            "probe_msec": ["21", "4", "104"],
                        }
                    }
                },
                "3": {
                    "paths": {
                        1: {
                            "address": "192.168.14.61",
                            "label_info": {"MPLS": {"label": "302537", "exp": 0}},
                            "probe_msec": ["134", "1", "55"],
                        }
                    }
                },
                "7": {
                    "paths": {
                        1: {
                            "address": "172.31.166.10",
                            "probe_msec": ["92", "51", "148"],
                        }
                    }
                },
            },
        }
    }
}
