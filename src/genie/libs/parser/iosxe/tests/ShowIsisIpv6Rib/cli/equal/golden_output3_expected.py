expected_output = {
    "tag": {
        "1": {
            "rib_root": "local RIB",
            "flex_algo": {
                "None": {
                    "prefix": {
                        "12:12::/64": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "via": {
                                "FE80::A8BB:CCFF:FE00:9C10": {
                                    "type": {
                                        "L1": {
                                            "metric": 20,
                                            "tag": "0",
                                            "interface": "Ethernet0/1",
                                            "filtered_out": False,
                                        }
                                    }
                                }
                            }
                        },
                        "13:13::/64": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "via": {
                                "FE80::A8BB:CCFF:FE00:9D20": {
                                    "type": {
                                        "L1": {
                                            "metric": 20,
                                            "tag": "0",
                                            "interface": "Ethernet0/2",
                                            "filtered_out": False,
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
