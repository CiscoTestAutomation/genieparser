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
                        "4.4.4.4": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "subnet": "32",
                            "source_router_id": "4.4.4.4",
                            "algo": {
                                0: {
                                    "sid_index": 604,
                                    "bound": True
                                },
                                1: {}
                            },
                            "via_interface": {
                                "GigabitEthernet0/2/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "4.4.4.4": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 2,
                                                        "rtp_lsp_index": 2,
                                                        "rtp_lsp_version": 5324,
                                                        "tpl_lsp_version": 5324
                                                    },
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "24.24.1.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "host": "asr1k-40.00-00",
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 604,
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
                                        }
                                    }
                                }
                            }
                        },
                        "7.7.7.7": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "subnet": "32",
                            "algo": {
                                0: {
                                    "sid_index": 607,
                                    "bound": True
                                },
                                1: {}
                            },
                            "via_interface": {
                                "GigabitEthernet0/2/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "7.7.7.7": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 2,
                                                        "rtp_lsp_index": 15,
                                                        "rtp_lsp_version": 5322,
                                                        "tpl_lsp_version": 5322
                                                    },
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "24.24.1.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "host": "asr1k-40.00-00",
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 607,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "100607"
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
                        "10.10.10.10": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "subnet": "32",
                            "algo": {
                                0: {
                                    "sid_index": 610,
                                    "bound": True
                                },
                                1: {}
                            },
                            "via_interface": {
                                "GigabitEthernet0/2/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "10.10.10.10": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 2,
                                                        "rtp_lsp_index": 17,
                                                        "rtp_lsp_version": 5322,
                                                        "tpl_lsp_version": 5322
                                                    },
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "24.24.1.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "host": "asr1k-40.00-00",
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 610,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "100610"
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
                },
                129: {},
                140: {},
                141: {},
                142: {},
                143: {},
                144: {},
                145: {},
                146: {},
                147: {},
                148: {},
                149: {},
                150: {},
                151: {},
                152: {},
                153: {},
                154: {},
                155: {},
                156: {},
                157: {}
            }
        },
        "2": {
            "topo_type": "unicast",
            "topo_name": "base",
            "tid": 0,
            "topo_id": "0x0",
            "flex_algo": {
                128: {}
            }
        }
    }
}