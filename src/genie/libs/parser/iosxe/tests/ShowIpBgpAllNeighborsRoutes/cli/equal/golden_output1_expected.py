expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "10.1.1.1": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "bgp_table_version": 13,
                            "local_router_id": "10.5.5.5",
                            "routes": {},
                        },
                        "vpnv4 unicast RD 65000:100": {
                            "bgp_table_version": 13,
                            "default_vrf": "VRF100",
                            "local_router_id": "10.5.5.5",
                            "route_distinguisher": "65000:100",
                            "routes": {
                                "192.168.121.0": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 0,
                                            "next_hop": "10.6.6.6",
                                            "origin_codes": "?",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "192.168.122.0": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 0,
                                            "next_hop": "10.6.6.6",
                                            "origin_codes": "i",
                                            "path": "65001",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                            },
                        },
                        "vpnv4 unicast RD 65000:200": {
                            "bgp_table_version": 13,
                            "default_vrf": "VRF200",
                            "local_router_id": "10.5.5.5",
                            "route_distinguisher": "65000:200",
                            "routes": {
                                "192.168.221.0": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 0,
                                            "next_hop": "10.6.6.6",
                                            "origin_codes": "?",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "192.168.222.0": {
                                    "index": {
                                        1: {
                                            "localprf": 100,
                                            "metric": 0,
                                            "next_hop": "10.6.6.6",
                                            "origin_codes": "i",
                                            "path": "65001",
                                            "path_type": "i",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                            },
                        },
                    }
                }
            }
        }
    },
    "total_num_of_prefixes": 4
}
