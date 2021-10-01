expected_output = {
    "vrf": {
        "Red": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:192:168:2::/64": {
                            "route": "2001:192:168:2::/64",
                            "active": true,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Vlan11,": {
                                        "outgoing_interface": "Vlan11,"
                                    }
                                }
                            }
                        },
                        "2001:192:168:2::1/128": {
                            "route": "2001:192:168:2::1/128",
                            "active": true,
                            "metric": 0,
                            "route_preference": 20,
                            "source_protocol_codes": "B",
                            "source_protocol": "bgp",
                            "next_hop": {
                                "next_hop_list": {
                                    "1": {
                                        "index": 1,
                                        "next_hop": "33.33.33.33",
                                        "outgoing_interface": "Vlan100%default",
                                        "vrf": "default"
                                    }
                                }
                            }
                        },
                        "2001:192:168:2::100/128": {
                            "route": "2001:192:168:2::100/128",
                            "active": true,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {}
                        },
                        "an11": {
                            "route": "an11",
                            "active": true,
                            "source_protocol_codes": "via Vl",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "receive": {
                                        "outgoing_interface": "receive"
                                    }
                                }
                            }
                        },
                        "2001:192:168:255::/64": {
                            "route": "2001:192:168:255::/64",
                            "active": true,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Vlan4000,": {
                                        "outgoing_interface": "Vlan4000,"
                                    }
                                }
                            }
                        },
                        "2001:192:168:255::1/128": {
                            "route": "2001:192:168:255::1/128",
                            "active": true,
                            "metric": 0,
                            "route_preference": 20,
                            "source_protocol_codes": "B",
                            "source_protocol": "bgp",
                            "next_hop": {
                                "next_hop_list": {
                                    "1": {
                                        "index": 1,
                                        "next_hop": "33.33.33.33",
                                        "outgoing_interface": "Vlan100%default",
                                        "vrf": "default"
                                    }
                                }
                            }
                        },
                        "2001:192:168:255::100/128": {
                            "route": "2001:192:168:255::100/128",
                            "active": true,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {}
                        },
                        "an4000": {
                            "route": "an4000",
                            "active": true,
                            "source_protocol_codes": "via Vl",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "receive": {
                                        "outgoing_interface": "receive"
                                    }
                                }
                            }
                        },
                        "FF00::/8": {
                            "route": "FF00::/8",
                            "active": true,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {}
                        },
                        "ll0": {
                            "route": "ll0",
                            "active": true,
                            "source_protocol_codes": "via Nu",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "receive": {
                                        "outgoing_interface": "receive"
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