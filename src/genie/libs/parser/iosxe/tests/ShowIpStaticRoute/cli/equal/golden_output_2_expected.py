expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.16.2.2/32": {
                            "route": "10.16.2.2/32",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "active": True,
                                        "next_hop": "10.1.2.2",
                                        "outgoing_interface": "GigabitEthernet0/0",
                                        "preference": 1,
                                        "owner_code": "M",
                                    },
                                    2: {
                                        "index": 2,
                                        "active": False,
                                        "next_hop": "10.186.2.2",
                                        "outgoing_interface": "GigabitEthernet0/1",
                                        "preference": 2,
                                        "owner_code": "M",
                                    },
                                    3: {
                                        "index": 3,
                                        "active": False,
                                        "next_hop": "10.186.2.2",
                                        "preference": 3,
                                        "owner_code": "M",
                                    },
                                }
                            },
                        },
                        "10.36.3.3/32": {
                            "route": "10.36.3.3/32",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/2": {
                                        "active": True,
                                        "outgoing_interface": "GigabitEthernet0/2",
                                        "preference": 1,
                                        "owner_code": "M",
                                    },
                                    "GigabitEthernet0/3": {
                                        "active": True,
                                        "outgoing_interface": "GigabitEthernet0/3",
                                        "preference": 1,
                                        "owner_code": "M",
                                    },
                                }
                            },
                        },
                    }
                }
            }
        }
    }
}
