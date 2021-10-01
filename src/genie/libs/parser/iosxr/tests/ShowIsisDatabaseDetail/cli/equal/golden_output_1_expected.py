

expected_output = {
    "instance": {
        "test": {
            "level": {
                1: {
                    "lspid": {
                        "R3.00-00": {
                            "lsp": {
                                "seq_num": "0x0000000d",
                                "checksum": "0x0476",
                                "local_router": True,
                                "holdtime": 578,
                                "attach_bit": 1,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "49.0002",
                            "nlpid": ["0xcc", "0x8e"],
                            "ip_address": "10.36.3.3",
                            "extended_ipv4_reachability": {
                                "10.36.3.0/24": {
                                    "ip_prefix": "10.36.3.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                                "10.2.3.0/24": {
                                    "ip_prefix": "10.2.3.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                            },
                            "hostname": "R3",
                            "ipv6_address": "2001:db8:3:3:3::3",
                            "mt_ipv6_reachability": {
                                "2001:db8:3:3:3::3/128": {
                                    "ip_prefix": "2001:db8:3:3:3::3",
                                    "prefix_length": "128",
                                    "metric": 10,
                                },
                                "2001:db8:10:2::/64": {
                                    "ip_prefix": "2001:db8:10:2::",
                                    "prefix_length": "64",
                                    "metric": 10,
                                },
                            },
                            "mt_entries": {
                                "Standard (IPv4 Unicast)": {},
                                "IPv6 Unicast": {
                                    "attach_bit": 1,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                            },
                            "extended_is_neighbor": {
                                "R3.03": {"metric": 10},
                                "R5.01": {"metric": 10},
                            },
                            "mt_is_neighbor": {
                                "R3.03": {
                                    "metric": 10,
                                    "mt_id": "MT (IPv6 Unicast)"},
                                "R5.01": {
                                    "metric": 10,
                                    "mt_id": "MT (IPv6 Unicast)"},
                            },
                        },
                        "R3.03-00": {
                            "lsp": {
                                "seq_num": "0x00000007",
                                "checksum": "0x8145",
                                "local_router": False,
                                "holdtime": 988,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "extended_is_neighbor": {
                                "R3.00": {
                                    "metric": 0},
                                "R4.00": {
                                    "metric": 0},
                            },
                        },
                        "R3.05-00": {
                            "lsp": {
                                "seq_num": "0x00000004",
                                "checksum": "0x7981",
                                "local_router": False,
                                "holdtime": 600,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "extended_is_neighbor": {
                                "R3.00": {
                                    "metric": 0},
                                "R6.00": {
                                    "metric": 0},
                            },
                        },
                        "R4.00-00": {
                            "lsp": {
                                "seq_num": "0x0000000c",
                                "checksum": "0x5c39",
                                "local_router": False,
                                "holdtime": 1115,
                                "received": 1200,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "49.0002",
                            "extended_is_neighbor": {
                                "R3.03": {
                                    "metric": 10},
                                "R4.01": {
                                    "metric": 10},
                            },
                            "nlpid": ["0xcc", "0x8e"],
                            "ip_address": "10.64.4.4",
                            "extended_ipv4_reachability": {
                                "10.64.4.4/32": {
                                    "ip_prefix": "10.64.4.4",
                                    "prefix_length": "32",
                                    "metric": 10,
                                },
                                "10.3.4.0/24": {
                                    "ip_prefix": "10.3.4.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                            },
                            "hostname": "R4",
                            "mt_is_neighbor": {
                                "R3.03": {
                                    "metric": 10,
                                    "mt_id": "MT (IPv6 Unicast)"},
                                "R4.01": {
                                    "metric": 10,
                                    "mt_id": "MT (IPv6 Unicast)"},
                            },
                            "ipv6_address": "2001:db8:4:4:4::4",
                            "mt_ipv6_reachability": {
                                "2001:db8:4:4:4::4/128": {
                                    "ip_prefix": "2001:db8:4:4:4::4",
                                    "prefix_length": "128",
                                    "metric": 10,
                                },
                                "2001:db8:10:3::/64": {
                                    "ip_prefix": "2001:db8:10:3::",
                                    "prefix_length": "64",
                                    "metric": 10,
                                },
                            },
                            "mt_entries": {
                                "Standard (IPv4 Unicast)": {},
                                "IPv6 Unicast": {
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                            },
                        },
                        "R4.01-00": {
                            "lsp": {
                                "seq_num": "0x00000004",
                                "checksum": "0xf9a0",
                                "local_router": False,
                                "holdtime": 616,
                                "received": 1200,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "extended_is_neighbor": {
                                "R4.00": {
                                    "metric": 0},
                                "R5.00": {
                                    "metric": 0},
                            },
                        },
                        "R5.00-00": {
                            "lsp": {
                                "seq_num": "0x00000009",
                                "checksum": "0x09f9",
                                "local_router": False,
                                "holdtime": 980,
                                "received": 1199,
                                "attach_bit": 1,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "49.0002",
                            "nlpid": ["0xcc", "0x8e"],
                            "mt_entries": {
                                "Standard (IPv4 Unicast)": {},
                                "IPv6 Unicast": {
                                    "attach_bit": 1,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                            },
                            "hostname": "R5",
                            "extended_is_neighbor": {
                                "R5.01": {
                                    "metric": 10},
                                "R4.01": {
                                    "metric": 10},
                            },
                            "mt_is_neighbor": {
                                "R5.01": {
                                    "metric": 10,
                                    "mt_id": "MT (IPv6 Unicast)"},
                                "R4.01": {
                                    "metric": 10,
                                    "mt_id": "MT (IPv6 Unicast)"},
                            },
                            "ip_address": "10.100.5.5",
                            "extended_ipv4_reachability": {
                                "10.100.5.5/32": {
                                    "ip_prefix": "10.100.5.5",
                                    "prefix_length": "32",
                                    "metric": 10,
                                },
                                "10.3.5.0/24": {
                                    "ip_prefix": "10.3.5.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                            },
                            "ipv6_address": "2001:db8:5:5:5::5",
                            "mt_ipv6_reachability": {
                                "2001:db8:5:5:5::5/128": {
                                    "ip_prefix": "2001:db8:5:5:5::5",
                                    "prefix_length": "128",
                                    "metric": 10,
                                },
                                "2001:db8:10:3::/64": {
                                    "ip_prefix": "2001:db8:10:3::",
                                    "prefix_length": "64",
                                    "metric": 10,
                                },
                            },
                        },
                        "R5.01-00": {
                            "lsp": {
                                "seq_num": "0x00000004",
                                "checksum": "0x4ac5",
                                "local_router": False,
                                "holdtime": 521,
                                "received": 1199,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "extended_is_neighbor": {
                                "R5.00": {
                                    "metric": 0},
                                "R3.00": {
                                    "metric": 0},
                            },
                        },
                        "R5.03-00": {
                            "lsp": {
                                "seq_num": "0x00000004",
                                "checksum": "0x3c38",
                                "local_router": False,
                                "holdtime": 1023,
                                "received": 1199,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "extended_is_neighbor": {
                                "R5.00": {
                                    "metric": 0},
                                "R7.00": {
                                    "metric": 0},
                            },
                        },
                        "R6.00-00": {
                            "lsp": {
                                "seq_num": "0x00000008",
                                "checksum": "0x1869",
                                "local_router": False,
                                "holdtime": 923,
                                "received": 1199,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "49.0002",
                            "nlpid": ["0xcc", "0x8e"],
                            "router_id": "10.144.6.6",
                            "ip_address": "10.144.6.6",
                            "mt_entries": {
                                "IPv6 Unicast": {
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "Standard (IPv4 Unicast)": {},
                            },
                            "hostname": "R6",
                            "mt_is_neighbor": {
                                "R7.02": {
                                    "metric": 40,
                                    "mt_id": "MT (IPv6 Unicast)"},
                                "R3.05": {
                                    "metric": 40,
                                    "mt_id": "MT (IPv6 Unicast)"},
                            },
                            "extended_is_neighbor": {
                                "R7.02": {
                                    "metric": 40},
                                "R3.05": {
                                    "metric": 40},
                            },
                            "extended_ipv4_reachability": {
                                "10.144.6.0/24": {
                                    "ip_prefix": "10.144.6.0",
                                    "prefix_length": "24",
                                    "metric": 1,
                                },
                                "10.6.7.0/24": {
                                    "ip_prefix": "10.6.7.0",
                                    "prefix_length": "24",
                                    "metric": 40,
                                },
                                "10.3.6.0/24": {
                                    "ip_prefix": "10.3.6.0",
                                    "prefix_length": "24",
                                    "metric": 40,
                                },
                            },
                            "mt_ipv6_reachability": {
                                "2001:db8:6:6:6::6/128": {
                                    "ip_prefix": "2001:db8:6:6:6::6",
                                    "prefix_length": "128",
                                    "metric": 1,
                                },
                                "2001:db8:10:6::/64": {
                                    "ip_prefix": "2001:db8:10:6::",
                                    "prefix_length": "64",
                                    "metric": 40,
                                },
                            },
                        },
                        "R7.00-00": {
                            "lsp": {
                                "seq_num": "0x00000008",
                                "checksum": "0xaba8",
                                "local_router": False,
                                "holdtime": 965,
                                "received": 1198,
                                "attach_bit": 1,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "49.0002",
                            "nlpid": ["0xcc", "0x8e"],
                            "router_id": "10.196.7.7",
                            "ip_address": "10.196.7.7",
                            "mt_entries": {
                                "IPv6 Unicast": {
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "Standard (IPv4 Unicast)": {},
                            },
                            "hostname": "R7",
                            "mt_is_neighbor": {
                                "R7.02": {
                                    "metric": 40,
                                    "mt_id": "MT (IPv6 Unicast)"},
                                "R5.03": {
                                    "metric": 40,
                                    "mt_id": "MT (IPv6 Unicast)"},
                            },
                            "extended_is_neighbor": {
                                "R7.02": {
                                    "metric": 40},
                                "R5.03": {
                                    "metric": 40},
                            },
                            'ip_interarea': {
                                '10.7.8.0/24': {
                                    'address_family': {
                                        'ipv4 unicast': {
                                            'metric': 40,
                                        },
                                    },
                                },
                                '2001:db8:10:7::/64': {
                                    'address_family': {
                                        'IPv6 Unicast': {
                                            'metric': 40,
                                        },
                                    },
                                },
                            },
                            "extended_ipv4_reachability": {
                                "10.196.7.7/32": {
                                    "ip_prefix": "10.196.7.7",
                                    "prefix_length": "32",
                                    "metric": 1,
                                },
                                "10.7.9.0/24": {
                                    "ip_prefix": "10.7.9.0",
                                    "prefix_length": "24",
                                    "metric": 40,
                                },
                            },
                            "mt_ipv6_reachability": {
                                "2001:db8:7:7:7::7/128": {
                                    "ip_prefix": "2001:db8:7:7:7::7",
                                    "prefix_length": "128",
                                    "metric": 1,
                                }
                            },
                        },
                        "R7.02-00": {
                            "lsp": {
                                "seq_num": "0x00000005",
                                "checksum": "0x8c3d",
                                "local_router": False,
                                "holdtime": 884,
                                "received": 1198,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "extended_is_neighbor": {
                                "R6.00": {"metric": 0},
                                "R7.00": {"metric": 0},
                            },
                        },
                    },
                    "total_lsp_count": 11,
                    "local_lsp_count": 1,
                },
                2: {
                    "lspid": {
                        "R2.00-00": {
                            "lsp": {
                                "seq_num": "0x00000009",
                                "checksum": "0x5188",
                                "local_router": False,
                                "holdtime": 1082,
                                "received": 1199,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "49.0001",
                            "nlpid": ["0xcc", "0x8e"],
                            "mt_entries": {
                                "Standard (IPv4 Unicast)": {},
                                "IPv6 Unicast": {
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                            },
                            "hostname": "R2",
                            "extended_is_neighbor": {
                                "R3.07": {
                                    "metric": 10}},
                            "mt_is_neighbor": {
                                "R3.07": {
                                    "metric": 10,
                                    "mt_id": "MT (IPv6 Unicast)"}
                            },
                            "ip_address": "10.16.2.2",
                            "extended_ipv4_reachability": {
                                "10.16.2.2/32": {
                                    "ip_prefix": "10.16.2.2",
                                    "prefix_length": "32",
                                    "metric": 10,
                                },
                                "10.1.2.0/24": {
                                    "ip_prefix": "10.1.2.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                            },
                            "ipv6_address": "2001:db8:2:2:2::2",
                            "mt_ipv6_reachability": {
                                "2001:db8:2:2:2::2/128": {
                                    "ip_prefix": "2001:db8:2:2:2::2",
                                    "prefix_length": "128",
                                    "metric": 10,
                                },
                                "2001:db8:10:1::/64": {
                                    "ip_prefix": "2001:db8:10:1::",
                                    "prefix_length": "64",
                                    "metric": 10,
                                },
                            },
                        },
                        "R3.00-00": {
                            "lsp": {
                                "seq_num": "0x00000011",
                                "checksum": "0x4c4c",
                                "local_router": True,
                                "holdtime": 979,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "49.0002",
                            "extended_is_neighbor": {
                                "R3.07": {
                                    "metric": 10},
                                "R5.01": {
                                    "metric": 10},
                            },
                            "nlpid": ["0xcc", "0x8e"],
                            "ip_address": "10.36.3.3",
                            "extended_ipv4_reachability": {
                                "10.36.3.0/24": {
                                    "ip_prefix": "10.36.3.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                                "10.2.3.0/24": {
                                    "ip_prefix": "10.2.3.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                            },
                            "hostname": "R3",
                            "mt_is_neighbor": {
                                "R3.07": {
                                    "metric": 10,
                                    "mt_id": "MT (IPv6 Unicast)"},
                                "R5.01": {
                                    "metric": 10,
                                    "mt_id": "MT (IPv6 Unicast)"},
                            },
                            "ipv6_address": "2001:db8:3:3:3::3",
                            "mt_ipv6_reachability": {
                                "2001:db8:3:3:3::3/128": {
                                    "ip_prefix": "2001:db8:3:3:3::3",
                                    "prefix_length": "128",
                                    "metric": 10,
                                },
                                "2001:db8:10:2::/64": {
                                    "ip_prefix": "2001:db8:10:2::",
                                    "prefix_length": "64",
                                    "metric": 10,
                                },
                            },
                            "mt_entries": {
                                "Standard (IPv4 Unicast)": {},
                                "IPv6 Unicast": {
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                            },
                        },
                        "R3.07-00": {
                            "lsp": {
                                "seq_num": "0x00000007",
                                "checksum": "0x652a",
                                "local_router": False,
                                "holdtime": 604,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "extended_is_neighbor": {
                                "R3.00": {
                                    "metric": 0},
                                "R2.00": {
                                    "metric": 0},
                            },
                        },
                        "R5.00-00": {
                            "lsp": {
                                "seq_num": "0x0000000b",
                                "checksum": "0x93bc",
                                "local_router": False,
                                "holdtime": 903,
                                "received": 1199,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "49.0002",
                            "nlpid": ["0xcc", "0x8e"],
                            "mt_entries": {
                                "Standard (IPv4 Unicast)": {},
                                "IPv6 Unicast": {
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                            },
                            "hostname": "R5",
                            "extended_is_neighbor": {
                                "R5.01": {
                                    "metric": 10},
                                "R5.03": {
                                    "metric": 10},
                            },
                            "mt_is_neighbor": {
                                "R5.01": {
                                    "metric": 10,
                                    "mt_id": "MT (IPv6 Unicast)"},
                                "R5.03": {
                                    "metric": 10,
                                    "mt_id": "MT (IPv6 Unicast)"},
                            },
                            "ip_address": "10.100.5.5",
                            "extended_ipv4_reachability": {
                                "10.100.5.5/32": {
                                    "ip_prefix": "10.100.5.5",
                                    "prefix_length": "32",
                                    "metric": 10,
                                },
                                "10.3.5.0/24": {
                                    "ip_prefix": "10.3.5.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                            },
                            "ipv6_address": "2001:db8:5:5:5::5",
                            "mt_ipv6_reachability": {
                                "2001:db8:5:5:5::5/128": {
                                    "ip_prefix": "2001:db8:5:5:5::5",
                                    "prefix_length": "128",
                                    "metric": 10,
                                },
                                "2001:db8:10:3::/64": {
                                    "ip_prefix": "2001:db8:10:3::",
                                    "prefix_length": "64",
                                    "metric": 10,
                                },
                            },
                        },
                        "R5.01-00": {
                            "lsp": {
                                "seq_num": "0x00000004",
                                "checksum": "0x6236",
                                "local_router": False,
                                "holdtime": 426,
                                "received": 1199,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "extended_is_neighbor": {
                                "R5.00": {
                                    "metric": 0},
                                "R3.00": {
                                    "metric": 0},
                            },
                        },
                        "R5.03-00": {
                            "lsp": {
                                "seq_num": "0x00000004",
                                "checksum": "0x54a8",
                                "local_router": False,
                                "holdtime": 965,
                                "received": 1199,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "extended_is_neighbor": {
                                "R5.00": {
                                    "metric": 0},
                                "R7.00": {
                                    "metric": 0},
                            },
                        },
                        "R7.00-00": {
                            "lsp": {
                                "seq_num": "0x00000009",
                                "checksum": "0x7d78",
                                "local_router": False,
                                "holdtime": 766,
                                "received": 1198,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "49.0002",
                            "nlpid": ["0xcc", "0x8e"],
                            "router_id": "10.196.7.7",
                            "ip_address": "10.196.7.7",
                            "mt_entries": {
                                "IPv6 Unicast": {
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                                "Standard (IPv4 Unicast)": {},
                            },
                            "hostname": "R7",
                            "mt_is_neighbor": {
                                "R9.01": {
                                    "metric": 40,
                                    "mt_id": "MT (IPv6 Unicast)"},
                                "R8.01": {
                                    "metric": 40,
                                    "mt_id": "MT (IPv6 Unicast)"},
                            },
                            "extended_is_neighbor": {
                                "R9.01": {
                                    "metric": 40},
                                "R8.01": {
                                    "metric": 40},
                            },
                            "extended_ipv4_reachability": {
                                "10.6.7.0/24": {
                                    "ip_prefix": "10.6.7.0",
                                    "prefix_length": "24",
                                    "metric": 40,
                                },
                                "10.196.7.7/32": {
                                    "ip_prefix": "10.196.7.7",
                                    "prefix_length": "32",
                                    "metric": 1,
                                },
                            },
                            "mt_ipv6_reachability": {
                                "2001:db8:10:6::/64": {
                                    "ip_prefix": "2001:db8:10:6::",
                                    "prefix_length": "64",
                                    "metric": 40,
                                },
                                "2001:db8:7:7:7::7/128": {
                                    "ip_prefix": "2001:db8:7:7:7::7",
                                    "prefix_length": "128",
                                    "metric": 1,
                                },
                            },
                        },
                        "R8.00-00": {
                            "lsp": {
                                "seq_num": "0x00000005",
                                "checksum": "0x1309",
                                "local_router": False,
                                "holdtime": 453,
                                "received": 1198,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "49.0003",
                            "nlpid": ["0xcc", "0x8e"],
                            "mt_entries": {
                                "Standard (IPv4 Unicast)": {},
                                "IPv6 Unicast": {
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                            },
                            "hostname": "R8",
                            "extended_is_neighbor": {
                                "R8.01": {
                                    "metric": 10}},
                            "mt_is_neighbor": {
                                "R8.01": {
                                    "metric": 10,
                                    "mt_id": "MT (IPv6 Unicast)"}
                            },
                            "ip_address": "10.1.8.8",
                            "extended_ipv4_reachability": {
                                "10.1.8.8/32": {
                                    "ip_prefix": "10.1.8.8",
                                    "prefix_length": "32",
                                    "metric": 10,
                                },
                                "10.7.8.0/24": {
                                    "ip_prefix": "10.7.8.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                            },
                            "ipv6_address": "2001:db8:8:8:8::8",
                            "mt_ipv6_reachability": {
                                "2001:db8:8:8:8::8/128": {
                                    "ip_prefix": "2001:db8:8:8:8::8",
                                    "prefix_length": "128",
                                    "metric": 10,
                                },
                                "2001:db8:10:7::/64": {
                                    "ip_prefix": "2001:db8:10:7::",
                                    "prefix_length": "64",
                                    "metric": 10,
                                },
                            },
                        },
                        "R8.01-00": {
                            "lsp": {
                                "seq_num": "0x00000004",
                                "checksum": "0x9503",
                                "local_router": False,
                                "holdtime": 1143,
                                "received": 1198,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "extended_is_neighbor": {
                                "R8.00": {
                                    "metric": 0},
                                "R7.00": {
                                    "metric": 0},
                            },
                        },
                        "R9.00-00": {
                            "lsp": {
                                "seq_num": "0x00000006",
                                "checksum": "0xfd4e",
                                "local_router": False,
                                "holdtime": 800,
                                "received": 1198,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "49.0004",
                            "nlpid": ["0xcc", "0x8e"],
                            "mt_entries": {
                                "Standard (IPv4 Unicast)": {},
                                "IPv6 Unicast": {
                                    "attach_bit": 0,
                                    "p_bit": 0,
                                    "overload_bit": 0,
                                },
                            },
                            "hostname": "R9",
                            "extended_is_neighbor": {
                                "R9.01": {
                                    "metric": 10}},
                            "mt_is_neighbor": {
                                "R9.01": {
                                    "metric": 10,
                                    "mt_id": "MT (IPv6 Unicast)"}
                            },
                            "ip_address": "10.69.9.9",
                            "extended_ipv4_reachability": {
                                "10.69.9.9/32": {
                                    "ip_prefix": "10.69.9.9",
                                    "prefix_length": "32",
                                    "metric": 10,
                                },
                                "10.7.9.0/24": {
                                    "ip_prefix": "10.7.9.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                                "10.9.10.0/24": {
                                    "ip_prefix": "10.9.10.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                                "10.10.10.10/32": {
                                    "ip_prefix": "10.10.10.10",
                                    "prefix_length": "32",
                                    "metric": 20,
                                },
                            },
                            "ipv6_address": "2001:db8:9:9:9::9",
                            "mt_ipv6_reachability": {
                                "2001:db8:9:9:9::9/128": {
                                    "ip_prefix": "2001:db8:9:9:9::9",
                                    "prefix_length": "128",
                                    "metric": 10,
                                },
                                "2001:db8:10:7::/64": {
                                    "ip_prefix": "2001:db8:10:7::",
                                    "prefix_length": "64",
                                    "metric": 10,
                                },
                            },
                            "ipv6_reachability": {
                                "2001:2:2:2::2/128": {
                                    "ip_prefix": "2001:2:2:2::2",
                                    "prefix_length": "128",
                                    "metric": "10",
                                }
                            },
                        },
                        "R9.01-00": {
                            "lsp": {
                                "seq_num": "0x00000003",
                                "checksum": "0xfdce",
                                "local_router": False,
                                "holdtime": 706,
                                "received": 1198,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "extended_is_neighbor": {
                                "R9.00": {
                                    "metric": 0},
                                "R7.00": {
                                    "metric": 0},
                            },
                        },
                    },
                    "total_lsp_count": 11,
                    "local_lsp_count": 1,
                },
            }
        }
    }
}
