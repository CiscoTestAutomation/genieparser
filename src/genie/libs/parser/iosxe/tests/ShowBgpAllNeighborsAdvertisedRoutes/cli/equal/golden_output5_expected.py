expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "192.168.36.119": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "advertised": {},
                            "bgp_table_version": 334,
                            "local_router_id": "10.169.197.254",
                        },
                        "vpnv4 unicast RD 1234:150": {
                            "bgp_table_version": 334,
                            "local_router_id": "10.169.197.254",
                            "route_distinguisher": "1234:150",
                            "default_vrf": "VRF",
                            "advertised": {
                                "192.168.10.0": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "?",
                                            "weight": 32768,
                                            "localprf": 0,
                                        }
                                    }
                                }
                            },
                        },
                        "vpnv4 unicast RD 1234:4093": {
                            "bgp_table_version": 334,
                            "local_router_id": "10.169.197.254",
                            "route_distinguisher": "1234:4093",
                            "default_vrf": "VRF2",
                            "advertised": {
                                "10.229.11.11/32": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "192.168.10.253",
                                            "origin_codes": "?",
                                            "weight": 0,
                                            "metric": 0,
                                            "path": "1234 65555",
                                        }
                                    }
                                },
                                "192.168.10.0": {
                                    "index": {
                                        1: {
                                            "status_codes": "*>",
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "?",
                                            "weight": 32768,
                                            "localprf": 0,
                                        }
                                    }
                                },
                            },
                        },
                    }
                }
            }
        }
    }
}
