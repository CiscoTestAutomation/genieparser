expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "10.186.0.2": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "bgp_table_version": 66,
                            "local_router_id": "10.64.4.4",
                            "received_routes": {},
                        },
                        "vpnv4 unicast RD 300:1": {
                            "bgp_table_version": 66,
                            "default_vrf": "VRF1",
                            "local_router_id": "10.64.4.4",
                            "received_routes": {
                                "10.169.1.0/24": {
                                    "index": {
                                        1: {
                                            "metric": 2219,
                                            "next_hop": "10.4.6.6",
                                            "origin_codes": "e",
                                            "path": "300 33299 51178 47751 {27016}",
                                            "status_codes": "*",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.169.2.0/24": {
                                    "index": {
                                        1: {
                                            "metric": 2219,
                                            "next_hop": "10.4.6.6",
                                            "origin_codes": "e",
                                            "path": "300 33299 51178 47751 {27016}",
                                            "status_codes": "*",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.169.3.0/24": {
                                    "index": {
                                        1: {
                                            "metric": 2219,
                                            "next_hop": "10.4.6.6",
                                            "origin_codes": "e",
                                            "path": "300 33299 51178 47751 {27016}",
                                            "status_codes": "*",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.169.4.0/24": {
                                    "index": {
                                        1: {
                                            "metric": 2219,
                                            "next_hop": "10.4.6.6",
                                            "origin_codes": "e",
                                            "path": "300 33299 51178 47751 {27016}",
                                            "status_codes": "*",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "10.169.5.0/24": {
                                    "index": {
                                        1: {
                                            "metric": 2219,
                                            "next_hop": "10.4.6.6",
                                            "origin_codes": "e",
                                            "path": "300 33299 51178 47751 {27016}",
                                            "status_codes": "*",
                                            "weight": 0,
                                        }
                                    }
                                },
                            },
                            "route_distinguisher": "300:1",
                        },
                    }
                }
            }
        }
    }
}
