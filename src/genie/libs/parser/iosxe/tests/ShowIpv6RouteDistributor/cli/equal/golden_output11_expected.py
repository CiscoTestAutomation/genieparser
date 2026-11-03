expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:db8:6::/64": {
                            "route": "2001:db8:6::/64",
                            "active": True,
                            "route_preference": 10,
                            "metric": 1,
                            "source_protocol": "lisp",
                            "source_protocol_codes": "la",
                            "next_hop": {},
                        }
                    }
                }
            }
        }
    }
}
