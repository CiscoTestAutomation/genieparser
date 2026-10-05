expected_output = {
    "vrf": {
        "vrf-b": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "40:1:1::/64": {
                            "route": "40:1:1::/64",
                            "active": True,
                            "metric": 20,
                            "route_preference": 110,
                            "source_protocol_codes": "O",
                            "source_protocol": "ospf",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "FE80::A8BB:CCFF:FE02:7800",
                                        "outgoing_interface": "Ethernet0/0",
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
