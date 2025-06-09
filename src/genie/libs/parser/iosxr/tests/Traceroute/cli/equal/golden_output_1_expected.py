expected_output = {
    "traceroute": {
        "2000:90:33:1::2": {
            "address": "2000:90:33:1::2",
            "hops": {
                "1": {
                    "paths": {
                        1: {
                            "address": "2000:90:11:1::1",
                            "probe_msec": [
                                "2",
                                "2",
                                "1"
                            ]
                        }
                    }
                },
                "2": {
                    "paths": {
                        1: {
                            "address": "::ffff:10.0.0.12",
                            "probe_msec": [
                                "2",
                                "2",
                                "2"
                            ],
                            "label_info": {
                                "MPLS": {
                                    "label": "16004/26061",
                                    "exp": 0
                                }
                            }
                        }
                    }
                },
                "3": {
                    "paths": {
                        1: {
                            "address": "::ffff:10.0.0.14",
                            "probe_msec": [
                                "3",
                                "2",
                                "2"
                            ],
                            "label_info": {
                                "MPLS": {
                                    "label": "16004/26061",
                                    "exp": 0
                                }
                            }
                        }
                    }
                },
                "4": {
                    "paths": {
                        1: {
                            "address": "2000:90:33:1::1",
                            "probe_msec": [
                                "2",
                                "1",
                                "1"
                            ]
                        }
                    }
                },
                "5": {
                    "paths": {
                        1: {
                            "address": "2000:90:33:1::2",
                            "probe_msec": [
                                "4",
                                "3",
                                "3"
                            ]
                        }
                    }
                }
            }
        }
    }
}
