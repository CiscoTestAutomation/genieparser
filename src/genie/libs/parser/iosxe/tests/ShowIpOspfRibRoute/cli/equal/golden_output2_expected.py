expected_output = {
    "vrf": {
        "default": {
            "instance": {
                "100": {
                    "network": {
                        "13.0.0.0/16": {
                            "route_type": "Ext2",
                            "cost": 20,
                            "fwd_cost": 1,
                            "tag": 0,
                            "area": "N/A",
                            "total_paths": 2,
                            "nexthop_ip": {
                                "100.5.0.2": {
                                    "interface": {
                                        "FiveGigabitEthernet0/0/2": {
                                            "label": 1048578,
                                            "strict_label": 1048578,
                                            "flags": ["RIB"],
                                            "repair": {
                                                "nexthop_ip": "100.6.0.2",
                                                "interface": "FiveGigabitEthernet0/0/3",
                                                "label": 1048578,
                                                "strict_label": 1048578,
                                                "cost": 1,
                                                "flags": [
                                                    "RIB",
                                                    "Repair",
                                                    "IntfDj",
                                                    "BcastDj",
                                                    "PrimPath",
                                                    "Downstr",
                                                ],
                                            },
                                        }
                                    }
                                },
                                "100.6.0.2": {
                                    "interface": {
                                        "FiveGigabitEthernet0/0/3": {
                                            "label": 1048578,
                                            "strict_label": 1048578,
                                            "flags": ["RIB"],
                                            "repair": {
                                                "nexthop_ip": "100.5.0.2",
                                                "interface": "FiveGigabitEthernet0/0/2",
                                                "label": 1048578,
                                                "strict_label": 1048578,
                                                "cost": 1,
                                                "flags": [
                                                    "RIB",
                                                    "Repair",
                                                    "IntfDj",
                                                    "BcastDj",
                                                    "PrimPath",
                                                    "Downstr",
                                                ],
                                            },
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
}
