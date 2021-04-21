expected_output = {
    "vrf": {
        "VRF1": {
            "address": {
                "10.64.4.4": {
                    "isconfigured": {
                        "True": {"address": "10.64.4.4", "isconfigured": True}
                    },
                    "type": {
                        "server": {
                            "address": "10.64.4.4",
                            "type": "server",
                            "vrf": "VRF1",
                        }
                    },
                }
            }
        },
        "default": {
            "address": {
                "10.4.1.1": {
                    "isconfigured": {
                        "True": {"address": "10.4.1.1", "isconfigured": True}
                    },
                    "type": {
                        "server": {
                            "address": "10.4.1.1",
                            "type": "server",
                            "vrf": "default",
                        }
                    },
                },
                "10.16.2.2": {
                    "isconfigured": {
                        "True": {"address": "10.16.2.2", "isconfigured": True}
                    },
                    "type": {
                        "server": {
                            "address": "10.16.2.2",
                            "type": "server",
                            "vrf": "default",
                        }
                    },
                },
                "10.2.1.1": {
                    "isconfigured": {
                        "True": {"address": "10.2.1.1", "isconfigured": True}
                    },
                    "type": {
                        "server": {
                            "address": "10.2.1.1",
                            "type": "server",
                            "vrf": "default",
                            "preferred": True,
                        }
                    },
                },
            }
        },
    }
}
