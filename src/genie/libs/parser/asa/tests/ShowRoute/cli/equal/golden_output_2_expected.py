expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "10.121.65.0/24": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "date": "7w0d",
                                "route": "10.121.65.0/24",
                                "source_protocol_codes": "O",
                                "source_protocol": "ospf",
                                "metric": 20,
                                "route_preference": 110,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.121.64.35",
                                            "outgoing_interface_name": "inside"
                                        },
                                        2: {
                                            "index": 2,
                                            "next_hop": "10.121.64.34",
                                            "outgoing_interface_name": "inside"
                                        }
                                    }
                                }
                            }
                        },
                        "10.121.67.0/24": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "date": "2w1d",
                                "route": "10.121.67.0/24",
                                "source_protocol_codes": "EX",
                                "source_protocol": "eigrp",
                                "metric": 345856,
                                "route_preference": 170,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.9.193.99",
                                            "outgoing_interface_name": "esavpn"
                                        },
                                        2: {
                                            "index": 2,
                                            "next_hop": "10.9.193.98",
                                            "outgoing_interface_name": "esavpn"
                                        }
                                    }
                                }
                            }
                        },
                        "10.121.68.0/24": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "date": "2w1d",
                                "route": "10.121.68.0/24",
                                "source_protocol_codes": "EX",
                                "source_protocol": "eigrp",
                                "metric": 345856,
                                "route_preference": 170,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.9.193.99",
                                            "outgoing_interface_name": "esavpn"
                                        },
                                        2: {
                                            "index": 2,
                                            "next_hop": "10.9.193.98",
                                            "outgoing_interface_name": "esavpn"
                                        }
                                    }
                                }
                            }
                        },
                        "10.121.69.0/24": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "date": "7w0d",
                                "route": "10.121.69.0/24",
                                "source_protocol_codes": "O",
                                "source_protocol": "ospf",
                                "metric": 20,
                                "route_preference": 110,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.121.64.35",
                                            "outgoing_interface_name": "inside"
                                        },
                                        2: {
                                            "index": 2,
                                            "next_hop": "10.121.64.34",
                                            "outgoing_interface_name": "inside"
                                        }
                                    }
                                }
                            }
                        },
                        "10.121.70.0/24": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "date": "2w1d",
                                "route": "10.121.70.0/24",
                                "source_protocol_codes": "EX",
                                "source_protocol": "eigrp",
                                "metric": 345856,
                                "route_preference": 170,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.9.193.99",
                                            "outgoing_interface_name": "esavpn"
                                        },
                                        2: {
                                            "index": 2,
                                            "next_hop": "10.9.193.98",
                                            "outgoing_interface_name": "esavpn"
                                        }
                                    }
                                }
                            }
                        },
                        "10.121.71.0/24": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "date": "2w1d",
                                "route": "10.121.71.0/24",
                                "source_protocol_codes": "EX",
                                "source_protocol": "eigrp",
                                "metric": 345856,
                                "route_preference": 170,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.9.193.99",
                                            "outgoing_interface_name": "esavpn"
                                        },
                                        2: {
                                            "index": 2,
                                            "next_hop": "10.9.193.98",
                                            "outgoing_interface_name": "esavpn"
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
}