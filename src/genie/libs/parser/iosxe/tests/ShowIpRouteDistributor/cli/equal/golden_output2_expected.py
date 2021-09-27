expected_output = {
    "vrf": {
        "VRF1": {
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
                                        "outgoing_interface": "GigabitEthernet2.420",
                                        "updated": "00:00:17",
                                    },
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.13.120.3",
                                        "outgoing_interface": "GigabitEthernet3.420",
                                        "updated": "00:00:20",
                                    },
                                }
                            },
                        },
                        "10.23.115.0/24": {
                            "route": "10.23.115.0/24",
                            "active": True,
                            "route_preference": 115,
                            "metric": 50,
                            "source_protocol": "isis",
                            "source_protocol_codes": "i L1",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.13.115.3",
                                        "outgoing_interface": "GigabitEthernet3.415",
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
                                        "outgoing_interface": "GigabitEthernet2.410",
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
                                        "outgoing_interface": "GigabitEthernet2.390",
                                        "updated": "4d19h",
                                    },
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.13.90.3",
                                        "outgoing_interface": "GigabitEthernet3.390",
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
                                    "GigabitEthernet3.420": {
                                        "outgoing_interface": "GigabitEthernet3.420"
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
                                    "GigabitEthernet3.420": {
                                        "outgoing_interface": "GigabitEthernet3.420"
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
                                    "GigabitEthernet3.415": {
                                        "outgoing_interface": "GigabitEthernet3.415"
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
                                    "GigabitEthernet3.415": {
                                        "outgoing_interface": "GigabitEthernet3.415"
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
                                    "GigabitEthernet3.410": {
                                        "outgoing_interface": "GigabitEthernet3.410"
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
                                    "GigabitEthernet3.410": {
                                        "outgoing_interface": "GigabitEthernet3.410"
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
                                    "GigabitEthernet3.390": {
                                        "outgoing_interface": "GigabitEthernet3.390"
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
                                    "GigabitEthernet3.390": {
                                        "outgoing_interface": "GigabitEthernet3.390"
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
                                    "GigabitEthernet2.420": {
                                        "outgoing_interface": "GigabitEthernet2.420"
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
                                    "GigabitEthernet2.420": {
                                        "outgoing_interface": "GigabitEthernet2.420"
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
                                    "GigabitEthernet2.415": {
                                        "outgoing_interface": "GigabitEthernet2.415"
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
                                    "GigabitEthernet2.415": {
                                        "outgoing_interface": "GigabitEthernet2.415"
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
                                    "GigabitEthernet2.410": {
                                        "outgoing_interface": "GigabitEthernet2.410"
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
                                    "GigabitEthernet2.410": {
                                        "outgoing_interface": "GigabitEthernet2.410"
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
                                    "GigabitEthernet2.390": {
                                        "outgoing_interface": "GigabitEthernet2.390"
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
                                    "GigabitEthernet2.390": {
                                        "outgoing_interface": "GigabitEthernet2.390"
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
                                        "outgoing_interface": "GigabitEthernet3.390",
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
                                        "outgoing_interface": "GigabitEthernet2.390",
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
                                    "Loopback300": {"outgoing_interface": "Loopback300"}
                                }
                            },
                        },
                    }
                }
            }
        }
    }
}