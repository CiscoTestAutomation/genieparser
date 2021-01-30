expected_output = {
    "isis_nodes": 0,
    "inet_nodes": 6,
    "node": {
        "10.4.1.1": {
            "type": "Rtr",
            "age": 1024,
            "link_in": 0,
            "link_out": 1,
            "protocol": {
                "OSPF(0.0.0.4)": {
                    "to": {
                        "172.16.1.1": {
                            "local": {
                                "10.4.0.2": {
                                    "remote": {
                                        "10.4.0.1": {
                                            "local_interface_index": 0,
                                            "remote_interface_index": 0,
                                            "color": "0 <none>",
                                            "metric": 1,
                                            "static_bw": "2000Mbps",
                                            "reservable_bw": "0bps",
                                            "available_bw": {
                                                0: {"bw": "10bps"},
                                                1: {"bw": "10bps"},
                                                2: {"bw": "0bps"},
                                                3: {"bw": "0bps"},
                                                4: {"bw": "10bps"},
                                                5: {"bw": "0bps"},
                                                6: {"bw": "0bps"},
                                                7: {"bw": "0bps"},
                                            },
                                            "interface_switching_capability_descriptor": {
                                                "1": {
                                                    "switching_type": "Packet",
                                                    "encoding_type": "Packet",
                                                    "maximum_lsp_bw": {
                                                        0: {"bw": "0bps"},
                                                        1: {"bw": "0bps"},
                                                        2: {"bw": "0bps"},
                                                        3: {"bw": "0bps"},
                                                        4: {"bw": "0bps"},
                                                        5: {"bw": "0bps"},
                                                        6: {"bw": "0bps"},
                                                        7: {"bw": "0bps"},
                                                    },
                                                }
                                            },
                                            "p2p_adj_sid": {
                                                "sid": {
                                                    "12345": {
                                                        "address_family": "IPV4",
                                                        "flags": "0x24",
                                                        "weight": 0,
                                                    }
                                                }
                                            },
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "prefixes": {
                        "10.4.1.1/32": {
                            "flags": "0x60",
                            "prefix_sid": {1234: {"flags": "0x00", "algo": 0}},
                        }
                    },
                    "spring_capabilities": {
                        "srgb_block": {"start": 12000, "range": 3000, "flags": "0x00"}
                    },
                    "spring_algorithms": ["0", "1"],
                }
            },
        },
        "10.16.2.2-1": {
            "type": "Net",
            "age": 1024,
            "link_in": 0,
            "link_out": 2,
            "protocol": {
                "OSPF(0.0.0.4)": {
                    "to": {
                        "10.16.2.34": {
                            "local": {
                                "0.0.0.0": {
                                    "remote": {
                                        "0.0.0.0": {
                                            "local_interface_index": 0,
                                            "remote_interface_index": 0,
                                            "metric": 0,
                                            "interface_switching_capability_descriptor": {
                                                "1": {
                                                    "switching_type": "Packet",
                                                    "encoding_type": "Packet",
                                                    "maximum_lsp_bw": {
                                                        0: {"bw": "0bps"},
                                                        1: {"bw": "0bps"},
                                                        2: {"bw": "0bps"},
                                                        3: {"bw": "0bps"},
                                                        4: {"bw": "0bps"},
                                                        5: {"bw": "0bps"},
                                                        6: {"bw": "1000bps"},
                                                        7: {"bw": "0bps"},
                                                    },
                                                }
                                            },
                                        }
                                    }
                                }
                            }
                        },
                        "10.16.2.42": {
                            "local": {
                                "0.0.0.0": {
                                    "remote": {
                                        "0.0.0.0": {
                                            "local_interface_index": 0,
                                            "remote_interface_index": 0,
                                            "metric": 0,
                                            "interface_switching_capability_descriptor": {
                                                "1": {
                                                    "switching_type": "Packet",
                                                    "encoding_type": "Packet",
                                                    "maximum_lsp_bw": {
                                                        0: {"bw": "0bps"},
                                                        1: {"bw": "0bps"},
                                                        2: {"bw": "0bps"},
                                                        3: {"bw": "0bps"},
                                                        4: {"bw": "0bps"},
                                                        5: {"bw": "0bps"},
                                                        6: {"bw": "0bps"},
                                                        7: {"bw": "0bps"},
                                                    },
                                                }
                                            },
                                        }
                                    }
                                }
                            }
                        },
                    }
                }
            },
        },
        "172.16.1.4-1": {
            "type": "Net",
            "age": 2048,
            "link_in": 0,
            "link_out": 2,
            "protocol": {
                "OSPF(0.0.0.4)": {
                    "to": {
                        "172.16.85.48": {
                            "local": {
                                "0.0.0.0": {
                                    "remote": {
                                        "0.0.0.0": {
                                            "local_interface_index": 0,
                                            "remote_interface_index": 0,
                                            "metric": 0,
                                            "interface_switching_capability_descriptor": {
                                                "1": {
                                                    "switching_type": "Packet",
                                                    "encoding_type": "Packet",
                                                    "maximum_lsp_bw": {
                                                        0: {"bw": "0bps"},
                                                        1: {"bw": "0bps"},
                                                        2: {"bw": "0bps"},
                                                        3: {"bw": "0bps"},
                                                        4: {"bw": "0bps"},
                                                        5: {"bw": "0bps"},
                                                        6: {"bw": "0bps"},
                                                        7: {"bw": "0bps"},
                                                    },
                                                }
                                            },
                                        }
                                    }
                                }
                            }
                        },
                        "172.16.85.52": {
                            "local": {
                                "0.0.0.0": {
                                    "remote": {
                                        "0.0.0.0": {
                                            "local_interface_index": 0,
                                            "remote_interface_index": 0,
                                            "metric": 0,
                                            "interface_switching_capability_descriptor": {
                                                "1": {
                                                    "switching_type": "Packet",
                                                    "encoding_type": "Packet",
                                                    "maximum_lsp_bw": {
                                                        0: {"bw": "0bps"},
                                                        1: {"bw": "0bps"},
                                                        2: {"bw": "0bps"},
                                                        3: {"bw": "0bps"},
                                                        4: {"bw": "0bps"},
                                                        5: {"bw": "0bps"},
                                                        6: {"bw": "0bps"},
                                                        7: {"bw": "0bps"},
                                                    },
                                                }
                                            },
                                        }
                                    }
                                }
                            }
                        },
                    }
                }
            },
        },
        "10.36.3.3": {"type": "---", "age": 3440, "link_in": 1, "link_out": 0},
        "10.64.4.4": {"type": "---", "age": 2560, "link_in": 1, "link_out": 0},
    },
}
