expected_output = {
    "vrf": {
        "default": {
            "local_ldp_identifier": {
                "10.81.1.1:0": {
                    "targeted_hellos": {
                        "10.81.1.1": {
                            "172.16.25.16": {
                                "session": "tdp",
                                "active": False,
                                "tdp_id": "172.16.94.33:0",
                                "xmit": True,
                                "recv": True,
                            },
                            "172.16.94.33": {
                                "active": True,
                                "session": "ldp",
                                "ldp_id": "172.16.94.33:0",
                                "xmit": True,
                                "recv": True,
                            },
                        }
                    },
                    "discovery_sources": {
                        "interfaces": {
                            "Ethernet1/1/3": {
                                "session": "ldp",
                                "xmit": True,
                                "recv": True,
                                "ldp_id": {
                                    "172.16.25.77:0": {},
                                    "172.16.55.55:0": {},
                                    "172.16.81.44:0": {},
                                },
                            },
                            "ATM3/0.1": {
                                "session": "ldp",
                                "xmit": True,
                                "recv": True,
                                "ldp_id": {"192.168.240.7:2": {}},
                            },
                            "ATM0/0.2": {
                                "session": "tdp",
                                "xmit": True,
                                "recv": True,
                                "tdp_id": {"10.120.0.1:1": {}},
                            },
                        }
                    },
                }
            }
        }
    }
}
