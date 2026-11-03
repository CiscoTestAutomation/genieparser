expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:db8:4::/64": {
                            "route": "2001:db8:4::/64",
                            "active": True,
                            "route_preference": 1,
                            "metric": 0,
                            "source_protocol": "mobile",
                            "source_protocol_codes": "M",
                            "next_hop": {},
                        }
                    }
                }
            }
        }
    }
}
