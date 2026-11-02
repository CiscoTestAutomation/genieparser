expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.2.2.0/24": {
                            "route": "10.2.2.0/24",
                            "active": True,
                            "route_preference": 115,
                            "metric": 20,
                            "source_protocol": "isis",
                            "source_protocol_codes": "i L1",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.2.2.2",
                                        "updated": "00:00:12",
                                        "outgoing_interface": "Ethernet0/1",
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
