expected_output = {
    "tag": {
        "VRF1": {
            "level": {
                1: {
                    "R2.00-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x00000007",
                        "lsp_checksum": "0x8A6D",
                        "lsp_holdtime": "403",
                        "lsp_rcvd": "*",
                        "attach_bit": 1,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "area_address": "49.0001",
                        "nlpid": "0xCC 0x8E",
                        "topology": {
                            "ipv4": {
                                "code": "0x0"
                            },
                            "ipv6": {
                                "code": "0x4002 ATT"
                            }
                        },
                        "hostname": "R2",
                        "ip_address": "10.84.66.66",
                        "ipv4_internal_reachability": {
                            "10.229.7.0/24": [
                                {
                                    "ip_prefix": "10.229.7.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ],
                            "10.84.66.66/32": [
                                {
                                    "ip_prefix": "10.84.66.66",
                                    "prefix_len": "32",
                                    "metric": 10
                                }
                            ]
                        },
                        "ipv6_address": "2001:DB8:66:66:66::66",
                        "mt_ipv6_reachability": {
                            "2001:DB8:20:2::/64": [
                                {
                                    "ip_prefix": "2001:DB8:20:2::",
                                    "prefix_len": "64",
                                    "metric": 10
                                }
                            ],
                            "2001:DB8:66:66:66::66/128": [
                                {
                                    "ip_prefix": "2001:DB8:66:66:66::66",
                                    "prefix_len": "128",
                                    "metric": 10
                                }
                            ]
                        }
                    }
                },
                2: {
                    "R2.00-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x00000008",
                        "lsp_checksum": "0x621E",
                        "lsp_holdtime": "1158",
                        "lsp_rcvd": "*",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "area_address": "49.0001",
                        "nlpid": "0xCC 0x8E",
                        "topology": {
                            "ipv4": {
                                "code": "0x0"
                            },
                            "ipv6": {
                                "code": "0x2"
                            }
                        },
                        "hostname": "R2",
                        "extended_is_neighbor": {
                            "R2.01": [
                                {
                                    "neighbor_id": "R2.01",
                                    "metric": 10
                                }
                            ]
                        },
                        "mt_is_neighbor": {
                            "R2.01": [
                                {
                                    "neighbor_id": "R2.01",
                                    "metric": 10
                                }
                            ]
                        },
                        "ip_address": "10.84.66.66",
                        "ipv4_internal_reachability": {
                            "10.229.7.0/24": [
                                {
                                    "ip_prefix": "10.229.7.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ],
                            "10.84.66.66/32": [
                                {
                                    "ip_prefix": "10.84.66.66",
                                    "prefix_len": "32",
                                    "metric": 10
                                }
                            ]
                        },
                        "ipv6_address": "2001:DB8:66:66:66::66",
                        "mt_ipv6_reachability": {
                            "2001:DB8:20:2::/64": [
                                {
                                    "ip_prefix": "2001:DB8:20:2::",
                                    "prefix_len": "64",
                                    "metric": 10
                                }
                            ],
                            "2001:DB8:66:66:66::66/128": [
                                {
                                    "ip_prefix": "2001:DB8:66:66:66::66",
                                    "prefix_len": "128",
                                    "metric": 10
                                }
                            ]
                        }
                    },
                    "R2.01-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x00000002",
                        "lsp_checksum": "0x3334",
                        "lsp_holdtime": "414",
                        "lsp_rcvd": "*",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "extended_is_neighbor": {
                            "R2.00": [
                                {
                                    "neighbor_id": "R2.00",
                                    "metric": 0
                                }
                            ],
                            "R7.00": [
                                {
                                    "neighbor_id": "R7.00",
                                    "metric": 0
                                }
                            ]
                        }
                    },
                    "R7.00-00": {
                        "lsp_sequence_num": "0x00000005",
                        "lsp_checksum": "0x056E",
                        "lsp_holdtime": "735",
                        "lsp_rcvd": "1199",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "area_address": "49.0002",
                        "nlpid": "0xCC 0x8E",
                        "router_id": "10.1.77.77",
                        "ip_address": "10.1.77.77",
                        "topology": {
                            "ipv6": {
                                "code": "0x2"
                            },
                            "ipv4": {
                                "code": "0x0"
                            }
                        },
                        "hostname": "R7",
                        "mt_is_neighbor": {
                            "R2.01": [
                                {
                                    "neighbor_id": "R2.01",
                                    "metric": 40
                                }
                            ]
                        },
                        "extended_is_neighbor": {
                            "R2.01": [
                                {
                                    "neighbor_id": "R2.01",
                                    "metric": 40
                                }
                            ]
                        },
                        "ipv4_internal_reachability": {
                            "10.1.77.77/32": [
                                {
                                    "ip_prefix": "10.1.77.77",
                                    "prefix_len": "32",
                                    "metric": 1
                                }
                            ],
                            "10.229.7.0/24": [
                                {
                                    "ip_prefix": "10.229.7.0",
                                    "prefix_len": "24",
                                    "metric": 40
                                }
                            ]
                        },
                        "mt_ipv6_reachability": {
                            "2001:DB8:77:77:77::77/128": [
                                {
                                    "ip_prefix": "2001:DB8:77:77:77::77",
                                    "prefix_len": "128",
                                    "metric": 1
                                }
                            ],
                            "2001:DB8:20:2::/64": [
                                {
                                    "ip_prefix": "2001:DB8:20:2::",
                                    "prefix_len": "64",
                                    "metric": 40
                                }
                            ]
                        }
                    }
                }
            }
        }
    }
}
