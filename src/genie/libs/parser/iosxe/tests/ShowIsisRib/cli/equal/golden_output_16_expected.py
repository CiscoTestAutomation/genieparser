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
                        "1.1.1.1": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "32",
                            "source_router_id": "1.1.1.1",
                            "algo": {
                                0: {
                                    "sid_index": 11,
                                    "bound": True
                                },
                                1: {
                                    "attribute": "SR_POLICY_STRICT",
                                    "sid_index": 101,
                                    "bound": True
                                }
                            },
                            "via_interface": {
                                "Ethernet0/0": {
                                    "level": {
                                        "L1": {
                                            "source_ip": {
                                                "1.1.1.1": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 3,
                                                        "rtp_lsp_index": 3,
                                                        "rtp_lsp_version": 88
                                                    },
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "12.1.0.1",
                                                    "tag": "0",
                                                    "filtered_out": True,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "source_router_id": "1.1.1.1",
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 11,
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
                                                            "sid_index": 101,
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
                                "Ethernet0/2": {
                                    "level": {
                                        "L1": {
                                            "source_ip": {
                                                "1.1.1.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "13.1.1.2",
                                                    "tag": "0",
                                                    "filtered_out": True,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "source_router_id": "1.1.1.1",
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 11,
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
                                                            "sid_index": 101,
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
                                                        "ALT": True,
                                                        "SR_POLICY": True,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "forced": "bdw forced",
                                                    "had_repair_path": True,
                                                    "installed": True
                                                }
                                            }
                                        }
                                    }
                                },
                                "GigabitEthernet0/3/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "6.6.6.6": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 3,
                                                        "rtp_lsp_index": 115,
                                                        "rtp_lsp_version": 220
                                                    },
                                                    "distance": 115,
                                                    "metric": 50,
                                                    "via_ip": "12.12.12.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
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
                                                            "label": "100061,"
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
                                                    "installed": False,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": True,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "199.1.2.2",
                                                        "interface": "Tunnel4002",
                                                        "metric": 50,
                                                        "stale": True,
                                                        "rtp_lsp_index": 115,
                                                        "next_hop_ip": "not found",
                                                        "lfa_type": "remote LFA",
                                                        "algo": {
                                                            0: {
                                                                "label": "100061"
                                                            }
                                                        },
                                                        "repair_source": {
                                                            "host": "asr1k-24"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "Ethernet1/2": {
                                    "level": {
                                        "L1": {
                                            "source_ip": {
                                                "4.4.4.4": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 3,
                                                        "rtp_lsp_index": 4,
                                                        "rtp_lsp_version": 52,
                                                        "tpl_lsp_version": 52
                                                    },
                                                    "distance": 115,
                                                    "metric": 70,
                                                    "via_ip": "20.20.10.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "host": "R3.00-00",
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 4,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "16004"
                                                        },
                                                        1: {}
                                                    },
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "5.5.5.5",
                                                        "interface": "MPLS-SR-Tunnel4",
                                                        "metric": 65,
                                                        "stale": False,
                                                        "next_hop_interface": "Ethernet1/1",
                                                        "next_hop_ip": "10.10.20.2",
                                                        "lfa_type": "TI-LFA node/SRLG-protecting",
                                                        "algo": {
                                                            0: {
                                                                "sid_index": 3,
                                                                "flags": {
                                                                    "r_flag": False,
                                                                    "n_flag": True,
                                                                    "p_flag": False,
                                                                    "e_flag": False,
                                                                    "v_flag": False,
                                                                    "l_flag": False
                                                                },
                                                                "label": "16003"
                                                            }
                                                        },
                                                        "nodes": {
                                                            "host": {
                                                                "R4": {
                                                                    "node_type": "P",
                                                                    "ip": "4.4.4.4",
                                                                    "label": "16004"
                                                                },
                                                                "R5": {
                                                                    "node_type": "P",
                                                                    "ip": "5.5.5.5",
                                                                    "label": "16005"
                                                                }
                                                            }
                                                        }
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000
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

