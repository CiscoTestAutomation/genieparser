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
                            "SR1.00": {
                                "neighbor_id": "SR1.00",
                                "metric": 120,
                                "adjacency_sid": {
                                    16: {
                                        "f_flag": False,
                                        "b_flag": False,
                                        "v_flag": True,
                                        "l_flag": True,
                                        "s_flag": False,
                                        "p_flag": False,
                                        "weight": 0
                                    }
                                },
                                "uni_link_loss": {
                                    "percent": "0.799998",
                                    "anomalous": True
                                },
                                "admin_weight": 120,
                                "asla": {
                                    "l_flag": False,
                                    "sa_length": 1,
                                    "uda_length": 0
                                },
                                "standard_application": {
                                    "FLEX-ALGO": {
                                        "bit_mask": "0x10",
                                        "appl_spec_uni_link_loss": {
                                            "percent": "0.899997",
                                            "anomalous": False
                                        },
                                        "appl_spec_ext_admin_group": [
                                            "0x00000000 0x00000000 0x00000000 0x00000000",
                                            "0x00400000"
                                        ]
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