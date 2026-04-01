expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "64:FF9B::/96": {
                            "route": "64:FF9B::/96",
                            "active": True,
                            "metric": 0,
                            "route_preference": 1,
                            "source_protocol_codes": "S",
                            "source_protocol": "static",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "::100.0.0.2",
                                        "outgoing_interface": "NVI0"
                                    }
                                }
                            }
                        },
                        "2001:DA8:3::/64": {
                            "route": "2001:DA8:3::/64",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0/4": {
                                        "outgoing_interface": "GigabitEthernet0/0/4"
                                    }
                                }
                            }
                        },
                        "2001:DA8:3::1/128": {
                            "route": "2001:DA8:3::1/128",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0/4": {
                                        "outgoing_interface": "GigabitEthernet0/0/4"
                                    }
                                }
                            }
                        },
                        "2001:DA8:B001::/48": {
                            "route": "2001:DA8:B001::/48",
                            "active": True,
                            "metric": 0,
                            "route_preference": 1,
                            "source_protocol_codes": "S",
                            "source_protocol": "static",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "2001:DA8:3::2"
                                    }
                                }
                            }
                        },
                        "2001:DA8:B001:FFFF::/64": {
                            "route": "2001:DA8:B001:FFFF::/64",
                            "active": True,
                            "metric": 0,
                            "route_preference": 1,
                            "source_protocol_codes": "S",
                            "source_protocol": "static",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "::128.0.1.0",
                                        "outgoing_interface": "NVI0"
                                    }
                                }
                            }
                        },
                        "FF00::/8": {
                            "route": "FF00::/8",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Null0": {
                                        "outgoing_interface": "Null0"
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