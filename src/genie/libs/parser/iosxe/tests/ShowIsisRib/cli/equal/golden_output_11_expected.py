expected_output = {
    "tag": {
        "1": {
            "prefix": {
                "15.0.0.15": {
                    "subnet": "32",
                    "prefix_attr": {
                        "x_flag": False,
                        "r_flag": False,
                        "n_flag": False
                    },
                    "strict_sid_bound_attribute": "SR_POLICY_STRICT",
                    "strict_sid_bound_attribute_te": True,
                    "via_interface": {
                        "TenGigabitEthernet0/0/5": {
                            "distance": 115,
                            "route_type": "L1",
                            "metric": 30,
                            "via_ip": "20.20.20.2",
                            "src_ip": "5.5.5.5",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 1,
                                "rtp_lsp_index": 4,
                                "rtp_lsp_version": 294
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "installed": True
                        },
                        "GigabitEthernet0/0/3": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 50,
                            "via_ip": "10.10.10.2",
                            "src_ip": "6.6.6.6",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 6,
                                "rtp_lsp_index": 10,
                                "rtp_lsp_version": 239
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            }
                        }
                    }
                }
            }
        }
    }
}