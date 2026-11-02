expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:db8:2::/64": {
                            "route": "2001:db8:2::/64",
                            "active": True,
                            "route_preference": 115,
                            "metric": 20,
                            "source_protocol": "isis",
                            "source_protocol_codes": "I1",
                            "next_hop": {},
                        }
                    }
                }
            }
        }
    }
}
