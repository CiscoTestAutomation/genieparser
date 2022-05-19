expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.1.1.0/24": {
                            "route": "10.1.1.0/24",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "active": True,
                                        "next_hop": "10.16.0.2",
                                        "outgoing_interface": "GigabitEthernet2.2",
                                        "preference": 1,
                                        "owner_code": "M",
                                    },
                                    2: {
                                        "index": 2,
                                        "active": False,
                                        "next_hop": "192.168.1.1",
                                        "outgoing_interface": "GigabitEthernet1",
                                        "preference": 3,
                                        "owner_code": "M",
                                    },
                                }
                            },
                        },
                        "10.186.1.0/24": {
                            "route": "10.186.1.0/24",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "active": True,
                                        "next_hop": "192.168.1.1",
                                        "outgoing_interface": "GigabitEthernet1",
                                        "preference": 3,
                                        "owner_code": "M",
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
