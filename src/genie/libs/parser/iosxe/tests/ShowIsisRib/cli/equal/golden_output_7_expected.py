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
                        "3.3.3.3": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "subnet": "32",
                            "source_router_id": "3.3.3.3",
                            "algo": {
                                0: {
                                    "sid_index": 3,
                                    "bound": True
                                },
                                1: {}
                            },
                            "via_interface": {
                                "Ethernet1/2": {
                                    "level": {
                                        "L1": {
                                            "source_ip": {
                                                "3.3.3.3": {
                                                    "lsp": {
                                                        "next_hop_lsp_index": 3,
                                                        "rtp_lsp_index": 3,
                                                        "rtp_lsp_version": 13,
                                                        "tpl_lsp_version": 13
                                                    },
                                                    "distance": 115,
                                                    "metric": 20,
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
                                                            "sid_index": 3,
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
                                                        "lfa_type": "TI-LFA link-protecting",
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
                                                        },
                                                        "repair_source": {
                                                            "host": "R3",
                                                            "rtp_lsp_index": 3
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

