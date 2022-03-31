expected_output = {
    "tag": {
        "1": {
            "level": {
                1: {
                    "R1.00-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x00000006",
                        "lsp_checksum": "0x92B8",
                        "lsp_holdtime": "1171",
                        "lsp_rcvd": "*",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "area_address": "49",
                        "nlpid": "0xCC 0x8E",
                        "hostname": "R1",
                        "router_id": "1.1.1.1",
                        "ip_address": "1.1.1.1",
                        "ipv4_internal_reachability": {
                            "1.1.1.1/32": {
                                "ip_prefix": "1.1.1.1",
                                "prefix_len": "32",
                                "metric": 10,
                                "prefix_attr": {
                                    "x_flag": False,
                                    "r_flag": False,
                                    "n_flag": True
                                },
                                "source_router_id": "1.1.1.1",
                                "route_admin_tag": 30
                            },
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
                    }
                }
            }
        }
    }
}