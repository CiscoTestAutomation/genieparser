expected_output = {
    "vrf": {
        "v2": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.10.10.0/24": {
                            "route": "10.10.10.0/24",
                            "active": True,
                            "route_preference": 1,
                            "metric": 0,
                            "source_protocol": "static",
                            "source_protocol_codes": "S +",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "192.168.1.2",
                                        "vrf": "v1",
                                        "outgoing_interface": "Loopback10",
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
