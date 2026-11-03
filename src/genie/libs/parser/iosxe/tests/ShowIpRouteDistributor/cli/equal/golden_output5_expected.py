expected_output = {
    "vrf": {
        "vrf-a": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.1.1.0/24": {
                            "route": "10.1.1.0/24",
                            "active": True,
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Ethernet0/0": {
                                        "outgoing_interface": "Ethernet0/0"
                                    }
                                }
                            },
                        },
                        "10.1.1.1/32": {
                            "route": "10.1.1.1/32",
                            "active": True,
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Ethernet0/0": {
                                        "outgoing_interface": "Ethernet0/0"
                                    }
                                }
                            },
                        },
                        "20.1.1.0/24": {
                            "route": "20.1.1.0/24",
                            "active": True,
                            "source_protocol": "connected",
                            "source_protocol_codes": "C +",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Ethernet0/1": {
                                        "outgoing_interface": "Ethernet0/1"
                                    }
                                }
                            },
                        },
                        "20.1.1.1/32": {
                            "route": "20.1.1.1/32",
                            "active": True,
                            "source_protocol": "local",
                            "source_protocol_codes": "L &",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Ethernet0/1": {
                                        "outgoing_interface": "Ethernet0/1"
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
