expected_output = {
    "vrf": {
        "default": {
            "address": {
                "10.16.2.2": {
                    "isconfigured": {
                        "True": {"address": "10.16.2.2", "isconfigured": True}
                    },
                    "type": {
                        "server": {
                            "address": "10.16.2.2",
                            "source": "Loopback0",
                            "type": "server",
                            "vrf": "default",
                        }
                    },
                },
                "10.36.3.3": {
                    "isconfigured": {
                        "True": {"address": "10.36.3.3", "isconfigured": True}
                    },
                    "type": {
                        "server": {
                            "address": "10.36.3.3",
                            "type": "server",
                            "vrf": "default",
                        }
                    },
                },
            }
        }
    }
}
