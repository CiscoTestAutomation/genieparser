expected_output = {
    "vrf": {
        "vrf-b": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "40.1.1.0/24": {
                            "route": "40.1.1.0/24",
                            "active": True,
                            "metric": 20,
                            "route_preference": 110,
                            "source_protocol_codes": "O E2+",
                            "source_protocol": "ospf",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.1.1.2",
                                        "updated": "00:04:20",
                                        "outgoing_interface": "Ethernet0/0",
                                        "vrf": "vrf-a",
                                    }
                                }
                            },
                        },
                        "192.168.0.1/32": {
                            "route": "192.168.0.1/32",
                            "active": True,
                            "metric": 20,
                            "route_preference": 110,
                            "source_protocol_codes": "O E2+",
                            "source_protocol": "ospf",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.1.1.2",
                                        "updated": "00:04:20",
                                        "outgoing_interface": "Ethernet0/0",
                                        "vrf": "vrf-a",
                                    }
                                }
                            },
                        },
                    }
                }
            }
        }
    }
}
