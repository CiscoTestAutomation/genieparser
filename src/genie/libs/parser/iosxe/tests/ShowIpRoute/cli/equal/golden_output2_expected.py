expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.0.0.0/24": {
                            "route": "10.0.0.0/24",
                            "active": True,
                            "route_preference": 110,
                            "metric": 1,
                            "source_protocol_codes": "O",
                            "source_protocol": "ospf",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.81.1.2",
                                        "updated": "01:02:20",
                                        "outgoing_interface": "GigabitEthernet0/0/2.100",
                                    }
                                }
                            },
                        },
                        "10.0.1.0/24": {
                            "route": "10.0.1.0/24",
                            "active": True,
                            "route_preference": 110,
                            "metric": 1,
                            "source_protocol_codes": "O",
                            "source_protocol": "ospf",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.81.1.2",
                                        "updated": "01:02:20",
                                        "outgoing_interface": "GigabitEthernet0/0/2.100",
                                    }
                                }
                            },
                        },
                        "10.0.2.0/24": {
                            "route": "10.0.2.0/24",
                            "active": True,
                            "route_preference": 110,
                            "metric": 1,
                            "source_protocol_codes": "O",
                            "source_protocol": "ospf",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.81.1.2",
                                        "updated": "01:02:20",
                                        "outgoing_interface": "GigabitEthernet0/0/2.100",
                                    }
                                }
                            },
                        },
                        "10.145.0.0/24": {
                            "route": "10.145.0.0/24",
                            "active": True,
                            "route_preference": 200,
                            "metric": 1,
                            "source_protocol_codes": "B",
                            "source_protocol": "bgp",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "192.168.51.1",
                                        "updated": "01:01:10",
                                    }
                                }
                            },
                        },
                        "10.145.1.0/24": {
                            "route": "10.145.1.0/24",
                            "active": True,
                            "route_preference": 200,
                            "metric": 1,
                            "source_protocol_codes": "B",
                            "source_protocol": "bgp",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "192.168.51.1",
                                        "updated": "01:01:10",
                                    }
                                }
                            },
                        },
                        "10.145.2.0/24": {
                            "route": "10.145.2.0/24",
                            "active": True,
                            "route_preference": 200,
                            "metric": 1,
                            "source_protocol_codes": "B",
                            "source_protocol": "bgp",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "192.168.51.1",
                                        "updated": "01:01:10",
                                    }
                                }
                            },
                        },
                        "10.81.1.0/24": {
                            "route": "10.81.1.0/24",
                            "active": True,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0/2.100": {
                                        "outgoing_interface": "GigabitEthernet0/0/2.100"
                                    }
                                }
                            },
                        },
                        "10.81.1.1/32": {
                            "route": "10.81.1.1/32",
                            "active": True,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0/2.100": {
                                        "outgoing_interface": "GigabitEthernet0/0/2.100"
                                    }
                                }
                            },
                        },
                        "192.168.4.0/24": {
                            "route": "192.168.4.0/24",
                            "active": True,
                            "route_preference": 200,
                            "metric": 0,
                            "source_protocol_codes": "B",
                            "source_protocol": "bgp",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "192.168.51.1",
                                        "updated": "01:01:10",
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
