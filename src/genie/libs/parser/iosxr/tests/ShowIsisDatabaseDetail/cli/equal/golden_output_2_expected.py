

expected_output = {
    "instance": {
        "isp": {
            "level": {
                1: {
                    "lspid": {
                        "router-5.00-00": {
                            "lsp": {
                                "seq_num": "0x00000003",
                                "checksum": "0x8074460",
                                "local_router": False,
                                "holdtime": 457,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "49",
                            "nlpid": ["0xcc"],
                            "hostname": "router-5",
                            "ip_address": "172.16.186.5",
                            "ip_neighbor": {
                                "172.16.115.0/24": {
                                    "ip_prefix": "172.16.115.0",
                                    "prefix_length": "24",
                                    "metric": 0,
                                },
                                "172.16.166.0/24": {
                                    "ip_prefix": "172.16.166.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                                "172.16.166.0/24": {
                                    "ip_prefix": "172.16.166.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                            },
                            "is_neighbor": {
                                "router-11.00": {
                                    "metric": 10},
                                "router-11.01": {
                                    "metric": 10},
                            },
                        },
                        "router-11.00-00": {
                            "lsp": {
                                "seq_num": "0x0000000b",
                                "checksum": "0x8074460",
                                "local_router": True,
                                "holdtime": 1161,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "49",
                            "nlpid": ["0xcc"],
                            "hostname": "router-11",
                            "ip_address": "172.16.196.11",
                            "ip_neighbor": {
                                "172.16.76.0/24": {
                                    "ip_prefix": "172.16.76.0",
                                    "prefix_length": "24",
                                    "metric": 0,
                                },
                                "172.16.166.0/24": {
                                    "ip_prefix": "172.16.166.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                                "172.16.166.0/24": {
                                    "ip_prefix": "172.16.166.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                            },
                            "is_neighbor": {
                                "router-11.01": {
                                    "metric": 10},
                                "router-5.00": {
                                    "metric": 10},
                            },
                        },
                        "router-11.01-00": {
                            "lsp": {
                                "seq_num": "0x00000001",
                                "checksum": "0x80770ec",
                                "local_router": True,
                                "holdtime": 457,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "is_neighbor": {
                                "router-11.00": {
                                    "metric": 0},
                                "router-5.00": {
                                    "metric": 0},
                            },
                        },
                    },
                    "total_lsp_count": 3,
                    "local_lsp_count": 2,
                },
                2: {
                    "lspid": {
                        "router-5.00-00": {
                            "lsp": {
                                "seq_num": "0x00000005",
                                "checksum": "0x807997c",
                                "local_router": False,
                                "holdtime": 457,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "49",
                            "nlpid": ["0xcc"],
                            "hostname": "router-5",
                            "ip_address": "172.16.166.5",
                            "ip_neighbor": {
                                "172.16.115.0/24": {
                                    "ip_prefix": "172.16.115.0",
                                    "prefix_length": "24",
                                    "metric": 0,
                                },
                                "172.16.166.0/24": {
                                    "ip_prefix": "172.16.166.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                                "172.16.94.0/24": {
                                    "ip_prefix": "172.16.94.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                                "172.16.21.0/24": {
                                    "ip_prefix": "172.16.21.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                            },
                            "is_neighbor": {
                                "router-11.00": {
                                    "metric": 10},
                                "router-11.01": {
                                    "metric": 10},
                            },
                        },
                        "router-11.00-00": {
                            "lsp": {
                                "seq_num": "0x0000000d",
                                "checksum": "0x807997c",
                                "local_router": True,
                                "holdtime": 1184,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "49",
                            "nlpid": ["0xcc"],
                            "hostname": "router-11",
                            "ip_address": "172.28.111.111",
                            "ip_neighbor": {
                                "172.16.21.0/24": {
                                    "ip_prefix": "172.16.21.0",
                                    "prefix_length": "24",
                                    "metric": 0,
                                },
                                "172.16.166.0/24": {
                                    "ip_prefix": "172.16.166.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                                "172.16.166.0/24": {
                                    "ip_prefix": "172.16.166.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                                "172.16.115.0/24": {
                                    "ip_prefix": "172.16.115.0",
                                    "prefix_length": "24",
                                    "metric": 10,
                                },
                            },
                            "is_neighbor": {
                                "router-11.01": {
                                    "metric": 10},
                                "router-5.00": {
                                    "metric": 10},
                            },
                        },
                        "router-gsr11.01-00": {
                            "lsp": {
                                "seq_num": "0x00000001",
                                "checksum": "0x80770ec",
                                "local_router": True,
                                "holdtime": 457,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "is_neighbor": {
                                "router-11.00": {
                                    "metric": 0},
                                "router-5.00": {
                                    "metric": 0},
                            },
                        },
                    },
                    "total_lsp_count": 3,
                    "local_lsp_count": 2,
                },
            }
        }
    }
}
