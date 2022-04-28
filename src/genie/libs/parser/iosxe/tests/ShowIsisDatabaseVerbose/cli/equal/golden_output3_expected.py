expected_output = {
    "tag": {
        "1": {
            "level": {
                1: {
                    "R1.00-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x00000009",
                        "lsp_checksum": "0xE369",
                        "lsp_holdtime": "1192",
                        "lsp_rcvd": "*",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "area_address": "49",
                        "nlpid": "0xCC 0x8E",
                        "router_id": "1.1.1.1",
                        "router_cap": "1.1.1.1",
                        "d_flag": False,
                        "s_flag": False,
                        "flex_algo": {
                            128: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "m_flag": True,
                                "segment_routing": True
                            },
                            129: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "m_flag": True,
                                "segment_routing": True
                            },
                            130: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            131: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            132: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            133: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            134: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            135: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            136: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            137: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            138: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            139: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            140: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            141: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            142: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            143: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            144: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            145: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            146: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            },
                            147: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "segment_routing": True
                            }
                        },
                        "segment_routing": {
                            "i_flag": True,
                            "v_flag": False,
                            "srgb_base": 16000,
                            "srgb_range": 8000,
                            "spf": True,
                            "strict_spf": True,
                            "algorithms": [
                                128,
                                129,
                                130,
                                131,
                                132,
                                133,
                                134,
                                135,
                                136,
                                137,
                                138,
                                139,
                                140,
                                141,
                                142,
                                143,
                                144,
                                145,
                                146,
                                147
                            ],
                            "srlb_base": 15000,
                            "srlb_range": 1000
                        },
                        "node_msd": 16,
                        "hostname": "R1",
                        "ip_address": "1.1.1.1",
                        "ipv4_internal_reachability": {
                            "12.12.12.0/24": {
                                "ip_prefix": "12.12.12.0",
                                "prefix_len": "24",
                                "metric": 10,
                                "prefix_attr": {
                                    "x_flag": False,
                                    "r_flag": False,
                                    "n_flag": False
                                }
                            },
                            "13.13.13.0/24": {
                                "ip_prefix": "13.13.13.0",
                                "prefix_len": "24",
                                "metric": 10,
                                "prefix_attr": {
                                    "x_flag": False,
                                    "r_flag": False,
                                    "n_flag": False
                                }
                            },
                            "21.21.21.0/24": {
                                "ip_prefix": "21.21.21.0",
                                "prefix_len": "24",
                                "metric": 10,
                                "prefix_attr": {
                                    "x_flag": False,
                                    "r_flag": False,
                                    "n_flag": False
                                }
                            }
                        },
                        "ipv6_address": "111::111",
                        "ipv6_reachability": {
                            "111::111/128": {
                                "ip_prefix": "111::111",
                                "prefix_len": "128",
                                "metric": 10,
                                "prefix_attr": {
                                    "x_flag": False,
                                    "r_flag": False,
                                    "n_flag": True
                                }
                            },
                            "12:12::/64": {
                                "ip_prefix": "12:12::",
                                "prefix_len": "64",
                                "metric": 10,
                                "prefix_attr": {
                                    "x_flag": False,
                                    "r_flag": False,
                                    "n_flag": False
                                }
                            },
                            "13:13::/64": {
                                "ip_prefix": "13:13::",
                                "prefix_len": "64",
                                "metric": 10,
                                "prefix_attr": {
                                    "x_flag": False,
                                    "r_flag": False,
                                    "n_flag": False
                                }
                            },
                            "21:21::/64": {
                                "ip_prefix": "21:21::",
                                "prefix_len": "64",
                                "metric": 10,
                                "prefix_attr": {
                                    "x_flag": False,
                                    "r_flag": False,
                                    "n_flag": False
                                }
                            }
                        }
                    },
                    "R1.00-01": {
                        "local_router": True,
                        "lsp_sequence_num": "0x00000002",
                        "lsp_checksum": "0x0153",
                        "lsp_holdtime": "1109",
                        "lsp_rcvd": "*",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "extended_is_neighbor": {
                            "R2.00": {
                                "neighbor_id": "R2.00",
                                "metric": 10,
                                "adjacency_sid": {
                                    16: {
                                        "f_flag": False,
                                        "b_flag": False,
                                        "v_flag": True,
                                        "l_flag": True,
                                        "s_flag": False,
                                        "p_flag": False,
                                        "weight": 0
                                    },
                                    17: {
                                        "f_flag": False,
                                        "b_flag": True,
                                        "v_flag": True,
                                        "l_flag": True,
                                        "s_flag": False,
                                        "p_flag": False,
                                        "weight": 0
                                    },
                                    18: {
                                        "f_flag": False,
                                        "b_flag": False,
                                        "v_flag": True,
                                        "l_flag": True,
                                        "s_flag": False,
                                        "p_flag": False,
                                        "weight": 0
                                    },
                                    19: {
                                        "f_flag": False,
                                        "b_flag": True,
                                        "v_flag": True,
                                        "l_flag": True,
                                        "s_flag": False,
                                        "p_flag": False,
                                        "weight": 0
                                    }
                                },
                                "local_interface_id": 5,
                                "remote_interface_id": 5,
                                "admin_weight": 10,
                                "neighbor_ipv6_address": "21:21::2"
                            },
                            "R3.00": {
                                "neighbor_id": "R3.00",
                                "metric": 10,
                                "adjacency_sid": {
                                    20: {
                                        "f_flag": False,
                                        "b_flag": False,
                                        "v_flag": True,
                                        "l_flag": True,
                                        "s_flag": False,
                                        "p_flag": False,
                                        "weight": 0
                                    },
                                    21: {
                                        "f_flag": False,
                                        "b_flag": True,
                                        "v_flag": True,
                                        "l_flag": True,
                                        "s_flag": False,
                                        "p_flag": False,
                                        "weight": 0
                                    }
                                },
                                "local_interface_id": 2,
                                "remote_interface_id": 2,
                                "admin_weight": 10,
                                "neighbor_ipv6_address": "13:13::2"
                            }
                        },
                        "ipv4_internal_reachability": {
                            "1.1.1.1/32": {
                                "ip_prefix": "1.1.1.1",
                                "prefix_len": "32",
                                "metric": 10,
                                "route_admin_tag": 30,
                                "prefix_attr": {
                                    "x_flag": False,
                                    "r_flag": False,
                                    "n_flag": True
                                },
                                "prefix_sid_index": {
                                    1: {
                                        "algorithm": "SPF",
                                        "flags": {
                                            "r_flag": False,
                                            "n_flag": True,
                                            "p_flag": False,
                                            "e_flag": False,
                                            "v_flag": False,
                                            "l_flag": False
                                        }
                                    },
                                    128: {
                                        "flex_algo": 128,
                                        "flags": {
                                            "r_flag": False,
                                            "n_flag": True,
                                            "p_flag": False,
                                            "e_flag": False,
                                            "v_flag": False,
                                            "l_flag": False
                                        }
                                    }
                                },
                                "source_router_id": "1.1.1.1"
                            }
                        }
                    }
                }
            }
        }
    }
}