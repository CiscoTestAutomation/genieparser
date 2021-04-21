expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:2:2:2::2/128": {
                            "route": "2001:2:2:2::2/128",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Null0": {
                                        "outgoing_interface": "Null0",
                                        "active": True,
                                        "preference": 2,
                                    }
                                }
                            },
                        },
                        "2001:3:3:3::3/128": {
                            "route": "2001:3:3:3::3/128",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Null0": {
                                        "outgoing_interface": "Null0",
                                        "active": True,
                                        "preference": 3,
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
