expected_output = {
    "vrf": {
        "h11": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:103::/64": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "outgoing_interface": {
                                    "Ethernet0/0.103": {
                                        "outgoing_interface": "Ethernet0/0.103"
                                    }
                                }
                            },
                            "route": "2001:103::/64",
                            "route_preference": 2,
                            "source_protocol": "nd",
                            "source_protocol_codes": "NDp"
                        },
                        "2001:103::A8BB:1FF:FE03:11/128": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "outgoing_interface": {
                                    "Ethernet0/0.103": {
                                        "outgoing_interface": "Ethernet0/0.103"
                                    }
                                }
                            },
                            "route": "2001:103::A8BB:1FF:FE03:11/128",
                            "route_preference": 0,
                            "source_protocol": "local",
                            "source_protocol_codes": "L"
                        },
                        "2001:103::D1E7:7861:541D:7E5/128": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "outgoing_interface": {
                                    "Ethernet0/0.103": {
                                        "outgoing_interface": "Ethernet0/0.103"
                                    }
                                }
                            },
                            "route": "2001:103::D1E7:7861:541D:7E5/128",
                            "route_preference": 0,
                            "source_protocol": "local_connected",
                            "source_protocol_codes": "LC"
                        },
                        "::/0": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "FE80::A8BB:CCFF:FE83:D2FF",
                                        "outgoing_interface": "Ethernet0/0.103"
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "FE80::A8BB:CCFF:FE03:7500",
                                        "outgoing_interface": "Ethernet0/0.103"
                                    }
                                }
                            },
                            "route": "::/0",
                            "route_preference": 2,
                            "source_protocol": "nd",
                            "source_protocol_codes": "ND"
                        },
                        "FF00::/8": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "outgoing_interface": {
                                    "Null0": {
                                        "outgoing_interface": "Null0"
                                    }
                                }
                            },
                            "route": "FF00::/8",
                            "route_preference": 0,
                            "source_protocol": "local",
                            "source_protocol_codes": "L"
                        }
                    }
                }
            }
        }
    }
}
