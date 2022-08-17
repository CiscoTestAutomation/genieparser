expected_output = {
    "vrf": {
        "VRF2": {
            "address_family": {
                "ipv4": {
                    "multicast_group": {
                        "239.2.1.100": {
                            "source_address": {
                                "*": {
                                    "uptime": "01:09:45",
                                    "expire": "stopped",
                                    "flags": "SPF",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "88.88.88.88",
                                    "rpf_nbr": "100.88.88.88",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.88.88.88",
                                            "lisp_vrf": "VRF1",
                                        }
                                    },
                                },
                                "193.168.1.2": {
                                    "uptime": "01:09:45",
                                    "expire": "00:02:46",
                                    "flags": "PFTE",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "0.0.0.0",
                                    "rpf_info": "registering",
                                    "incoming_interface_list": {
                                        "Vlan1025": {
                                            "rpf_nbr": "0.0.0.0",
                                            "rpf_info": "registering",
                                        }
                                    },
                                    "extranet_rx_vrf_list": {
                                        "VRF1": {
                                            "e_src": "193.168.1.2",
                                            "e_grp": "239.2.1.100",
                                            "e_uptime": "00:02:11",
                                            "e_expire": "00:00:48",
                                            "e_oif_count": "0",
                                            "e_flags": "PFT",
                                        }
                                    },
                                },
                            }
                        },
                        "239.3.1.100": {
                            "source_address": {
                                "*": {
                                    "uptime": "00:15:34",
                                    "expire": "stopped",
                                    "flags": "SJC",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "70.4.1.1",
                                    "rpf_nbr": "100.88.88.88",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.88.88.88",
                                            "lisp_vrf": "VRF1",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "Vlan1025": {
                                            "uptime": "00:15:34",
                                            "expire": "00:02:56",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                },
                                "70.3.0.2": {
                                    "uptime": "00:13:55",
                                    "expire": "stopped",
                                    "flags": "T",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "100.88.88.88",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.88.88.88",
                                            "lisp_vrf": "VRF1",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "Vlan1025": {
                                            "uptime": "00:13:55",
                                            "expire": "00:02:56",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                },
                            }
                        },
                        "239.1.1.100": {
                            "source_address": {
                                "*": {
                                    "uptime": "00:15:34",
                                    "expire": "stopped",
                                    "flags": "SJC",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "88.88.88.88",
                                    "rpf_nbr": "100.88.88.88",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.88.88.88",
                                            "lisp_vrf": "VRF1",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "Vlan1025": {
                                            "uptime": "00:15:34",
                                            "expire": "00:02:56",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                },
                                "70.3.0.2": {
                                    "uptime": "00:13:55",
                                    "expire": "stopped",
                                    "flags": "T",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "100.88.88.88",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.88.88.88",
                                            "lisp_vrf": "VRF1",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "Vlan1025": {
                                            "uptime": "00:13:55",
                                            "expire": "00:02:56",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                },
                            }
                        },
                        "239.6.1.100": {
                            "source_address": {
                                "*": {
                                    "uptime": "01:09:45",
                                    "expire": "00:03:12",
                                    "flags": "SF",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "152.1.1.1",
                                    "rpf_nbr": "0.0.0.0",
                                    "outgoing_interface_list": {
                                        "LISP0.4101": {
                                            "uptime": "00:15:26",
                                            "expire": "00:03:12",
                                            "state_mode": "forward/sparse",
                                            "lisp_mcast_source": "100.88.88.88",
                                        }
                                    },
                                },
                                "193.168.1.2": {
                                    "uptime": "00:21:14",
                                    "expire": "00:01:49",
                                    "flags": "FT",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "0.0.0.0",
                                    "incoming_interface_list": {
                                        "Vlan1025": {"rpf_nbr": "0.0.0.0"}
                                    },
                                    "outgoing_interface_list": {
                                        "LISP0.4101": {
                                            "uptime": "00:15:26",
                                            "expire": "00:03:12",
                                            "state_mode": "forward/sparse",
                                            "lisp_mcast_source": "100.88.88.88",
                                        }
                                    },
                                },
                            }
                        },
                        "239.7.1.100": {
                            "source_address": {
                                "*": {
                                    "uptime": "00:59:52",
                                    "expire": "stopped",
                                    "flags": "SJCE",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "153.1.1.1",
                                    "rpf_nbr": "100.22.22.22",
                                    "incoming_interface_list": {
                                        "LISP0.4101": {"rpf_nbr": "100.22.22.22"}
                                    },
                                    "outgoing_interface_list": {
                                        "Vlan1025": {
                                            "uptime": "00:15:34",
                                            "expire": "00:02:56",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                    "extranet_rx_vrf_list": {
                                        "VRF1": {
                                            "e_src": "*",
                                            "e_grp": "239.7.1.100",
                                            "e_uptime": "00:58:24",
                                            "e_expire": "stopped",
                                            "e_oif_count": "0",
                                            "e_flags": "SP",
                                            "e_rp": "153.1.1.1",
                                        }
                                    },
                                },
                                "70.3.0.2": {
                                    "uptime": "00:13:55",
                                    "expire": "stopped",
                                    "flags": "JT",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "100.88.88.88",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.88.88.88",
                                            "lisp_vrf": "VRF1",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "Vlan1025": {
                                            "uptime": "00:13:55",
                                            "expire": "00:02:56",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                },
                            }
                        },
                        "239.4.1.100": {
                            "source_address": {
                                "*": {
                                    "uptime": "01:09:45",
                                    "expire": "stopped",
                                    "flags": "SPF",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "70.4.1.1",
                                    "rpf_nbr": "100.88.88.88",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.88.88.88",
                                            "lisp_vrf": "VRF1",
                                        }
                                    },
                                },
                                "193.168.1.2": {
                                    "uptime": "01:09:45",
                                    "expire": "00:02:46",
                                    "flags": "PFTE",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "0.0.0.0",
                                    "rpf_info": "registering",
                                    "incoming_interface_list": {
                                        "Vlan1025": {
                                            "rpf_nbr": "0.0.0.0",
                                            "rpf_info": "registering",
                                        }
                                    },
                                    "extranet_rx_vrf_list": {
                                        "VRF1": {
                                            "e_src": "193.168.1.2",
                                            "e_grp": "239.4.1.100",
                                            "e_uptime": "00:02:11",
                                            "e_expire": "00:00:48",
                                            "e_oif_count": "0",
                                            "e_flags": "PFT",
                                        }
                                    },
                                },
                            }
                        },
                        "239.5.1.100": {
                            "source_address": {
                                "*": {
                                    "uptime": "01:09:35",
                                    "expire": "00:02:50",
                                    "flags": "SJCE",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "152.1.1.1",
                                    "rpf_nbr": "0.0.0.0",
                                    "outgoing_interface_list": {
                                        "LISP0.4101": {
                                            "uptime": "00:15:15",
                                            "expire": "00:02:50",
                                            "state_mode": "forward/sparse",
                                            "lisp_mcast_source": "100.22.22.22",
                                        },
                                        "Vlan1025": {
                                            "uptime": "00:15:34",
                                            "expire": "00:02:56",
                                            "state_mode": "forward/sparse",
                                        },
                                    },
                                    "extranet_rx_vrf_list": {
                                        "VRF1": {
                                            "e_src": "*",
                                            "e_grp": "239.5.1.100",
                                            "e_uptime": "01:09:35",
                                            "e_expire": "stopped",
                                            "e_oif_count": "0",
                                            "e_flags": "SP",
                                            "e_rp": "152.1.1.1",
                                        }
                                    },
                                },
                                "70.3.0.2": {
                                    "uptime": "00:13:55",
                                    "expire": "00:01:20",
                                    "flags": "T",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "100.88.88.88",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.88.88.88",
                                            "lisp_vrf": "VRF1",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "Vlan1025": {
                                            "uptime": "00:13:55",
                                            "expire": "00:02:56",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                },
                            }
                        },
                        "239.10.1.100": {
                            "source_address": {
                                "*": {
                                    "uptime": "01:09:45",
                                    "expire": "stopped",
                                    "flags": "SPF",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "100.100.100.100",
                                    "rpf_nbr": "100.99.99.99",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.99.99.99",
                                            "lisp_vrf": "VRF1",
                                        }
                                    },
                                },
                                "193.168.1.2": {
                                    "uptime": "01:09:45",
                                    "expire": "00:02:43",
                                    "flags": "PFTE",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "0.0.0.0",
                                    "rpf_info": "registering",
                                    "incoming_interface_list": {
                                        "Vlan1025": {
                                            "rpf_nbr": "0.0.0.0",
                                            "rpf_info": "registering",
                                        }
                                    },
                                    "extranet_rx_vrf_list": {
                                        "VRF1": {
                                            "e_src": "193.168.1.2",
                                            "e_grp": "239.10.1.100",
                                            "e_uptime": "00:02:11",
                                            "e_expire": "00:00:48",
                                            "e_oif_count": "0",
                                            "e_flags": "PFT",
                                        }
                                    },
                                },
                            }
                        },
                        "239.8.1.100": {
                            "source_address": {
                                "*": {
                                    "uptime": "01:09:45",
                                    "expire": "stopped",
                                    "flags": "SPF",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "153.1.1.1",
                                    "rpf_nbr": "100.22.22.22",
                                    "incoming_interface_list": {
                                        "LISP0.4101": {"rpf_nbr": "100.22.22.22"}
                                    },
                                },
                                "193.168.1.2": {
                                    "uptime": "00:21:14",
                                    "expire": "00:01:54",
                                    "flags": "FT",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "0.0.0.0",
                                    "incoming_interface_list": {
                                        "Vlan1025": {"rpf_nbr": "0.0.0.0"}
                                    },
                                    "outgoing_interface_list": {
                                        "LISP0.4101": {
                                            "uptime": "00:15:26",
                                            "expire": "00:03:09",
                                            "state_mode": "forward/sparse",
                                            "lisp_mcast_source": "100.88.88.88",
                                        }
                                    },
                                },
                            }
                        },
                        "239.9.1.100": {
                            "source_address": {
                                "*": {
                                    "uptime": "00:15:34",
                                    "expire": "stopped",
                                    "flags": "SJC",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "100.100.100.100",
                                    "rpf_nbr": "100.99.99.99",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.99.99.99",
                                            "lisp_vrf": "VRF1",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "Vlan1025": {
                                            "uptime": "00:15:34",
                                            "expire": "00:02:56",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                }
                            }
                        },
                        "232.100.1.2": {
                            "source_address": {
                                "193.168.1.2": {
                                    "uptime": "00:17:51",
                                    "expire": "00:03:22",
                                    "flags": "sT",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "0.0.0.0",
                                    "incoming_interface_list": {
                                        "Vlan1025": {"rpf_nbr": "0.0.0.0"}
                                    },
                                    "outgoing_interface_list": {
                                        "LISP0.4101": {
                                            "uptime": "00:17:51",
                                            "expire": "00:03:22",
                                            "state_mode": "forward/sparse",
                                            "lisp_mcast_source": "100.88.88.88",
                                        }
                                    },
                                }
                            }
                        },
                        "232.100.1.3": {
                            "source_address": {
                                "70.3.0.2": {
                                    "uptime": "00:16:46",
                                    "expire": "stopped",
                                    "flags": "sTI",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "100.88.88.88",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.88.88.88",
                                            "lisp_vrf": "VRF1",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "Vlan1025": {
                                            "uptime": "00:16:46",
                                            "expire": "00:01:13",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                }
                            }
                        },
                        "232.100.1.1": {
                            "source_address": {
                                "193.168.1.2": {
                                    "uptime": "00:17:28",
                                    "expire": "00:02:44",
                                    "flags": "sT",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "0.0.0.0",
                                    "incoming_interface_list": {
                                        "Vlan1025": {"rpf_nbr": "0.0.0.0"}
                                    },
                                    "outgoing_interface_list": {
                                        "LISP0.4101": {
                                            "uptime": "00:17:28",
                                            "expire": "00:02:44",
                                            "state_mode": "forward/sparse",
                                            "lisp_mcast_source": "100.22.22.22",
                                        }
                                    },
                                }
                            }
                        },
                        "232.100.1.4": {
                            "source_address": {
                                "192.168.1.2": {
                                    "uptime": "00:16:46",
                                    "expire": "stopped",
                                    "flags": "sTI",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "100.22.22.22",
                                    "incoming_interface_list": {
                                        "LISP0.4101": {"rpf_nbr": "100.22.22.22"}
                                    },
                                    "outgoing_interface_list": {
                                        "Vlan1025": {
                                            "uptime": "00:16:46",
                                            "expire": "00:01:13",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                }
                            }
                        },
                        "224.0.1.40": {
                            "source_address": {
                                "*": {
                                    "uptime": "19:22:20",
                                    "expire": "00:02:35",
                                    "flags": "DCL",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rp": "0.0.0.0",
                                    "rpf_nbr": "0.0.0.0",
                                    "outgoing_interface_list": {
                                        "Loopback3": {
                                            "uptime": "19:22:20",
                                            "expire": "00:02:35",
                                            "state_mode": "forward/sparse",
                                        }
                                    },
                                }
                            }
                        },
                    }
                }
            }
        }
    }
}

