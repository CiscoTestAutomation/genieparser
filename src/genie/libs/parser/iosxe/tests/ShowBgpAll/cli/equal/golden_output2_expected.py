expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "vpnv4 unicast RD 200:1": {
                    "bgp_table_version": 56,
                    "default_vrf": "default",
                    "route_distinguisher": "200:1",
                    "route_identifier": "10.64.4.4",
                    "routes": {
                        "10.1.1.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "* i",
                                    "weight": 0,
                                },
                                2: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "*>i",
                                    "weight": 0,
                                },
                            }
                        },
                        "10.1.2.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "* i",
                                    "weight": 0,
                                },
                                2: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "*>i",
                                    "weight": 0,
                                },
                            }
                        },
                    },
                },
                "vpnv4 unicast RD 200:2": {
                    "bgp_table_version": 56,
                    "default_vrf": "default",
                    "route_distinguisher": "200:2",
                    "route_identifier": "10.64.4.4",
                    "routes": {
                        "10.1.1.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "*>i",
                                    "weight": 0,
                                },
                                2: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "* i",
                                    "weight": 0,
                                },
                            }
                        },
                        "10.1.2.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "*>i",
                                    "weight": 0,
                                },
                                2: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "* i",
                                    "weight": 0,
                                },
                            }
                        },
                        "10.1.3.0/24": {
                            "index": {
                                1: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "*>i",
                                    "weight": 0,
                                },
                                2: {
                                    "metric": 2219,
                                    "next_hop": "10.4.1.1",
                                    "localpref": 100,
                                    "origin_codes": "e",
                                    "path": "200 33299 51178 47751 {27016}",
                                    "status_codes": "* i",
                                    "weight": 0,
                                },
                            }
                        },
                    },
                },
            }
        }
    }
}
