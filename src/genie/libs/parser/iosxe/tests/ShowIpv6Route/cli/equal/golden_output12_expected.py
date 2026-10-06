expected_output = {
    "vrf": {
        "vrf-b": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "40:1:1::/64": {
                            "route": "40:1:1::/64",
                            "active": True,
                            "metric": 0,
                            "route_preference": 200,
                            "source_protocol_codes": "B",
                            "source_protocol": "bgp",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10:1:1::2",
                                        "vrf": "vrf-a",
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
