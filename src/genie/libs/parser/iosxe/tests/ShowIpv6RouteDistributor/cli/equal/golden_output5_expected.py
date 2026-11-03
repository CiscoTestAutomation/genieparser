expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:db8:1::/64": {
                            "route": "2001:db8:1::/64",
                            "active": True,
                            "route_preference": 90,
                            "metric": 15360,
                            "source_protocol": "eigrp",
                            "source_protocol_codes": "D",
                            "next_hop": {},
                        }
                    }
                }
            }
        }
    }
}
