expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "FF00::/8": {
                            "route": "FF00::/8",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Null0": {"outgoing_interface": "Null0"}
                                }
                            },
                        }
                    }
                }
            }
        }
    }
}
