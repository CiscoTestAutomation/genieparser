expected_output = {
    "isis_nodes": 0,
    "inet_nodes": 13,
    "node": {
        "10.4.1.1": {
            "type": "Rtr",
            "age": 2048,
            "link_in": 6,
            "link_out": 2,
            "protocol": {
                "OSPF(0.0.0.4)": {
                    "to": {
                        "172.16.1.1": {
                            "local": {
                                "172.16.1.2": {
                                    "remote": {
                                        "172.16.1.3": {
                                            "local_interface_index": 123,
                                            "remote_interface_index": 0,
                                            "color": "0 <none>",
                                            "metric": 4,
                                            "static_bw": "500Mbps",
                                            "reservable_bw": "500Mbps",
                                            "available_bw": {
                                                0: {"bw": "500Mbps"},
                                                1: {"bw": "500Mbps"},
                                                2: {"bw": "500Mbps"},
                                                3: {"bw": "500Mbps"},
                                                4: {"bw": "500Mbps"},
                                                5: {"bw": "500Mbps"},
                                                6: {"bw": "500Mbps"},
                                                7: {"bw": "500Mbps"},
                                            },
                                            "interface_switching_capability_descriptor": {
                                                "1": {
                                                    "switching_type": "Packet",
                                                    "encoding_type": "Packet",
                                                    "maximum_lsp_bw": {
                                                        0: {"bw": "500Mbps"},
                                                        1: {"bw": "500Mbps"},
                                                        2: {"bw": "500Mbps"},
                                                        3: {"bw": "500Mbps"},
                                                        4: {"bw": "500Mbps"},
                                                        5: {"bw": "500Mbps"},
                                                        6: {"bw": "500Mbps"},
                                                        7: {"bw": "500Mbps"},
                                                    },
                                                }
                                            },
                                            "p2p_adj_sid": {
                                                "sid": {
                                                    "8": {
                                                        "address_family": "IPV4",
                                                        "flags": "0x35",
                                                        "weight": 0,
                                                    }
                                                }
                                            },
                                        }
                                    }
                                }
                            }
                        },
                        "172.16.1.4": {
                            "local": {
                                "172.16.1.5": {
                                    "remote": {
                                        "172.16.1.6": {
                                            "local_interface_index": 456,
                                            "remote_interface_index": 0,
                                            "color": "0x2 blue",
                                            "metric": 350,
                                            "static_bw": "500Mbps",
                                            "reservable_bw": "500Mbps",
                                            "available_bw": {
                                                0: {"bw": "500Mbps"},
                                                1: {"bw": "500Mbps"},
                                                2: {"bw": "500Mbps"},
                                                3: {"bw": "500Mbps"},
                                                4: {"bw": "500Mbps"},
                                                5: {"bw": "500Mbps"},
                                                6: {"bw": "500Mbps"},
                                                7: {"bw": "500Mbps"},
                                            },
                                            "interface_switching_capability_descriptor": {
                                                "1": {
                                                    "switching_type": "Packet",
                                                    "encoding_type": "Packet",
                                                    "maximum_lsp_bw": {
                                                        0: {"bw": "500Mbps"},
                                                        1: {"bw": "500Mbps"},
                                                        2: {"bw": "500Mbps"},
                                                        3: {"bw": "500Mbps"},
                                                        4: {"bw": "500Mbps"},
                                                        5: {"bw": "500Mbps"},
                                                        6: {"bw": "500Mbps"},
                                                        7: {"bw": "500Mbps"},
                                                    },
                                                }
                                            },
                                            "p2p_adj_sid": {
                                                "sid": {
                                                    "39": {
                                                        "address_family": "IPV4",
                                                        "flags": "0x40",
                                                        "weight": 0,
                                                    }
                                                }
                                            },
                                        }
                                    }
                                }
                            }
                        },
                    },
                    "prefixes": {
                        "192.168.0.1/32": {
                            "flags": "0x30",
                            "prefix_sid": {42: {"flags": "0x00", "algo": 0}},
                        }
                    },
                    "spring_capabilities": {
                        "srgb_block": {"start": 8000, "range": 6000, "flags": "0x00"}
                    },
                    "spring_algorithms": ["0"],
                }
            },
        }
    },
}
