expected_output = {
    "tag": {
        "1": {
            "level": {
                1: {
                    "R1.00-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x00000005",
                        "lsp_checksum": "0x83C1",
                        "lsp_holdtime": "1130",
                        "lsp_rcvd": "*",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
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
                        "hostname": "R1",
                        "is_neighbor": {
                            "R2.00": {
                                "neighbor_id": "R2.00",
                                "metric": 10
                            },
                            "R3.00": {
                                "neighbor_id": "R3.00",
                                "metric": 10
                            }
                        },
                        "ip_address": "1.1.1.1",
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