expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:DB8:1:3::/64": {
                            "index": {
                                1: {
                                    "metric": 2,
                                    "interface": "GigabitEthernet3.100",
                                    "next_hop": "FE80::F816:3EFF:FEFF:1E3D",
                                    "expire_time": "179",
                                }
                            }
                        },
                        "2001:DB8:2:3::/64": {
                            "index": {
                                1: {
                                    "metric": 2,
                                    "installed": True,
                                    "interface": "GigabitEthernet3.100",
                                    "next_hop": "FE80::F816:3EFF:FEFF:1E3D",
                                    "expire_time": "179",
                                }
                            }
                        },
                        "2001:DB8:2222:2222::/64": {
                            "index": {
                                1: {
                                    "metric": 7,
                                    "installed": True,
                                    "interface": "GigabitEthernet3.100",
                                    "next_hop": "FE80::F816:3EFF:FEFF:1E3D",
                                    "expire_time": "179",
                                }
                            }
                        },
                        "2001:DB8:2223:2223::/64": {
                            "index": {
                                1: {
                                    "metric": 6,
                                    "installed": True,
                                    "interface": "GigabitEthernet2.100",
                                    "next_hop": "FE80::F816:3EFF:FE7B:437",
                                    "expire_time": "173",
                                }
                            }
                        },
                    }
                }
            }
        }
    }
}
