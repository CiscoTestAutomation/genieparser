expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "10.106.101.1": {
                    "address_family": {
                        "ipv4 unicast": {
                            "advertised": {
                                "10.1.17.0/24": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "192.168.14.52",
                                            "origin_codes": "?",
                                            "weight": 0,
                                            "metric": 5288,
                                            "path": "65114",
                                        }
                                    }
                                },
                                "10.1.94.17/32": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "192.168.12.168",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "metric": 0,
                                            "path": "65115.1",
                                        }
                                    }
                                },
                                "10.1.94.18/32": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "192.168.12.168",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "metric": 0,
                                            "path": "65115.1 65115.1 65115.1",
                                        }
                                    }
                                },
                            },
                            "bgp_table_version": 1531435,
                            "local_router_id": "10.250.102.43",
                        }
                    }
                }
            }
        }
    }
}
