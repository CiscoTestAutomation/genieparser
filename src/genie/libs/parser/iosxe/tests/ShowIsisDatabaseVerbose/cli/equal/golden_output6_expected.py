expected_output = {
    "tag": {
        "1": {
            "level": {
                2: {
                    "R1.00-00": {
                        "area_address": "50.1234",
                        "attach_bit": 0,
                        "d_flag": False,
                        "extended_is_neighbor": {
                            "R2.00": [
                                {
                                    "neighbor_id": "R2.00",
                                    "metric": 10,
                                    "adjacency_sid": {
                                        18: {
                                            "f_flag": False,
                                            "b_flag": False,
                                            "v_flag": True,
                                            "l_flag": True,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0,
                                        }
                                    },
                                    "admin_weight": 10,
                                }
                            ],
                            "R3.00": [
                                {
                                    "neighbor_id": "R3.00",
                                    "metric": 10,
                                    "adjacency_sid": {
                                        19: {
                                            "f_flag": False,
                                            "b_flag": False,
                                            "v_flag": True,
                                            "l_flag": True,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0,
                                        }
                                    },
                                    "admin_weight": 10,
                                }
                            ],
                        },
                        "flex_algo": {
                            128: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            129: {
                                "alg_type": "SPF",
                                "metric_type": "Min-delay",
                                "priority": 128,
                            },
                            130: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            131: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            132: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            133: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            134: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            135: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            136: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            137: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            138: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            139: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            140: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            141: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            142: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            143: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            144: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            145: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            146: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            147: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            148: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            149: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            150: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            151: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            152: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            153: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            154: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            155: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                        },
                        "hostname": "R1",
                        "ip_address": "1.1.1.1",
                        "ipv4_internal_reachability": {
                            "12.1.1.0/24": [
                                {
                                    "ip_prefix": "12.1.1.0",
                                    "prefix_len": "24",
                                    "metric": 10,
                                    "prefix_attr": {
                                        "x_flag": False,
                                        "r_flag": False,
                                        "n_flag": False,
                                    },
                                }
                            ],
                            "13.1.1.0/24": [
                                {
                                    "ip_prefix": "13.1.1.0",
                                    "prefix_len": "24",
                                    "metric": 10,
                                    "prefix_attr": {
                                        "x_flag": False,
                                        "r_flag": False,
                                        "n_flag": False,
                                    },
                                }
                            ],
                        },
                        "ipv6_address": "111::111",
                        "ipv6_reachability": {
                            "111::111/128": [
                                {
                                    "ip_prefix": "111::111",
                                    "prefix_len": "128",
                                    "metric": 10,
                                    "prefix_attr": {
                                        "x_flag": False,
                                        "r_flag": False,
                                        "n_flag": True,
                                    },
                                }
                            ],
                            "12:12::/64": [
                                {
                                    "ip_prefix": "12:12::",
                                    "prefix_len": "64",
                                    "metric": 10,
                                    "prefix_attr": {
                                        "x_flag": False,
                                        "r_flag": False,
                                        "n_flag": False,
                                    },
                                }
                            ],
                            "13:13::/64": [
                                {
                                    "ip_prefix": "13:13::",
                                    "prefix_len": "64",
                                    "metric": 10,
                                    "prefix_attr": {
                                        "x_flag": False,
                                        "r_flag": False,
                                        "n_flag": False,
                                    },
                                }
                            ],
                        },
                        "lsp_checksum": "0xB97E",
                        "lsp_holdtime": "1087",
                        "lsp_rcvd": "1199",
                        "lsp_sequence_num": "0x0000000D",
                        "nlpid": "0xCC 0x8E",
                        "node_msd": 16,
                        "overload_bit": 0,
                        "p_bit": 0,
                        "router_cap": "1.1.1.1",
                        "router_id": "1.1.1.1",
                        "s_flag": False,
                        "segment_routing": {
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
                                147,
                                148,
                                149,
                                150,
                                151,
                                152,
                                153,
                                154,
                                155,
                            ],
                            "i_flag": True,
                            "spf": True,
                            "srgb_base": 16000,
                            "srgb_range": 8000,
                            "srlb_base": 15000,
                            "srlb_range": 1000,
                            "strict_spf": True,
                            "v_flag": False,
                        },
                    },
                    "R1.00-01": {
                        "attach_bit": 0,
                        "ipv4_internal_reachability": {
                            "1.1.1.1/32": [
                                {
                                    "ip_prefix": "1.1.1.1",
                                    "prefix_len": "32",
                                    "metric": 10,
                                    "prefix_attr": {
                                        "x_flag": False,
                                        "r_flag": False,
                                        "n_flag": True,
                                    },
                                    "prefix_sid_index": {
                                        11: {
                                            "algorithm": "SPF",
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        12: {
                                            "algorithm": "Strict-SPF",
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        123: {
                                            "flex_algo": 128,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        124: {
                                            "flex_algo": 129,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        125: {
                                            "flex_algo": 130,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        126: {
                                            "flex_algo": 131,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        127: {
                                            "flex_algo": 132,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        128: {
                                            "flex_algo": 133,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        129: {
                                            "flex_algo": 134,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        130: {
                                            "flex_algo": 135,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        131: {
                                            "flex_algo": 136,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        132: {
                                            "flex_algo": 137,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        133: {
                                            "flex_algo": 138,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        134: {
                                            "flex_algo": 139,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        135: {
                                            "flex_algo": 140,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        136: {
                                            "flex_algo": 141,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        137: {
                                            "flex_algo": 142,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        138: {
                                            "flex_algo": 143,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        139: {
                                            "flex_algo": 144,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        140: {
                                            "flex_algo": 145,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        141: {
                                            "flex_algo": 146,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        142: {
                                            "flex_algo": 147,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        143: {
                                            "flex_algo": 148,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        144: {
                                            "flex_algo": 149,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        145: {
                                            "flex_algo": 150,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        146: {
                                            "flex_algo": 151,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        147: {
                                            "flex_algo": 152,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        148: {
                                            "flex_algo": 153,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                        149: {
                                            "flex_algo": 154,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        },
                                    },
                                    "source_router_id": "1.1.1.1",
                                },
                                {
                                    "ip_prefix": "1.1.1.1",
                                    "prefix_len": "32",
                                    "metric": 10,
                                    "prefix_sid_index": {
                                        150: {
                                            "flex_algo": 155,
                                            "flags": {
                                                "r_flag": False,
                                                "n_flag": True,
                                                "p_flag": False,
                                                "e_flag": False,
                                                "v_flag": False,
                                                "l_flag": False,
                                            },
                                        }
                                    },
                                },
                            ],
                        },
                        "lsp_checksum": "0x191C",
                        "lsp_holdtime": "1082",
                        "lsp_rcvd": "1198",
                        "lsp_sequence_num": "0x00000006",
                        "overload_bit": 0,
                        "p_bit": 0,
                    },
                    "R2.00-00": {
                        "area_address": "50.1234",
                        "attach_bit": 0,
                        "d_flag": False,
                        "extended_is_neighbor": {
                            "R1.00": [
                                {
                                    "neighbor_id": "R1.00",
                                    "metric": 10,
                                    "adjacency_sid": {
                                        16: {
                                            "f_flag": False,
                                            "b_flag": False,
                                            "v_flag": True,
                                            "l_flag": True,
                                            "s_flag": False,
                                            "p_flag": False,
                                            "weight": 0,
                                        }
                                    },
                                    "admin_weight": 10,
                                }
                            ],
                        },
                        "flex_algo": {
                            130: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            131: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            132: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            133: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            134: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            135: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            136: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            137: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            138: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            139: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            140: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            141: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            142: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            143: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            144: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            145: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            146: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            147: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            148: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            149: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            150: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            151: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            152: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            153: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            154: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                            155: {
                                "alg_type": "SPF",
                                "metric_type": "IGP",
                                "priority": 128,
                            },
                        },
                        "hostname": "R2",
                        "ip_address": "2.2.2.2",
                        "ipv4_internal_reachability": {
                            "12.1.1.0/24": [
                                {
                                    "ip_prefix": "12.1.1.0",
                                    "prefix_len": "24",
                                    "metric": 10,
                                    "prefix_attr": {
                                        "x_flag": False,
                                        "r_flag": False,
                                        "n_flag": False,
                                    },
                                }
                            ],
                            "24.1.1.0/24": [
                                {
                                    "ip_prefix": "24.1.1.0",
                                    "prefix_len": "24",
                                    "metric": 10,
                                    "prefix_attr": {
                                        "x_flag": False,
                                        "r_flag": False,
                                        "n_flag": False,
                                    },
                                }
                            ],
                        },
                        "ipv6_address": "222::222",
                        "ipv6_reachability": {
                            "12:12::/64": [
                                {
                                    "ip_prefix": "12:12::",
                                    "prefix_len": "64",
                                    "metric": 10,
                                    "prefix_attr": {
                                        "x_flag": False,
                                        "r_flag": False,
                                        "n_flag": False,
                                    },
                                }
                            ],
                            "222::222/128": [
                                {
                                    "ip_prefix": "222::222",
                                    "prefix_len": "128",
                                    "metric": 10,
                                    "prefix_attr": {
                                        "x_flag": False,
                                        "r_flag": False,
                                        "n_flag": True,
                                    },
                                }
                            ],
                            "24:24::/64": [
                                {
                                    "ip_prefix": "24:24::",
                                    "prefix_len": "64",
                                    "metric": 10,
                                    "prefix_attr": {
                                        "x_flag": False,
                                        "r_flag": False,
                                        "n_flag": False,
                                    },
                                }
                            ],
                        },
                        "lsp_checksum": "0xEF96",
                        "lsp_holdtime": "1087",
                        "lsp_rcvd": "1199",
                        "lsp_sequence_num": "0x0000000D",
                        "nlpid": "0xCC 0x8E",
                        "node_msd": 16,
                        "overload_bit": 0,
                        "p_bit": 0,
                        "router_cap": "2.2.2.2",
                        "router_id": "2.2.2.2",
                        "s_flag": False,
                        "segment_routing": {
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
                                147,
                                148,
                                149,
                                150,
                                151,
                                152,
                                153,
                                154,
                                155,
                            ],
                            "i_flag": True,
                            "spf": True,
                            "srgb_base": 16000,
                            "srgb_range": 8000,
                            "srlb_base": 15000,
                            "srlb_range": 1000,
                            "strict_spf": True,
                            "v_flag": False,
                        },
                    },
                },
            },
        },
    },
}
