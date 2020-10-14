expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "": {
                    "routes": {
                        "192.168.0.1/21": {
                            "index": {
                                1: {
                                    "status_codes": "* i",
                                    "path": "20450 65500 3549",
                                    "next_hop": "10.0.0.5",
                                    "localpref": 233451,
                                    "weight": 123450,
                                    "metric": 134430,
                                    "origin_codes": "i",
                                }
                            }
                        },
                        "192.168.0.2/21": {
                            "index": {
                                1: {
                                    "status_codes": "* i",
                                    "path": "20450 65500 3549",
                                    "next_hop": "10.0.0.5",
                                    "localpref": 1000,
                                    "weight": 0,
                                    "origin_codes": "i",
                                }
                            }
                        },
                        "192.168.0.3/21": {
                            "index": {
                                1: {
                                    "status_codes": "* i",
                                    "path": "20450 65500 3549",
                                    "next_hop": "10.0.0.5",
                                    "weight": 0,
                                    "metric": 0,
                                    "origin_codes": "i",
                                }
                            }
                        },
                        "192.168.0.4/21": {
                            "index": {
                                1: {
                                    "status_codes": "* i",
                                    "path": "20450 65500 3549",
                                    "next_hop": "10.0.0.5",
                                    "weight": 0,
                                    "origin_codes": "i",
                                }
                            }
                        },
                        "10.1.2.0/24": {
                            "index": {
                                1: {
                                    "status_codes": "*m",
                                    "path": "20450 65500 3549 {27016}",
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "weight": 0,
                                    "metric": 2219,
                                    "origin_codes": "e",
                                }
                            }
                        },
                        "10.1.3.0/24": {
                            "index": {
                                1: {
                                    "status_codes": "*rm",
                                    "path": "20450 65500 3549 {27016}",
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "weight": 0,
                                    "metric": 2219,
                                    "origin_codes": "e",
                                }
                            }
                        },
                    }
                }
            }
        }
    }
}
