expected_output = {
    "vrf": {
        "default": {
            "local_label": {
                22: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "10/1[TE-Bind]": {
                                    "outgoing_interface": {
                                        "Tunnel10": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "65757/1[TE-Bind]": {
                                    "outgoing_interface": {
                                        "Tunnel65757": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
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
                                "65758/1[TE-Bind]": {
                                    "outgoing_interface": {
                                        "Tunnel65758": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                19: {
                    "outgoing_label_or_vc": {
                        "No Label": {
                            "prefix_or_tunnel_id": {
                                "30.30.30.0/24": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/0/3": {
                                            "next_hop": "10.10.10.2",
                                            "bytes_label_switched": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16021: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "2.2.2.2/32": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/0/3": {
                                            "next_hop": "10.10.10.2",
                                            "bytes_label_switched": 0,
                                            "merged": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16022: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "0-2.2.2.2/32-2": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/0/3": {
                                            "next_hop": "10.10.10.2",
                                            "bytes_label_switched": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                25: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "5.5.5.5/32": {
                                    "outgoing_interface": {
                                        "Tunnel65758": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        },
                                        "Tunnel20": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        },
                                        "Tunnel65757": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        },
                                        "Tunnel10": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                26: {
                    "outgoing_label_or_vc": {
                        "No Label": {
                            "prefix_or_tunnel_id": {
                                "60.60.60.0/24": {
                                    "outgoing_interface": {
                                        "Tunnel65758": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        },
                                        "Tunnel20": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        },
                                        "Tunnel10": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        },
                                        "Tunnel65757": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                28: {
                    "outgoing_label_or_vc": {
                        "16061": {
                            "prefix_or_tunnel_id": {
                                "6.6.6.6/32": {
                                    "outgoing_interface": {
                                        "Tunnel20": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        },
                                        "Tunnel10": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                29: {
                    "outgoing_label_or_vc": {
                        "No Label": {
                            "prefix_or_tunnel_id": {
                                "90.90.90.0/24": {
                                    "outgoing_interface": {
                                        "TenGigabitEthernet0/0/5": {
                                            "next_hop": "20.20.20.2",
                                            "bytes_label_switched": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                30: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "10.10.10.2-A": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/0/3": {
                                            "next_hop": "10.10.10.2",
                                            "bytes_label_switched": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                31: {
                    "outgoing_label_or_vc": {
                        "No Label": {
                            "prefix_or_tunnel_id": {
                                "80.80.80.0/24": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/0/3": {
                                            "next_hop": "10.10.10.2",
                                            "bytes_label_switched": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                32: {
                    "outgoing_label_or_vc": {
                        "No Label": {
                            "prefix_or_tunnel_id": {
                                "70.70.70.0/24": {
                                    "outgoing_interface": {
                                        "Tunnel20": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        },
                                        "Tunnel10": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                34: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "20/1[TE-Bind]": {
                                    "outgoing_interface": {
                                        "Tunnel20": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                35: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "20.20.20.2-A": {
                                    "outgoing_interface": {
                                        "TenGigabitEthernet0/0/5": {
                                            "next_hop": "20.20.20.2",
                                            "bytes_label_switched": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16041: {
                    "outgoing_label_or_vc": {
                        "16041": {
                            "prefix_or_tunnel_id": {
                                "4.4.4.4/32": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/0/3": {
                                            "next_hop": "10.10.10.2",
                                            "bytes_label_switched": 0,
                                            "merged": True
                                        },
                                        "TenGigabitEthernet0/0/5": {
                                            "next_hop": "20.20.20.2",
                                            "bytes_label_switched": 0,
                                            "merged": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                42: {
                    "outgoing_label_or_vc": {
                        "No Label": {
                            "prefix_or_tunnel_id": {
                                "50.50.50.0/24": {
                                    "outgoing_interface": {
                                        "TenGigabitEthernet0/0/5": {
                                            "next_hop": "20.20.20.2",
                                            "bytes_label_switched": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                45: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "3.3.3.3/32": {
                                    "outgoing_interface": {
                                        "TenGigabitEthernet0/0/5": {
                                            "next_hop": "20.20.20.2",
                                            "bytes_label_switched": 0,
                                            "merged": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                46: {
                    "outgoing_label_or_vc": {
                        "No Label": {
                            "prefix_or_tunnel_id": {
                                "40.40.40.0/24": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/0/3": {
                                            "next_hop": "10.10.10.2",
                                            "bytes_label_switched": 0
                                        },
                                        "TenGigabitEthernet0/0/5": {
                                            "next_hop": "20.20.20.2",
                                            "bytes_label_switched": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                47: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "2.2.2.2/32": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/0/3": {
                                            "next_hop": "10.10.10.2",
                                            "bytes_label_switched": 0,
                                            "merged": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                48: {
                    "outgoing_label_or_vc": {
                        "16041": {
                            "prefix_or_tunnel_id": {
                                "4.4.4.4/32": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/0/3": {
                                            "next_hop": "10.10.10.2",
                                            "bytes_label_switched": 0,
                                            "merged": True
                                        },
                                        "TenGigabitEthernet0/0/5": {
                                            "next_hop": "20.20.20.2",
                                            "bytes_label_switched": 0,
                                            "merged": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16051: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "0-5.5.5.5/32-1": {
                                    "outgoing_interface": {
                                        "Tunnel65758": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        },
                                        "Tunnel20": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16052: {
                    "outgoing_label_or_vc": {
                        "16052": {
                            "prefix_or_tunnel_id": {
                                "0-5.5.5.5/32-2": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/0/3": {
                                            "next_hop": "10.10.10.2",
                                            "bytes_label_switched": 0
                                        },
                                        "TenGigabitEthernet0/0/5": {
                                            "next_hop": "20.20.20.2",
                                            "bytes_label_switched": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16031: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "3.3.3.3/32": {
                                    "outgoing_interface": {
                                        "TenGigabitEthernet0/0/5": {
                                            "next_hop": "20.20.20.2",
                                            "bytes_label_switched": 0,
                                            "merged": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16061: {
                    "outgoing_label_or_vc": {
                        "16061": {
                            "prefix_or_tunnel_id": {
                                "0-6.6.6.6/32-1": {
                                    "outgoing_interface": {
                                        "Tunnel65758": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        },
                                        "Tunnel20": {
                                            "next_hop": "point2point",
                                            "tsp_tunnel": True
                                        },
                                        "GigabitEthernet0/0/3": {
                                            "next_hop": "10.10.10.2"
                                        },
                                        "TenGigabitEthernet0/0/5": {
                                            "next_hop": "20.20.20.2",
                                            "bytes_label_switched": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16062: {
                    "outgoing_label_or_vc": {
                        "16062": {
                            "prefix_or_tunnel_id": {
                                "0-6.6.6.6/32-2": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/0/3": {
                                            "next_hop": "10.10.10.2",
                                            "bytes_label_switched": 0
                                        },
                                        "TenGigabitEthernet0/0/5": {
                                            "next_hop": "20.20.20.2",
                                            "bytes_label_switched": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16032: {
                    "outgoing_label_or_vc": {
                        "Pop Label": {
                            "prefix_or_tunnel_id": {
                                "0-3.3.3.3/32-2": {
                                    "outgoing_interface": {
                                        "TenGigabitEthernet0/0/5": {
                                            "next_hop": "20.20.20.2",
                                            "bytes_label_switched": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16042: {
                    "outgoing_label_or_vc": {
                        "16042": {
                            "prefix_or_tunnel_id": {
                                "0-4.4.4.4/32-2": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/0/3": {
                                            "next_hop": "10.10.10.2",
                                            "bytes_label_switched": 0
                                        },
                                        "TenGigabitEthernet0/0/5": {
                                            "next_hop": "20.20.20.2",
                                            "bytes_label_switched": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                21: {
                    "outgoing_label_or_vc": {
                        "No Label": {
                            "prefix_or_tunnel_id": {
                                "45.45.45.0/24": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/0/3": {
                                            "next_hop": "10.10.10.2",
                                            "bytes_label_switched": 0
                                        },
                                        "TenGigabitEthernet0/0/5": {
                                            "next_hop": "20.20.20.2",
                                            "bytes_label_switched": 0
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