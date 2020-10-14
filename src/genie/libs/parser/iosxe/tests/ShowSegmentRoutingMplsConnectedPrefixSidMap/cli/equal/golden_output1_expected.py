expected_output = {
    "segment_routing": {
        "bindings": {
            "local_prefix_sid": {
                "ipv4": {
                    "ipv4_prefix_sid_local": {
                        "10.4.1.1/32": {
                            "algorithm": {
                                "ALGO_0": {
                                    "prefix": "10.4.1.1/32",
                                    "algorithm": "ALGO_0",
                                    "value_type": "Indx",
                                    "sid": "1",
                                    "range": "1",
                                    "srgb": "Y",
                                }
                            }
                        }
                    }
                }
            },
            "connected_prefix_sid_map": {
                "ipv4": {
                    "ipv4_prefix_sid": {
                        "10.4.1.1/32": {
                            "algorithm": {
                                "ALGO_0": {
                                    "prefix": "10.4.1.1/32",
                                    "algorithm": "ALGO_0",
                                    "value_type": "Indx",
                                    "sid": "1",
                                    "range": "1",
                                    "srgb": "Y",
                                    "source": "OSPF Area 8 10.4.1.1",
                                }
                            }
                        },
                        "10.16.2.2/32": {
                            "algorithm": {
                                "ALGO_0": {
                                    "prefix": "10.16.2.2/32",
                                    "algorithm": "ALGO_0",
                                    "value_type": "Indx",
                                    "sid": "2",
                                    "range": "1",
                                    "srgb": "Y",
                                    "source": "OSPF Area 8 10.16.2.2",
                                }
                            }
                        },
                    }
                }
            },
        }
    }
}
