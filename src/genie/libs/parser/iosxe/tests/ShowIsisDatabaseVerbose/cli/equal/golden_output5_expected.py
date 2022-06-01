expected_output = {
    "tag": {
        "1": {
            "level": {
                1: {
                    "r1.00-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x00000009",
                        "lsp_checksum": "0x423A",
                        "lsp_holdtime": "1194",
                        "lsp_rcvd": "*",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "lsp_index": 1,
                        "area_address": "49",
                        "nlpid": "0xCC 0x8E",
                        "topology": {
                            "ipv4": {
                                "code": "0x0"
                            },
                            "ipv6": {
                                "code": "0x2"
                            }
                        },
                        "router_id": "11.11.11.11",
                        "router_cap": "11.11.11.11",
                        "d_flag": False,
                        "s_flag": False,
                        "segment_routing": {
                            "i_flag": True,
                            "v_flag": False,
                            "srgb_base": 16000,
                            "srgb_range": 8000,
                            "srlb_base": 15000,
                            "srlb_range": 1000,
                            "spf": True,
                            "strict_spf": True,
                            "algorithms": {
                                128
                            }
                        },
                        "node_msd": 16,
                        "flex_algo": {
                            128: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128
                            }
                        },
                        "hostname": "r1",
                        "extended_is_neighbor": {
                            "r2.00": {
                                "neighbor_id": "r2.00",
                                "metric": 10,
                                "adjacency_sid": {
                                    19: {
                                        "f_flag": False,
                                        "b_flag": False,
                                        "v_flag": True,
                                        "l_flag": True,
                                        "s_flag": False,
                                        "p_flag": False,
                                        "weight": 0
                                    },
                                    20: {
                                        "f_flag": False,
                                        "b_flag": True,
                                        "v_flag": True,
                                        "l_flag": True,
                                        "s_flag": False,
                                        "p_flag": False,
                                        "weight": 0
                                    }
                                },
                                "local_interface_id": 1,
                                "remote_interface_id": 1,
                                "reservable_global_pool_bw": 0,
                                "unreserved_global_pool_bw": {
                                    "bw_0": 0,
                                    "bw_1": 0,
                                    "bw_2": 0,
                                    "bw_3": 0,
                                    "bw_4": 0,
                                    "bw_5": 0,
                                    "bw_6": 0,
                                    "bw_7": 0
                                },
                                "affinity": "0x80000200",
                                "extended_affinity": [
                                    "0x80000200 0x80000200 0x80000200 0x80000200",
                                    "0x80000200 0x80000200 0x80000200 0x80000200",
                                    "0x80000200"
                                ],
                                "admin_weight": 150
                            }
                        },
                        "ip_address": "11.11.11.11",
                        "ipv4_internal_reachability": {
                            "100.0.0.0/24": {
                                "ip_prefix": "100.0.0.0",
                                "prefix_len": "24",
                                "metric": 10,
                                "prefix_attr": {
                                    "x_flag": False,
                                    "r_flag": False,
                                    "n_flag": False
                                }
                            },
                            "11.11.11.11/32": {
                                "ip_prefix": "11.11.11.11",
                                "prefix_len": "32",
                                "metric": 0,
                                "prefix_attr": {
                                    "x_flag": False,
                                    "r_flag": False,
                                    "n_flag": True
                                },
                                "source_router_id": "11.11.11.11",
                                "prefix_sid_index": {
                                    11: {
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
                                    101: {
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
                                }
                            }
                        },
                        "ipv6_address": "111::111",
                        "mt_ipv6_reachability": {
                            "100:1:1:1:1:1:1:0/112": {
                                "ip_prefix": "100:1:1:1:1:1:1:0",
                                "prefix_len": "112",
                                "metric": 10,
                                "prefix_attr": {
                                    "x_flag": False,
                                    "r_flag": False,
                                    "n_flag": False
                                }
                            },
                            "111::111/128": {
                                "ip_prefix": "111::111",
                                "prefix_len": "128",
                                "metric": 0,
                                "prefix_attr": {
                                    "x_flag": False,
                                    "r_flag": False,
                                    "n_flag": True
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}