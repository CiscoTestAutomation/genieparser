expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.1.1.0/24": {
                            "route": "10.1.1.0/24",
                            "active": True,
                            "route_preference": 90,
                            "metric": 15360,
                            "source_protocol": "eigrp",
                            "source_protocol_codes": "D",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.1.1.2",
                                        "updated": "00:00:12",
                                        "outgoing_interface": "Ethernet0/0",
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
