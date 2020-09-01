expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "10.100.5.5/32": {
                            "epoch": 3,
                            "feature_space": {
                                "broker": {"distribution_priority": 4},
                                "iprm": "0x00028000",
                                "lfd": {"10.100.5.5/32": {"local_labels": 2}},
                                "local_label_info": {
                                    "dflt": "global/25 [0x23]",
                                    "sr": "global/17000 [0x1B]",
                                },
                                "path_extension_list": {
                                    "dflt": {
                                        "disposition_chain": {
                                            "0x7F2B22651570": {
                                                "frr": {
                                                    "primary": {
                                                        "primary": {
                                                            "tag_adj": {
                                                                "GigabitEthernet0/1/6": {
                                                                    "addr": "10.19.198.25"
                                                                }
                                                            }
                                                        }
                                                    }
                                                },
                                                "label": 63300,
                                            }
                                        },
                                        "label_switch_chain": {
                                            "0x7F2B22651570": {
                                                "frr": {
                                                    "primary": {
                                                        "primary": {
                                                            "tag_adj": {
                                                                "GigabitEthernet0/1/6": {
                                                                    "addr": "10.19.198.25"
                                                                }
                                                            }
                                                        }
                                                    }
                                                },
                                                "label": 63300,
                                            }
                                        },
                                    },
                                    "sr": {
                                        "disposition_chain": {
                                            "0x7F2B22651440": {
                                                "frr": {
                                                    "primary": {
                                                        "primary": {
                                                            "tag_adj": {
                                                                "GigabitEthernet0/1/6": {
                                                                    "addr": "10.19.198.25"
                                                                }
                                                            }
                                                        }
                                                    }
                                                },
                                                "label": 17000,
                                            }
                                        },
                                        "label_switch_chain": {
                                            "0x7F2B22651440": {
                                                "frr": {
                                                    "primary": {
                                                        "primary": {
                                                            "tag_adj": {
                                                                "GigabitEthernet0/1/6": {
                                                                    "addr": "10.19.198.25"
                                                                }
                                                            }
                                                        }
                                                    }
                                                },
                                                "label": 17000,
                                            }
                                        },
                                    },
                                },
                            },
                            "ifnums": {
                                "GigabitEthernet0/1/6": {
                                    "address": "10.19.198.25",
                                    "ifnum": 15,
                                },
                                "GigabitEthernet0/1/7": {
                                    "address": "10.19.198.29",
                                    "ifnum": 16,
                                },
                            },
                            "output_chain": {
                                "frr": {
                                    "primary": {
                                        "info": "0x80007F2B146ED518",
                                        "primary": {
                                            "tag_adj": {
                                                "GigabitEthernet0/1/6": {
                                                    "addr": "10.19.198.25",
                                                    "addr_info": "7F2B21B245A8",
                                                }
                                            }
                                        },
                                        "repair": {
                                            "tag_adj": {
                                                "GigabitEthernet0/1/7": {
                                                    "addr": "10.19.198.29",
                                                    "addr_info": "7F2B21B24148",
                                                }
                                            }
                                        },
                                    }
                                },
                                "label": ["[63300|68544](elc)-(local:25)"],
                            },
                            "path_list": {
                                "7F2B22A8B0A0": {
                                    "flags": "0x4D [shble, hvsh, rif, hwcn]",
                                    "locks": 477,
                                    "path": {
                                        "7F2B22A6C220": {
                                            "flags": "[has-rpr]",
                                            "for": "IPv4",
                                            "nexthop": {
                                                "10.19.198.25": {
                                                    "outgoing_interface": {
                                                        "GigabitEthernet0/1/6": {
                                                            "ip_adj": {
                                                                "GigabitEthernet0/1/6": {
                                                                    "addr": "10.19.198.25",
                                                                    "addr_info": "7F2B21B247D8",
                                                                }
                                                            },
                                                            "local_label": 25,
                                                            "outgoing_label": ["63300"],
                                                            "outgoing_label_backup": "68544",
                                                            "outgoing_label_info": "elc",
                                                        }
                                                    }
                                                }
                                            },
                                            "share": "1/1",
                                            "type": "attached nexthop",
                                        },
                                        "7F2B22A6C3C0": {
                                            "flags": "[rpr,",
                                            "for": "IPv4",
                                            "nexthop": {
                                                "10.19.198.29": {
                                                    "outgoing_interface": {
                                                        "GigabitEthernet0/1/7": {
                                                            "local_label": 17000,
                                                            "outgoing_label": ["17000"],
                                                        }
                                                    }
                                                }
                                            },
                                            "share": "1/1",
                                            "type": "attached nexthop",
                                        },
                                    },
                                    "sharing": "per-destination",
                                }
                            },
                            "refcnt": 6,
                            "rib": "[I]",
                            "sharing": "per-destination",
                            "sources": ["RIB,", "LTE"],
                        }
                    }
                }
            }
        }
    }
}
