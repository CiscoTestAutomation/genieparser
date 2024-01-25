expected_output = {
    "vrf": {
        "default": {
            "instance": {
                "1": {
                    "network": {
                        "4.4.4.4/32": {
                            "route_type": "Intra",
                            "cost": 21,
                            "area": "0",
                            "total_paths": 4,
                            "nexthop_ip": {
                                "13.1.19.2": {
                                    "interface": {
                                        "Ethernet0/2.19": {
                                            "label": 16004,
                                            "strict_label": 16104,
                                            "flags": ["RIB", "MFI"],
                                            "repair": {
                                                "nexthop_ip": "12.1.11.2",
                                                "interface": "Ethernet0/0.11",
                                                "label": 16004,
                                                "strict_label": 16104,
                                                "cost": 21,
                                                "flags": [
                                                    "RIB",
                                                    "Repair",
                                                    "PostConvrg",
                                                    "IntfDj",
                                                    "BcastDj",
                                                    "PrimPath",
                                                    "NodeProt",
                                                    "Downstr",
                                                    "LoadShare",
                                                ],
                                            },
                                        }
                                    }
                                },
                                "13.1.17.2": {
                                    "interface": {
                                        "Ethernet0/2.17": {
                                            "label": 16004,
                                            "strict_label": 16104,
                                            "flags": ["RIB", "MFI"],
                                            "repair": {
                                                "nexthop_ip": "12.1.14.2",
                                                "interface": "Ethernet0/0.14",
                                                "label": 16004,
                                                "strict_label": 16104,
                                                "cost": 21,
                                                "flags": [
                                                    "RIB",
                                                    "Repair",
                                                    "PostConvrg",
                                                    "IntfDj",
                                                    "BcastDj",
                                                    "PrimPath",
                                                    "NodeProt",
                                                    "Downstr",
                                                    "LoadShare",
                                                ],
                                            },
                                        }
                                    }
                                },
                                "13.1.20.2": {
                                    "interface": {
                                        "Ethernet0/2.20": {
                                            "label": 16004,
                                            "strict_label": 16104,
                                            "flags": ["RIB", "MFI"],
                                            "repair": {
                                                "nexthop_ip": "13.1.17.2",
                                                "interface": "Ethernet0/2.17",
                                                "label": 16004,
                                                "strict_label": 16104,
                                                "cost": 21,
                                                "flags": [
                                                    "RIB",
                                                    "Repair",
                                                    "PostConvrg",
                                                    "IntfDj",
                                                    "BcastDj",
                                                    "PrimPath",
                                                    "Downstr",
                                                    "LoadShare",
                                                ],
                                            },
                                        }
                                    }
                                },
                                "13.1.18.2": {
                                    "interface": {
                                        "Ethernet0/2.18": {
                                            "label": 16004,
                                            "strict_label": 16104,
                                            "flags": ["RIB", "MFI"],
                                            "repair": {
                                                "nexthop_ip": "13.1.12.2",
                                                "interface": "Ethernet0/2.12",
                                                "label": 16004,
                                                "strict_label": 16104,
                                                "cost": 21,
                                                "flags": [
                                                    "RIB",
                                                    "Repair",
                                                    "PostConvrg",
                                                    "IntfDj",
                                                    "BcastDj",
                                                    "PrimPath",
                                                    "Downstr",
                                                    "LoadShare",
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
