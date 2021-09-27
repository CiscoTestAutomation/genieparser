expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.23.120.0/24": {
                            "route": "10.23.120.0/24",
                            "active": True,
                            "route_preference": 120,
                            "metric": 1,
                            "source_protocol": "rip",
                            "source_protocol_codes": "R",
                            "next_hop": {
                                "next_hop_list": {
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.12.120.2",
                                        "outgoing_interface": "GigabitEthernet2.120",
                                        "updated": "00:00:02",
                                    },
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.13.120.3",
                                        "outgoing_interface": "GigabitEthernet3.120",
                                        "updated": "00:00:08",
                                    },
                                }
                            },
                        },
                        "10.23.115.0/24": {
                            "route": "10.23.115.0/24",
                            "active": True,
                            "route_preference": 115,
                            "metric": 20,
                            "source_protocol": "isis",
                            "source_protocol_codes": "i L1",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.12.115.2",
                                        "outgoing_interface": "GigabitEthernet2.115",
                                        "updated": "4d19h",
                                    }
                                }
                            },
                        },
                        "10.23.110.0/24": {
                            "route": "10.23.110.0/24",
                            "active": True,
                            "route_preference": 110,
                            "metric": 2,
                            "source_protocol": "ospf",
                            "source_protocol_codes": "O",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.12.110.2",
                                        "outgoing_interface": "GigabitEthernet2.110",
                                        "updated": "4d19h",
                                    }
                                }
                            },
                        },
                        "10.23.90.0/24": {
                            "route": "10.23.90.0/24",
                            "active": True,
                            "route_preference": 90,
                            "metric": 15360,
                            "source_protocol": "eigrp",
                            "source_protocol_codes": "D",
                            "next_hop": {
                                "next_hop_list": {
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.12.90.2",
                                        "outgoing_interface": "GigabitEthernet2.90",
                                        "updated": "4d19h",
                                    },
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.13.90.3",
                                        "outgoing_interface": "GigabitEthernet3.90",
                                        "updated": "4d19h",
                                    },
                                }
                            },
                        },
                        "10.13.120.1/32": {
                            "route": "10.13.120.1/32",
                            "active": True,
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.120": {
                                        "outgoing_interface": "GigabitEthernet3.120"
                                    }
                                }
                            },
                        },
                        "10.13.120.0/24": {
                            "route": "10.13.120.0/24",
                            "active": True,
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.120": {
                                        "outgoing_interface": "GigabitEthernet3.120"
                                    }
                                }
                            },
                        },
                        "10.13.115.1/32": {
                            "route": "10.13.115.1/32",
                            "active": True,
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.115": {
                                        "outgoing_interface": "GigabitEthernet3.115"
                                    }
                                }
                            },
                        },
                        "10.13.115.0/24": {
                            "route": "10.13.115.0/24",
                            "active": True,
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.115": {
                                        "outgoing_interface": "GigabitEthernet3.115"
                                    }
                                }
                            },
                        },
                        "10.13.110.1/32": {
                            "route": "10.13.110.1/32",
                            "active": True,
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.110": {
                                        "outgoing_interface": "GigabitEthernet3.110"
                                    }
                                }
                            },
                        },
                        "10.13.110.0/24": {
                            "route": "10.13.110.0/24",
                            "active": True,
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.110": {
                                        "outgoing_interface": "GigabitEthernet3.110"
                                    }
                                }
                            },
                        },
                        "10.13.90.1/32": {
                            "route": "10.13.90.1/32",
                            "active": True,
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.90": {
                                        "outgoing_interface": "GigabitEthernet3.90"
                                    }
                                }
                            },
                        },
                        "10.13.90.0/24": {
                            "route": "10.13.90.0/24",
                            "active": True,
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.90": {
                                        "outgoing_interface": "GigabitEthernet3.90"
                                    }
                                }
                            },
                        },
                        "10.12.120.1/32": {
                            "route": "10.12.120.1/32",
                            "active": True,
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.120": {
                                        "outgoing_interface": "GigabitEthernet2.120"
                                    }
                                }
                            },
                        },
                        "10.12.120.0/24": {
                            "route": "10.12.120.0/24",
                            "active": True,
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.120": {
                                        "outgoing_interface": "GigabitEthernet2.120"
                                    }
                                }
                            },
                        },
                        "10.12.115.1/32": {
                            "route": "10.12.115.1/32",
                            "active": True,
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.115": {
                                        "outgoing_interface": "GigabitEthernet2.115"
                                    }
                                }
                            },
                        },
                        "10.12.115.0/24": {
                            "route": "10.12.115.0/24",
                            "active": True,
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.115": {
                                        "outgoing_interface": "GigabitEthernet2.115"
                                    }
                                }
                            },
                        },
                        "10.12.110.1/32": {
                            "route": "10.12.110.1/32",
                            "active": True,
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.110": {
                                        "outgoing_interface": "GigabitEthernet2.110"
                                    }
                                }
                            },
                        },
                        "10.12.110.0/24": {
                            "route": "10.12.110.0/24",
                            "active": True,
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.110": {
                                        "outgoing_interface": "GigabitEthernet2.110"
                                    }
                                }
                            },
                        },
                        "10.12.90.1/32": {
                            "route": "10.12.90.1/32",
                            "active": True,
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.90": {
                                        "outgoing_interface": "GigabitEthernet2.90"
                                    }
                                }
                            },
                        },
                        "10.12.90.0/24": {
                            "route": "10.12.90.0/24",
                            "active": True,
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.90": {
                                        "outgoing_interface": "GigabitEthernet2.90"
                                    }
                                }
                            },
                        },
                        "10.36.3.3/32": {
                            "route": "10.36.3.3/32",
                            "active": True,
                            "route_preference": 90,
                            "metric": 2570240,
                            "source_protocol": "eigrp",
                            "source_protocol_codes": "D",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.13.90.3",
                                        "outgoing_interface": "GigabitEthernet3.90",
                                        "updated": "4d19h",
                                    }
                                }
                            },
                        },
                        "10.16.2.2/32": {
                            "route": "10.16.2.2/32",
                            "active": True,
                            "route_preference": 90,
                            "metric": 10752,
                            "source_protocol": "eigrp",
                            "source_protocol_codes": "D",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.12.90.2",
                                        "outgoing_interface": "GigabitEthernet2.90",
                                        "updated": "4d19h",
                                    }
                                }
                            },
                        },
                        "10.4.1.1/32": {
                            "route": "10.4.1.1/32",
                            "active": True,
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Loopback0": {"outgoing_interface": "Loopback0"}
                                }
                            },
                        },
                    }
                }
            }
        }
    }
}