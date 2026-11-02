expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.5.5.0/24": {
                            "route": "10.5.5.0/24",
                            "active": True,
                            "route_preference": 1,
                            "metric": 0,
                            "source_protocol": "mobile",
                            "source_protocol_codes": "M",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.5.5.2",
                                        "updated": "00:00:12",
                                        "outgoing_interface": "Ethernet0/4",
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
