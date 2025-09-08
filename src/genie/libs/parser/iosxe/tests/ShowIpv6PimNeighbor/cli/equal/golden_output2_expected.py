expected_output = {
    "vrf": {
        "vrf1": {
            "interfaces": {
                "Port-channel10": {
                    "address_family": {
                        "ipv6": {
                            "neighbors": {
                                "FE80::20:1:2": {
                                    "bidir_capable": True,
                                    "designated_router": True,
                                    "dr_priority": 1,
                                    "expiration": "00:01:34",
                                    "genid_capable": True,
                                    "interface": "Port-channel10",
                                    "up_time": "00:03:08"
                                }
                            }
                        }
                    }
                },
                "Tunnel2": {
                    "address_family": {
                        "ipv6": {
                            "neighbors": {
                                "::FFFF:4.4.4.4": {
                                    "bidir_capable": True,
                                    "dr_priority": 1,
                                    "expiration": "00:01:26",
                                    "genid_capable": True,
                                    "interface": "Tunnel2",
                                    "up_time": "00:02:18"
                                },
                                "::FFFF:6.6.6.6": {
                                    "bidir_capable": True,
                                    "designated_router": True,
                                    "dr_priority": 1,
                                    "expiration": "00:01:25",
                                    "genid_capable": True,
                                    "interface": "Tunnel2",
                                    "up_time": "00:02:17"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
