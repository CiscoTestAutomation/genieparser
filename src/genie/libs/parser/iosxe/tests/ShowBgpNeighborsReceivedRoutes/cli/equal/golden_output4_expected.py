expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "10.82.15.252": {
                    "address_family": {
                        "vpnv4": {
                            "received_routes": {},
                            "bgp_table_version": 18,
                            "local_router_id": "100.127.142.250"
                        },
                        "vpnv4 RD 65357:201": {
                            "bgp_table_version": 18,
                            "local_router_id": "100.127.142.250",
                            "route_distinguisher": "65357:201",
                            "default_vrf": "WAN_VRF",
                            "received_routes": {
                                "0.0.0.0": {
                                    "index": {
                                        1: {
                                            "status_codes": "",
                                            "next_hop": "10.82.15.252",
                                            "origin_codes": "i",
                                            "weight": 0,
                                            "path": "0 65500 65340"
                                        }
                                    }
                                },
                                "10.1.1.0/24": {
                                    "index": {
                                        1: {
                                            "status_codes": "",
                                            "next_hop": "10.82.15.252",
                                            "origin_codes": "?",
                                            "weight": 0,
                                            "path": "0 65500 65340"
                                        }
                                    }
                                },
                                "10.1.2.0/24": {
                                    "index": {
                                        1: {
                                            "status_codes": "",
                                            "next_hop": "10.82.15.252",
                                            "origin_codes": "?",
                                            "weight": 0,
                                            "path": "0 65500 65340"
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