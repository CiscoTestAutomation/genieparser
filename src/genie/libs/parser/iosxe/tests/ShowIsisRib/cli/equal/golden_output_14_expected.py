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
                        "15.0.0.15": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "32",
                            "algo": {
                                0: {},
                                1: {
                                    "attribute": "SR_POLICY_STRICT"
                                }
                            },
                            "via_interface": {
                                "GigabitEthernet0/0/3": {
                                    "level": {
                                        "L1": {
                                            "source_ip": {
                                                "5.5.5.5": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 2,
                                                        "rtp_lsp_index": 4,
                                                        "rtp_lsp_version": 577
                                                    },
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.10.10.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
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
                                                    "had_repair_path": False,
                                                    "installed": True
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/5": {
                                    "level": {
                                        "L1": {
                                            "source_ip": {
                                                "5.5.5.5": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 1,
                                                        "rtp_lsp_index": 4,
                                                        "rtp_lsp_version": 577
                                                    },
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "20.20.20.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
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
                                                    "had_repair_path": False,
                                                    "installed": True
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