expected_output = {
    "tag": {
        "test": {
            "level": {
                1: {
                    "R1_xe.01-00": {
                        "p_bit": 0,
                        "ipv4_interarea_reachability": {
                            "10.100.100.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.100.100.0",
                                "metric": 10
                            }
                        },
                        "extended_is_neighbor": {
                            "R1_xe.00": {
                                "metric": 0,
                                "neighbor_id": "R1_xe.00"
                            },
                            "R2_xr.00": {
                                "metric": 0,
                                "neighbor_id": "R2_xr.00"
                            }
                        },
                        "lsp_rcvd": "*",
                        "lsp_holdtime": "1087",
                        "attach_bit": 0,
                        "lsp_sequence_num": "0x00000118",
                        "overload_bit": 0,
                        "lsp_checksum": "0x850F",
                        "local_router": True
                    },
                    "R1_xe.00-00": {
                        "ipv6_address": "2001:10:13:115::1",
                        "hostname": "R1_xe",
                        "mt_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.02"
                            },
                            "R1_xe.01": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.01"
                            }
                        },
                        "lsp_sequence_num": "0x0000011D",
                        "overload_bit": 0,
                        "nlpid": "0xCC 0x8E",
                        "lsp_checksum": "0x2165",
                        "mt_ipv6_reachability": {
                            "2001:10:12:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:12:115::",
                                "metric": 10
                            },
                            "2001:10:13:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:13:115::",
                                "metric": 10
                            }
                        },
                        "ipv4_internal_reachability": {
                            "10.12.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.12.115.0",
                                "metric": 10
                            },
                            "10.13.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.13.115.0",
                                "metric": 10
                            }
                        },
                        "area_address": "49.0001",
                        "extended_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.02"
                            },
                            "R1_xe.01": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.01"
                            }
                        },
                        "lsp_rcvd": "*",
                        "lsp_holdtime": "519",
                        "attach_bit": 0,
                        "topology": {
                            "ipv4": {
                                "code": "0x0"
                            },
                            "ipv6": {
                                "code": "0x2"
                            }
                        },
                        "ip_address": "10.13.115.1",
                        "p_bit": 0,
                        "local_router": True
                    },
                    "R1_xe.02-00": {
                        "p_bit": 0,
                        "extended_is_neighbor": {
                            "R3_nx.00": {
                                "metric": 0,
                                "neighbor_id": "R3_nx.00"
                            },
                            "R1_xe.00": {
                                "metric": 0,
                                "neighbor_id": "R1_xe.00"
                            }
                        },
                        "lsp_rcvd": "*",
                        "lsp_holdtime": "752",
                        "attach_bit": 0,
                        "lsp_sequence_num": "0x00000118",
                        "overload_bit": 0,
                        "lsp_checksum": "0x7EAE",
                        "local_router": True
                    },
                    "R3_nx.00-00": {
                        "router_id": "10.36.3.3",
                        "hostname": "R3_nx",
                        "mt_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 40,
                                "neighbor_id": "R1_xe.02"
                            },
                            "R2_xr.03": {
                                "metric": 40,
                                "neighbor_id": "R2_xr.03"
                            }
                        },
                        "lsp_sequence_num": "0x00000193",
                        "overload_bit": 0,
                        "nlpid": "0xCC 0x8E",
                        "lsp_checksum": "0x8022",
                        "mt_ipv6_reachability": {
                            "2001:10:23:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:23:115::",
                                "metric": 40
                            },
                            "2001:3:3:3::3/128": {
                                "prefix_len": "128",
                                "ip_prefix": "2001:3:3:3::3",
                                "metric": 1
                            },
                            "2001:10:13:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:13:115::",
                                "metric": 40
                            }
                        },
                        "ipv4_internal_reachability": {
                            "10.23.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.23.115.0",
                                "metric": 40
                            },
                            "10.13.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.13.115.0",
                                "metric": 40
                            },
                            "10.36.3.3/32": {
                                "prefix_len": "32",
                                "ip_prefix": "10.36.3.3",
                                "metric": 1
                            }
                        },
                        "area_address": "49.0001",
                        "extended_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 40,
                                "neighbor_id": "R1_xe.02"
                            },
                            "R2_xr.03": {
                                "metric": 40,
                                "neighbor_id": "R2_xr.03"
                            }
                        },
                        "lsp_rcvd": "1200",
                        "lsp_holdtime": "1018",
                        "attach_bit": 0,
                        "ip_address": "10.36.3.3",
                        "p_bit": 0,
                        "topology": {
                            "ipv4": {
                                "code": "0x0"
                            },
                            "ipv6": {
                                "code": "0x2"
                            }
                        }
                    },
                    "R2_xr.00-00": {
                        "ipv6_address": "2001:2:2:2::2",
                        "extended_is_neighbor": {
                            "R1_xe.01": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.01"
                            },
                            "R2_xr.03": {
                                "metric": 10,
                                "neighbor_id": "R2_xr.03"
                            }
                        },
                        "ipv4_interarea_reachability": {
                            "10.200.200.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.200.200.0",
                                "metric": 10
                            },
                            "10.220.220.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.220.220.0",
                                "metric": 10
                            }
                        },
                        "mt_is_neighbor": {
                            "R1_xe.01": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.01"
                            },
                            "R2_xr.03": {
                                "metric": 10,
                                "neighbor_id": "R2_xr.03"
                            }
                        },
                        "lsp_sequence_num": "0x00000120",
                        "overload_bit": 0,
                        "nlpid": "0xCC 0x8E",
                        "lsp_checksum": "0xC84E",
                        "mt_ipv6_reachability": {
                            "2001:10:12:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:12:115::",
                                "metric": 10
                            },
                            "2001:10:23:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:23:115::",
                                "metric": 10
                            },
                            "2001:2:2:2::2/128": {
                                "prefix_len": "128",
                                "ip_prefix": "2001:2:2:2::2",
                                "metric": 10
                            }
                        },
                        "ipv4_internal_reachability": {
                            "10.12.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.12.115.0",
                                "metric": 10
                            },
                            "10.23.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.23.115.0",
                                "metric": 10
                            },
                            "10.16.2.2/32": {
                                "prefix_len": "32",
                                "ip_prefix": "10.16.2.2",
                                "metric": 10
                            }
                        },
                        "area_address": "49.0001",
                        "hostname": "R2_xr",
                        "lsp_rcvd": "1200",
                        "lsp_holdtime": "754",
                        "attach_bit": 0,
                        "ip_address": "10.16.2.2",
                        "p_bit": 0,
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
                        "extended_is_neighbor": {
                            "R3_nx.00": {
                                "metric": 0,
                                "neighbor_id": "R3_nx.00"
                            },
                            "R2_xr.00": {
                                "metric": 0,
                                "neighbor_id": "R2_xr.00"
                            }
                        },
                        "lsp_rcvd": "1200",
                        "lsp_holdtime": "563",
                        "attach_bit": 0,
                        "lsp_sequence_num": "0x00000118",
                        "overload_bit": 0,
                        "lsp_checksum": "0xF5F1",
                        "p_bit": 0
                    }
                },
                2: {
                    "R1_xe.01-00": {
                        "p_bit": 0,
                        "ipv4_interarea_reachability": {
                            "10.100.100.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.100.100.0",
                                "metric": 10
                            }
                        },
                        "extended_is_neighbor": {
                            "R1_xe.00": {
                                "metric": 0,
                                "neighbor_id": "R1_xe.00"
                            },
                            "R2_xr.00": {
                                "metric": 0,
                                "neighbor_id": "R2_xr.00"
                            }
                        },
                        "lsp_rcvd": "*",
                        "lsp_holdtime": "930",
                        "attach_bit": 0,
                        "lsp_sequence_num": "0x00000118",
                        "overload_bit": 0,
                        "lsp_checksum": "0x9D7F",
                        "local_router": True
                    },
                    "R1_xe.00-00": {
                        "ipv6_address": "2001:10:13:115::1",
                        "hostname": "R1_xe",
                        "mt_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.02"
                            },
                            "R1_xe.01": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.01"
                            }
                        },
                        "lsp_sequence_num": "0x0000011D",
                        "overload_bit": 0,
                        "nlpid": "0xCC 0x8E",
                        "lsp_checksum": "0x27D0",
                        "mt_ipv6_reachability": {
                            "2001:10:12:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:12:115::",
                                "metric": 10
                            },
                            "2001:10:23:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:23:115::",
                                "metric": 20
                            },
                            "2001:10:13:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:13:115::",
                                "metric": 10
                            }
                        },
                        "ipv4_internal_reachability": {
                            "10.12.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.12.115.0",
                                "metric": 10
                            },
                            "10.23.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.23.115.0",
                                "metric": 20
                            },
                            "10.13.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.13.115.0",
                                "metric": 10
                            }
                        },
                        "area_address": "49.0001",
                        "extended_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.02"
                            },
                            "R1_xe.01": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.01"
                            }
                        },
                        "lsp_rcvd": "*",
                        "lsp_holdtime": "521",
                        "attach_bit": 0,
                        "topology": {
                            "ipv4": {
                                "code": "0x0"
                            },
                            "ipv6": {
                                "code": "0x2"
                            }
                        },
                        "ip_address": "10.13.115.1",
                        "p_bit": 0,
                        "local_router": True
                    },
                    "R1_xe.02-00": {
                        "p_bit": 0,
                        "extended_is_neighbor": {
                            "R3_nx.00": {
                                "metric": 0,
                                "neighbor_id": "R3_nx.00"
                            },
                            "R1_xe.00": {
                                "metric": 0,
                                "neighbor_id": "R1_xe.00"
                            }
                        },
                        "lsp_rcvd": "*",
                        "lsp_holdtime": "1098",
                        "attach_bit": 0,
                        "lsp_sequence_num": "0x0000011E",
                        "overload_bit": 0,
                        "lsp_checksum": "0x8A25",
                        "local_router": True
                    },
                    "R3_nx.00-00": {
                        "router_id": "10.36.3.3",
                        "hostname": "R3_nx",
                        "mt_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 40,
                                "neighbor_id": "R1_xe.02"
                            },
                            "R2_xr.03": {
                                "metric": 40,
                                "neighbor_id": "R2_xr.03"
                            }
                        },
                        "lsp_sequence_num": "0x00000192",
                        "overload_bit": 0,
                        "nlpid": "0xCC 0x8E",
                        "lsp_checksum": "0x8221",
                        "mt_ipv6_reachability": {
                            "2001:10:23:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:23:115::",
                                "metric": 40
                            },
                            "2001:3:3:3::3/128": {
                                "prefix_len": "128",
                                "ip_prefix": "2001:3:3:3::3",
                                "metric": 1
                            },
                            "2001:10:13:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:13:115::",
                                "metric": 40
                            }
                        },
                        "ipv4_internal_reachability": {
                            "10.23.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.23.115.0",
                                "metric": 40
                            },
                            "10.13.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.13.115.0",
                                "metric": 40
                            },
                            "10.36.3.3/32": {
                                "prefix_len": "32",
                                "ip_prefix": "10.36.3.3",
                                "metric": 1
                            }
                        },
                        "area_address": "49.0001",
                        "extended_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 40,
                                "neighbor_id": "R1_xe.02"
                            },
                            "R2_xr.03": {
                                "metric": 40,
                                "neighbor_id": "R2_xr.03"
                            }
                        },
                        "lsp_rcvd": "1199",
                        "lsp_holdtime": "1132",
                        "attach_bit": 0,
                        "ip_address": "10.36.3.3",
                        "p_bit": 0,
                        "topology": {
                            "ipv4": {
                                "code": "0x0"
                            },
                            "ipv6": {
                                "code": "0x2"
                            }
                        }
                    },
                    "R2_xr.00-00": {
                        "ipv6_address": "2001:2:2:2::2",
                        "extended_is_neighbor": {
                            "R1_xe.01": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.01"
                            },
                            "R2_xr.03": {
                                "metric": 10,
                                "neighbor_id": "R2_xr.03"
                            }
                        },
                        "ipv4_interarea_reachability": {
                            "10.200.200.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.200.200.0",
                                "metric": 10
                            },
                            "10.220.220.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.220.220.0",
                                "metric": 10
                            }
                        },
                        "mt_is_neighbor": {
                            "R1_xe.01": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.01"
                            },
                            "R2_xr.03": {
                                "metric": 10,
                                "neighbor_id": "R2_xr.03"
                            }
                        },
                        "lsp_sequence_num": "0x00000120",
                        "overload_bit": 0,
                        "nlpid": "0xCC 0x8E",
                        "lsp_checksum": "0x1585",
                        "mt_ipv6_reachability": {
                            "2001:10:12:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:12:115::",
                                "metric": 10
                            },
                            "2001:10:23:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:23:115::",
                                "metric": 10
                            },
                            "2001:2:2:2::2/128": {
                                "prefix_len": "128",
                                "ip_prefix": "2001:2:2:2::2",
                                "metric": 10
                            },
                            "2001:3:3:3::3/128": {
                                "prefix_len": "128",
                                "ip_prefix": "2001:3:3:3::3",
                                "metric": 11
                            },
                            "2001:10:13:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:13:115::",
                                "metric": 20
                            }
                        },
                        "ipv4_internal_reachability": {
                            "10.12.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.12.115.0",
                                "metric": 10
                            },
                            "10.23.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.23.115.0",
                                "metric": 10
                            },
                            "10.13.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.13.115.0",
                                "metric": 20
                            },
                            "10.36.3.3/32": {
                                "prefix_len": "32",
                                "ip_prefix": "10.36.3.3",
                                "metric": 11
                            },
                            "10.16.2.2/32": {
                                "prefix_len": "32",
                                "ip_prefix": "10.16.2.2",
                                "metric": 10
                            }
                        },
                        "area_address": "49.0001",
                        "hostname": "R2_xr",
                        "lsp_rcvd": "1200",
                        "lsp_holdtime": "662",
                        "attach_bit": 0,
                        "ip_address": "10.16.2.2",
                        "p_bit": 0,
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
                        "extended_is_neighbor": {
                            "R3_nx.00": {
                                "metric": 0,
                                "neighbor_id": "R3_nx.00"
                            },
                            "R2_xr.00": {
                                "metric": 0,
                                "neighbor_id": "R2_xr.00"
                            }
                        },
                        "lsp_rcvd": "1200",
                        "lsp_holdtime": "872",
                        "attach_bit": 0,
                        "lsp_sequence_num": "0x00000118",
                        "overload_bit": 0,
                        "lsp_checksum": "0xF5F1",
                        "p_bit": 0
                    }
                }
            }
        },
        "test1": {
            "level": {
                1: {
                    "R1_xe.02-00": {
                        "p_bit": 0,
                        "extended_is_neighbor": {
                            "R3_nx.00": {
                                "metric": 0,
                                "neighbor_id": "R3_nx.00"
                            },
                            "R1_xe.00": {
                                "metric": 0,
                                "neighbor_id": "R1_xe.00"
                            }
                        },
                        "lsp_rcvd": "*",
                        "lsp_holdtime": "1080",
                        "attach_bit": 0,
                        "lsp_sequence_num": "0x0000011A",
                        "overload_bit": 0,
                        "lsp_checksum": "0x7AB0",
                        "local_router": True
                    },
                    "R3_nx.00-00": {
                        "router_id": "10.36.3.3",
                        "hostname": "R3_nx",
                        "mt_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 40,
                                "neighbor_id": "R1_xe.02"
                            }
                        },
                        "lsp_sequence_num": "0x00000191",
                        "overload_bit": 0,
                        "nlpid": "0xCC 0x8E",
                        "lsp_checksum": "0x7535",
                        "mt_ipv6_reachability": {
                            "2001:10:23:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:23:115::",
                                "metric": 40
                            },
                            "2001:3:3:3::3/128": {
                                "prefix_len": "128",
                                "ip_prefix": "2001:3:3:3::3",
                                "metric": 1
                            },
                            "2001:10:13:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:13:115::",
                                "metric": 40
                            }
                        },
                        "ipv4_internal_reachability": {
                            "10.23.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.23.115.0",
                                "metric": 40
                            },
                            "10.13.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.13.115.0",
                                "metric": 40
                            },
                            "10.36.3.3/32": {
                                "prefix_len": "32",
                                "ip_prefix": "10.36.3.3",
                                "metric": 1
                            }
                        },
                        "area_address": "49.0001",
                        "extended_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 40,
                                "neighbor_id": "R1_xe.02"
                            }
                        },
                        "lsp_rcvd": "1199",
                        "lsp_holdtime": "1068",
                        "attach_bit": 0,
                        "ip_address": "10.36.3.3",
                        "p_bit": 0,
                        "topology": {
                            "ipv4": {
                                "code": "0x0"
                            },
                            "ipv6": {
                                "code": "0x2"
                            }
                        }
                    },
                    "R1_xe.00-00": {
                        "ipv6_address": "2001:10:13:115::1",
                        "hostname": "R1_xe",
                        "mt_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.02"
                            }
                        },
                        "lsp_sequence_num": "0x0000011B",
                        "overload_bit": 0,
                        "nlpid": "0xCC 0x8E",
                        "lsp_checksum": "0x3941",
                        "mt_ipv6_reachability": {
                            "2001:10:12:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:12:115::",
                                "metric": 10
                            },
                            "2001:10:13:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:13:115::",
                                "metric": 10
                            }
                        },
                        "ipv4_internal_reachability": {
                            "10.12.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.12.115.0",
                                "metric": 10
                            },
                            "10.13.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.13.115.0",
                                "metric": 10
                            }
                        },
                        "area_address": "49.0001",
                        "extended_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.02"
                            }
                        },
                        "lsp_rcvd": "*",
                        "lsp_holdtime": "810",
                        "attach_bit": 0,
                        "topology": {
                            "ipv4": {
                                "code": "0x0"
                            },
                            "ipv6": {
                                "code": "0x2"
                            }
                        },
                        "ip_address": "10.13.115.1",
                        "p_bit": 0,
                        "local_router": True
                    }
                },
                2: {
                    "R1_xe.02-00": {
                        "p_bit": 0,
                        "extended_is_neighbor": {
                            "R3_nx.00": {
                                "metric": 0,
                                "neighbor_id": "R3_nx.00"
                            },
                            "R1_xe.00": {
                                "metric": 0,
                                "neighbor_id": "R1_xe.00"
                            }
                        },
                        "lsp_rcvd": "*",
                        "lsp_holdtime": "995",
                        "attach_bit": 0,
                        "lsp_sequence_num": "0x0000011B",
                        "overload_bit": 0,
                        "lsp_checksum": "0x9022",
                        "local_router": True
                    },
                    "R3_nx.00-00": {
                        "router_id": "10.36.3.3",
                        "hostname": "R3_nx",
                        "mt_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 40,
                                "neighbor_id": "R1_xe.02"
                            }
                        },
                        "lsp_sequence_num": "0x00000191",
                        "overload_bit": 0,
                        "nlpid": "0xCC 0x8E",
                        "lsp_checksum": "0x7535",
                        "mt_ipv6_reachability": {
                            "2001:10:23:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:23:115::",
                                "metric": 40
                            },
                            "2001:3:3:3::3/128": {
                                "prefix_len": "128",
                                "ip_prefix": "2001:3:3:3::3",
                                "metric": 1
                            },
                            "2001:10:13:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:13:115::",
                                "metric": 40
                            }
                        },
                        "ipv4_internal_reachability": {
                            "10.23.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.23.115.0",
                                "metric": 40
                            },
                            "10.13.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.13.115.0",
                                "metric": 40
                            },
                            "10.36.3.3/32": {
                                "prefix_len": "32",
                                "ip_prefix": "10.36.3.3",
                                "metric": 1
                            }
                        },
                        "area_address": "49.0001",
                        "extended_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 40,
                                "neighbor_id": "R1_xe.02"
                            }
                        },
                        "lsp_rcvd": "1199",
                        "lsp_holdtime": "958",
                        "attach_bit": 0,
                        "ip_address": "10.36.3.3",
                        "p_bit": 0,
                        "topology": {
                            "ipv4": {
                                "code": "0x0"
                            },
                            "ipv6": {
                                "code": "0x2"
                            }
                        }
                    },
                    "R1_xe.00-00": {
                        "ipv6_address": "2001:10:13:115::1",
                        "hostname": "R1_xe",
                        "mt_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.02"
                            }
                        },
                        "lsp_sequence_num": "0x0000011C",
                        "overload_bit": 0,
                        "nlpid": "0xCC 0x8E",
                        "lsp_checksum": "0x9618",
                        "mt_ipv6_reachability": {
                            "2001:10:12:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:12:115::",
                                "metric": 10
                            },
                            "2001:10:23:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:23:115::",
                                "metric": 50
                            },
                            "2001:10:13:115::/64": {
                                "prefix_len": "64",
                                "ip_prefix": "2001:10:13:115::",
                                "metric": 10
                            }
                        },
                        "ipv4_internal_reachability": {
                            "10.12.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.12.115.0",
                                "metric": 10
                            },
                            "10.23.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.23.115.0",
                                "metric": 50
                            },
                            "10.13.115.0/24": {
                                "prefix_len": "24",
                                "ip_prefix": "10.13.115.0",
                                "metric": 10
                            }
                        },
                        "area_address": "49.0001",
                        "extended_is_neighbor": {
                            "R1_xe.02": {
                                "metric": 10,
                                "neighbor_id": "R1_xe.02"
                            }
                        },
                        "lsp_rcvd": "*",
                        "lsp_holdtime": "1009",
                        "attach_bit": 0,
                        "topology": {
                            "ipv4": {
                                "code": "0x0"
                            },
                            "ipv6": {
                                "code": "0x2"
                            }
                        },
                        "ip_address": "10.13.115.1",
                        "p_bit": 0,
                        "local_router": True
                    }
                }
            }
        }
    }
}