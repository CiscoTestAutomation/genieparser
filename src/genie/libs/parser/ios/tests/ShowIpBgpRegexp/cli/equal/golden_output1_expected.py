expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "": {
                    "routes": {
                        "10.4.1.1/32": {
                            "index": {
                                1: {
                                    "metric": 0,
                                    "next_hop": "0.0.0.0",
                                    "origin_codes": "i",
                                    "status_codes": "*>",
                                    "weight": 32768,
                                }
                            }
                        },
                        "10.16.2.2/32": {
                            "index": {
                                1: {
                                    "localpref": 100,
                                    "metric": 0,
                                    "next_hop": "10.16.2.2",
                                    "origin_codes": "i",
                                    "status_codes": "r>i",
                                    "weight": 0,
                                }
                            }
                        },
                    }
                }
            }
        }
    }
}
