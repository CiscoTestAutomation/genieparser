expected_output = {
    "distribution": {
        "multicast": {
            "route": {
                "vrf": {
                    "default": {
                        "address_family": {
                            "ipv4": {
                                "num_groups": 11,
                                "gaddr": {
                                    "232.0.0.0/8": {
                                        "grp_len": 8,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "NULL",
                                                "flags": "DNf",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0
                                            }
                                        }
                                    },
                                    "239.0.2.30/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "port-channel100",
                                                "flags": "GLNf",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 18,
                                                    "Vlan361": {
                                                        "oif": "Vlan361",
                                                        "encap": "vpc",
                                                        "l2_oiflist_index": 1
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "239.1.1.13/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "36.2.0.101/32": {
                                                "src_len": 32,
                                                "rpf_ifname": "Ethernet1/7",
                                                "flags": "L",
                                                "rcv_packets": 13,
                                                "rcv_bytes": 845,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 24,
                                                    "port-channel100": {
                                                        "oif": "port-channel100"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "239.1.1.22/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "port-channel100",
                                                "flags": "GLNf",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 19,
                                                    "Vlan461": {
                                                        "oif": "Vlan461",
                                                        "encap": "vpc",
                                                        "l2_oiflist_index": 1
                                                    }
                                                }
                                            },
                                            "46.1.0.221/32": {
                                                "src_len": 32,
                                                "rpf_ifname": "Vlan461",
                                                "flags": "O",
                                                "rcv_packets": 13,
                                                "rcv_bytes": 845,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 25,
                                                    "Vlan461": {
                                                        "oif": "Vlan461",
                                                        "mem_l2_ports": "port-channel40",
                                                        "l2_oiflist_index": 1
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "239.1.1.23/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "port-channel100",
                                                "flags": "GLNf",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 19,
                                                    "Vlan461": {
                                                        "oif": "Vlan461",
                                                        "encap": "vpc",
                                                        "l2_oiflist_index": 1
                                                    }
                                                }
                                            },
                                            "46.1.0.231/32": {
                                                "src_len": 32,
                                                "rpf_ifname": "Vlan461",
                                                "flags": "O",
                                                "rcv_packets": 13,
                                                "rcv_bytes": 845,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 25,
                                                    "Vlan461": {
                                                        "oif": "Vlan461",
                                                        "mem_l2_ports": "port-channel40",
                                                        "l2_oiflist_index": 1
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "239.2.1.2/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "port-channel100",
                                                "flags": "GLNf",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 19,
                                                    "Vlan461": {
                                                        "oif": "Vlan461",
                                                        "encap": "vpc",
                                                        "l2_oiflist_index": 1
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "239.3.1.2/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "port-channel100",
                                                "flags": "GLNf",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 20,
                                                    "Vlan461": {
                                                        "oif": "Vlan461",
                                                        "encap": "vpc",
                                                        "mem_l2_ports": "Ethernet1/8",
                                                        "l2_oiflist_index": 7
                                                    }
                                                }
                                            },
                                            "46.1.0.211/32": {
                                                "src_len": 32,
                                                "rpf_ifname": "Vlan461",
                                                "flags": "O",
                                                "rcv_packets": 13,
                                                "rcv_bytes": 845,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 23,
                                                    "Vlan461": {
                                                        "oif": "Vlan461",
                                                        "mem_l2_ports": "port-channel40 Ethernet1/8",
                                                        "l2_oiflist_index": 7
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "239.3.1.3/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "port-channel100",
                                                "flags": "GLNf",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 20,
                                                    "Vlan461": {
                                                        "oif": "Vlan461",
                                                        "encap": "vpc",
                                                        "mem_l2_ports": "Ethernet1/8",
                                                        "l2_oiflist_index": 7
                                                    }
                                                }
                                            },
                                            "46.1.0.221/32": {
                                                "src_len": 32,
                                                "rpf_ifname": "Vlan461",
                                                "flags": "O",
                                                "rcv_packets": 13,
                                                "rcv_bytes": 845,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 23,
                                                    "Vlan461": {
                                                        "oif": "Vlan461",
                                                        "mem_l2_ports": "port-channel40 Ethernet1/8",
                                                        "l2_oiflist_index": 7
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "239.3.1.12/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "port-channel100",
                                                "flags": "GLNf",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 21,
                                                    "Ethernet1/7": {
                                                        "oif": "Ethernet1/7"
                                                    }
                                                }
                                            },
                                            "16.1.0.101/32": {
                                                "src_len": 32,
                                                "rpf_ifname": "port-channel100",
                                                "flags": "LNf",
                                                "rcv_packets": 13,
                                                "rcv_bytes": 845,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 21,
                                                    "Ethernet1/7": {
                                                        "oif": "Ethernet1/7"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "239.3.1.13/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "port-channel100",
                                                "flags": "GLNf",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 21,
                                                    "Ethernet1/7": {
                                                        "oif": "Ethernet1/7"
                                                    }
                                                }
                                            },
                                            "26.1.0.102/32": {
                                                "src_len": 32,
                                                "rpf_ifname": "port-channel100",
                                                "flags": "LNf",
                                                "rcv_packets": 13,
                                                "rcv_bytes": 845,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 21,
                                                    "Ethernet1/7": {
                                                        "oif": "Ethernet1/7"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "239.4.1.2/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "port-channel100",
                                                "flags": "GLNf",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 22,
                                                    "Vlan461": {
                                                        "oif": "Vlan461",
                                                        "encap": "vpc",
                                                        "mem_l2_ports": "port-channel10",
                                                        "l2_oiflist_index": 2
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