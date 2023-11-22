expected_output = {
    "vrf": {
        "Red": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:192:168:2::/64": {
                            "route": "2001:192:168:2::/64",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Vlan11": {
                                        "outgoing_interface": "Vlan11"
                                    }
                                }
                            }
                        },
                        "2001:192:168:2::1/128": {
                            "route": "2001:192:168:2::1/128",
                            "active": True,
                            "metric": 0,
                            "route_preference": 20,
                            "source_protocol_codes": "B",
                            "source_protocol": "bgp",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "33.33.33.33",
                                        "outgoing_interface": "Vlan100",
                                        "vrf": "default"
                                    }
                                }
                            }
                        },
                        "2001:192:168:2::100/128": {
                            "route": "2001:192:168:2::100/128",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Vlan11": {
                                        "outgoing_interface": "Vlan11"
                                    }
                                }
                            }
                        },
                        "2001:192:168:255::/64": {
                            "route": "2001:192:168:255::/64",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Vlan4000": {
                                        "outgoing_interface": "Vlan4000"
                                    }
                                }
                            }
                        },
                        "2001:192:168:255::1/128": {
                            "route": "2001:192:168:255::1/128",
                            "active": True,
                            "metric": 0,
                            "route_preference": 20,
                            "source_protocol_codes": "B",
                            "source_protocol": "bgp",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "33.33.33.33",
                                        "outgoing_interface": "Vlan100",
                                        "vrf": "default"
                                    }
                                }
                            }
                        },
                        "2001:192:168:255::100/128": {
                            "route": "2001:192:168:255::100/128",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Vlan4000": {
                                        "outgoing_interface": "Vlan4000"
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