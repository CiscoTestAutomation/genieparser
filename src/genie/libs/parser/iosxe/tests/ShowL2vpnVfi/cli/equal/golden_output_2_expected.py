expected_output = {
    "vfi": {
        "vfi-sample": {
            "bd_vfi_name": "vfi-sample",
            "signaling": "LDP",
            "bridge_domain": {
                "30": {
                    "vfi": {
                        "10.16.2.2": {
                            "pw_id": {
                                "pseudowire1": {"split_horizon": True, "vc_id": 12}
                            }
                        },
                        "10.64.4.4": {
                            "pw_id": {
                                "pseudowire3": {"split_horizon": True, "vc_id": 14}
                            }
                        },
                        "10.36.3.3": {
                            "pw_id": {
                                "pseudowire2": {"split_horizon": True, "vc_id": 13}
                            }
                        },
                    },
                    "pseudo_port_interface": "pseudowire100004",
                    "attachment_circuits": {},
                }
            },
            "vpn_id": 2000,
            "state": "up",
            "type": "multipoint",
        }
    }
}
