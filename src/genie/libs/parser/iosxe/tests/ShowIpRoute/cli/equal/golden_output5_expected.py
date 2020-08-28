expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.1.1.0/24": {
                            "active": True,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.4.1.1",
                                        "updated": "01:40:40",
                                    }
                                }
                            },
                            "source_protocol": "bgp",
                            "metric": 2219,
                            "route_preference": 200,
                            "source_protocol_codes": "B",
                            "route": "10.1.1.0/24",
                        }
                    }
                }
            }
        }
    }
}
