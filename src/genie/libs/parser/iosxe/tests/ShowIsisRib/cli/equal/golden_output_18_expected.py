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
                                "n_flag": False
                            },
                            "subnet": "32",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "Ethernet0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "6.6.6.6": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 40,
                                                    "via_ip": "12.1.1.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
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
                                                    "had_repair_path": False,
                                                    "installed": True
                                                }
                                            }
                                        }
                                    }
                                },
                                "Ethernet0/2": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "6.6.6.6": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 40,
                                                    "via_ip": "13.1.1.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
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
                                                    "had_repair_path": False,
                                                    "installed": True
                                                }
                                            }
                                        }
                                    }
                                },
                                "Ethernet0/3": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "4.4.4.4": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "10.1.6.4",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "host": "r604.00-00",
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 1004,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": False,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "from_srapp": True,
                                                            "label": "implicit-null"
                                                        },
                                                        1: {}
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