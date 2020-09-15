expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "rp": {
                        "rp_list": {
                            "10.36.3.3 BIDIR static": {
                                "info_source_type": "static",
                                "address": "10.36.3.3",
                                "mode": "BIDIR",
                            },
                            "10.145.0.3 SM autorp": {
                                "address": "10.145.0.3",
                                "info_source_address": "10.145.0.2",
                                "bsr_version": "v2v1",
                                "info_source_type": "autorp",
                                "expiration": "00:02:40",
                                "up_time": "00:22:08",
                                "mode": "SM",
                            },
                            "10.16.2.2 SM bootstrap": {
                                "address": "10.16.2.2",
                                "info_source_address": "10.64.4.4",
                                "bsr_version": "v2",
                                "info_source_type": "bootstrap",
                                "expiration": "00:02:03",
                                "up_time": "00:00:35",
                                "mode": "SM",
                            },
                            "10.36.3.3 SM bootstrap": {
                                "address": "10.36.3.3",
                                "info_source_address": "10.64.4.4",
                                "bsr_version": "v2",
                                "info_source_type": "bootstrap",
                                "expiration": "00:02:19",
                                "up_time": "00:00:19",
                                "mode": "SM",
                            },
                        },
                        "rp_mappings": {
                            "224.0.0.0/4 10.145.0.3 autorp": {
                                "group": "224.0.0.0/4",
                                "rp_address_host": "?",
                                "protocol": "autorp",
                                "expiration": "00:02:40",
                                "rp_address": "10.145.0.3",
                                "up_time": "00:22:08",
                            },
                            "224.0.0.0/4 10.16.2.2 bootstrap": {
                                "group": "224.0.0.0/4",
                                "rp_address_host": "?",
                                "hold_time": 150,
                                "priority": 10,
                                "protocol": "bootstrap",
                                "expiration": "00:02:03",
                                "rp_address": "10.16.2.2",
                                "up_time": "00:00:35",
                            },
                            "224.0.0.0/4 10.36.3.3 bootstrap": {
                                "group": "224.0.0.0/4",
                                "rp_address_host": "?",
                                "hold_time": 150,
                                "priority": 5,
                                "protocol": "bootstrap",
                                "expiration": "00:02:19",
                                "rp_address": "10.36.3.3",
                                "up_time": "00:00:19",
                            },
                            "224.0.0.0/4 10.36.3.3 static": {
                                "group": "224.0.0.0/4",
                                "protocol": "static",
                                "rp_address": "10.36.3.3",
                                "rp_address_host": "?",
                            },
                        },
                        "static_rp": {"10.36.3.3": {"bidir": {}}},
                        "bsr": {
                            "rp": {
                                "rp_address": "10.16.2.2",
                                "up_time": "00:22:08",
                                "group_policy": "224.0.0.0/4",
                            }
                        },
                    }
                }
            }
        }
    }
}
