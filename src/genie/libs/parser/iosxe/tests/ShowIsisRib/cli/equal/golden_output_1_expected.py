expected_output = {
    "tag": {
        "1": {
            "prefix": {
                "1.1.1.0": {
                    "subnet": "24",
                    "prefix_attr": {
                        "x_flag": False,
                        "r_flag": True,
                        "n_flag": False
                    },
                    'strict_sid_bound_attribute_te': False,
                    "via_interface": {
                        "Tunnel65537": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 50,
                            "via_ip": "6.6.6.6",
                            "src_ip": "6.6.6.6",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 221,
                                "rtp_lsp_index": 221,
                                "rtp_lsp_version": 99
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": True,
                                "n_flag": False
                            },
                            "srgb": 16000,
                            "srgb_range": 8000
                        },
                        "GigabitEthernet0/0/3": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 67108866,
                            "via_ip": "12.12.12.2",
                            "src_ip": "6.6.6.6",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 7,
                                "rtp_lsp_index": 30,
                                "rtp_lsp_version": 2034
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": True,
                                "n_flag": False
                            },
                            "srgb": 16000,
                            "srgb_range": 8000
                        },
                        "TenGigabitEthernet0/0/5": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 67108866,
                            "via_ip": "13.13.1.2",
                            "src_ip": "5.5.5.5",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 37,
                                "rtp_lsp_index": 13,
                                "rtp_lsp_version": 2055
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": True,
                                "n_flag": False
                            },
                            "srgb": 16000,
                            "srgb_range": 8000
                        },
                        "GigabitEthernet0/0/2": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 67108866,
                            "via_ip": "12.12.1.2",
                            "src_ip": "6.6.6.6",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 7,
                                "rtp_lsp_index": 30,
                                "rtp_lsp_version": 2034
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": True,
                                "n_flag": False
                            },
                            "srgb": 16000,
                            "srgb_range": 8000
                        }
                    }
                },
                "2.2.2.0": {
                    "subnet": "24",
                    "prefix_attr": {
                        "x_flag": False,
                        "r_flag": False,
                        "n_flag": False
                    },
                    'strict_sid_bound_attribute_te': False,
                    "via_interface": {
                        "GigabitEthernet0/0/2": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 50331652,
                            "via_ip": "12.12.1.2",
                            "src_ip": "6.6.6.6",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 7,
                                "rtp_lsp_index": 22,
                                "rtp_lsp_version": 2059
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "srgb": 16000,
                            "srgb_range": 8000,
                            "installed": True
                        },
                        "GigabitEthernet0/0/3": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 50331652,
                            "via_ip": "12.12.12.2",
                            "src_ip": "6.6.6.6",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 7,
                                "rtp_lsp_index": 22,
                                "rtp_lsp_version": 2059
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "srgb": 16000,
                            "srgb_range": 8000,
                            "installed": True
                        },
                        "TenGigabitEthernet0/0/5": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 50331662,
                            "via_ip": "13.13.1.2",
                            "src_ip": "5.5.5.5",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 37,
                                "rtp_lsp_index": 14,
                                "rtp_lsp_version": 2058
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "srgb": 16000,
                            "srgb_range": 8000
                        }
                    }
                },
                "2.2.3.0": {
                    "subnet": "24",
                    "prefix_attr": {
                        "x_flag": False,
                        "r_flag": False,
                        "n_flag": False
                    },
                    'strict_sid_bound_attribute_te': False,
                    "via_interface": {
                        "GigabitEthernet0/0/2": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 50331652,
                            "via_ip": "12.12.1.2",
                            "src_ip": "6.6.6.6",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 7,
                                "rtp_lsp_index": 23,
                                "rtp_lsp_version": 2058
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "srgb": 16000,
                            "srgb_range": 8000,
                            "installed": True
                        },
                        "GigabitEthernet0/0/3": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 50331652,
                            "via_ip": "12.12.12.2",
                            "src_ip": "6.6.6.6",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 7,
                                "rtp_lsp_index": 23,
                                "rtp_lsp_version": 2058
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "srgb": 16000,
                            "srgb_range": 8000,
                            "installed": True
                        },
                        "TenGigabitEthernet0/0/5": {
                            "distance": 115,
                            "route_type": "L2",
                            "metric": 50331662,
                            "via_ip": "13.13.1.2",
                            "src_ip": "5.5.5.5",
                            "tag": "0",
                            "lsp": {
                                "next_hop_lsp_index": 37,
                                "rtp_lsp_index": 14,
                                "rtp_lsp_version": 2058
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "srgb": 16000,
                            "srgb_range": 8000
                        }
                    }
                }
            }
        }
    }
}