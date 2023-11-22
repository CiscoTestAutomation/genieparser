expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "0.0.0.0/0": {
                            "route": "0.0.0.0/0",
                            "active": True,
                            "metric": 10,
                            "route_preference": 115,
                            "source_protocol_codes": "i*L2",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.190.110",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/4"
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "172.20.190.101",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/3"
                                    }
                                }
                            }
                        },
                        "172.20.2.32/27": {
                            "route": "172.20.2.32/27",
                            "active": True,
                            "source_protocol_codes": "i L2",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.190.110",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/4"
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "172.20.190.101",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/3"
                                    }
                                }
                            },
                            "metric": 5565,
                            "route_preference": 115
                        },
                        "172.20.2.253/32": {
                            "route": "172.20.2.253/32",
                            "active": True,
                            "source_protocol_codes": "i L1",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.190.101",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/3"
                                    }
                                }
                            },
                            "metric": 20,
                            "route_preference": 115
                        },
                        "172.20.2.254/32": {
                            "route": "172.20.2.254/32",
                            "active": True,
                            "source_protocol_codes": "i L1",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.190.110",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/4"
                                    }
                                }
                            },
                            "metric": 20,
                            "route_preference": 115
                        },
                        "172.20.30.0/24": {
                            "route": "172.20.30.0/24",
                            "active": True,
                            "source_protocol_codes": "i L2",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.190.110",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/4"
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "172.20.190.101",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/3"
                                    }
                                }
                            },
                            "metric": 5565,
                            "route_preference": 115
                        },
                        "172.20.190.65/32": {
                            "route": "172.20.190.65/32",
                            "active": True,
                            "source_protocol_codes": "i L1",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.190.110",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/4"
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "172.20.190.101",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/3"
                                    }
                                }
                            },
                            "metric": 20,
                            "route_preference": 115
                        },
                        "172.20.190.66/32": {
                            "route": "172.20.190.66/32",
                            "active": True,
                            "source_protocol_codes": "i L1",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.190.110",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/4"
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "172.20.190.101",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/3"
                                    }
                                }
                            },
                            "metric": 30,
                            "route_preference": 115
                        },
                        "172.20.190.67/32": {
                            "route": "172.20.190.67/32",
                            "active": True,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Loopback0": {
                                        "outgoing_interface": "Loopback0"
                                    }
                                }
                            }
                        },
                        "172.20.190.68/32": {
                            "route": "172.20.190.68/32",
                            "active": True,
                            "source_protocol_codes": "i L1",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.190.101",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/3"
                                    }
                                }
                            },
                            "metric": 30,
                            "route_preference": 115
                        },
                        "172.20.190.69/32": {
                            "route": "172.20.190.69/32",
                            "active": True,
                            "source_protocol_codes": "i L1",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.190.110",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/4"
                                    }
                                }
                            },
                            "metric": 30,
                            "route_preference": 115
                        },
                        "172.20.190.70/31": {
                            "route": "172.20.190.70/31",
                            "active": True,
                            "source_protocol_codes": "i L1",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.190.101",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/3"
                                    }
                                }
                            },
                            "metric": 20,
                            "route_preference": 115
                        },
                        "172.20.190.72/32": {
                            "route": "172.20.190.72/32",
                            "active": True,
                            "source_protocol_codes": "i L1",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.190.101",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/3"
                                    }
                                }
                            },
                            "metric": 30,
                            "route_preference": 115
                        },
                        "172.20.190.74/31": {
                            "route": "172.20.190.74/31",
                            "active": True,
                            "source_protocol_codes": "i L1",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.190.110",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/4"
                                    }
                                }
                            },
                            "metric": 20,
                            "route_preference": 115
                        },
                        "172.20.190.96/30": {
                            "route": "172.20.190.96/30",
                            "active": True,
                            "source_protocol_codes": "i L1",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.190.101",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/3"
                                    }
                                }
                            },
                            "metric": 20,
                            "route_preference": 115
                        },
                        "172.20.190.100/30": {
                            "route": "172.20.190.100/30",
                            "active": True,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "TenGigabitEthernet1/1/3": {
                                        "outgoing_interface": "TenGigabitEthernet1/1/3"
                                    }
                                }
                            }
                        },
                        "172.20.190.102/32": {
                            "route": "172.20.190.102/32",
                            "active": True,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "TenGigabitEthernet1/1/3": {
                                        "outgoing_interface": "TenGigabitEthernet1/1/3"
                                    }
                                }
                            }
                        },
                        "172.20.190.104/30": {
                            "route": "172.20.190.104/30",
                            "active": True,
                            "source_protocol_codes": "i L1",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.190.110",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/4"
                                    }
                                }
                            },
                            "metric": 20,
                            "route_preference": 115
                        },
                        "172.20.190.108/30": {
                            "route": "172.20.190.108/30",
                            "active": True,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "TenGigabitEthernet1/1/4": {
                                        "outgoing_interface": "TenGigabitEthernet1/1/4"
                                    }
                                }
                            }
                        },
                        "172.20.190.109/32": {
                            "route": "172.20.190.109/32",
                            "active": True,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "TenGigabitEthernet1/1/4": {
                                        "outgoing_interface": "TenGigabitEthernet1/1/4"
                                    }
                                }
                            }
                        },
                        "172.20.190.112/30": {
                            "route": "172.20.190.112/30",
                            "active": True,
                            "source_protocol_codes": "i L1",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.190.101",
                                        "updated": "5w6d",
                                        "outgoing_interface": "TenGigabitEthernet1/1/3"
                                    }
                                }
                            },
                            "metric": 20,
                            "route_preference": 115
                        },
                        "172.20.199.0/27": {
                            "route": "172.20.199.0/27",
                            "active": True,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Vlan1036": {
                                        "outgoing_interface": "Vlan1036"
                                    }
                                }
                            }
                        },
                        "172.20.199.1/32": {
                            "route": "172.20.199.1/32",
                            "active": True,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Vlan1036": {
                                        "outgoing_interface": "Vlan1036"
                                    }
                                }
                            }
                        },
                        "172.20.199.24/32": {
                            "route": "172.20.199.24/32",
                            "active": True,
                            "metric": 1,
                            "route_preference": 10,
                            "source_protocol_codes": "l",
                            "source_protocol": "lisp",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.199.24",
                                        "updated": "20:11:13",
                                        "outgoing_interface": "Vlan1036"
                                    }
                                }
                            }
                        },
                        "172.20.199.128/27": {
                            "route": "172.20.199.128/27",
                            "active": True,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Vlan1038": {
                                        "outgoing_interface": "Vlan1038"
                                    }
                                }
                            }
                        },
                        "172.20.199.129/32": {
                            "route": "172.20.199.129/32",
                            "active": True,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Vlan1038": {
                                        "outgoing_interface": "Vlan1038"
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