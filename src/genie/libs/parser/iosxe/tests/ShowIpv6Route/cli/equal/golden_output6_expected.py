expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:2:2:2::2/128": {
                            "active": True,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {"index": 1, "next_hop": "2001:DB8:1:1::2"}
                                }
                            },
                            "source_protocol": "local_connected",
                            "metric": 0,
                            "route_preference": 200,
                            "source_protocol_codes": "LC",
                            "route": "2001:2:2:2::2/128",
                        },
                        "2001:db8:cdc9:1b9::/64": {
                            "active": True,
                            "metric": 2219,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.4.1.1",
                                        "vrf": "default",
                                    }
                                }
                            },
                            "route": "2001:db8:cdc9:1b9::/64",
                            "route_preference": 200,
                            "source_protocol": "bgp",
                            "source_protocol_codes": "B",
                        },
                    }
                }
            }
        }
    }
}
