expected_output = {
    "tag": {
        "64512": {
            "level": {
                "level-1": {
                    "host": {
                        "R1.00": {
                            "ip_router_id": "192.0.2.53",
                            "ip_router_lsp_id": 0,
                            "ip_interface_address": "192.0.2.53",
                            "lsp_id": 0,
                            "ip_pq_address": "192.0.2.53",
                            "ip_prefix": {
                                "sid": 990,
                                "r_flag": 0,
                                "n_flag": 1,
                                "p_flag": 0,
                                "e_flag": 0,
                                "v_flag": 0,
                                "l_flag": 0
                            },
                            "ip_strict_spf": {
                                "sid": 990,
                                "r_flag": 0,
                                "n_flag": 1,
                                "p_flag": 0,
                                "e_flag": 0,
                                "v_flag": 0,
                                "l_flag": 0
                            },
                            "lsp_index": {
                                1: {
                                    "sr_capable": "Yes",
                                    "strict_spf_capable": "Yes"
                                }
                            },
                            "srgb": {
                                "start": 16000,
                                "range": 8000,
                                "lsp_id": 0
                            },
                            "srlb": {
                                "start": 15000,
                                "range": 1000,
                                "lsp_id": 0
                            },
                            "flex_algo": {
                                "129": {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 128,
                                    "affinity": {
                                        "Include-any": [
                                            "0x00000004"
                                        ]
                                    }
                                },
                                "130": {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 128,
                                    "affinity": {
                                        "Include-any": [
                                            "0x00000002"
                                        ]
                                    }
                                },
                                "139": {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 128,
                                    "affinity": {
                                        "Include-all": [
                                            "0x0000000C"
                                        ]
                                    }
                                },
                                "140": {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 128,
                                    "affinity": {
                                        "Include-all": [
                                            "0x0000000A"
                                        ]
                                    }
                                },
                                "149": {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 128,
                                    "affinity": {
                                        "Include-all": [
                                            "0x00000014"
                                        ]
                                    }
                                },
                                "150": {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 128,
                                    "affinity": {
                                        "Include-all": [
                                            "0x00000012"
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

