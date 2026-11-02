expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.7.7.0/24": {
                            "route": "10.7.7.0/24",
                            "active": True,
                            "route_preference": 10,
                            "metric": 1,
                            "source_protocol": "lisp",
                            "source_protocol_codes": "l",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.7.7.2",
                                        "updated": "00:00:12",
                                        "outgoing_interface": "Ethernet0/6",
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
