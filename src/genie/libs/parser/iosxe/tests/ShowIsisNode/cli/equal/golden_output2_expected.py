expected_output = {
    "tag": {
        "1": {
            "level": {
                "level-1": {
                    "hosts": {
                        "R1-asr1k-43.00": {
                            "ip_router_id": "1.1.1.1",
                            "ip_router_lsp": 0,
                            "ip_interface_address": "1.1.1.1",
                            "ip_interface_address_lsp": 0,
                            "adj_sid": {
                                16: {
                                    "lsp": 0,
                                    "to_host": "R3-asr1k-53",
                                    "from_host": "R1-asr1k-43.00"
                                }
                            },
                            "lsp_index": 38,
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
                                "sr": "No",
                                "strict_spf": "No",
                                "lsp": 0
                            },
                            "flex_algo": {
                                128: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                },
                                129: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                }
                            }
                        },
                        "R3-asr1k-53.00": {
                            "ip_router_id": "3.3.3.3",
                            "ip_router_lsp": 0,
                            "ip_interface_address": "3.3.3.3",
                            "ip_interface_address_lsp": 0,
                            "adj_sid": {
                                372: {
                                    "lsp": 1,
                                    "to_host": "R1-asr1k-43",
                                    "from_host": "R3-asr1k-53.00"
                                },
                                125: {
                                    "lsp": 1,
                                    "to_host": "R5-asr1k-11",
                                    "from_host": "R3-asr1k-53.00"
                                }
                            },
                            "lsp_index": 36,
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
                                "sr": "No",
                                "strict_spf": "No",
                                "lsp": 0
                            },
                            "flex_algo": {
                                128: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                },
                                129: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                }
                            }
                        },
                        "R5-asr1k-11.00": {
                            "ip_router_id": "5.5.5.5",
                            "ip_router_lsp": 0,
                            "ip_interface_address": "5.5.5.5",
                            "ip_interface_address_lsp": 0,
                            "adj_sid": {
                                16: {
                                    "lsp": 0,
                                    "to_host": "R3-asr1k-53",
                                    "from_host": "R5-asr1k-11.00"
                                },
                                55: {
                                    "lsp": 1,
                                    "to_host": "R6-asr1k-20",
                                    "from_host": "R5-asr1k-11.00"
                                },
                                57: {
                                    "lsp": 1,
                                    "to_host": "R6-asr1k-20",
                                    "from_host": "R5-asr1k-11.00"
                                }
                            },
                            "lsp_index": 4,
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
                                "sr": "No",
                                "strict_spf": "No",
                                "lsp": 0
                            },
                            "flex_algo": {
                                128: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                },
                                129: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                }
                            }
                        },
                        "R6-asr1k-20.00": {
                            "ip_router_id": "6.6.6.6",
                            "ip_router_lsp": 0,
                            "ip_interface_address": "6.6.6.6",
                            "ip_interface_address_lsp": 0,
                            "adj_sid": {
                                238: {
                                    "lsp": 0,
                                    "to_host": "R5-asr1k-11",
                                    "from_host": "R6-asr1k-20.00"
                                },
                                240: {
                                    "lsp": 0,
                                    "to_host": "R5-asr1k-11",
                                    "from_host": "R6-asr1k-20.00"
                                }
                            },
                            "lsp_index": 16,
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
                                "sr": "No",
                                "strict_spf": "No",
                                "lsp": 0
                            },
                            "flex_algo": {
                                128: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                },
                                129: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                }
                            }
                        }
                    }
                },
                "level-2": {
                    "hosts": {
                        "R1-asr1k-43.00": {
                            "ip_router_id": "1.1.1.1",
                            "ip_router_lsp": 0,
                            "ip_interface_address": "1.1.1.1",
                            "ip_interface_address_lsp": 0,
                            "adj_sid": {
                                17: {
                                    "lsp": 0,
                                    "to_host": "R3-asr1k-53",
                                    "from_host": "R1-asr1k-43.00"
                                }
                            },
                            "lsp_index": 39,
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
                                "sr": "No",
                                "strict_spf": "No",
                                "lsp": 1
                            },
                            "flex_algo": {
                                129: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                },
                                128: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                }
                            }
                        },
                        "R3-asr1k-53.00": {
                            "ip_router_id": "3.3.3.3",
                            "ip_router_lsp": 0,
                            "ip_interface_address": "3.3.3.3",
                            "ip_interface_address_lsp": 0,
                            "adj_sid": {
                                373: {
                                    "lsp": 0,
                                    "to_host": "R1-asr1k-43",
                                    "from_host": "R3-asr1k-53.00"
                                },
                                227: {
                                    "lsp": 4,
                                    "to_host": "R5-asr1k-11",
                                    "from_host": "R3-asr1k-53.00"
                                }
                            },
                            "lsp_index": 37,
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
                                "sr": "No",
                                "strict_spf": "No",
                                "lsp": 0
                            },
                            "flex_algo": {
                                128: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                },
                                129: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                }
                            }
                        },
                        "R5-asr1k-11.00": {
                            "ip_router_id": "5.5.5.5",
                            "ip_router_lsp": 0,
                            "ip_interface_address": "5.5.5.5",
                            "ip_interface_address_lsp": 0,
                            "adj_sid": {
                                17: {
                                    "lsp": 0,
                                    "to_host": "R3-asr1k-53",
                                    "from_host": "R5-asr1k-11.00"
                                },
                                56: {
                                    "lsp": 1,
                                    "to_host": "R6-asr1k-20",
                                    "from_host": "R5-asr1k-11.00"
                                },
                                58: {
                                    "lsp": 1,
                                    "to_host": "R6-asr1k-20",
                                    "from_host": "R5-asr1k-11.00"
                                }
                            },
                            "lsp_index": 11,
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
                                "sr": "No",
                                "strict_spf": "No",
                                "lsp": 0
                            },
                            "flex_algo": {
                                128: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                },
                                129: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                }
                            }
                        },
                        "R6-asr1k-20.00": {
                            "ip_router_id": "6.6.6.6",
                            "ip_router_lsp": 0,
                            "ip_interface_address": "6.6.6.6",
                            "ip_interface_address_lsp": 0,
                            "adj_sid": {
                                239: {
                                    "lsp": 1,
                                    "to_host": "R5-asr1k-11",
                                    "from_host": "R6-asr1k-20.00"
                                },
                                241: {
                                    "lsp": 1,
                                    "to_host": "R5-asr1k-11",
                                    "from_host": "R6-asr1k-20.00"
                                }
                            },
                            "lsp_index": 21,
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
                                "sr": "No",
                                "strict_spf": "No",
                                "lsp": 2
                            },
                            "flex_algo": {
                                128: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                },
                                129: {
                                    "metric_type": "IGP",
                                    "alg_type": "SPF",
                                    "priority": 131
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}