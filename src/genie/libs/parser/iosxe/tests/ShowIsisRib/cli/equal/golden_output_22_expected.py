expected_output = {
    "tag": {
        "ipfrr": {
            "topo_type": "unicast",
            "topo_name": "base",
            "tid": 0,
            "topo_id": "0x0",
            "flex_algo": {
                "None": {
                    "prefix": {
                        "40.0.0.2": {
                            "subnet": "32",
                            "algo": {
                                0: {},
                                1: {},
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False,
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/8": {
                                    "level": {
                                        "L1": {
                                            "source_ip": {
                                                "40.0.0.2": {
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "100.5.0.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "installed": True,
                                                    "had_repair_path": False,
                                                    "lsp": {},
                                                    "path_attribute": {
                                                        "ALT": False,
                                                        "SRTE": False,
                                                        "SRTE_STRICT": False,
                                                        "SR_POLICY": False,
                                                        "SR_POLICY_STRICT": False,
                                                        "TE": False,
                                                        "ULOOP_EP": False,
                                                    },
                                                    "repair_path": {
                                                        "ip": "100.6.0.2",
                                                        "interface": "TenGigabitEthernet0/0/9",
                                                        "metric": 25,
                                                        "stale": False,
                                                        "attributes": {
                                                            "DS": True,
                                                            "LC": False,
                                                            "NP": False,
                                                            "PP": False,
                                                            "SR": False,
                                                        },
                                                        "lfa_type": "local LFA",
                                                        "repair_source": {
                                                            "host": "R2"
                                                        },
                                                    },
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                        },
                        "100.5.0.0": {
                            "subnet": "16",
                            "algo": {
                                0: {},
                                1: {},
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False,
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/8": {
                                    "level": {
                                        "L1": {
                                            "source_ip": {
                                                "40.0.0.2": {
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "100.5.0.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "lsp": {},
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                        },
                        "100.6.0.0": {
                            "subnet": "16",
                            "algo": {
                                0: {},
                                1: {},
                            },
                            "prefix_attr": {
                                "x_flag": False,
                                "r_flag": False,
                                "n_flag": False,
                            },
                            "via_interface": {
                                "TenGigabitEthernet0/0/8": {
                                    "level": {
                                        "L1": {
                                            "source_ip": {
                                                "40.0.0.2": {
                                                    "distance": 115,
                                                    "metric": 20,
                                                    "via_ip": "100.5.0.2",
                                                    "tag": "0",
                                                    "filtered_out": False,
                                                    "lsp": {},
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                        },
                    },
                }
            },
        }
    }
}