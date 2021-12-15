expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "10.169.197.252": {
                    "address_family": {
                        "": {
                            "advertised": {
                                "10.69.9.9/32": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "192.168.36.119",
                                            "origin_codes": "?",
                                            "weight": 0,
                                            "metric": 0,
                                            "path": "5918",
                                        },
                                        2: {
                                            "status_codes": "*b a",
                                            "next_hop": "192.168.36.120",
                                            "origin_codes": "?",
                                            "weight": 0,
                                            "metric": 0,
                                            "path": "5918",
                                        },
                                    }
                                }
                            },
                            "bgp_table_version": 2,
                            "local_router_id": "10.169.197.254",
                        }
                    }
                }
            }
        }
    }
}
