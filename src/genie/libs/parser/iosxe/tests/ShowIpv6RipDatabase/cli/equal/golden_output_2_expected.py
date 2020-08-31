expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:DB8:1:2::/64": {
                            "index": {
                                1: {
                                    "metric": 2,
                                    "interface": "GigabitEthernet2.200",
                                    "next_hop": "FE80::F816:3EFF:FE7B:437",
                                    "expire_time": "166",
                                }
                            }
                        },
                        "2001:DB8:1:3::/64": {
                            "index": {
                                1: {
                                    "metric": 2,
                                    "interface": "GigabitEthernet3.200",
                                    "next_hop": "FE80::F816:3EFF:FEFF:1E3D",
                                    "expire_time": "169",
                                }
                            }
                        },
                        "2001:DB8:2:3::/64": {
                            "index": {
                                1: {
                                    "metric": 2,
                                    "installed": True,
                                    "interface": "GigabitEthernet3.200",
                                    "next_hop": "FE80::F816:3EFF:FEFF:1E3D",
                                    "expire_time": "169",
                                },
                                2: {
                                    "metric": 2,
                                    "installed": True,
                                    "interface": "GigabitEthernet2.200",
                                    "next_hop": "FE80::F816:3EFF:FE7B:437",
                                    "expire_time": "166",
                                },
                            }
                        },
                    }
                }
            }
        }
    }
}
