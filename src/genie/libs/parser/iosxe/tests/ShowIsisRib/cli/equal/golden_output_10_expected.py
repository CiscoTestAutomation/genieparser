expected_output = {
    "tag": {
        "1": {
            "prefix": {
                "3.3.3.0": {
                    "subnet": "24",
                    "prefix_attr": {
                        "x_flag": False,
                        "r_flag": False,
                        "n_flag": False
                    },
                    'strict_sid_bound_attribute_te': False,
                    "via_interface": {
                        "TenGigabitEthernet0/0/5": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 83886080,
                            "via_ip": "13.13.1.2",
                            "src_ip": "6.6.6.6",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 37,
                                "rtp_lsp_index": 21,
                                "rtp_lsp_version": 4000
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "srgb": 16000,
                            "srgb_range": 8000,
                            "installed": True
                        }
                    }
                }
            }
        }
    }
}