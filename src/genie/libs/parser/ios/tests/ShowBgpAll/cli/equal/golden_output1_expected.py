expected_output = {
    "vrf": {
        "evpn1": {
            "address_family": {
                "vpnv4 unicast RD 65535:1": {
                    "bgp_table_version": 5,
                    "default_vrf": "evpn1",
                    "route_distinguisher": "65535:1",
                    "route_identifier": "10.21.33.33",
                    "af_private_import_to_address_family": "L2VPN E-VPN",
                    "pfx_count": 2,
                    "pfx_limit": 1000,
                    "routes": {
                        "10.36.3.0/24": {
                            "index": {
                                1: {
                                    "metric": 0,
                                    "next_hop": "10.36.3.254",
                                    "origin_codes": "?",
                                    "path": "65530",
                                    "status_codes": "*",
                                    "weight": 0,
                                },
                                2: {
                                    "next_hop": "0.0.0.0",
                                    "origin_codes": "?",
                                    "weight": 32768,
                                    "status_codes": "*>",
                                    "metric": 0,
                                },
                            }
                        },
                        "10.1.1.0/24": {
                            "index": {
                                1: {
                                    "metric": 0,
                                    "next_hop": "0.0.0.0",
                                    "origin_codes": "?",
                                    "weight": 32768,
                                    "status_codes": "*>",
                                }
                            }
                        },
                    },
                },
                "l2vpn e-vpn RD 65535:1": {
                    "bgp_table_version": 4,
                    "default_vrf": "evpn1",
                    "route_distinguisher": "65535:1",
                    "route_identifier": "10.21.33.33",
                    "routes": {
                        "[5][65535:1][0][24][10.36.3.0]/17": {
                            "index": {
                                1: {
                                    "metric": 0,
                                    "next_hop": "0.0.0.0",
                                    "origin_codes": "?",
                                    "weight": 32768,
                                    "status_codes": "*>",
                                },
                                2: {
                                    "metric": 0,
                                    "next_hop": "10.36.3.254",
                                    "origin_codes": "?",
                                    "path": "65530",
                                    "status_codes": "*",
                                    "weight": 0,
                                },
                            }
                        },
                        "[5][65535:1][0][24][10.1.1.0]/17": {
                            "index": {
                                1: {
                                    "metric": 0,
                                    "next_hop": "0.0.0.0",
                                    "origin_codes": "?",
                                    "weight": 32768,
                                    "status_codes": "*>",
                                }
                            }
                        },
                    },
                },
            }
        }
    }
}
