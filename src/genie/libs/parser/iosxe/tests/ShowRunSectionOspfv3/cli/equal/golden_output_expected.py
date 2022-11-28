expected_output = {
"ospfv3": {
        "instance": {
            5: {
                "database_control": {
                    "max_lsa": 3300, 
                    "ignore_time": 34
                    },
                "vrf": {
                    "default": {
                        "address_family": {
                            "ipv4": {
                                "max_control": {
                                    "max_lsa": 200, 
                                    "ignore_count": 2
                                    }
                            },
                            "ipv6": {
                                "redist_max": {
                                    "max_redist": 10101, 
                                    "warn": True
                                    },
                                "max_control": {
                                    "max_lsa": 4294967295,
                                    "ignore_count": 65535,
                                },
                            },
                        }
                    },
                    "red": {
                        "address_family": {
                            "ipv4": {
                                "max_control": {
                                    "max_lsa": 300000, 
                                    "reset_time": 11
                                    }
                            },
                            "ipv6": {
                                "redist_max": {
                                    "max_redist": 388899, 
                                    "threshold": 76
                                    },
                                "max_control": {
                                    "max_lsa": 200000
                                    },
                            },
                        }
                    },
                },
            }
        }
    }
}