expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv4": {
                    "rp": {
                        "rp_mappings": {
                            "STATIC_RP_V4 192.168.151.1 static": {
                                "rp_address_host": "?",
                                "protocol": "static",
                                "rp_address": "192.168.151.1",
                                "group": "STATIC_RP_V4",
                            },
                            "224.0.0.0/4 10.1.5.5 static": {
                                "rp_address_host": "?",
                                "protocol": "static",
                                "rp_address": "10.1.5.5",
                                "group": "224.0.0.0/4",
                            },
                        },
                        "rp_list": {
                            "10.1.5.5 SM static": {
                                "mode": "SM",
                                "address": "10.1.5.5",
                                "info_source_type": "static",
                            },
                            "192.168.151.1 SM static": {
                                "mode": "SM",
                                "address": "192.168.151.1",
                                "info_source_type": "static",
                            },
                        },
                        "static_rp": {
                            "192.168.151.1": {
                                "sm": {"policy_name": "STATIC_RP_V4", "override": True}
                            }
                        },
                    }
                }
            }
        }
    }
}
