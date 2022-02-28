expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "2001:2:2:2::2": {
                    "address_family": {
                        "ipv6 unicast": {
                            "bgp_table_version": 6,
                            "local_router_id": "10.4.1.1",
                            "routes": {
                                "2001:2:2:2::2/128": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 0,
                                            "next_hop": "2001:2:2:2::2",
                                            "origin_codes": "i",
                                            "path_type": "i",
                                            "status_codes": "r>",
                                            "weight": 0,
                                        }
                                    }
                                }
                            },
                        },
                        "vpnv6 unicast": {
                            "bgp_table_version": 6,
                            "local_router_id": "10.4.1.1",
                            "routes": {},
                        },
                        "vpnv6 unicast RD 65000:1": {
                            "bgp_table_version": 6,
                            "default_vrf": "VRF1",
                            "local_router_id": "10.4.1.1",
                            "route_distinguisher": "65000:1",
                            "routes": {
                                "2001:2:2:2::2/128": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 0,
                                            "next_hop": "2001:2:2:2::2",
                                            "origin_codes": "i",
                                            "path_type": "i",
                                            "status_codes": "r>",
                                            "weight": 0,
                                        }
                                    }
                                }
                            },
                        },
                    }
                }
            }
        }
    },
    "total_num_of_prefixes": 2
}
