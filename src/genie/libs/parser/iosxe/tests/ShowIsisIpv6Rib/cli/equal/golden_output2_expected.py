expected_output = {
    "tag": {
        "1": {
            "rib_root": "local RIB",
            "flex_algo": {
                "None": {
                    "prefix": {
                        "FCCC:CCC1:AA33::/48": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "local_router": True,
                            "via": {
                                "FE80::A8BB:CCFF:FE00:6500": {
                                    "type": {
                                        "L2": {
                                            "metric": 20,
                                            "tag": "0",
                                            "interface": "Ethernet0/0",
                                            "filtered_out": True,
                                            "repair_path": {
                                                "attributes": {
                                                    "DS": True,
                                                    "LC": True,
                                                    "NP": True,
                                                    "PP": False,
                                                    "SR": True
                                                },
                                                "nh_addr": "FE80::A8BB:CCFF:FE00:6902",
                                                "interface": "Ethernet2/0",
                                                "metric": 110,
                                                "lfa_type": "TI-LFA link-protecting",
                                                "srv6_fwid": 25165856,
                                                "nodes": {
                                                    "R7": {
                                                        "pq_node": "Q",
                                                        "sid": "FCCC:CCC1:AA66:E000::"
                                                    }
                                                },
                                                "repair_source": "R3",
                                                "metric_to_prefix": 130
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "100:100::/64": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "local_router": True,
                            "via": {
                                "FE80::A8BB:CCFF:FE02:5E20": {
                                    "type": {
                                        "L2": {
                                            "metric": 20,
                                            "tag": "0",
                                            "interface": "Ethernet0/2",
                                            "filtered_out": False,
                                            "installed": True,
                                            "repair_path": {
                                                "attributes": {
                                                    "DS": True,
                                                    "LC": False,
                                                    "NP": False,
                                                    "PP": False,
                                                    "SR": True
                                                },
                                                "nh_addr": "FE80::A8BB:CCFF:FE02:5A10",
                                                "interface": "Ethernet0/1.139",
                                                "metric": 130,
                                                "lfa_type": "TI-LFA link-protecting",
                                                "srv6_fwid": 25165861,
                                                "nodes": {
                                                    "r604": {
                                                        "pq_node": "P",
                                                        "sid": "CAFE:0:604::"
                                                    },
                                                    "r605": {
                                                        "pq_node": "Q",
                                                        "sid": "CAFE:0:604:E002::"
                                                    }
                                                },
                                                "repair_source": "r606",
                                                "metric_to_prefix": 150
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "666::666/128": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "local_router": True,
                            "source_router_id": "666::666",
                            "via_uloop": {
                                "srv6_fwid": {
                                    "25165865": {
                                        "type": "L1",
                                        "metric": 65,
                                        "tag": "0",
                                        "nodes": {
                                            "R4": {
                                                "pq_node": "P",
                                                "sid": "FCCC:CCC1:D1::"
                                            }
                                        },
                                        "installed": True,
                                        "alt": True
                                    }
                                }
                            },
                            "via": {
                                "FE80::A8BB:CCFF:FE00:9C10": {
                                    "type": {
                                        "L1": {
                                            "metric": 65,
                                            "tag": "0",
                                            "interface": "Ethernet0/1",
                                            "filtered_out": False,
                                        }
                                    }
                                }
                            }
                        },
                        "FCCC:CCC1:AA77::/48": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "local_router": True,
                            "via_uloop": {
                                "srv6_fwid": {
                                    "25165858": {
                                        "type": "L2",
                                        "metric": 110,
                                        "tag": "0",
                                        "nodes": {
                                            "R6": {
                                                "pq_node": "P",
                                                "sid": "FCCC:CCC1:AA66::"
                                            },
                                            "R7": {
                                                "pq_node": "Q",
                                                "sid": "FCCC:CCC1:AA66:E000::"
                                            }
                                        },
                                        "alt": True
                                    }
                                }
                            },
                            "via": {
                                "FE80::A8BB:CCFF:FE00:6902": {
                                    "type": {
                                        "L2": {
                                            "metric": 110,
                                            "tag": "0",
                                            "interface": "Ethernet2/0",
                                            "filtered_out": False,
                                        }
                                    }
                                }
                            }
                        },
                        "2001:DB8:88:1::/64": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "via": {
                                "FE80::210:7BFF:FEC2:ACC9": {
                                    "type": {
                                        "L2": {
                                            "metric": 20,
                                            "interface": "GigabitEthernet2/0/0",
                                            "filtered_out": False,
                                            "lsp": {
                                                "rtp_lsp_index": "3",
                                                "rtp_lsp_version": "7"
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "111:111::/64": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "local_router": True,
                            "via": {
                                "::": {
                                    "type": {
                                        "Sum": {
                                            "metric": 30,
                                            "tag": "0",
                                            "interface": "Null0",
                                            "filtered_out": False,
                                        }
                                    }
                                }
                            }
                        },
                        "2001:DB8:45A::/64": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "local_router": True,
                            "via": {
                                "FE80::210:7BFF:FEC2:ACC9": {
                                    "type": {
                                        "L1": {
                                            "metric": 20,
                                            "interface": "GigabitEthernet2/0/0",
                                            "filtered_out": False,
                                            "lsp": {
                                                "rtp_lsp_index": "C",
                                                "rtp_lsp_version": "6"
                                            }
                                        },
                                        "L2": {
                                            "metric": 20,
                                            "interface": "GigabitEthernet2/0/0",
                                            "filtered_out": False,
                                            "lsp": {
                                                "rtp_lsp_index": "3",
                                                "rtp_lsp_version": "7"
                                            }
                                        }
                                    }
                                },
                                "FE80::210:7BFF:FEC2:ACCC": {
                                    "type": {
                                        "L1": {
                                            "metric": 20,
                                            "interface": "GigabitEthernet2/1/0",
                                            "filtered_out": False,
                                            "lsp": {
                                                "rtp_lsp_index": "C",
                                                "rtp_lsp_version": "6"
                                            }
                                        },
                                        "L2": {
                                            "metric": 20,
                                            "interface": "GigabitEthernet2/1/0",
                                            "filtered_out": False,
                                            "lsp": {
                                                "rtp_lsp_index": "3",
                                                "rtp_lsp_version": "7"
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
    }
}
