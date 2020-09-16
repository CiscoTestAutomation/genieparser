expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "0.0.0.0/0": {
                            "active": True,
                            "metric": 100,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.12.7.37",
                                        "outgoing_interface": "Vlan101",
                                        "updated": "3w6d",
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.12.7.33",
                                        "outgoing_interface": "Vlan100",
                                        "updated": "3w6d",
                                    },
                                }
                            },
                            "route": "0.0.0.0/0",
                            "route_preference": 115,
                            "source_protocol": "isis",
                            "source_protocol_codes": "i*L1",
                        },
                        "10.12.6.1/32": {
                            "active": True,
                            "metric": 200,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.12.7.33",
                                        "outgoing_interface": "Vlan100",
                                        "updated": "1w1d",
                                    }
                                }
                            },
                            "route": "10.12.6.1/32",
                            "route_preference": 115,
                            "source_protocol": "isis",
                            "source_protocol_codes": "i ia",
                        },
                        "10.12.6.10/32": {
                            "active": True,
                            "metric": 200,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.12.7.33",
                                        "outgoing_interface": "Vlan100",
                                        "updated": "2w1d",
                                    }
                                }
                            },
                            "route": "10.12.6.10/32",
                            "route_preference": 115,
                            "source_protocol": "isis",
                            "source_protocol_codes": "i ia",
                        },
                        "10.12.6.13/32": {
                            "active": True,
                            "metric": 250,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.12.7.33",
                                        "outgoing_interface": "Vlan100",
                                        "updated": "2w1d",
                                    }
                                }
                            },
                            "route": "10.12.6.13/32",
                            "route_preference": 115,
                            "source_protocol": "isis",
                            "source_protocol_codes": "i ia",
                        },
                        "10.12.6.14/32": {
                            "active": True,
                            "metric": 300,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.12.7.37",
                                        "outgoing_interface": "Vlan101",
                                        "updated": "2w1d",
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.12.7.33",
                                        "outgoing_interface": "Vlan100",
                                        "updated": "2w1d",
                                    },
                                }
                            },
                            "route": "10.12.6.14/32",
                            "route_preference": 115,
                            "source_protocol": "isis",
                            "source_protocol_codes": "i ia",
                        },
                        "10.12.6.15/32": {
                            "active": True,
                            "metric": 250,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.12.7.37",
                                        "outgoing_interface": "Vlan101",
                                        "updated": "2w1d",
                                    }
                                }
                            },
                            "route": "10.12.6.15/32",
                            "route_preference": 115,
                            "source_protocol": "isis",
                            "source_protocol_codes": "i ia",
                        },
                        "10.12.6.2/32": {
                            "active": True,
                            "metric": 100,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.12.7.33",
                                        "outgoing_interface": "Vlan100",
                                        "updated": "6w0d",
                                    }
                                }
                            },
                            "route": "10.12.6.2/32",
                            "route_preference": 115,
                            "source_protocol": "isis",
                            "source_protocol_codes": "i L1",
                        },
                        "10.12.6.3/32": {
                            "active": True,
                            "metric": 100,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.12.7.37",
                                        "outgoing_interface": "Vlan101",
                                        "updated": "3w6d",
                                    }
                                }
                            },
                            "route": "10.12.6.3/32",
                            "route_preference": 115,
                            "source_protocol": "isis",
                            "source_protocol_codes": "i L1",
                        },
                        "10.12.6.4/32": {
                            "active": True,
                            "metric": 50,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.12.7.33",
                                        "outgoing_interface": "Vlan100",
                                        "updated": "6w0d",
                                    }
                                }
                            },
                            "route": "10.12.6.4/32",
                            "route_preference": 115,
                            "source_protocol": "isis",
                            "source_protocol_codes": "i L1",
                        },
                        "10.12.6.7/32": {
                            "active": True,
                            "metric": 50,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.12.7.37",
                                        "outgoing_interface": "Vlan101",
                                        "updated": "3w6d",
                                    }
                                }
                            },
                            "route": "10.12.6.7/32",
                            "route_preference": 115,
                            "source_protocol": "isis",
                            "source_protocol_codes": "i L1",
                        },
                        "10.12.6.9/32": {
                            "active": True,
                            "next_hop": {
                                "outgoing_interface": {
                                    "Loopback0": {"outgoing_interface": "Loopback0"}
                                }
                            },
                            "route": "10.12.6.9/32",
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                        },
                        "10.12.7.32/30": {
                            "active": True,
                            "next_hop": {
                                "outgoing_interface": {
                                    "Vlan100": {"outgoing_interface": "Vlan100"}
                                }
                            },
                            "route": "10.12.7.32/30",
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                        },
                        "10.12.7.34/32": {
                            "active": True,
                            "next_hop": {
                                "outgoing_interface": {
                                    "Vlan100": {"outgoing_interface": "Vlan100"}
                                }
                            },
                            "route": "10.12.7.34/32",
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                        },
                        "10.12.7.36/30": {
                            "active": True,
                            "next_hop": {
                                "outgoing_interface": {
                                    "Vlan101": {"outgoing_interface": "Vlan101"}
                                }
                            },
                            "route": "10.12.7.36/30",
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                        },
                        "10.12.7.38/32": {
                            "active": True,
                            "next_hop": {
                                "outgoing_interface": {
                                    "Vlan101": {"outgoing_interface": "Vlan101"}
                                }
                            },
                            "route": "10.12.7.38/32",
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                        },
                    }
                }
            }
        }
    }
}
