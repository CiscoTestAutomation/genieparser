expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:db8:3::/64": {
                            "route": "2001:db8:3::/64",
                            "active": True,
                            "route_preference": 120,
                            "metric": 1,
                            "source_protocol": "rip",
                            "source_protocol_codes": "R",
                            "next_hop": {},
                        }
                    }
                }
            }
        }
    }
}
