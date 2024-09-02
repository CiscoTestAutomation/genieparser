expected_output = {
    "tag": {
        "1": {
            "level": {
                1: {
                    "iolR1.00-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x00000028",
                        "lsp_checksum": "0xEE4D",
                        "lsp_holdtime": "1184",
                        "lsp_rcvd": "*",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "area_address": "50.1234",
                        "nlpid": "0xCC 0x8E",
                        "router_id": "1.1.1.1",
                        "router_cap": "1.1.1.1",
                        "d_flag": False,
                        "s_flag": False,
                        "segment_routing": {
                            "spf": True,
                            "strict_spf": True,
                            "algorithms": [128, 129, 130, 131, 132, 133, 134],
                            "i_flag": True,
                            "v_flag": False,
                            "srgb_base": 16000,
                            "srgb_range": 8000,
                            "srlb_base": 12000,
                            "srlb_range": 2001,
                        },
                        "node_msd": 16,
                        "flex_algo": {
                            128: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                                "include_all": [
                                    "0x00000000 0x00000000 0x00000000 0x00000010",
                                    "0x00000000 0x00000000 0x00000100",
                                ],
                            },
                            129: {
                                "metric_type": "Min-delay",
                                "alg_type": "SPF",
                                "priority": 128,
                            },
                            130: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                            },
                            131: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                            },
                            132: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                            },
                            133: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                            },
                            134: {
                                "metric_type": "IGP",
                                "alg_type": "SPF",
                                "priority": 128,
                            },
                        },
                        "hostname": "iolR1",
                        "ip_address": "1.1.1.1",
                        "ipv6_address": "111::111",
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
                        },
                    }
                }
            }
        }
    }
}
