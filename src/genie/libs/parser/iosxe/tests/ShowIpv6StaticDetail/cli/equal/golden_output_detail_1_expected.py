expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:2:2:2::2/128": {
                            "route": "2001:2:2:2::2/128",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "active": False,
                                        "next_hop": "2001:10:1:2::2",
                                        "resolved_outgoing_interface": "GigabitEthernet0/0",
                                        "resolved_paths_number": 1,
                                        "max_depth": 1,
                                        "preference": 3,
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "2001:20:1:2::2",
                                        "active": True,
                                        "outgoing_interface": "GigabitEthernet0/1",
                                        "preference": 1,
                                    },
                                    3: {
                                        "index": 3,
                                        "active": False,
                                        "next_hop": "2001:10:1:2::2",
                                        "outgoing_interface": "GigabitEthernet0/0",
                                        "rejected_by": "routing table",
                                        "preference": 11,
                                        "tag": 100,
                                        "track": 1,
                                        "track_state": "up",
                                    },
                                }
                            },
                        },
                        "2001:3:3:3::3/128": {
                            "route": "2001:3:3:3::3/128",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/3": {
                                        "outgoing_interface": "GigabitEthernet0/3",
                                        "active": True,
                                        "preference": 1,
                                    },
                                    "GigabitEthernet0/2": {
                                        "outgoing_interface": "GigabitEthernet0/2",
                                        "active": True,
                                        "preference": 1,
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
