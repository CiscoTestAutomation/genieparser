expected_output = {
    "vrf": {
        "vrf-a": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "10:1:1::/64": {
                            "route": "10:1:1::/64",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Ethernet0/0": {
                                        "outgoing_interface": "Ethernet0/0",
                                    },
                                },
                            },
                        },
                        "20:1:1::/64": {
                            "route": "20:1:1::/64",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Ethernet0/1": {
                                        "outgoing_interface": "Ethernet0/1",
                                        "vrf": "vrf-b",
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
