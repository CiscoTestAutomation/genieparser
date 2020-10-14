expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "172.16.1.1": {
                    "address_family": {
                        "vpnv4": {
                            "advertised": {},
                            "bgp_table_version": 166,
                            "local_router_id": "172.16.1.1",
                        },
                        "vpnv4 RD 65000:100": {
                            "bgp_table_version": 166,
                            "local_router_id": "172.16.1.1",
                            "route_distinguisher": "65000:100",
                            "default_vrf": "TEST-VPN",
                            "advertised": {
                                "192.168.1.0": {
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
                    }
                }
            }
        }
    }
}
