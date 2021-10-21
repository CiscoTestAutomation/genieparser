expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.34.0.1/32": {
                            "route": "10.34.0.1/32",
                            "active": True,
                            "metric": 0,
                            "route_preference": 1,
                            "source_protocol_codes": "S %",
                            "source_protocol": "static",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "192.168.16.1"
                                    }
                                }
                            }
                        },
                        "10.34.0.2/32": {
                            "route": "10.34.0.2/32",
                            "active": True,
                            "source_protocol_codes": "C p",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Loopback0": {
                                        "outgoing_interface": "Loopback0"
                                    }
                                }
                            }
                        },
                        "10.69.0.0/16": {
                            "route": "10.69.0.0/16",
                            "active": True,
                            "metric": 0,
                            "route_preference": 1,
                            "source_protocol_codes": "S &",
                            "source_protocol": "static",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.34.0.1"
                                    }
                                }
                            }
                        },
                        "10.186.1.0/24": {
                            "route": "10.186.1.0/24",
                            "active": True,
                            "metric": 0,
                            "route_preference": 1,
                            "source_protocol_codes": "S +",
                            "source_protocol": "static",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.144.0.1",
                                        "vrf": "red"
                                    }
                                }
                            }
                        },
                        "192.168.16.0/24": {
                            "route": "192.168.16.0/24",
                            "active": True,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Ethernet0/1": {
                                        "outgoing_interface": "Ethernet0/1"
                                    }
                                }
                            }
                        },
                        "192.168.16.2/32": {
                            "route": "192.168.16.2/32",
                            "active": True,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Ethernet0/1": {
                                        "outgoing_interface": "Ethernet0/1"
                                    }
                                }
                            }
                        },
                        "10.55.0.0/24": {
                            "route": "10.55.0.0/24",
                            "active": True,
                            "metric": 0,
                            "route_preference": 20,
                            "source_protocol_codes": "B +",
                            "source_protocol": "bgp",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.144.0.1",
                                        "updated": "00:00:09",
                                        "vrf": "red"
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