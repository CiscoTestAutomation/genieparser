expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "10.19.198.239/32": {
                            "epoch": 2,
                            "feature_space": {
                                "broker": {"distribution_priority": 1},
                                "iprm": "0x00028000",
                                "lfd": {"10.19.198.239/32": {"local_labels": 2}},
                                "local_label_info": {
                                    "dflt": "global/28 [0x3]",
                                    "sr": "global/16073 [0x1B]",
                                },
                                "path_extension_list": {
                                    "dflt": {
                                        "disposition_chain": {
                                            "0x7F0FF19606C0": {
                                                "frr": {
                                                    "primary": {
                                                        "primary": {
                                                            "tag_adj": {
                                                                "GigabitEthernet0/1/6": {
                                                                    "addr": "10.169.196.213"
                                                                }
                                                            }
                                                        }
                                                    }
                                                },
                                                "label": 51885,
                                            }
                                        },
                                        "label_switch_chain": {
                                            "0x7F0FF19606C0": {
                                                "frr": {
                                                    "primary": {
                                                        "primary": {
                                                            "tag_adj": {
                                                                "GigabitEthernet0/1/6": {
                                                                    "addr": "10.169.196.213"
                                                                }
                                                            }
                                                        }
                                                    }
                                                },
                                                "label": 51885,
                                            }
                                        },
                                    },
                                    "sr": {
                                        "disposition_chain": {
                                            "0x7F0FF1960590": {
                                                "frr": {
                                                    "primary": {
                                                        "primary": {
                                                            "tag_adj": {
                                                                "GigabitEthernet0/1/6": {
                                                                    "addr": "10.169.196.213"
                                                                }
                                                            }
                                                        }
                                                    }
                                                },
                                                "label": 16073,
                                            }
                                        },
                                        "label_switch_chain": {
                                            "0x7F0FF1960590": {
                                                "frr": {
                                                    "primary": {
                                                        "primary": {
                                                            "tag_adj": {
                                                                "GigabitEthernet0/1/6": {
                                                                    "addr": "10.169.196.213"
                                                                }
                                                            }
                                                        }
                                                    }
                                                },
                                                "label": 16073,
                                            }
                                        },
                                    },
                                },
                            },
                            "ifnums": {
                                "GigabitEthernet0/1/6": {
                                    "address": "10.169.196.213",
                                    "ifnum": 15,
                                },
                                "MPLS-SR-Tunnel1": {"ifnum": 29},
                            },
                            "output_chain": {
                                "frr": {
                                    "primary": {
                                        "info": "0x80007F0FF094DD88",
                                        "primary": {
                                            "tag_adj": {
                                                "GigabitEthernet0/1/6": {
                                                    "addr": "10.169.196.213",
                                                    "addr_info": "7F0FF08D46D0",
                                                }
                                            }
                                        },
                                        "repair": {
                                            "tag_midchain": {
                                                "MPLS-SR-Tunnel1": {
                                                    "label": ["98"],
                                                    "tag_adj": {
                                                        "GigabitEthernet0/1/7": {
                                                            "addr": "10.169.196.217",
                                                            "addr_info": "7F0FF0AFB2F8",
                                                        }
                                                    },
                                                    "tag_midchain_info": "7F0FF0AFAC68",
                                                }
                                            }
                                        },
                                    }
                                },
                                "label": ["[51885|16073]-(local:28)"],
                            },
                            "path_list": {
                                "7F0FEC884768": {
                                    "flags": "0x4D [shble, hvsh, rif, hwcn]",
                                    "locks": 19,
                                    "path": {
                                        "7F0FF11E0AE0": {
                                            "flags": "[has-rpr]",
                                            "for": "IPv4",
                                            "nexthop": {
                                                "10.169.196.213": {
                                                    "outgoing_interface": {
                                                        "GigabitEthernet0/1/6": {
                                                            "ip_adj": {
                                                                "GigabitEthernet0/1/6": {
                                                                    "addr": "10.169.196.213",
                                                                    "addr_info": "7F0FF08D4900",
                                                                }
                                                            },
                                                            "local_label": 28,
                                                            "outgoing_label": ["51885"],
                                                            "outgoing_label_backup": "16073",
                                                        }
                                                    }
                                                }
                                            },
                                            "share": "1/1",
                                            "type": "attached nexthop",
                                        }
                                    },
                                    "sharing": "per-destination",
                                }
                            },
                            "refcnt": 7,
                            "rib": "[I]",
                            "sharing": "per-destination",
                            "sources": ["RIB,", "RR,", "LTE"],
                            "subblocks": {
                                1: {
                                    "non_eos_chain_loadinfo": "7F0FF16E6F38",
                                    "per-session": True,
                                    "flags": "0111",
                                    "locks": 8,
                                    "rr_source": [
                                        "non-eos indirection",
                                        "heavily shared",
                                    ],
                                }
                            },
                        }
                    }
                }
            }
        }
    }
}
