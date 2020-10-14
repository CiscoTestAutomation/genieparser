expected_output = {
    "vrf": {
        "default": {
            "local_ldp_identifier": {
                "10.66.12.12:0": {
                    "discovery_sources": {
                        "interfaces": {
                            "ATM1/1/0.1": {
                                "session": "tdp",
                                "xmit": True,
                                "recv": True,
                                "tdp_id": {"10.229.11.11:0": {}},
                            }
                        }
                    }
                }
            }
        },
        "vpn2": {
            "local_ldp_identifier": {
                "10.64.0.2:0": {
                    "discovery_sources": {
                        "interfaces": {
                            "ATM3/0/0.2": {
                                "session": "ldp",
                                "xmit": True,
                                "recv": True,
                                "ldp_id": {"10.19.14.14:0": {}},
                            }
                        }
                    }
                }
            }
        },
        "vpn1": {
            "local_ldp_identifier": {
                "10.94.0.2:0": {
                    "discovery_sources": {
                        "interfaces": {
                            "ATM3/0/0.1": {
                                "session": "ldp",
                                "xmit": True,
                                "recv": True,
                                "ldp_id": {"10.19.14.14:0": {}},
                            }
                        }
                    }
                }
            }
        },
    }
}
