expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.121.65.0/24": {
                            "active": True,
                            "candidate_default": False,
                            "date": "7w0d",
                            "metric": 20,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.121.64.35",
                                        "outgoing_interface_name": "inside",
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.121.64.34",
                                        "outgoing_interface_name": "inside",
                                    },
                                }
                            },
                            "route": "10.121.65.0/24",
                            "route_preference": 110,
                            "source_protocol": "ospf",
                            "source_protocol_codes": "O",
                        },
                        "10.121.67.0/24": {
                            "active": True,
                            "candidate_default": False,
                            "date": "2w1d",
                            "metric": 345856,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.9.193.99",
                                        "outgoing_interface_name": "esavpn",
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.9.193.98",
                                        "outgoing_interface_name": "esavpn",
                                    },
                                }
                            },
                            "route": "10.121.67.0/24",
                            "route_preference": 170,
                            "source_protocol": "eigrp",
                            "source_protocol_codes": "EX",
                        },
                        "10.121.68.0/24": {
                            "active": True,
                            "candidate_default": False,
                            "date": "2w1d",
                            "metric": 345856,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.9.193.99",
                                        "outgoing_interface_name": "esavpn",
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.9.193.98",
                                        "outgoing_interface_name": "esavpn",
                                    },
                                }
                            },
                            "route": "10.121.68.0/24",
                            "route_preference": 170,
                            "source_protocol": "eigrp",
                            "source_protocol_codes": "EX",
                        },
                        "10.121.69.0/24": {
                            "active": True,
                            "candidate_default": False,
                            "date": "7w0d",
                            "metric": 20,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.121.64.35",
                                        "outgoing_interface_name": "inside",
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.121.64.34",
                                        "outgoing_interface_name": "inside",
                                    },
                                }
                            },
                            "route": "10.121.69.0/24",
                            "route_preference": 110,
                            "source_protocol": "ospf",
                            "source_protocol_codes": "O",
                        },
                        "10.121.70.0/24": {
                            "active": True,
                            "candidate_default": False,
                            "date": "2w1d",
                            "metric": 345856,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.9.193.99",
                                        "outgoing_interface_name": "esavpn",
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.9.193.98",
                                        "outgoing_interface_name": "esavpn",
                                    },
                                }
                            },
                            "route": "10.121.70.0/24",
                            "route_preference": 170,
                            "source_protocol": "eigrp",
                            "source_protocol_codes": "EX",
                        },
                        "10.121.71.0/24": {
                            "active": True,
                            "candidate_default": False,
                            "date": "2w1d",
                            "metric": 345856,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.9.193.99",
                                        "outgoing_interface_name": "esavpn",
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.9.193.98",
                                        "outgoing_interface_name": "esavpn",
                                    },
                                }
                            },
                            "route": "10.121.71.0/24",
                            "route_preference": 170,
                            "source_protocol": "eigrp",
                            "source_protocol_codes": "EX",
                        },
                    }
                }
            }
        }
    }
}
