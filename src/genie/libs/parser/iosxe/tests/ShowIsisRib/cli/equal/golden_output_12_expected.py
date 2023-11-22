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
                                0: {
                                    "sid_index": 105,
                                    "bound": True,
                                    "attribute": "SR_POLICY"
                                },
                                1: {
                                    "sid_index": 505,
                                    "bound": True,
                                    "attribute": "TE"
                                }
                            },
                            "via_interface": {
                                "Tunnel65827": {
                                    "level": {
                                        "L1": {
                                            "source_ip": {
                                                "5.5.5.5": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 4,
                                                        "rtp_lsp_index": 4,
                                                        "rtp_lsp_version": 338
                                                    },
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "15.0.0.15",
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
                                                        0: {
                                                            "sid_index": 105,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": False,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "implicit-null"
                                                        },
                                                        1: {
                                                            "sid_index": 505,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": False,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "implicit-null"
                                                        }
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": True,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "installed": True
                                                }
                                            }
                                        }
                                    }
                                },
                                "GigabitEthernet0/0/3": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "6.6.6.6": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 6,
                                                        "rtp_lsp_index": 10,
                                                        "rtp_lsp_version": 283
                                                    },
                                                    "distance": 115,
                                                    "metric": 50,
                                                    "via_ip": "10.10.10.2",
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
                                                        0: {
                                                            "sid_index": 105,
                                                            "flags": {
                                                                "r_flag": True,
                                                                "n_flag": False,
                                                                "p_flag": True,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            }
                                                        },
                                                        1: {
                                                            "sid_index": 505,
                                                            "flags": {
                                                                "r_flag": True,
                                                                "n_flag": False,
                                                                "p_flag": True,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            }
                                                        }
                                                    }
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
                                                        "rtp_lsp_version": 338
                                                    },
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "20.20.20.2",
                                                    "tag": "0",
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 105,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": False,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "16105"
                                                        },
                                                        1: {
                                                            "sid_index": 505,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": False,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "16505"
                                                        }
                                                    },
                                                    "path_attribute": {
                                                        "ALT": True,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "installed": False,
                                                    "had_repair_path": False,
                                                    "filtered_out": False,
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