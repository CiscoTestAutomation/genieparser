expected_output = {
    "vfi": {
        "vfi-sample": {
            "ve_range": 15,
            "ve_id": 1,
            "type": "multipoint",
            "bd_vfi_name": "vfi-sample",
            "state": "up",
            "bridge_domain": {
                "30": {
                    "vfi": {
                        "10.36.3.3": {
                            "pw_id": {
                                "pseudowire100006": {
                                    "local_label": 29,
                                    "remote_label": 20,
                                    "ve_id": 3,
                                    "split_horizon": True,
                                }
                            }
                        },
                        "10.64.4.4": {
                            "pw_id": {
                                "pseudowire100007": {
                                    "local_label": 30,
                                    "remote_label": 24015,
                                    "ve_id": 4,
                                    "split_horizon": True,
                                }
                            }
                        },
                        "10.16.2.2": {
                            "pw_id": {
                                "pseudowire100005": {
                                    "local_label": 28,
                                    "remote_label": 24,
                                    "ve_id": 2,
                                    "split_horizon": True,
                                }
                            }
                        },
                    },
                    "attachment_circuits": {},
                }
            },
            "rt": ["100:2000", "100:100"],
            "vpn_id": 2000,
            "signaling": "BGP",
            "rd": "100:2000",
        }
    }
}
