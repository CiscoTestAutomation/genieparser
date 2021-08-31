expected_output = {
    "tag": {
        "1": {
            "prefix": {
                "6.6.6.6": {
                    "subnet": "32",
                    "prefix_attr": {
                        "x_flag": False,
                        "r_flag": False,
                        "n_flag": True
                    },
                    "source_router_id": "6.6.6.6",
                    "prefix_sid_index": 61,
                    "sid_bound_attribute": "SR_POLICY",
                    "via_interface": {
                        "Tunnel65536": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 50,
                            "via_ip": "6.6.6.6",
                            "src_ip": "6.6.6.6",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 209,
                                "rtp_lsp_index": 209,
                                "rtp_lsp_version": 18349
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "srgb": 100000,
                            "srgb_range": 30001,
                            "prefix_sid_index": 61,
                            "non_strict_sid_flags": {
                                "r_flag": False,
                                "n_flag": True,
                                "p_flag": False,
                                "e_flag": False,
                                "v_flag": False,
                                "l_flag": False
                            },
                            "strict_spf_sid_index": 6,
                            "strict_spf_sid_flags": {
                                "r_flag": False,
                                "n_flag": True,
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
                        "Tunnel65537": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 50,
                            "via_ip": "6.6.6.6",
                            "src_ip": "6.6.6.6",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 209,
                                "rtp_lsp_index": 209,
                                "rtp_lsp_version": 18349
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "srgb": 100000,
                            "srgb_range": 30001,
                            "prefix_sid_index": 61,
                            "non_strict_sid_flags": {
                                "r_flag": False,
                                "n_flag": True,
                                "p_flag": False,
                                "e_flag": False,
                                "v_flag": False,
                                "l_flag": False
                            },
                            "strict_spf_sid_index": 6,
                            "strict_spf_sid_flags": {
                                "r_flag": False,
                                "n_flag": True,
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
                        "Tunnel10000": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 50,
                            "via_ip": "6.6.6.6",
                            "src_ip": "6.6.6.6",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 209,
                                "rtp_lsp_index": 209,
                                "rtp_lsp_version": 18349
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "srgb": 100000,
                            "srgb_range": 30001,
                            "prefix_sid_index": 61,
                            "non_strict_sid_flags": {
                                "r_flag": False,
                                "n_flag": True,
                                "p_flag": False,
                                "e_flag": False,
                                "v_flag": False,
                                "l_flag": False
                            },
                            "strict_spf_sid_index": 6,
                            "strict_spf_sid_flags": {
                                "r_flag": False,
                                "n_flag": True,
                                "p_flag": False,
                                "e_flag": False,
                                "v_flag": False,
                                "l_flag": False
                            },
                            "label": "implicit-null",
                            "strict_spf_label": "implicit-null",
                            "path_attribute": "SRTE",
                            "installed": True
                        },
                        "Tunnel4001": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 50,
                            "via_ip": "199.1.1.2",
                            "src_ip": "6.6.6.6",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 105,
                                "rtp_lsp_index": 209,
                                "rtp_lsp_version": 18349
                            },
                            "srgb": 100000,
                            "srgb_range": 30001,
                            "prefix_sid_index": 61,
                            "non_strict_sid_flags": {
                                "r_flag": False,
                                "n_flag": True,
                                "p_flag": False,
                                "e_flag": False,
                                "v_flag": False,
                                "l_flag": False
                            },
                            "strict_spf_sid_index": 6,
                            "strict_spf_sid_flags": {
                                "r_flag": False,
                                "n_flag": True,
                                "p_flag": False,
                                "e_flag": False,
                                "v_flag": False,
                                "l_flag": False
                            },
                            "label": "100061",
                            "strict_spf_label": "100006",
                            "path_attribute": "ALT",
                            "installed": True
                        },
                        "Tunnel4002": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 50,
                            "via_ip": "199.1.2.2",
                            "src_ip": "6.6.6.6",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 105,
                                "rtp_lsp_index": 209,
                                "rtp_lsp_version": 18349
                            },
                            "srgb": 100000,
                            "srgb_range": 30001,
                            "prefix_sid_index": 61,
                            "non_strict_sid_flags": {
                                "r_flag": False,
                                "n_flag": True,
                                "p_flag": False,
                                "e_flag": False,
                                "v_flag": False,
                                "l_flag": False
                            },
                            "strict_spf_sid_index": 6,
                            "strict_spf_sid_flags": {
                                "r_flag": False,
                                "n_flag": True,
                                "p_flag": False,
                                "e_flag": False,
                                "v_flag": False,
                                "l_flag": False
                            },
                            "label": "100061",
                            "strict_spf_label": "100006",
                            "path_attribute": "ALT",
                            "installed": True
                        }
                    }
                }
            }
        }
    }
}