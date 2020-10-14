expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.4.1.1/32": {
                            "route": "10.4.1.1/32",
                            "active": True,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Loopback0": {"outgoing_interface": "Loopback0"}
                                }
                            },
                        },
                        "10.16.2.2/32": {
                            "route": "10.16.2.2/32",
                            "active": True,
                            "route_preference": 1,
                            "metric": 0,
                            "source_protocol_codes": "S",
                            "source_protocol": "static",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.186.2.2",
                                        "outgoing_interface": "GigabitEthernet0/1",
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.1.2.2",
                                        "outgoing_interface": "GigabitEthernet0/0",
                                    },
                                }
                            },
                        },
                        "10.36.3.3/32": {
                            "route": "10.36.3.3/32",
                            "active": True,
                            "source_protocol_codes": "S",
                            "source_protocol": "static",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/3": {
                                        "outgoing_interface": "GigabitEthernet0/3"
                                    },
                                    "GigabitEthernet0/2": {
                                        "outgoing_interface": "GigabitEthernet0/2"
                                    },
                                }
                            },
                        },
                        "10.1.2.0/24": {
                            "route": "10.1.2.0/24",
                            "active": True,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0": {
                                        "outgoing_interface": "GigabitEthernet0/0"
                                    }
                                }
                            },
                        },
                        "10.1.2.1/32": {
                            "route": "10.1.2.1/32",
                            "active": True,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0": {
                                        "outgoing_interface": "GigabitEthernet0/0"
                                    }
                                }
                            },
                        },
                        "10.1.3.0/24": {
                            "route": "10.1.3.0/24",
                            "active": True,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/2": {
                                        "outgoing_interface": "GigabitEthernet0/2"
                                    }
                                }
                            },
                        },
                        "10.1.3.1/32": {
                            "route": "10.1.3.1/32",
                            "active": True,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/2": {
                                        "outgoing_interface": "GigabitEthernet0/2"
                                    }
                                }
                            },
                        },
                        "10.2.3.0/24": {
                            "route": "10.2.3.0/24",
                            "active": True,
                            "route_preference": 110,
                            "metric": 2,
                            "source_protocol_codes": "O",
                            "source_protocol": "ospf",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.186.2.2",
                                        "updated": "06:46:59",
                                        "outgoing_interface": "GigabitEthernet0/1",
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.1.2.2",
                                        "updated": "06:46:59",
                                        "outgoing_interface": "GigabitEthernet0/0",
                                    },
                                }
                            },
                        },
                        "10.151.22.22/32": {
                            "route": "10.151.22.22/32",
                            "active": True,
                            "route_preference": 115,
                            "metric": 20,
                            "source_protocol_codes": "i L1",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.186.2.2",
                                        "updated": "06:47:04",
                                        "outgoing_interface": "GigabitEthernet0/1",
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.1.2.2",
                                        "updated": "06:47:04",
                                        "outgoing_interface": "GigabitEthernet0/0",
                                    },
                                }
                            },
                        },
                        "10.16.32.32/32": {
                            "route": "10.16.32.32/32",
                            "active": True,
                            "route_preference": 200,
                            "metric": 0,
                            "source_protocol_codes": "B",
                            "source_protocol": "bgp",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.66.12.12",
                                        "updated": "1d00h",
                                    }
                                }
                            },
                        },
                    }
                }
            }
        }
    }
}
