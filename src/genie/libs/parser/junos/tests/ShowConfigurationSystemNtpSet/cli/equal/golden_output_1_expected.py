expected_output = {
    "vrf": {
        "default": {
            "address": {
                "10.2.2.2": {
                    "isconfigured": {
                        "True": {"address": "10.2.2.2", "isconfigured": True}
                    },
                    "type": {
                        "peer": {
                            "address": "10.2.2.2",
                            "type": "peer",
                            "vrf": "default",
                        }
                    },
                }
            }
        },
        "mgmt_junos": {
            "address": {
                "172.16.229.65": {
                    "isconfigured": {
                        "True": {"address": "172.16.229.65", "isconfigured": True}
                    },
                    "type": {
                        "server": {
                            "address": "172.16.229.65",
                            "type": "server",
                            "vrf": "mgmt_junos",
                        }
                    },
                },
                "172.16.229.66": {
                    "isconfigured": {
                        "True": {"address": "172.16.229.66", "isconfigured": True}
                    },
                    "type": {
                        "server": {
                            "address": "172.16.229.66",
                            "type": "server",
                            "vrf": "mgmt_junos",
                        }
                    },
                },
                "10.145.32.44": {
                    "isconfigured": {
                        "True": {"address": "10.145.32.44", "isconfigured": True}
                    },
                    "type": {
                        "server": {
                            "address": "10.145.32.44",
                            "type": "server",
                            "vrf": "mgmt_junos",
                        }
                    },
                },
            }
        },
    }
}
