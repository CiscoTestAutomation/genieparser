expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "0.0.0.0/0": {
                            "active": True,
                            "candidate_default": True,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.16.251.1",
                                        "outgoing_interface_name": "outside",
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.16.251.2",
                                        "outgoing_interface_name": "pod1000",
                                    },
                                }
                            },
                            "route": "0.0.0.0/0",
                            "route_preference": 10,
                            "source_protocol": "static",
                            "source_protocol_codes": "S",
                        },
                        "0.0.0.1/0": {
                            "active": True,
                            "candidate_default": False,
                            "metric": 5,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.16.255.1",
                                        "outgoing_interface_name": "outside",
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.16.255.2",
                                        "outgoing_interface_name": "pod1001",
                                    },
                                    3: {
                                        "index": 3,
                                        "next_hop": "10.16.255.3",
                                        "outgoing_interface_name": "pod1002",
                                    },
                                }
                            },
                            "route": "0.0.0.1/0",
                            "route_preference": 10,
                            "source_protocol": "static",
                            "source_protocol_codes": "S",
                        },
                        "10.0.0.0/24": {
                            "active": True,
                            "candidate_default": False,
                            "date": "0:19:52",
                            "metric": 30720,
                            "next_hop": {
                                "outgoing_interface_name": {
                                    "inside": {"outgoing_interface_name": "inside"}
                                }
                            },
                            "route": "10.0.0.0/24",
                            "route_preference": 90,
                            "source_protocol": "eigrp",
                            "source_protocol_codes": "D",
                        },
                        "10.10.1.1/16": {
                            "active": True,
                            "candidate_default": False,
                            "next_hop": {
                                "outgoing_interface_name": {
                                    "_internal_loopback": {
                                        "outgoing_interface_name": "_internal_loopback"
                                    }
                                }
                            },
                            "route": "10.10.1.1/16",
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                        },
                        "10.10.1.2/23": {
                            "active": True,
                            "candidate_default": False,
                            "next_hop": {
                                "outgoing_interface_name": {
                                    "outside": {"outgoing_interface_name": "outside"}
                                }
                            },
                            "route": "10.10.1.2/23",
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                        },
                        "10.10.1.3/32": {
                            "active": True,
                            "candidate_default": False,
                            "next_hop": {
                                "outgoing_interface_name": {
                                    "pod2002": {"outgoing_interface_name": "pod2002"}
                                }
                            },
                            "route": "10.10.1.3/32",
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                        },
                        "10.10.1.4/32": {
                            "active": True,
                            "candidate_default": False,
                            "next_hop": {
                                "outgoing_interface_name": {
                                    "admin": {"outgoing_interface_name": "admin"}
                                }
                            },
                            "route": "10.10.1.4/32",
                            "source_protocol": "vpn",
                            "source_protocol_codes": "V",
                        },
                        "10.10.1.5/32": {
                            "active": True,
                            "candidate_default": False,
                            "next_hop": {
                                "outgoing_interface_name": {
                                    "pod2500": {"outgoing_interface_name": "pod2500"}
                                }
                            },
                            "route": "10.10.1.5/32",
                            "source_protocol": "local",
                            "source_protocol_codes": "L",
                        },
                        "10.10.1.6/24": {
                            "active": True,
                            "candidate_default": False,
                            "next_hop": {
                                "outgoing_interface_name": {
                                    "pod3000": {"outgoing_interface_name": "pod3000"}
                                }
                            },
                            "route": "10.10.1.6/24",
                            "source_protocol": "connected",
                            "source_protocol_codes": "C",
                        },
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
                        "10.122.3.0/24": {
                            "active": True,
                            "candidate_default": False,
                            "date": "7w0d",
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {"index": 1, "next_hop": "172.25.141.2"}
                                }
                            },
                            "route": "10.122.3.0/24",
                            "route_preference": 20,
                            "source_protocol": "bgp",
                            "source_protocol_codes": "B",
                        },
                        "10.20.2.64/26": {
                            "active": True,
                            "candidate_default": False,
                            "date": "2d03h",
                            "metric": 1,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.19.1.1",
                                        "outgoing_interface_name": "wan2",
                                    }
                                }
                            },
                            "route": "10.20.2.64/26",
                            "route_preference": 110,
                            "source_protocol": "ospf",
                            "source_protocol_codes": "E2",
                        },
                        "10.20.58.64/26": {
                            "active": True,
                            "candidate_default": False,
                            "date": "3w6d",
                            "metric": 11,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.192.3",
                                        "outgoing_interface_name": "wan1",
                                    }
                                }
                            },
                            "route": "10.20.58.64/26",
                            "route_preference": 110,
                            "source_protocol": "ospf",
                            "source_protocol_codes": "E2",
                        },
                        "10.30.79.64/26": {
                            "active": True,
                            "candidate_default": False,
                            "date": "1w1d",
                            "metric": 11,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "10.20.192.3",
                                        "outgoing_interface_name": "wan3",
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "10.20.192.4",
                                        "outgoing_interface_name": "wan4",
                                    },
                                }
                            },
                            "route": "10.30.79.64/26",
                            "route_preference": 110,
                            "source_protocol": "ospf",
                            "source_protocol_codes": "E2",
                        },
                        "10.205.8.0/23": {
                            "active": True,
                            "candidate_default": False,
                            "date": "7w0d",
                            "metric": 20,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.20.1.1",
                                        "outgoing_interface_name": "wan5",
                                    }
                                }
                            },
                            "route": "10.205.8.0/23",
                            "route_preference": 110,
                            "source_protocol": "ospf",
                            "source_protocol_codes": "O",
                        },
                    }
                }
            }
        }
    }
}
