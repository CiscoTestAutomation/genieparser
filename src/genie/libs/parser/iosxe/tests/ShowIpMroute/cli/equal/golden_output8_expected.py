expected_output = {
    "vrf": {
        "red": {
            "address_family": {
                "ipv4": {
                    "multicast_group": {
                        "232.64.64.1": {
                            "source_address": {
                                "192.168.1.2": {
                                    "uptime": "4d23h",
                                    "expire": "00:03:27",
                                    "flags": "sTEpl",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "100.11.11.11",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.11.11.11",
                                            "iif_lisp_rloc": "100.11.11.11",
                                            "iif_lisp_group": "232.100.100.66",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "LISP0.4100": {
                                            "uptime": "4d23h",
                                            "expire": "stopped",
                                            "state_mode": "forward/sparse",
                                            "flags": "pt",
                                            "pkts": 0,
                                            "lisp_mcast_source": "100.99.99.99",
                                            "lisp_mcast_group": "232.132.100.66",
                                            "lisp_join_sender_list": {
                                                "32.1.1.110": {
                                                    "uptime": "4d23h",
                                                    "expire": "00:03:05",
                                                },
                                                "100.120.120.120": {
                                                    "uptime": "4d23h",
                                                    "expire": "00:03:27",
                                                },
                                            },
                                        }
                                    },
                                    "extranet_rx_vrf_list": {
                                        "internet": {
                                            "e_src": "192.168.1.2",
                                            "e_grp": "232.64.64.1",
                                            "e_uptime": "4d23h",
                                            "e_expire": "00:03:02",
                                            "e_oif_count": "1",
                                            "e_flags": "sTpl",
                                        }
                                    },
                                },
                                "192.168.1.3": {
                                    "uptime": "4d23h",
                                    "expire": "00:02:56",
                                    "flags": "sTEpl",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "100.22.22.22",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.22.22.22",
                                            "iif_lisp_rloc": "100.22.22.22",
                                            "iif_lisp_group": "232.100.100.218",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "LISP0.4100": {
                                            "uptime": "4d23h",
                                            "expire": "stopped",
                                            "state_mode": "forward/sparse",
                                            "flags": "pt",
                                            "pkts": 0,
                                            "lisp_mcast_source": "100.99.99.99",
                                            "lisp_mcast_group": "232.132.100.218",
                                            "lisp_join_sender_list": {
                                                "100.120.120.120": {
                                                    "uptime": "4d23h",
                                                    "expire": "00:02:56",
                                                }
                                            },
                                        }
                                    },
                                    "extranet_rx_vrf_list": {
                                        "internet": {
                                            "e_src": "192.168.1.3",
                                            "e_grp": "232.64.64.1",
                                            "e_uptime": "4d23h",
                                            "e_expire": "00:02:54",
                                            "e_oif_count": "1",
                                            "e_flags": "sTpl",
                                        }
                                    },
                                },
                                "172.168.1.2": {
                                    "uptime": "4d23h",
                                    "expire": "00:02:47",
                                    "flags": "sTEpl",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "100.110.110.110",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.110.110.110",
                                            "iif_lisp_rloc": "100.110.110.110",
                                            "iif_lisp_group": "232.132.100.165",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "LISP0.4100": {
                                            "uptime": "4d23h",
                                            "expire": "stopped",
                                            "state_mode": "forward/sparse",
                                            "flags": "p",
                                            "pkts": 0,
                                            "lisp_mcast_source": "100.99.99.99",
                                            "lisp_mcast_group": "232.100.100.165",
                                            "lisp_join_sender_list": {
                                                "100.11.11.11": {
                                                    "uptime": "4d23h",
                                                    "expire": "00:02:47",
                                                }
                                            },
                                        }
                                    },
                                    "extranet_rx_vrf_list": {
                                        "internet": {
                                            "e_src": "172.168.1.2",
                                            "e_grp": "232.64.64.1",
                                            "e_uptime": "4d23h",
                                            "e_expire": "00:03:16",
                                            "e_oif_count": "1",
                                            "e_flags": "sTpl",
                                        }
                                    },
                                },
                                "182.168.1.2": {
                                    "uptime": "4d23h",
                                    "expire": "00:03:13",
                                    "flags": "sTEpl",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "100.120.120.120",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.120.120.120",
                                            "iif_lisp_rloc": "100.120.120.120",
                                            "iif_lisp_group": "232.132.100.202",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "LISP0.4100": {
                                            "uptime": "4d23h",
                                            "expire": "stopped",
                                            "state_mode": "forward/sparse",
                                            "flags": "p",
                                            "pkts": 0,
                                            "lisp_mcast_source": "100.99.99.99",
                                            "lisp_mcast_group": "232.100.100.202",
                                            "lisp_join_sender_list": {
                                                "100.22.22.22": {
                                                    "uptime": "4d23h",
                                                    "expire": "00:03:13",
                                                },
                                                "100.11.11.11": {
                                                    "uptime": "4d23h",
                                                    "expire": "00:03:05",
                                                },
                                            },
                                        }
                                    },
                                    "extranet_rx_vrf_list": {
                                        "internet": {
                                            "e_src": "182.168.1.2",
                                            "e_grp": "232.64.64.1",
                                            "e_uptime": "4d23h",
                                            "e_expire": "00:02:54",
                                            "e_oif_count": "1",
                                            "e_flags": "sTpl",
                                        }
                                    },
                                },
                            }
                        },
                        "232.114.114.114": {
                            "source_address": {
                                "192.168.1.3": {
                                    "uptime": "4d23h",
                                    "expire": "00:02:55",
                                    "flags": "sTpl",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "100.22.22.22",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.22.22.22",
                                            "iif_lisp_rloc": "100.22.22.22",
                                            "iif_lisp_group": "232.100.100.101",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "LISP0.4100": {
                                            "uptime": "4d23h",
                                            "expire": "stopped",
                                            "state_mode": "forward/sparse",
                                            "flags": "pt",
                                            "pkts": 0,
                                            "lisp_mcast_source": "100.99.99.99",
                                            "lisp_mcast_group": "232.132.100.101",
                                            "lisp_join_sender_list": {
                                                "32.1.1.110": {
                                                    "uptime": "4d23h",
                                                    "expire": "00:02:55",
                                                }
                                            },
                                        }
                                    },
                                }
                            }
                        },
                        "232.104.104.1": {
                            "source_address": {
                                "192.168.1.3": {
                                    "uptime": "4d23h",
                                    "expire": "stopped",
                                    "flags": "sTEl",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "100.22.22.22",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.22.22.22",
                                            "iif_lisp_rloc": "100.22.22.22",
                                            "iif_lisp_group": "232.100.100.175",
                                        }
                                    },
                                    "extranet_rx_vrf_list": {
                                        "internet": {
                                            "e_src": "192.168.1.3",
                                            "e_grp": "232.104.104.1",
                                            "e_uptime": "4d23h",
                                            "e_expire": "00:03:20",
                                            "e_oif_count": "1",
                                            "e_flags": "sTpl",
                                        }
                                    },
                                }
                            }
                        },
                        "232.134.134.134": {
                            "source_address": {
                                "192.168.1.3": {
                                    "uptime": "4d23h",
                                    "expire": "00:02:55",
                                    "flags": "sTpl",
                                    "msdp_learned": False,
                                    "rp_bit": False,
                                    "rpf_nbr": "100.22.22.22",
                                    "incoming_interface_list": {
                                        "LISP0.4100": {
                                            "rpf_nbr": "100.22.22.22",
                                            "iif_lisp_rloc": "100.22.22.22",
                                            "iif_lisp_group": "232.100.100.234",
                                        }
                                    },
                                    "outgoing_interface_list": {
                                        "LISP0.4100": {
                                            "uptime": "4d23h",
                                            "expire": "stopped",
                                            "state_mode": "forward/sparse",
                                            "flags": "pt",
                                            "pkts": 0,
                                            "lisp_mcast_source": "100.99.99.99",
                                            "lisp_mcast_group": "232.132.100.234",
                                            "lisp_join_sender_list": {
                                                "100.120.120.120": {
                                                    "uptime": "4d23h",
                                                    "expire": "00:02:55",
                                                }
                                            },
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

