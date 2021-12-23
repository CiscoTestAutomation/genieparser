expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "0.0.0.0/0": {
                            "candidate_default": True,
                            "active": True,
                            "route": "0.0.0.0/0",
                            "source_protocol_codes": "S",
                            "source_protocol": "static",
                            "metric": 0,
                            "route_preference": 1,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "192.2.0.1",
                                        "outgoing_interface_name": "Outside-Port-Channel"
                                    }
                                }
                            }
                        },
                        "1.1.1.0/24": {
                            "candidate_default": False,
                            "active": True,
                            "date": "2d19h",
                            "route": "1.1.1.0/24",
                            "source_protocol_codes": "B",
                            "source_protocol": "bgp",
                            "metric": 0,
                            "route_preference": 20,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.98.126.1"
                                    }
                                }
                            }
                        },
                        "4.33.104.119/32": {
                            "candidate_default": False,
                            "active": True,
                            "date": "2d19h",
                            "route": "4.33.104.119/32",
                            "source_protocol_codes": "B",
                            "source_protocol": "bgp",
                            "metric": 0,
                            "route_preference": 20,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.98.126.1"
                                    }
                                }
                            }
                        },
                    },
                    "tunneled_routes": {
                        "0.0.0.0/0": {
                            "candidate_default": False,
                            "active": True,
                            "route": "0.0.0.0/0",
                            "source_protocol_codes": "S",
                            "source_protocol": "static",
                            "metric": 0,
                            "route_preference": 255,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.98.126.1",
                                        "outgoing_interface_name": "Inside-Port-Channel"
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