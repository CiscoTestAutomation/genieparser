expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:db8:8::/64": {
                            "route": "2001:db8:8::/64",
                            "active": True,
                            "route_preference": 160,
                            "metric": 1,
                            "source_protocol": "odr",
                            "source_protocol_codes": "o",
                            "next_hop": {},
                        }
                    }
                }
            }
        }
    }
}
