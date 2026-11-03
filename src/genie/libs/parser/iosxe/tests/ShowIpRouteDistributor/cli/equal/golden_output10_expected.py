expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.3.3.0/24": {
                            "route": "10.3.3.0/24",
                            "active": True,
                            "route_preference": 120,
                            "metric": 1,
                            "source_protocol": "rip",
                            "source_protocol_codes": "R",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.3.3.2",
                                        "updated": "00:00:12",
                                        "outgoing_interface": "Ethernet0/2",
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
