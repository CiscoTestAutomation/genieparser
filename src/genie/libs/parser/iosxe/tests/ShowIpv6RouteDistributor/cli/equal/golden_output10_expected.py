expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:db8:5::/64": {
                            "route": "2001:db8:5::/64",
                            "active": True,
                            "route_preference": 250,
                            "metric": 1,
                            "source_protocol": "nhrp",
                            "source_protocol_codes": "H",
                            "next_hop": {},
                        }
                    }
                }
            }
        }
    }
}
