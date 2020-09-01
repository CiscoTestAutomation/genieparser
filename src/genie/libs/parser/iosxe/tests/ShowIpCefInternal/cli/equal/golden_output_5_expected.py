expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "0.0.0.0/0": {
                            "epoch": 2,
                            "flags": ["DefRtHndlr", "defrt"],
                            "output_chain": {},
                            "path_list": {
                                "7FEE80648560": {
                                    "flags": "0x41 [shble, hwcn]",
                                    "locks": 4,
                                    "path": {
                                        "7FEE80648DB0": {
                                            "for": "IPv4",
                                            "share": "1/1",
                                            "type": "special prefix",
                                        }
                                    },
                                    "sharing": "per-destination",
                                }
                            },
                            "refcnt": 5,
                            "sharing": "per-destination",
                            "sources": ["DRH"],
                        },
                        "0.0.0.0/32": {
                            "epoch": 2,
                            "feature_space": {"broker": {"distribution_priority": 4}},
                            "flags": ["rcv"],
                            "output_chain": {},
                            "path_list": {
                                "7FEE54E13390": {
                                    "flags": "0x41 [shble, hwcn]",
                                    "locks": 11,
                                    "path": {
                                        "7FEE54E13708": {
                                            "for": "IPv4",
                                            "share": "1/1",
                                            "type": "receive",
                                        }
                                    },
                                    "sharing": "per-destination",
                                }
                            },
                            "refcnt": 6,
                            "sharing": "per-destination",
                            "sources": ["Spc"],
                        },
                        "0.0.0.0/8": {
                            "epoch": 2,
                            "feature_space": {"broker": {"distribution_priority": 4}},
                            "output_chain": {},
                            "path_list": {
                                "7FEE54E132F0": {
                                    "flags": "0x41 [shble, hwcn]",
                                    "locks": 11,
                                    "path": {
                                        "7FEE54E13638": {
                                            "for": "IPv4",
                                            "share": "1/1",
                                            "type": "special prefix",
                                        }
                                    },
                                    "sharing": "per-destination",
                                }
                            },
                            "refcnt": 6,
                            "sharing": "per-destination",
                            "sources": ["Spc"],
                        },
                        "10.4.1.1/32": {
                            "epoch": 2,
                            "feature_space": {
                                "broker": {"distribution_priority": 2},
                                "iprm": "0x0003800C",
                            },
                            "flags": ["att", "cnn", "rcv", "local", "SrcElgbl"],
                            "output_chain": {},
                            "path_list": {
                                "7FEE5AF88090": {
                                    "flags": "0x41 [shble, hwcn]",
                                    "locks": 3,
                                    "path": {
                                        "7FEE5AF88B40": {
                                            "for": "IPv4",
                                            "share": "1/1",
                                            "type": "receive",
                                        }
                                    },
                                    "sharing": "per-destination",
                                }
                            },
                            "refcnt": 6,
                            "rib": "[C]",
                            "sharing": "per-destination",
                        },
                        "10.12.90.0/24": {
                            "epoch": 2,
                            "feature_space": {
                                "broker": {"distribution_priority": 2},
                                "iprm": "0x0003800C",
                            },
                            "flags": ["att", "cnn", "cover", "deagg"],
                            "output_chain": {},
                            "path_list": {
                                "7FEE874A8868": {
                                    "flags": "0x49 [shble, rif, hwcn]",
                                    "locks": 3,
                                    "path": {
                                        "7FEE5B901428": {
                                            "for": "IPv4",
                                            "share": "1/1",
                                            "type": "connected prefix",
                                        }
                                    },
                                    "sharing": "per-destination",
                                }
                            },
                            "refcnt": 6,
                            "rib": "[C]",
                            "sharing": "per-destination",
                            "sources": ["RIB"],
                        },
                        "10.36.3.3/32": {
                            "epoch": 2,
                            "feature_space": {
                                "broker": {"distribution_priority": 4},
                                "iprm": "0x00028000",
                                "local_label_info": {"dflt": "global/16 [0x3]"},
                                "path_extension_list": {
                                    "dflt": {
                                        "disposition_chain": {"0x7FEE86F48B90": {}}
                                    }
                                },
                            },
                            "output_chain": {},
                            "path_list": {
                                "7FEE5AC45458": {
                                    "flags": "0x49 [shble, rif, hwcn]",
                                    "locks": 5,
                                    "path": {
                                        "7FEE7ECE0A78": {
                                            "for": "IPv4",
                                            "nexthop": {
                                                "10.13.90.3": {
                                                    "outgoing_interface": {
                                                        "GigabitEthernet3.90": {}
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
                            "refcnt": 6,
                            "rib": "[I]",
                            "sharing": "per-destination",
                            "sources": ["RIB,", "LTE"],
                        },
                    }
                }
            }
        }
    }
}
