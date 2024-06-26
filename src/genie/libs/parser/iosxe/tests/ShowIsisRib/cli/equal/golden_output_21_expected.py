expected_output = {
    "tag": {
        "64512": {
            "topo_type": "unicast",
            "topo_name": "base",
            "tid": 0,
            "topo_id": "0x0",
            "flex_algo": {
                "None": {
                    "prefix": {
                        "10.1.2.0": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 110,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": False,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 120,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                },
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 120,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 120,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.2.4": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": False,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 30,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                },
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.2.8": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 110,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": False,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 120,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                },
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 120,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 120,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.2.12": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": False,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 30,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                },
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.3.0": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 110,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 110,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R3"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.3": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 110,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.2.5.21",
                                                        "interface": "TenGigabitEthernet0/0/0",
                                                        "metric": 110,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R2"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.3.4": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 20,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R3"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.3": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.2.5.21",
                                                        "interface": "TenGigabitEthernet0/0/0",
                                                        "metric": 20,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R2"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.3.8": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 110,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 110,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R3"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.3": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 110,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.2.5.21",
                                                        "interface": "TenGigabitEthernet0/0/0",
                                                        "metric": 110,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R2"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.3.12": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 20,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R3"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.3": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.2.5.21",
                                                        "interface": "TenGigabitEthernet0/0/0",
                                                        "metric": 20,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R2"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.4.0": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.3": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 110,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": False,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "10.2.5.21",
                                                        "interface": "TenGigabitEthernet0/0/0",
                                                        "metric": 120,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                },
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 120,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 120,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.4.4": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.3": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": False,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "10.2.5.21",
                                                        "interface": "TenGigabitEthernet0/0/0",
                                                        "metric": 30,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                },
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.4.8": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.3": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 110,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": False,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "10.2.5.21",
                                                        "interface": "TenGigabitEthernet0/0/0",
                                                        "metric": 120,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                },
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 120,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 120,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.4.12": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.3": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": False,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "10.2.5.21",
                                                        "interface": "TenGigabitEthernet0/0/0",
                                                        "metric": 30,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                },
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.5.0": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 120,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 120,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                },
                                                "192.0.2.52": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 130,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 120,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.2.5.21",
                                                        "interface": "TenGigabitEthernet0/0/0",
                                                        "metric": 120,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                },
                                                "192.0.2.52": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 130,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.5.4": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 30,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                },
                                                "192.0.2.52": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 40,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.2.5.21",
                                                        "interface": "TenGigabitEthernet0/0/0",
                                                        "metric": 30,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                },
                                                "192.0.2.52": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 40,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.5.8": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 110,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": False,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 120,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R2"
                                                        }
                                                    }
                                                },
                                                "192.0.2.51": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 120,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.5.12": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": False,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 30,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R2"
                                                        }
                                                    }
                                                },
                                                "192.0.2.51": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.5.16": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.3": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 110,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.1.5.20": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.3": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.2.5.0": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 110,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": False,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 120,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R2"
                                                        }
                                                    }
                                                },
                                                "192.0.2.52": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 130,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.52": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 130,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.2.5.4": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": False,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 30,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R2"
                                                        }
                                                    }
                                                },
                                                "192.0.2.52": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 40,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.52": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 40,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.2.5.8": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 120,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 120,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                },
                                                "192.0.2.51": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 120,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 120,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.2.5.21",
                                                        "interface": "TenGigabitEthernet0/0/0",
                                                        "metric": 120,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R4"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.2.5.12": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 30,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                },
                                                "192.0.2.51": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.2.5.21",
                                                        "interface": "TenGigabitEthernet0/0/0",
                                                        "metric": 30,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R4"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.2.5.16": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 110,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.2.5.20": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False
                            },
                            "subnet": "30",
                            "algo": {
                                0: {},
                                1: {}
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": False
                                                    },
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "192.0.2.1": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "subnet": "32",
                            "source_router_id": "192.0.2.1",
                            "algo": {
                                0: {
                                    "sid_index": 10,
                                    "bound": True
                                },
                                1: {
                                    "sid_index": 11,
                                    "bound": True
                                }
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.1": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 10,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "source_router_id": "192.0.2.1",
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 10,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "implicit-null"
                                                        },
                                                        1: {
                                                            "sid_index": 11,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "implicit-null"
                                                        }
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": False,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 20,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "algo": {
                                                            0: {
                                                                "label": "16010"
                                                            }
                                                        },
                                                        "repair_source": {
                                                            "host": "R2"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "192.0.2.2": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "subnet": "32",
                            "source_router_id": "192.0.2.2",
                            "algo": {
                                0: {
                                    "sid_index": 20,
                                    "bound": True
                                },
                                1: {
                                    "sid_index": 21,
                                    "bound": True
                                }
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "source_router_id": "192.0.2.2",
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 20,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "16020"
                                                        },
                                                        1: {
                                                            "sid_index": 21,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "16021"
                                                        }
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 20,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "algo": {
                                                            0: {
                                                                "label": "16020"
                                                            }
                                                        },
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.2": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "source_router_id": "192.0.2.2",
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 20,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "16020"
                                                        },
                                                        1: {
                                                            "sid_index": 21,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "16021"
                                                        }
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.2.5.21",
                                                        "interface": "TenGigabitEthernet0/0/0",
                                                        "metric": 20,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "algo": {
                                                            0: {
                                                                "label": "16020"
                                                            }
                                                        },
                                                        "repair_source": {
                                                            "host": "R1"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "192.0.2.3": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "subnet": "32",
                            "source_router_id": "192.0.2.3",
                            "algo": {
                                0: {
                                    "sid_index": 30,
                                    "bound": True
                                },
                                1: {
                                    "sid_index": 31,
                                    "bound": True
                                }
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.3": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 10,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "source_router_id": "192.0.2.3",
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 30,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "implicit-null"
                                                        },
                                                        1: {
                                                            "sid_index": 31,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "implicit-null"
                                                        }
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": False,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "10.2.5.21",
                                                        "interface": "TenGigabitEthernet0/0/0",
                                                        "metric": 20,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "algo": {
                                                            0: {
                                                                "label": "16030"
                                                            }
                                                        },
                                                        "repair_source": {
                                                            "host": "R3"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "192.0.2.51": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "subnet": "32",
                            "source_router_id": "192.0.2.51",
                            "algo": {
                                0: {
                                    "sid_index": 880,
                                    "bound": True
                                },
                                1: {
                                    "sid_index": 881,
                                    "bound": True
                                }
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.51": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "source_router_id": "192.0.2.51",
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 880,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "16880"
                                                        },
                                                        1: {
                                                            "sid_index": 881,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "16881"
                                                        }
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": False,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 40,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "algo": {
                                                            0: {
                                                                "label": "16880"
                                                            }
                                                        },
                                                        "repair_source": {
                                                            "host": "R4"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "192.0.2.52": {
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": True
                            },
                            "subnet": "32",
                            "source_router_id": "192.0.2.52",
                            "algo": {
                                0: {
                                    "sid_index": 770,
                                    "bound": True
                                },
                                1: {
                                    "sid_index": 771,
                                    "bound": True
                                }
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/0": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.52": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.2.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "source_router_id": "192.0.2.52",
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 770,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "16770"
                                                        },
                                                        1: {
                                                            "sid_index": 771,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "16771"
                                                        }
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.1.5.21",
                                                        "interface": "TenGigabitEthernet0/0/1",
                                                        "metric": 30,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "algo": {
                                                            0: {
                                                                "label": "16770"
                                                            }
                                                        },
                                                        "repair_source": {
                                                            "host": "R5"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "TenGigabitEthernet0/0/1": {
                                    "level": {
                                        "L2": {
                                            "source_ip": {
                                                "192.0.2.52": {
                                                    "lsp": {},
                                                    "distance": 115,
                                                    "metric": 30,
                                                    "via_ip": "10.1.5.21",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "prefix_attr": {
                                                        "x_flag": False,
                                                        "r_flag": False,
                                                        "n_flag": True
                                                    },
                                                    "source_router_id": "192.0.2.52",
                                                    "srgb_start": 16000,
                                                    "srgb_range": 8000,
                                                    "algo": {
                                                        0: {
                                                            "sid_index": 770,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "16770"
                                                        },
                                                        1: {
                                                            "sid_index": 771,
                                                            "flags": {
                                                                "r_flag": False,
                                                                "n_flag": True,
                                                                "p_flag": False,
                                                                "e_flag": False,
                                                                "v_flag": False,
                                                                "l_flag": False
                                                            },
                                                            "label": "16771"
                                                        }
                                                    },
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "ULOOP_EP": False,
                                                        "TE": False
                                                    },
                                                    "had_repair_path": False,
                                                    "installed": True,
                                                    "repair_path": {
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": True,
                                                            "PP": True,
                                                            "SR": True
                                                        },
                                                        "ip": "10.2.5.21",
                                                        "interface": "TenGigabitEthernet0/0/0",
                                                        "metric": 30,
                                                        "stale": False,
                                                        "lfa_type": "local LFA",
                                                        "algo": {
                                                            0: {
                                                                "label": "16770"
                                                            }
                                                        },
                                                        "repair_source": {
                                                            "host": "R5"
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
        }
    }
}

