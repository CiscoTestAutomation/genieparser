expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "65109": {
                            "areas": {
                                "0.0.0.8": {
                                    "interfaces": {
                                        "GigabitEthernet0/0/0": {
                                            "mpls": {
                                                "ldp": {
                                                    "autoconfig": False,
                                                    "autoconfig_area_id": "0.0.0.8",
                                                    "holddown_timer": False,
                                                    "igp_sync": True,
                                                    "state": "up",
                                                }
                                            }
                                        },
                                        "GigabitEthernet0/0/2": {
                                            "mpls": {
                                                "ldp": {
                                                    "autoconfig": False,
                                                    "autoconfig_area_id": "0.0.0.8",
                                                    "holddown_timer": False,
                                                    "igp_sync": True,
                                                    "state": "up",
                                                }
                                            }
                                        },
                                        "Loopback0": {
                                            "mpls": {
                                                "ldp": {
                                                    "autoconfig": False,
                                                    "autoconfig_area_id": "0.0.0.8",
                                                    "holddown_timer": False,
                                                    "igp_sync": False,
                                                    "state": "up",
                                                }
                                            }
                                        },
                                    }
                                }
                            },
                            "mpls": {
                                "ldp": {
                                    "autoconfig": False,
                                    "autoconfig_area_id": "0.0.0.8",
                                }
                            },
                        }
                    }
                }
            }
        }
    }
}
