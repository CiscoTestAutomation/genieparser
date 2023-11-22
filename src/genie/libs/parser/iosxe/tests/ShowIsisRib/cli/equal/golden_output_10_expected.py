expected_output = {
    "tag": {
        "1": {
            "topo_type": "unicast",
            "topo_name": "base",
            "tid": 0,
            "topo_id": "0x0",
            "flex_algo": {
                "None": {
                    "prefix": {
                        "3.3.3.0": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "24",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/5": {
                                    "level": {
                                        "L1": {
                                            "source_ip": {
                                                "3.3.3.3": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 36,
                                                        "rtp_lsp_index": 36,
                                                        "rtp_lsp_version": 3971
                                                    },
                                                    "distance": 115,
                                                    "metric": 16777224,
                                                    "via_ip": "13.13.1.2",
                                                    "tag": "0",
                                                    "had_repair_path": False,
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "installed": True
                                                }
                                            }
                                        },
                                        "L2": {
                                            "source_ip": {
                                                "3.3.3.3": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 37,
                                                        "rtp_lsp_index": 37,
                                                        "rtp_lsp_version": 3978
                                                    },
                                                    "distance": 115,
                                                    "metric": 16777224,
                                                    "via_ip": "13.13.1.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                },
                                                "5.5.5.5": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 37,
                                                        "rtp_lsp_index": 11,
                                                        "rtp_lsp_version": 3994
                                                    },
                                                    "distance": 115,
                                                    "metric": 50331652,
                                                    "via_ip": "13.13.1.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": True,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                },
                                                "6.6.6.6": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 37,
                                                        "rtp_lsp_index": 21,
                                                        "rtp_lsp_version": 4000
                                                    },
                                                    "distance": 115,
                                                    "metric": 83886080,
                                                    "via_ip": "13.13.1.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": True,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}