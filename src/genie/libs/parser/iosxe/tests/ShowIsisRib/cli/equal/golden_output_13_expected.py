expected_output = {
    "tag": {
        "1": {
            "topo_type": "unicast",
            "topo_name": "base",
            "tid": 0,
            "topo_id": "0x0",
            "flex_algo": {
                128: {
                    "prefix": {
                        "2.2.2.2": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "subnet": "32",
                            "source_router_id": "2.2.2.2",
                            "algo": {
                                0: {
                                    "sid_index": 23,
                                    "bound": True
                                },
                                1: {}
                            },
                            "via_interface": {
                                "Ethernet0/1": {
                                    "level": {
                                        "L1": {
                                            "source_ip": {
                                                "2.2.2.2": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 3,
                                                        "rtp_lsp_index": 3,
                                                        "rtp_lsp_version": 9,
                                                        "tpl_lsp_version": 9
                                                    },
                                                    "distance": 115,
                                                    "metric": 10,
                                                    "via_ip": "12.1.1.2",
                                                    "tag": "0",
                                                    "host": "R2.00-00",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 23,
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
                                                        1: {}
                                                    }
                                                }
                                            }
                                        },
                                        "L2": {
                                            "source_ip": {
                                                "2.2.2.2": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 4,
                                                        "rtp_lsp_index": 4,
                                                        "rtp_lsp_version": 15,
                                                        "tpl_lsp_version": 15
                                                    },
                                                    "distance": 115,
                                                    "metric": 10,
                                                    "via_ip": "12.1.1.2",
                                                    "tag": "0",
                                                    "host": "R2.00-00",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 23,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            }
                                                        },
                                                        1: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "Ethernet0/2": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "3.3.3.3": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 6,
                                                        "rtp_lsp_index": 6,
                                                        "rtp_lsp_version": 17,
                                                        "tpl_lsp_version": 17
                                                    },
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "13.1.1.2",
                                                    "tag": "0",
                                                    "host": "R3.00-00",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": True,
                                                        "n_flag": True
                                                    },
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 23,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            }
                                                        },
                                                        1: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "3.3.3.3": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "subnet": "32",
                            "algo": {
                                0: {
                                    "sid_index": 33,
                                    "bound": True
                                },
                                1: {}
                            },
                            "via_interface": {
                                "Ethernet0/2": {
                                    "level": {
                                        "L1": {
                                            "source_ip": {
                                                "3.3.3.3": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 5,
                                                        "rtp_lsp_index": 5,
                                                        "rtp_lsp_version": 9,
                                                        "tpl_lsp_version": 9
                                                    },
                                                    "distance": 115,
                                                    "metric": 10,
                                                    "via_ip": "13.1.1.2",
                                                    "tag": "0",
                                                    "host": "R3.00-00",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 33,
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
                                                        1: {}
                                                    }
                                                }
                                            }
                                        },
                                        "L2": {
                                            "source_ip": {
                                                "3.3.3.3": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 6,
                                                        "rtp_lsp_index": 6,
                                                        "rtp_lsp_version": 17,
                                                        "tpl_lsp_version": 17
                                                    },
                                                    "distance": 115,
                                                    "metric": 10,
                                                    "via_ip": "13.1.1.2",
                                                    "tag": "0",
                                                    "host": "R3.00-00",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 33,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            }
                                                        },
                                                        1: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "Ethernet0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "2.2.2.2": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 4,
                                                        "rtp_lsp_index": 4,
                                                        "rtp_lsp_version": 15,
                                                        "tpl_lsp_version": 15
                                                    },
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "12.1.1.2",
                                                    "tag": "0",
                                                    "host": "R2.00-00",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": True,
                                                        "n_flag": True
                                                    },
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 33,
                                                            "flags": {
                                                                "r_flag": True,
                                                                "n_flag": True,
                                                                "p_flag": True,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            }
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