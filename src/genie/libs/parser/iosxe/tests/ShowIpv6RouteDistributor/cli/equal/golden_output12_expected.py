expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:db8:7::1/128": {
                            "route": "2001:db8:7::1/128",
                            "active": True,
                            "route_preference": 0,
                            "metric": 0,
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Ethernet0/6": {
                                        "outgoing_interface": "Ethernet0/6"
                                    }
                                }
                            },
                        }
                    }
                }
            }
        }
    }
}
