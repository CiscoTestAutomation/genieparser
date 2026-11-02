expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.8.8.1/32": {
                            "route": "10.8.8.1/32",
                            "active": True,
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Ethernet0/7": {
                                        "outgoing_interface": "Ethernet0/7"
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
