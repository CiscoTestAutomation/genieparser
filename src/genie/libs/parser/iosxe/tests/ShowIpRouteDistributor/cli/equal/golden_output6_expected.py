expected_output = {
    "vrf": {
        "foo": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "20.0.0.0/8": {
                            "route": "20.0.0.0/8",
                            "active": True,
                            "route_preference": 1,
                            "metric": 0,
                            "source_protocol": "static",
                            "source_protocol_codes": "S +",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.0.0.2",
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
