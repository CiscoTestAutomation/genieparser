expected_output = {
    "tag": {
        "1": {
            "level": {
                "level-1": {
                    "hosts": {
                        "asr1k-34.00": {
                            "ip_router_id": "1.1.1.1",
                            "ip_router_lsp": 0,
                            "ip_interface_address": "1.1.1.1",
                            "ip_interface_address_lsp": 0,
                            "ip_pq_address": "1.1.1.1",
                            "ip_prefix_sid": {
                                "id": 11,
                                "r_flag": 0,
                                "n_flag": 1,
                                "p_flag": 0,
                                "e_flag": 0,
                                "v_flag": 0,
                                "l_flag": 0
                            },
                            "ip_strict_spf_sid": {
                                "id": 111,
                                "r_flag": 0,
                                "n_flag": 1,
                                "p_flag": 0,
                                "e_flag": 0,
                                "v_flag": 0,
                                "l_flag": 0
                            },
                            "adj_sid": {
                                36: {
                                    "lsp": 0,
                                    "to_host": "asr1k-25",
                                    "from_host": "asr1k-34.00"
                                },
                                29: {
                                    "lsp": 0,
                                    "to_host": "asr1k-23",
                                    "from_host": "asr1k-34.00"
                                }
                            },
                            "lsp_index": 1,
                            "srgb": {
                                "start": 16000,
                                "range": 8000,
                                "lsp": 0
                            },
                            "srlb": {
                                "start": 15000,
                                "range": 1000,
                                "lsp": 0
                            },
                            "capability": {
                                "sr": "Yes",
                                "strict_spf": "Yes",
                                "lsp": 0
                            }
                        },
                        "asr1k-25.00": {
                            "ip_router_id": "3.3.3.3",
                            "ip_router_lsp": 0,
                            "ip_interface_address": "3.3.3.3",
                            "ip_interface_address_lsp": 0,
                            "ip_pq_address": "3.3.3.3",
                            "ip_prefix_sid": {
                                "id": 31,
                                "r_flag": 0,
                                "n_flag": 1,
                                "p_flag": 0,
                                "e_flag": 0,
                                "v_flag": 0,
                                "l_flag": 0
                            },
                            "ip_strict_spf_sid": {
                                "id": 131,
                                "r_flag": 0,
                                "n_flag": 1,
                                "p_flag": 0,
                                "e_flag": 0,
                                "v_flag": 0,
                                "l_flag": 0
                            },
                            "adj_sid": {
                                17: {
                                    "lsp": 0,
                                    "to_host": "asr1k-34",
                                    "from_host": "asr1k-25.00"
                                },
                                16: {
                                    "lsp": 0,
                                    "to_host": "ncs-3",
                                    "from_host": "asr1k-25.00"
                                }
                            },
                            "lsp_index": 2,
                            "srgb": {
                                "start": 16000,
                                "range": 8000,
                                "lsp": 0
                            },
                            "srlb": {
                                "start": 15000,
                                "range": 1000,
                                "lsp": 0
                            },
                            "capability": {
                                "sr": "Yes",
                                "strict_spf": "Yes",
                                "lsp": 0
                            }
                        },
                        "ncs-nm-1.00": {
                            "ip_router_id": "4.4.4.4",
                            "ip_router_lsp": 0,
                            "ip_interface_address": "4.4.4.4",
                            "ip_interface_address_lsp": 0,
                            "ip_pq_address": "4.4.4.4",
                            "ip_prefix_sid": {
                                "id": 41,
                                "r_flag": 0,
                                "n_flag": 1,
                                "p_flag": 0,
                                "e_flag": 0,
                                "v_flag": 0,
                                "l_flag": 0
                            },
                            "ip_strict_spf_sid": {
                                "id": 141,
                                "r_flag": 0,
                                "n_flag": 1,
                                "p_flag": 0,
                                "e_flag": 0,
                                "v_flag": 0,
                                "l_flag": 0
                            },
                            "adj_sid": {
                                24001: {
                                    "lsp": 0,
                                    "to_host": "asr1k-23",
                                    "from_host": "ncs-nm-1.00"
                                }
                            },
                            "lsp_index": 5,
                            "srgb": {
                                "start": 100000,
                                "range": 30001,
                                "lsp": 0
                            },
                            "srlb": {
                                "start": 15000,
                                "range": 1000,
                                "lsp": 0
                            },
                            "capability": {
                                "sr": "Yes",
                                "strict_spf": "Yes",
                                "lsp": 0
                            },
                            "sr_endpoint": "4.4.4.4",
                            "policy": {
                                "id": "Tunnel65536",
                                "ifnum": 23,
                                "metric": 0,
                                "flag": 0
                            }
                        },
                        "ncs-3.00": {
                            "ip_router_id": "5.5.5.5",
                            "ip_router_lsp": 0,
                            "ip_interface_address": "5.5.5.5",
                            "ip_interface_address_lsp": 0,
                            "ip_pq_address": "5.5.5.5",
                            "ip_prefix_sid": {
                                "id": 51,
                                "r_flag": 0,
                                "n_flag": 1,
                                "p_flag": 0,
                                "e_flag": 0,
                                "v_flag": 0,
                                "l_flag": 0
                            },
                            "ip_strict_spf_sid": {
                                "id": 151,
                                "r_flag": 0,
                                "n_flag": 1,
                                "p_flag": 0,
                                "e_flag": 0,
                                "v_flag": 0,
                                "l_flag": 0
                            },
                            "adj_sid": {
                                24001: {
                                    "lsp": 0,
                                    "to_host": "asr1k-25",
                                    "from_host": "ncs-3.00"
                                }
                            },
                            "lsp_index": 3,
                            "srgb": {
                                "start": 100000,
                                "range": 30001,
                                "lsp": 0
                            },
                            "srlb": {
                                "start": 15000,
                                "range": 1000,
                                "lsp": 0
                            },
                            "capability": {
                                "sr": "Yes",
                                "strict_spf": "Yes",
                                "lsp": 0
                            },
                            "sr_endpoint": "5.5.5.5",
                            "policy": {
                                "id": "Tunnel65537",
                                "ifnum": 24,
                                "metric": 0,
                                "flag": 0
                            }
                        }
                    }
                }
            }
        }
    }
}