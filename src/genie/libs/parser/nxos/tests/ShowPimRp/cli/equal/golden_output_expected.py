expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "rp": {
                        "rp_list": {
                            "22.22.22.22 SM static": {
                                "address": "22.22.22.22",
                                "info_source_type": "static",
                                "up_time": "00:29:22",
                                "df_ordinal": 0,
                                "priority": 255,
                                "mode": "SM",
                                "group_ranges": "225.0.0.0/8"
                            }
                        },
                        "static_rp": {
                            "22.22.22.22": {
                                "sm": {
                                    "policy_name": "225.0.0.0/8"
                                }
                            }
                        },
                        "rp_mappings": {
                            "225.0.0.0/8 22.22.22.22 static": {
                                "rp_address": "22.22.22.22",
                                "protocol": "static",
                                "group": "225.0.0.0/8",
                                "up_time": "00:29:22"
                            }
                        }
                    }
                }
            }
        }
    }
}
