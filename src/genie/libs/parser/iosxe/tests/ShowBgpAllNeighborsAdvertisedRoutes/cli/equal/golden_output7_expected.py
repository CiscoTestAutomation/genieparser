expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "10.3.4.5": {
                    "address_family": {
                        "ipv4 unicast": {
                            "advertised": {
                                "10.111.222.0/24": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "i",
                                            "weight": 32768,
                                            "localprf": 0
                                        }
                                    }
                                },
                                "10.111.223.3/3": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "i",
                                            "weight": 32768,
                                            "localprf": 0
                                        }
                                    }
                                },
                                "10.200.1.1/32": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "i",
                                            "weight": 32768,
                                            "localprf": 0
                                        }
                                    }
                                },
                                "15.16.17.0/20": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "i",
                                            "weight": 32768,
                                            "localprf": 0
                                        }
                                    }
                                }
                            },
                            "bgp_table_version": 87654,
                            "local_router_id": "10.1.2.3"
                        }
                    }
                }
            }
        }
    }
}