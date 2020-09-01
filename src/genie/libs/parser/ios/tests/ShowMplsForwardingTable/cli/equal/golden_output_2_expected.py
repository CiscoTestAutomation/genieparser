expected_output = {
    "vrf": {
        "default": {
            "local_label": {
                16: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "10.4.1.2-A": {
                                    "outgoing_interface": {
                                        "Ethernet0/0": {
                                            "next_hop": "10.4.1.2",
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                17: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "10.4.1.2-A": {
                                    "outgoing_interface": {
                                        "Ethernet0/0": {
                                            "next_hop": "10.4.1.2",
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                18: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "10.4.1.2-A": {
                                    "outgoing_interface": {
                                        "Ethernet0/0": {
                                            "next_hop": "10.4.1.2",
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                19: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "10.135.15.2-A": {
                                    "outgoing_interface": {
                                        "Ethernet0/1": {
                                            "next_hop": "10.135.15.2",
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                20: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "10.135.15.2-A": {
                                    "outgoing_interface": {
                                        "Ethernet0/1": {
                                            "next_hop": "10.135.15.2",
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                21: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "10.135.15.2-A": {
                                    "outgoing_interface": {
                                        "Ethernet0/1": {
                                            "next_hop": "10.135.15.2",
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                22: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "192.168.0.1/32": {
                                    "outgoing_interface": {
                                        "GigabitEthernet2": {
                                            "next_hop": "192.168.0.2",
                                            "merged": True,
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16110: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "10.70.20.20/32": {
                                    "outgoing_interface": {
                                        "Ethernet0/0": {
                                            "next_hop": "10.4.1.2",
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16120: {
                    "outgoing_label_or_vc": {
                        "16120": {
                            "prefix_or_tunnel_id": {
                                "10.30.30.30/32": {
                                    "outgoing_interface": {
                                        "Ethernet0/0": {
                                            "next_hop": "10.4.1.2",
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16130: {
                    "outgoing_label_or_vc": {
                        "16130": {
                            "prefix_or_tunnel_id": {
                                "10.25.40.40/32": {
                                    "outgoing_interface": {
                                        "Ethernet0/0": {
                                            "next_hop": "10.4.1.2",
                                            "bytes_label_switched": 0,
                                        },
                                        "Tunnel1": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True,
                                            "bytes_label_switched": 0,
                                        },
                                    }
                                }
                            }
                        }
                    }
                },
                16140: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "10.55.50.50/32": {
                                    "outgoing_interface": {
                                        "Tunnel1": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True,
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16200: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "10.220.100.100/32": {
                                    "outgoing_interface": {
                                        "Ethernet0/1": {
                                            "next_hop": "10.135.15.2",
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                17100: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "0-10.70.20.20/32-0": {
                                    "outgoing_interface": {
                                        "Ethernet0/0": {
                                            "next_hop": "10.4.1.2",
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                17200: {
                    "outgoing_label_or_vc": {
                        "17200": {
                            "prefix_or_tunnel_id": {
                                "0-10.30.30.30/32-0": {
                                    "outgoing_interface": {
                                        "Ethernet0/0": {
                                            "next_hop": "10.4.1.2",
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                17300: {
                    "outgoing_label_or_vc": {
                        "17300": {
                            "prefix_or_tunnel_id": {
                                "0-10.25.40.40/32-0": {
                                    "outgoing_interface": {
                                        "Ethernet0/1": {
                                            "next_hop": "10.135.15.2",
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                17400: {
                    "outgoing_label_or_vc": {
                        "17400": {
                            "prefix_or_tunnel_id": {
                                "0-10.55.50.50/32-0": {
                                    "outgoing_interface": {
                                        "Ethernet0/1": {
                                            "next_hop": "10.135.15.2",
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                18000: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "0-10.220.100.100/32-0": {
                                    "outgoing_interface": {
                                        "Ethernet0/1": {
                                            "next_hop": "10.135.15.2",
                                            "bytes_label_switched": 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
            }
        }
    }
}
