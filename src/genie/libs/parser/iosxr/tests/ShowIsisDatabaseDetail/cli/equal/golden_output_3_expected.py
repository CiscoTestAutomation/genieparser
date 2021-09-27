

expected_output = {
    "instance": {
        "": {
            "level": {
                1: {
                    "lspid": {
                        "0000.0CFF.0C35.00-00": {
                            "lsp": {
                                "seq_num": "0x0000000C",
                                "checksum": "0x5696",
                                "local_router": False,
                                "holdtime": 325,
                                "attach_bit": 0,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "39.0001",
                            "is_neighbor": {
                                "0000.0CFF.62E6.03": {
                                    "metric": 10}},
                            "es_neighbor": {
                                "0000.0CFF.0C35": {
                                    "metric": 0}},
                        },
                        "0000.0CFF.40AF.00-00": {
                            "lsp": {
                                "seq_num": "0x00000009",
                                "checksum": "0x8452",
                                "local_router": True,
                                "holdtime": 608,
                                "attach_bit": 1,
                                "p_bit": 0,
                                "overload_bit": 0,
                            },
                            "area_address": "47.0004.00FF.4D4E",
                            "topology": ["IPv4 (0x0)", "IPv6 (0x2)"],
                            "nlpid": ["0x8E"],
                            "ip_address": "172.16.21.49",
                            "is_neighbor": {
                                "0800.2BFF.3A01.01": {
                                    "metric": 10},
                                "0000.0CFF.62E6.03": {
                                    "metric": 10},
                                "cisco.03": {
                                    "metric": 10},
                            },
                            "es_neighbor": {
                                "0000.0CFF.40AF": {
                                    "metric": 0}},
                            "ipv6_address": "2001:0DB8::/32",
                            "ipv6_reachability": {
                                "2001:0DB8::/64": {
                                    "ip_prefix": "2001:0DB8::",
                                    "prefix_length": "64",
                                    "metric": "10",
                                }
                            },
                            "extended_is_neighbor": {
                                "cisco.03": {
                                    "metric": 5},
                                "cisco1.03": {
                                    "metric": 10},
                            },
                        },
                    }
                }
            }
        }
    }
}
