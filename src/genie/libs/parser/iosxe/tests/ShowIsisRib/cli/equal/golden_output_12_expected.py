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
                    "prefix_sid_index": 105,
                    "sid_bound_attribute": "SR_POLICY",
                    "strict_spf_sid_index": 505,
                    "strict_sid_bound_attribute_te": True,
                    "via_interface": {
                        "Tunnel65827": {
                            "distance": 115,
                            "route_type": "L1",
                            "metric": 30,
                            "via_ip": "15.0.0.15",
                            "src_ip": "5.5.5.5",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 4,
                                "rtp_lsp_index": 4,
                                "rtp_lsp_version": 338
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "srgb": 16000,
                            "srgb_range": 8000,
                            "prefix_sid_index": 105,
                            "non_strict_sid_flags": {
                                "r_flag": False,
                                "n_flag": False,
                                "p_flag": False,
                                "e_flag": False,
                                "v_flag": False,
                                "l_flag": False
                            },
                            "strict_spf_sid_index": 505,
                            "strict_spf_sid_flags": {
                                "r_flag": False,
                                "n_flag": False,
                                "p_flag": False,
                                "e_flag": False,
                                "v_flag": False,
                                "l_flag": False
                            },
                            "label": "implicit-null",
                            "strict_spf_label": "implicit-null",
                            "path_attribute": "SR_POLICY",
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
                                "rtp_lsp_version": 283
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "srgb": 16000,
                            "srgb_range": 8000,
                            "prefix_sid_index": 105,
                            "non_strict_sid_flags": {
                                "r_flag": True,
                                "n_flag": False,
                                "p_flag": True,
                                "e_flag": False,
                                "v_flag": False,
                                "l_flag": False
                            },
                            "strict_spf_sid_index": 505,
                            "strict_spf_sid_flags": {
                                "r_flag": True,
                                "n_flag": False,
                                "p_flag": True,
                                "e_flag": False,
                                "v_flag": False,
                                "l_flag": False
                            }
                        },
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
                                "rtp_lsp_version": 338
                            },
                            "srgb": 16000,
                            "srgb_range": 8000,
                            "prefix_sid_index": 105,
                            "non_strict_sid_flags": {
                                "r_flag": False,
                                "n_flag": False,
                                "p_flag": False,
                                "e_flag": False,
                                "v_flag": False,
                                "l_flag": False
                            },
                            'path_attribute': 'ALT',
                            "strict_spf_sid_index": 505,
                            "strict_spf_sid_flags": {
                                "r_flag": False,
                                "n_flag": False,
                                "p_flag": False,
                                "e_flag": False,
                                "v_flag": False,
                                "l_flag": False
                            },
                            "label": "16105",
                            "strict_spf_label": "16505"
                        }
                    }
                }
            }
        }
    }
}