expected_output = {
    "tag": {
        "1": {
            "tid": 0,
            "flex_algo": {
                "None": {
                    "prefix": {
                        "2.2.3.0": {
                            "prefix_attr": {
                                "r_flag": False,
                                "x_flag": False,
                                "n_flag": False
                            },
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "GigabitEthernet0/0/2": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "2.2.2.2": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 7,
                                                        "rtp_lsp_index": 7,
                                                        "rtp_lsp_version": 2056
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": False,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 16777224,
                                                    "via_ip": "12.12.1.2",
                                                    "filtered_out": False,
                                                },
                                                "6.6.6.6": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 7,
                                                        "rtp_lsp_index": 23,
                                                        "rtp_lsp_version": 2058
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": True,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 50331652,
                                                    "via_ip": "12.12.1.2"
                                                }
                                            }
                                        },
                                        "L1": {
                                            "source_ip": {
                                                "2.2.2.2": {
                                                    "path_attribute": {
                                                        "SRTE_STRICT": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SR_POLICY": False,
                                                        "ULOOP_EP": False,
                                                        "ALT": False,
                                                        "TE": False,
                                                        "SRTE": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "metric": 16777224,
                                                    "installed": True,
                                                    "tag": "0",
                                                    "had_repair_path": False,
                                                    "filtered_out": False,
                                                    "lsp": {
                                                        "next_hop_lsp_index": 2,
                                                        "rtp_lsp_index": 2,
                                                        "rtp_lsp_version": 2060
                                                    },
                                                    "distance": 115,
                                                    "prefix_attr": {
                                                        "r_flag": False,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "via_ip": "12.12.1.2",
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "GigabitEthernet0/0/3": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "2.2.2.2": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 7,
                                                        "rtp_lsp_index": 7,
                                                        "rtp_lsp_version": 2056
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": False,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 16777224,
                                                    "via_ip": "12.12.12.2"
                                                },
                                                "6.6.6.6": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 7,
                                                        "rtp_lsp_index": 23,
                                                        "rtp_lsp_version": 2058
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": True,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 50331652,
                                                    "via_ip": "12.12.12.2"
                                                }
                                            }
                                        },
                                        "L1": {
                                            "source_ip": {
                                                "2.2.2.2": {
                                                    "path_attribute": {
                                                        "SRTE_STRICT": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SR_POLICY": False,
                                                        "ULOOP_EP": False,
                                                        "ALT": False,
                                                        "TE": False,
                                                        "SRTE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "filtered_out": False,
                                                    "srgb_start": 16000,
                                                    "metric": 16777224,
                                                    "installed": True,
                                                    "tag": "0",
                                                    "lsp": {
                                                        "next_hop_lsp_index": 2,
                                                        "rtp_lsp_index": 2,
                                                        "rtp_lsp_version": 2060
                                                    },
                                                    "distance": 115,
                                                    "prefix_attr": {
                                                        "r_flag": False,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "via_ip": "12.12.12.2",
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/5": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "3.3.3.3": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 37,
                                                        "rtp_lsp_index": 41,
                                                        "rtp_lsp_version": 2046
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": True,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 16777234,
                                                    "via_ip": "13.13.1.2"
                                                },
                                                "5.5.5.5": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 37,
                                                        "rtp_lsp_index": 14,
                                                        "rtp_lsp_version": 2058
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": True,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 50331662,
                                                    "via_ip": "13.13.1.2"
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            "subnet": "24"
                        },
                        "1.1.1.0": {
                            "prefix_attr": {
                                "r_flag": True,
                                "x_flag": False,
                                "n_flag": False
                            },
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/5": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "3.3.3.3": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 37,
                                                        "rtp_lsp_index": 41,
                                                        "rtp_lsp_version": 2046
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": True,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 33554438,
                                                    "via_ip": "13.13.1.2"
                                                },
                                                "5.5.5.5": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 37,
                                                        "rtp_lsp_index": 13,
                                                        "rtp_lsp_version": 2055
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": True,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 67108866,
                                                    "via_ip": "13.13.1.2"
                                                }
                                            }
                                        }
                                    }
                                },
                                "GigabitEthernet0/0/2": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "6.6.6.6": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 7,
                                                        "rtp_lsp_index": 30,
                                                        "rtp_lsp_version": 2034
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": True,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 67108866,
                                                    "via_ip": "12.12.1.2"
                                                }
                                            }
                                        }
                                    }
                                },
                                "GigabitEthernet0/0/3": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "2.2.2.2": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 7,
                                                        "rtp_lsp_index": 7,
                                                        "rtp_lsp_version": 2056
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": True,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 33554438,
                                                    "via_ip": "12.12.12.2"
                                                },
                                                "6.6.6.6": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 7,
                                                        "rtp_lsp_index": 30,
                                                        "rtp_lsp_version": 2034
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": True,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 67108866,
                                                    "via_ip": "12.12.12.2"
                                                }
                                            }
                                        }
                                    }
                                },
                                "Tunnel65537": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "6.6.6.6": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 221,
                                                        "rtp_lsp_index": 221,
                                                        "rtp_lsp_version": 99
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": True,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 50,
                                                    "via_ip": "6.6.6.6"
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            "subnet": "24"
                        },
                        "2.2.2.0": {
                            "prefix_attr": {
                                "r_flag": False,
                                "x_flag": False,
                                "n_flag": False
                            },
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "GigabitEthernet0/0/2": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "2.2.2.2": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 7,
                                                        "rtp_lsp_index": 7,
                                                        "rtp_lsp_version": 2056
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": False,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 16777224,
                                                    "via_ip": "12.12.1.2"
                                                },
                                                "6.6.6.6": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 7,
                                                        "rtp_lsp_index": 22,
                                                        "rtp_lsp_version": 2059
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": True,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 50331652,
                                                    "via_ip": "12.12.1.2"
                                                }
                                            }
                                        },
                                        "L1": {
                                            "source_ip": {
                                                "2.2.2.2": {
                                                    "path_attribute": {
                                                        "SRTE_STRICT": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SR_POLICY": False,
                                                        "ULOOP_EP": False,
                                                        "ALT": False,
                                                        "TE": False,
                                                        "SRTE": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "metric": 16777224,
                                                    "installed": True,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "had_repair_path": False,
                                                    "lsp": {
                                                        "next_hop_lsp_index": 2,
                                                        "rtp_lsp_index": 2,
                                                        "rtp_lsp_version": 2060
                                                    },
                                                    "distance": 115,
                                                    "prefix_attr": {
                                                        "r_flag": False,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "via_ip": "12.12.1.2",
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "GigabitEthernet0/0/3": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "2.2.2.2": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 7,
                                                        "rtp_lsp_index": 7,
                                                        "rtp_lsp_version": 2056
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": False,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 16777224,
                                                    "via_ip": "12.12.12.2"
                                                },
                                                "6.6.6.6": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 7,
                                                        "rtp_lsp_index": 22,
                                                        "rtp_lsp_version": 2059
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": True,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 50331652,
                                                    "via_ip": "12.12.12.2"
                                                }
                                            }
                                        },
                                        "L1": {
                                            "source_ip": {
                                                "2.2.2.2": {
                                                    "path_attribute": {
                                                        "SRTE_STRICT": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SR_POLICY": False,
                                                        "ULOOP_EP": False,
                                                        "ALT": False,
                                                        "TE": False,
                                                        "SRTE": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "metric": 16777224,
                                                    "installed": True,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "had_repair_path": False,
                                                    "lsp": {
                                                        "next_hop_lsp_index": 2,
                                                        "rtp_lsp_index": 2,
                                                        "rtp_lsp_version": 2060
                                                    },
                                                    "distance": 115,
                                                    "prefix_attr": {
                                                        "r_flag": False,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "via_ip": "12.12.12.2",
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/5": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "3.3.3.3": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 37,
                                                        "rtp_lsp_index": 41,
                                                        "rtp_lsp_version": 2046
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": True,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 16777234,
                                                    "via_ip": "13.13.1.2"
                                                },
                                                "5.5.5.5": {
                                                    "distance": 115,
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "lsp": {
                                                        "next_hop_lsp_index": 37,
                                                        "rtp_lsp_index": 14,
                                                        "rtp_lsp_version": 2058
                                                    },
                                                    "srgb_start": 16000,
                                                    "prefix_attr": {
                                                        "r_flag": True,
                                                        "x_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "metric": 50331662,
                                                    "via_ip": "13.13.1.2"
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            "subnet": "24"
                        }
                    }
                }
            },
            "topo_type": "unicast",
            "topo_id": "0x0",
            "topo_name": "base"
        }
    }
}