expected_output = {
    "tag": {
        "test": {
            "level": {
                1: {
                    "R1_xe.00-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x0000011D",
                        "lsp_checksum": "0x2165",
                        "lsp_holdtime": "519",
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
                        "hostname": "R1_xe",
                        "extended_is_neighbor": {
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 10
                                }
                            ],
                            "R1_xe.01": [
                                {
                                    "neighbor_id": "R1_xe.01",
                                    "metric": 10
                                }
                            ]
                        },
                        "mt_is_neighbor": {
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 10
                                }
                            ],
                            "R1_xe.01": [
                                {
                                    "neighbor_id": "R1_xe.01",
                                    "metric": 10
                                }
                            ]
                        },
                        "ip_address": "10.13.115.1",
                        "ipv4_internal_reachability": {
                            "10.12.115.0/24": [
                                {
                                    "ip_prefix": "10.12.115.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ],
                            "10.13.115.0/24": [
                                {
                                    "ip_prefix": "10.13.115.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ]
                        },
                        "ipv6_address": "2001:10:13:115::1",
                        "mt_ipv6_reachability": {
                            "2001:10:12:115::/64": [
                                {
                                    "ip_prefix": "2001:10:12:115::",
                                    "prefix_len": "64",
                                    "metric": 10
                                }
                            ],
                            "2001:10:13:115::/64": [
                                {
                                    "ip_prefix": "2001:10:13:115::",
                                    "prefix_len": "64",
                                    "metric": 10
                                }
                            ]
                        }
                    },
                    "R1_xe.01-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x00000118",
                        "lsp_checksum": "0x850F",
                        "lsp_holdtime": "1087",
                        "lsp_rcvd": "*",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "extended_is_neighbor": {
                            "R1_xe.00": [
                                {
                                    "neighbor_id": "R1_xe.00",
                                    "metric": 0
                                }
                            ],
                            "R2_xr.00": [
                                {
                                    "neighbor_id": "R2_xr.00",
                                    "metric": 0
                                }
                            ]
                        },
                        "ipv4_interarea_reachability": {
                            "10.100.100.0/24": [
                                {
                                    "ip_prefix": "10.100.100.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ]
                        }
                    },
                    "R1_xe.02-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x00000118",
                        "lsp_checksum": "0x7EAE",
                        "lsp_holdtime": "752",
                        "lsp_rcvd": "*",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "extended_is_neighbor": {
                            "R1_xe.00": [
                                {
                                    "neighbor_id": "R1_xe.00",
                                    "metric": 0
                                }
                            ],
                            "R3_nx.00": [
                                {
                                    "neighbor_id": "R3_nx.00",
                                    "metric": 0
                                }
                            ]
                        }
                    },
                    "R2_xr.00-00": {
                        "lsp_sequence_num": "0x00000120",
                        "lsp_checksum": "0xC84E",
                        "lsp_holdtime": "754",
                        "lsp_rcvd": "1200",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "area_address": "49.0001",
                        "extended_is_neighbor": {
                            "R1_xe.01": [
                                {
                                    "neighbor_id": "R1_xe.01",
                                    "metric": 10
                                }
                            ],
                            "R2_xr.03": [
                                {
                                    "neighbor_id": "R2_xr.03",
                                    "metric": 10
                                }
                            ]
                        },
                        "nlpid": "0xCC 0x8E",
                        "ip_address": "10.16.2.2",
                        "ipv4_internal_reachability": {
                            "10.16.2.2/32": [
                                {
                                    "ip_prefix": "10.16.2.2",
                                    "prefix_len": "32",
                                    "metric": 10
                                }
                            ],
                            "10.12.115.0/24": [
                                {
                                    "ip_prefix": "10.12.115.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ],
                            "10.23.115.0/24": [
                                {
                                    "ip_prefix": "10.23.115.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ]
                        },
                        "ipv4_interarea_reachability": {
                            "10.200.200.0/24": [
                                {
                                    "ip_prefix": "10.200.200.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ],
                            "10.220.220.0/24": [
                                {
                                    "ip_prefix": "10.220.220.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ]
                        },
                        "hostname": "R2_xr",
                        "mt_is_neighbor": {
                            "R1_xe.01": [
                                {
                                    "neighbor_id": "R1_xe.01",
                                    "metric": 10
                                }
                            ],
                            "R2_xr.03": [
                                {
                                    "neighbor_id": "R2_xr.03",
                                    "metric": 10
                                }
                            ]
                        },
                        "ipv6_address": "2001:2:2:2::2",
                        "mt_ipv6_reachability": {
                            "2001:2:2:2::2/128": [
                                {
                                    "ip_prefix": "2001:2:2:2::2",
                                    "prefix_len": "128",
                                    "metric": 10
                                }
                            ],
                            "2001:10:12:115::/64": [
                                {
                                    "ip_prefix": "2001:10:12:115::",
                                    "prefix_len": "64",
                                    "metric": 10
                                }
                            ],
                            "2001:10:23:115::/64": [
                                {
                                    "ip_prefix": "2001:10:23:115::",
                                    "prefix_len": "64",
                                    "metric": 10
                                }
                            ]
                        },
                        "topology": {
                            "ipv4": {
                                "code": "0x0"
                            },
                            "ipv6": {
                                "code": "0x2"
                            }
                        }
                    },
                    "R2_xr.03-00": {
                        "lsp_sequence_num": "0x00000118",
                        "lsp_checksum": "0xF5F1",
                        "lsp_holdtime": "563",
                        "lsp_rcvd": "1200",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "extended_is_neighbor": {
                            "R2_xr.00": [
                                {
                                    "neighbor_id": "R2_xr.00",
                                    "metric": 0
                                }
                            ],
                            "R3_nx.00": [
                                {
                                    "neighbor_id": "R3_nx.00",
                                    "metric": 0
                                }
                            ]
                        }
                    },
                    "R3_nx.00-00": {
                        "lsp_sequence_num": "0x00000193",
                        "lsp_checksum": "0x8022",
                        "lsp_holdtime": "1018",
                        "lsp_rcvd": "1200",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "area_address": "49.0001",
                        "nlpid": "0xCC 0x8E",
                        "router_id": "10.36.3.3",
                        "ip_address": "10.36.3.3",
                        "topology": {
                            "ipv6": {
                                "code": "0x2"
                            },
                            "ipv4": {
                                "code": "0x0"
                            }
                        },
                        "hostname": "R3_nx",
                        "mt_is_neighbor": {
                            "R2_xr.03": [
                                {
                                    "neighbor_id": "R2_xr.03",
                                    "metric": 40
                                }
                            ],
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 40
                                }
                            ]
                        },
                        "extended_is_neighbor": {
                            "R2_xr.03": [
                                {
                                    "neighbor_id": "R2_xr.03",
                                    "metric": 40
                                }
                            ],
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 40
                                }
                            ]
                        },
                        "ipv4_internal_reachability": {
                            "10.36.3.3/32": [
                                {
                                    "ip_prefix": "10.36.3.3",
                                    "prefix_len": "32",
                                    "metric": 1
                                }
                            ],
                            "10.13.115.0/24": [
                                {
                                    "ip_prefix": "10.13.115.0",
                                    "prefix_len": "24",
                                    "metric": 40
                                }
                            ],
                            "10.23.115.0/24": [
                                {
                                    "ip_prefix": "10.23.115.0",
                                    "prefix_len": "24",
                                    "metric": 40
                                }
                            ]
                        },
                        "mt_ipv6_reachability": {
                            "2001:3:3:3::3/128": [
                                {
                                    "ip_prefix": "2001:3:3:3::3",
                                    "prefix_len": "128",
                                    "metric": 1
                                }
                            ],
                            "2001:10:13:115::/64": [
                                {
                                    "ip_prefix": "2001:10:13:115::",
                                    "prefix_len": "64",
                                    "metric": 40
                                }
                            ],
                            "2001:10:23:115::/64": [
                                {
                                    "ip_prefix": "2001:10:23:115::",
                                    "prefix_len": "64",
                                    "metric": 40
                                }
                            ]
                        }
                    }
                },
                2: {
                    "R1_xe.00-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x0000011D",
                        "lsp_checksum": "0x27D0",
                        "lsp_holdtime": "521",
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
                        "hostname": "R1_xe",
                        "extended_is_neighbor": {
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 10
                                }
                            ],
                            "R1_xe.01": [
                                {
                                    "neighbor_id": "R1_xe.01",
                                    "metric": 10
                                }
                            ]
                        },
                        "mt_is_neighbor": {
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 10
                                }
                            ],
                            "R1_xe.01": [
                                {
                                    "neighbor_id": "R1_xe.01",
                                    "metric": 10
                                }
                            ]
                        },
                        "ip_address": "10.13.115.1",
                        "ipv4_internal_reachability": {
                            "10.12.115.0/24": [
                                {
                                    "ip_prefix": "10.12.115.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ],
                            "10.13.115.0/24": [
                                {
                                    "ip_prefix": "10.13.115.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ],
                            "10.23.115.0/24": [
                                {
                                    "ip_prefix": "10.23.115.0",
                                    "prefix_len": "24",
                                    "metric": 20
                                }
                            ]
                        },
                        "ipv6_address": "2001:10:13:115::1",
                        "mt_ipv6_reachability": {
                            "2001:10:12:115::/64": [
                                {
                                    "ip_prefix": "2001:10:12:115::",
                                    "prefix_len": "64",
                                    "metric": 10
                                }
                            ],
                            "2001:10:13:115::/64": [
                                {
                                    "ip_prefix": "2001:10:13:115::",
                                    "prefix_len": "64",
                                    "metric": 10
                                }
                            ],
                            "2001:10:23:115::/64": [
                                {
                                    "ip_prefix": "2001:10:23:115::",
                                    "prefix_len": "64",
                                    "metric": 20
                                }
                            ]
                        }
                    },
                    "R1_xe.01-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x00000118",
                        "lsp_checksum": "0x9D7F",
                        "lsp_holdtime": "930",
                        "lsp_rcvd": "*",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "extended_is_neighbor": {
                            "R1_xe.00": [
                                {
                                    "neighbor_id": "R1_xe.00",
                                    "metric": 0
                                }
                            ],
                            "R2_xr.00": [
                                {
                                    "neighbor_id": "R2_xr.00",
                                    "metric": 0
                                }
                            ]
                        },
                        "ipv4_interarea_reachability": {
                            "10.100.100.0/24": [
                                {
                                    "ip_prefix": "10.100.100.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ]
                        }
                    },
                    "R1_xe.02-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x0000011E",
                        "lsp_checksum": "0x8A25",
                        "lsp_holdtime": "1098",
                        "lsp_rcvd": "*",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "extended_is_neighbor": {
                            "R1_xe.00": [
                                {
                                    "neighbor_id": "R1_xe.00",
                                    "metric": 0
                                }
                            ],
                            "R3_nx.00": [
                                {
                                    "neighbor_id": "R3_nx.00",
                                    "metric": 0
                                }
                            ]
                        }
                    },
                    "R2_xr.00-00": {
                        "lsp_sequence_num": "0x00000120",
                        "lsp_checksum": "0x1585",
                        "lsp_holdtime": "662",
                        "lsp_rcvd": "1200",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "area_address": "49.0001",
                        "extended_is_neighbor": {
                            "R1_xe.01": [
                                {
                                    "neighbor_id": "R1_xe.01",
                                    "metric": 10
                                }
                            ],
                            "R2_xr.03": [
                                {
                                    "neighbor_id": "R2_xr.03",
                                    "metric": 10
                                }
                            ]
                        },
                        "nlpid": "0xCC 0x8E",
                        "ip_address": "10.16.2.2",
                        "ipv4_internal_reachability": {
                            "10.16.2.2/32": [
                                {
                                    "ip_prefix": "10.16.2.2",
                                    "prefix_len": "32",
                                    "metric": 10
                                }
                            ],
                            "10.12.115.0/24": [
                                {
                                    "ip_prefix": "10.12.115.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ],
                            "10.23.115.0/24": [
                                {
                                    "ip_prefix": "10.23.115.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ],
                            "10.36.3.3/32": [
                                {
                                    "ip_prefix": "10.36.3.3",
                                    "prefix_len": "32",
                                    "metric": 11
                                }
                            ],
                            "10.13.115.0/24": [
                                {
                                    "ip_prefix": "10.13.115.0",
                                    "prefix_len": "24",
                                    "metric": 20
                                }
                            ]
                        },
                        "ipv4_interarea_reachability": {
                            "10.200.200.0/24": [
                                {
                                    "ip_prefix": "10.200.200.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ],
                            "10.220.220.0/24": [
                                {
                                    "ip_prefix": "10.220.220.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ]
                        },
                        "hostname": "R2_xr",
                        "mt_is_neighbor": {
                            "R1_xe.01": [
                                {
                                    "neighbor_id": "R1_xe.01",
                                    "metric": 10
                                }
                            ],
                            "R2_xr.03": [
                                {
                                    "neighbor_id": "R2_xr.03",
                                    "metric": 10
                                }
                            ]
                        },
                        "ipv6_address": "2001:2:2:2::2",
                        "mt_ipv6_reachability": {
                            "2001:2:2:2::2/128": [
                                {
                                    "ip_prefix": "2001:2:2:2::2",
                                    "prefix_len": "128",
                                    "metric": 10
                                }
                            ],
                            "2001:10:12:115::/64": [
                                {
                                    "ip_prefix": "2001:10:12:115::",
                                    "prefix_len": "64",
                                    "metric": 10
                                }
                            ],
                            "2001:10:23:115::/64": [
                                {
                                    "ip_prefix": "2001:10:23:115::",
                                    "prefix_len": "64",
                                    "metric": 10
                                }
                            ],
                            "2001:3:3:3::3/128": [
                                {
                                    "ip_prefix": "2001:3:3:3::3",
                                    "prefix_len": "128",
                                    "metric": 11
                                }
                            ],
                            "2001:10:13:115::/64": [
                                {
                                    "ip_prefix": "2001:10:13:115::",
                                    "prefix_len": "64",
                                    "metric": 20
                                }
                            ]
                        },
                        "topology": {
                            "ipv4": {
                                "code": "0x0"
                            },
                            "ipv6": {
                                "code": "0x2"
                            }
                        }
                    },
                    "R2_xr.03-00": {
                        "lsp_sequence_num": "0x00000118",
                        "lsp_checksum": "0xF5F1",
                        "lsp_holdtime": "872",
                        "lsp_rcvd": "1200",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "extended_is_neighbor": {
                            "R2_xr.00": [
                                {
                                    "neighbor_id": "R2_xr.00",
                                    "metric": 0
                                }
                            ],
                            "R3_nx.00": [
                                {
                                    "neighbor_id": "R3_nx.00",
                                    "metric": 0
                                }
                            ]
                        }
                    },
                    "R3_nx.00-00": {
                        "lsp_sequence_num": "0x00000192",
                        "lsp_checksum": "0x8221",
                        "lsp_holdtime": "1132",
                        "lsp_rcvd": "1199",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "area_address": "49.0001",
                        "nlpid": "0xCC 0x8E",
                        "router_id": "10.36.3.3",
                        "ip_address": "10.36.3.3",
                        "topology": {
                            "ipv6": {
                                "code": "0x2"
                            },
                            "ipv4": {
                                "code": "0x0"
                            }
                        },
                        "hostname": "R3_nx",
                        "mt_is_neighbor": {
                            "R2_xr.03": [
                                {
                                    "neighbor_id": "R2_xr.03",
                                    "metric": 40
                                }
                            ],
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 40
                                }
                            ]
                        },
                        "extended_is_neighbor": {
                            "R2_xr.03": [
                                {
                                    "neighbor_id": "R2_xr.03",
                                    "metric": 40
                                }
                            ],
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 40
                                }
                            ]
                        },
                        "ipv4_internal_reachability": {
                            "10.36.3.3/32": [
                                {
                                    "ip_prefix": "10.36.3.3",
                                    "prefix_len": "32",
                                    "metric": 1
                                }
                            ],
                            "10.13.115.0/24": [
                                {
                                    "ip_prefix": "10.13.115.0",
                                    "prefix_len": "24",
                                    "metric": 40
                                }
                            ],
                            "10.23.115.0/24": [
                                {
                                    "ip_prefix": "10.23.115.0",
                                    "prefix_len": "24",
                                    "metric": 40
                                }
                            ]
                        },
                        "mt_ipv6_reachability": {
                            "2001:3:3:3::3/128": [
                                {
                                    "ip_prefix": "2001:3:3:3::3",
                                    "prefix_len": "128",
                                    "metric": 1
                                }
                            ],
                            "2001:10:13:115::/64": [
                                {
                                    "ip_prefix": "2001:10:13:115::",
                                    "prefix_len": "64",
                                    "metric": 40
                                }
                            ],
                            "2001:10:23:115::/64": [
                                {
                                    "ip_prefix": "2001:10:23:115::",
                                    "prefix_len": "64",
                                    "metric": 40
                                }
                            ]
                        }
                    }
                }
            }
        },
        "test1": {
            "level": {
                1: {
                    "R1_xe.00-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x0000011B",
                        "lsp_checksum": "0x3941",
                        "lsp_holdtime": "810",
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
                        "hostname": "R1_xe",
                        "extended_is_neighbor": {
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 10
                                }
                            ]
                        },
                        "mt_is_neighbor": {
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 10
                                }
                            ]
                        },
                        "ip_address": "10.13.115.1",
                        "ipv4_internal_reachability": {
                            "10.12.115.0/24": [
                                {
                                    "ip_prefix": "10.12.115.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ],
                            "10.13.115.0/24": [
                                {
                                    "ip_prefix": "10.13.115.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ]
                        },
                        "ipv6_address": "2001:10:13:115::1",
                        "mt_ipv6_reachability": {
                            "2001:10:12:115::/64": [
                                {
                                    "ip_prefix": "2001:10:12:115::",
                                    "prefix_len": "64",
                                    "metric": 10
                                }
                            ],
                            "2001:10:13:115::/64": [
                                {
                                    "ip_prefix": "2001:10:13:115::",
                                    "prefix_len": "64",
                                    "metric": 10
                                }
                            ]
                        }
                    },
                    "R1_xe.02-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x0000011A",
                        "lsp_checksum": "0x7AB0",
                        "lsp_holdtime": "1080",
                        "lsp_rcvd": "*",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "extended_is_neighbor": {
                            "R1_xe.00": [
                                {
                                    "neighbor_id": "R1_xe.00",
                                    "metric": 0
                                }
                            ],
                            "R3_nx.00": [
                                {
                                    "neighbor_id": "R3_nx.00",
                                    "metric": 0
                                }
                            ]
                        }
                    },
                    "R3_nx.00-00": {
                        "lsp_sequence_num": "0x00000191",
                        "lsp_checksum": "0x7535",
                        "lsp_holdtime": "1068",
                        "lsp_rcvd": "1199",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "area_address": "49.0001",
                        "nlpid": "0xCC 0x8E",
                        "router_id": "10.36.3.3",
                        "ip_address": "10.36.3.3",
                        "topology": {
                            "ipv6": {
                                "code": "0x2"
                            },
                            "ipv4": {
                                "code": "0x0"
                            }
                        },
                        "hostname": "R3_nx",
                        "mt_is_neighbor": {
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 40
                                }
                            ]
                        },
                        "extended_is_neighbor": {
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 40
                                }
                            ]
                        },
                        "ipv4_internal_reachability": {
                            "10.36.3.3/32": [
                                {
                                    "ip_prefix": "10.36.3.3",
                                    "prefix_len": "32",
                                    "metric": 1
                                }
                            ],
                            "10.13.115.0/24": [
                                {
                                    "ip_prefix": "10.13.115.0",
                                    "prefix_len": "24",
                                    "metric": 40
                                }
                            ],
                            "10.23.115.0/24": [
                                {
                                    "ip_prefix": "10.23.115.0",
                                    "prefix_len": "24",
                                    "metric": 40
                                }
                            ]
                        },
                        "mt_ipv6_reachability": {
                            "2001:3:3:3::3/128": [
                                {
                                    "ip_prefix": "2001:3:3:3::3",
                                    "prefix_len": "128",
                                    "metric": 1
                                }
                            ],
                            "2001:10:13:115::/64": [
                                {
                                    "ip_prefix": "2001:10:13:115::",
                                    "prefix_len": "64",
                                    "metric": 40
                                }
                            ],
                            "2001:10:23:115::/64": [
                                {
                                    "ip_prefix": "2001:10:23:115::",
                                    "prefix_len": "64",
                                    "metric": 40
                                }
                            ]
                        }
                    }
                },
                2: {
                    "R1_xe.00-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x0000011C",
                        "lsp_checksum": "0x9618",
                        "lsp_holdtime": "1009",
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
                        "hostname": "R1_xe",
                        "extended_is_neighbor": {
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 10
                                }
                            ]
                        },
                        "mt_is_neighbor": {
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 10
                                }
                            ]
                        },
                        "ip_address": "10.13.115.1",
                        "ipv4_internal_reachability": {
                            "10.12.115.0/24": [
                                {
                                    "ip_prefix": "10.12.115.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ],
                            "10.13.115.0/24": [
                                {
                                    "ip_prefix": "10.13.115.0",
                                    "prefix_len": "24",
                                    "metric": 10
                                }
                            ],
                            "10.23.115.0/24": [
                                {
                                    "ip_prefix": "10.23.115.0",
                                    "prefix_len": "24",
                                    "metric": 50
                                }
                            ]
                        },
                        "ipv6_address": "2001:10:13:115::1",
                        "mt_ipv6_reachability": {
                            "2001:10:12:115::/64": [
                                {
                                    "ip_prefix": "2001:10:12:115::",
                                    "prefix_len": "64",
                                    "metric": 10
                                }
                            ],
                            "2001:10:13:115::/64": [
                                {
                                    "ip_prefix": "2001:10:13:115::",
                                    "prefix_len": "64",
                                    "metric": 10
                                }
                            ],
                            "2001:10:23:115::/64": [
                                {
                                    "ip_prefix": "2001:10:23:115::",
                                    "prefix_len": "64",
                                    "metric": 50
                                }
                            ]
                        }
                    },
                    "R1_xe.02-00": {
                        "local_router": True,
                        "lsp_sequence_num": "0x0000011B",
                        "lsp_checksum": "0x9022",
                        "lsp_holdtime": "995",
                        "lsp_rcvd": "*",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "extended_is_neighbor": {
                            "R1_xe.00": [
                                {
                                    "neighbor_id": "R1_xe.00",
                                    "metric": 0
                                }
                            ],
                            "R3_nx.00": [
                                {
                                    "neighbor_id": "R3_nx.00",
                                    "metric": 0
                                }
                            ]
                        }
                    },
                    "R3_nx.00-00": {
                        "lsp_sequence_num": "0x00000191",
                        "lsp_checksum": "0x7535",
                        "lsp_holdtime": "958",
                        "lsp_rcvd": "1199",
                        "attach_bit": 0,
                        "p_bit": 0,
                        "overload_bit": 0,
                        "area_address": "49.0001",
                        "nlpid": "0xCC 0x8E",
                        "router_id": "10.36.3.3",
                        "ip_address": "10.36.3.3",
                        "topology": {
                            "ipv6": {
                                "code": "0x2"
                            },
                            "ipv4": {
                                "code": "0x0"
                            }
                        },
                        "hostname": "R3_nx",
                        "mt_is_neighbor": {
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 40
                                }
                            ]
                        },
                        "extended_is_neighbor": {
                            "R1_xe.02": [
                                {
                                    "neighbor_id": "R1_xe.02",
                                    "metric": 40
                                }
                            ]
                        },
                        "ipv4_internal_reachability": {
                            "10.36.3.3/32": [
                                {
                                    "ip_prefix": "10.36.3.3",
                                    "prefix_len": "32",
                                    "metric": 1
                                }
                            ],
                            "10.13.115.0/24": [
                                {
                                    "ip_prefix": "10.13.115.0",
                                    "prefix_len": "24",
                                    "metric": 40
                                }
                            ],
                            "10.23.115.0/24": [
                                {
                                    "ip_prefix": "10.23.115.0",
                                    "prefix_len": "24",
                                    "metric": 40
                                }
                            ]
                        },
                        "mt_ipv6_reachability": {
                            "2001:3:3:3::3/128": [
                                {
                                    "ip_prefix": "2001:3:3:3::3",
                                    "prefix_len": "128",
                                    "metric": 1
                                }
                            ],
                            "2001:10:13:115::/64": [
                                {
                                    "ip_prefix": "2001:10:13:115::",
                                    "prefix_len": "64",
                                    "metric": 40
                                }
                            ],
                            "2001:10:23:115::/64": [
                                {
                                    "ip_prefix": "2001:10:23:115::",
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
