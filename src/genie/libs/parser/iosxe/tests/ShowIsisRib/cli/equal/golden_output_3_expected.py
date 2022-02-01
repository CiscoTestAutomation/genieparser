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
                        "6.6.6.6": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "subnet": "32",
                            "source_router_id": "6.6.6.6",
                            "algo": {
                                0: {
                                    "sid_index": 61,
                                    "bound": True,
                                    "attribute": "SR_POLICY"
                                },
                                1: {
                                    "sid_index": 6,
                                    "bound": True,
                                    "attribute": "TE"
                                }
                            },
                            "via_interface": {
                                "Tunnel65536": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "6.6.6.6": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 209,
                                                        "rtp_lsp_index": 209,
                                                        "rtp_lsp_version": 18349
                                                    },
                                                    "distance": 115,
                                                    "metric": 50,
                                                    "via_ip": "6.6.6.6",
                                                    "tag": "0",
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "source_router_id": "6.6.6.6",
                                                    "srgb_start": 100000,
                                                    "srgb_range": 30001,
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 61,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "implicit-null"
                                                        },
                                                        1: {
                                                            "sid_index": 6,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
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
                                                    "had_repair_path": False,
                                                    "filtered_out": False,
                                                    "installed": True
                                                }
                                            }
                                        }
                                    }
                                },
                                "Tunnel65537": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "6.6.6.6": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 209,
                                                        "rtp_lsp_index": 209,
                                                        "rtp_lsp_version": 18349
                                                    },
                                                    "distance": 115,
                                                    "metric": 50,
                                                    "via_ip": "6.6.6.6",
                                                    "tag": "0",
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "source_router_id": "6.6.6.6",
                                                    "srgb_start": 100000,
                                                    "srgb_range": 30001,
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 61,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "implicit-null"
                                                        },
                                                        1: {
                                                            "sid_index": 6,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
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
                                                    "had_repair_path": False,
                                                    "filtered_out": False,
                                                    "installed": True
                                                }
                                            }
                                        }
                                    }
                                },
                                "Tunnel10000": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "6.6.6.6": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 209,
                                                        "rtp_lsp_index": 209,
                                                        "rtp_lsp_version": 18349
                                                    },
                                                    "distance": 115,
                                                    "metric": 50,
                                                    "via_ip": "6.6.6.6",
                                                    "tag": "0",
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "source_router_id": "6.6.6.6",
                                                    "srgb_start": 100000,
                                                    "srgb_range": 30001,
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 61,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "implicit-null"
                                                        },
                                                        1: {
                                                            "sid_index": 6,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
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
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": True,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "filtered_out": False,
                                                    "installed": True
                                                }
                                            }
                                        }
                                    }
                                },
                                "Tunnel4001": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "6.6.6.6": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 105,
                                                        "rtp_lsp_index": 209,
                                                        "rtp_lsp_version": 18349
                                                    },
                                                    "distance": 115,
                                                    "metric": 50,
                                                    "via_ip": "199.1.1.2",
                                                    "tag": "0",
                                                    "srgb_start": 100000,
                                                    "srgb_range": 30001,
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 61,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "100061"
                                                        },
                                                        1: {
                                                            "sid_index": 6,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "100006"
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
                                                    "had_repair_path": False,
                                                    "filtered_out": False,
                                                    "installed": True
                                                }
                                            }
                                        }
                                    }
                                },
                                "Tunnel4002": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "6.6.6.6": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 105,
                                                        "rtp_lsp_index": 209,
                                                        "rtp_lsp_version": 18349
                                                    },
                                                    "distance": 115,
                                                    "metric": 50,
                                                    "via_ip": "199.1.2.2",
                                                    "tag": "0",
                                                    "srgb_start": 100000,
                                                    "srgb_range": 30001,
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 61,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "100061"
                                                        },
                                                        1: {
                                                            "sid_index": 6,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "100006"
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
                                                    "had_repair_path": False,
                                                    "filtered_out": False,
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