expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "10.193.16.177": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "bgp_table_version": 44278653,
                            "local_router_id": "203.62.187.142",
                            "received_routes": {}
                        },
                        "vpnv4 unicast RD 9268:10189": {
                            "bgp_table_version": 44278653,
                            "default_vrf": "tel-189",
                            "local_router_id": "203.62.187.142",
                            "received_routes": {
                                "172.25.193.0/24": {
                                    "index": {
                                        1: {
                                            "metric": 0,
                                            "next_hop": "10.193.16.177",
                                            "origin_codes": "?",
                                            "path": "65100",
                                            "status_codes": "*",
                                            "weight": 0
                                        }
                                    }
                                },
                                "172.26.193.0/24": {
                                    "index": {
                                        1: {
                                            "metric": 0,
                                            "next_hop": "10.193.16.177",
                                            "origin_codes": "?",
                                            "path": "65100",
                                            "status_codes": "*",
                                            "weight": 0
                                        }
                                    }
                                }
                            },
                            "route_distinguisher": "9268:10189"
                        }
                    }
                }
            }
        }
    }
}