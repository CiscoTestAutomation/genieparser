expected_output = {
    "vrf": {
        "vrf-a": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "40.1.1.0/24": {
                            "route": "40.1.1.0/24",
                            "active": True,
                            "route_preference": 200,
                            "metric": 0,
                            "source_protocol": "bgp",
                            "source_protocol_codes": "B",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.1.1.2",
                                        "updated": "00:00:06",
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
