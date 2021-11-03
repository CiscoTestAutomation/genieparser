expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "0.0.0.0/0": {
                            1: {
                                "index": 1,
                                "candidate_default": True,
                                "active": True,
                                "route": "0.0.0.0/0",
                                "source_protocol_codes": "S",
                                "source_protocol": "static",
                                "route_preference": 10,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.16.251.1",
                                            "outgoing_interface_name": "outside"
                                        },
                                        2: {
                                            "index": 2,
                                            "next_hop": "10.16.251.2",
                                            "outgoing_interface_name": "pod1000"
                                        }
                                    }
                                }
                            }
                        },
                        "0.0.0.1/0": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "route": "0.0.0.1/0",
                                "source_protocol_codes": "S",
                                "source_protocol": "static",
                                "metric": 5,
                                "route_preference": 10,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.16.255.1",
                                            "outgoing_interface_name": "outside"
                                        },
                                        2: {
                                            "index": 2,
                                            "next_hop": "10.16.255.2",
                                            "outgoing_interface_name": "pod1001"
                                        },
                                        "3": {
                                            "index": 3,
                                            "next_hop": "10.16.255.3",
                                            "outgoing_interface_name": "pod1002"
                                        }
                                    }
                                }
                            }
                        },
                        "10.10.1.1/16": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "route": "10.10.1.1/16",
                                "source_protocol_codes": "C",
                                "source_protocol": "connected",
                                "next_hop": {
                                    "outgoing_interface_name": {
                                        "_internal_loopback": {
                                            "outgoing_interface_name": "_internal_loopback"
                                        }
                                    }
                                }
                            }
                        },
                        "10.10.1.2/23": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "route": "10.10.1.2/23",
                                "source_protocol_codes": "C",
                                "source_protocol": "connected",
                                "next_hop": {
                                    "outgoing_interface_name": {
                                        "outside": {
                                            "outgoing_interface_name": "outside"
                                        }
                                    }
                                }
                            }
                        },
                        "10.122.3.0/24": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "date": "7w0d",
                                "route": "10.122.3.0/24",
                                "source_protocol_codes": "B",
                                "source_protocol": "bgp",
                                "metric": 0,
                                "route_preference": 20,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.25.141.2"
                                        }
                                    }
                                }
                            }
                        },
                        "10.10.1.3/32": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "route": "10.10.1.3/32",
                                "source_protocol_codes": "L",
                                "source_protocol": "local",
                                "next_hop": {
                                    "outgoing_interface_name": {
                                        "pod2002": {
                                            "outgoing_interface_name": "pod2002"
                                        }
                                    }
                                }
                            }
                        },
                        "10.10.1.4/32": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "route": "10.10.1.4/32",
                                "source_protocol_codes": "V",
                                "source_protocol": "vpn",
                                "next_hop": {
                                    "outgoing_interface_name": {
                                        "admin": {
                                            "outgoing_interface_name": "admin"
                                        }
                                    }
                                }
                            }
                        },
                        "10.10.1.5/32": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "route": "10.10.1.5/32",
                                "source_protocol_codes": "L",
                                "source_protocol": "local",
                                "next_hop": {
                                    "outgoing_interface_name": {
                                        "pod2500": {
                                            "outgoing_interface_name": "pod2500"
                                        }
                                    }
                                }
                            }
                        },
                        "10.10.1.6/24": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "route": "10.10.1.6/24",
                                "source_protocol_codes": "C",
                                "source_protocol": "connected",
                                "next_hop": {
                                    "outgoing_interface_name": {
                                        "pod3000": {
                                            "outgoing_interface_name": "pod3000"
                                        }
                                    }
                                }
                            }
                        },
                        "10.20.58.64/26": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "date": "3w6d",
                                "route": "10.20.58.64/26",
                                "source_protocol_codes": "E2",
                                "source_protocol": "ospf",
                                "metric": 11,
                                "route_preference": 110,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.20.192.3",
                                            "outgoing_interface_name": "wan1"
                                        }
                                    }
                                }
                            }
                        },
                        "10.20.2.64/26": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "date": "2d03h",
                                "route": "10.20.2.64/26",
                                "source_protocol_codes": "E2",
                                "source_protocol": "ospf",
                                "metric": 1,
                                "route_preference": 110,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.19.1.1",
                                            "outgoing_interface_name": "wan2"
                                        }
                                    }
                                }
                            }
                        },
                        "10.30.79.64/26": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "date": "1w1d",
                                "route": "10.30.79.64/26",
                                "source_protocol_codes": "E2",
                                "source_protocol": "ospf",
                                "metric": 11,
                                "route_preference": 110,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "10.20.192.3",
                                            "outgoing_interface_name": "wan3"
                                        },
                                        2: {
                                            "index": 2,
                                            "next_hop": "10.20.192.4",
                                            "outgoing_interface_name": "wan4"
                                        }
                                    }
                                }
                            }
                        },
                        "10.205.8.0/23": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "date": "7w0d",
                                "route": "10.205.8.0/23",
                                "source_protocol_codes": "O",
                                "source_protocol": "ospf",
                                "metric": 20,
                                "route_preference": 110,
                                "next_hop": {
                                    "next_hop_list": {
                                        1: {
                                            "index": 1,
                                            "next_hop": "172.20.1.1",
                                            "outgoing_interface_name": "wan5"
                                        }
                                    }
                                }
                            }
                        },
                        "10.0.0.0/24": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "date": "0:19:52",
                                "route": "10.0.0.0/24",
                                "source_protocol_codes": "D",
                                "source_protocol": "eigrp",
                                "metric": 30720,
                                "route_preference": 90,
                                "next_hop": {
                                    "outgoing_interface_name": {
                                        "inside": {
                                            "outgoing_interface_name": "inside"
                                        }
                                    }
                                }
                            }
                        },
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
                        },
                        "10.121.0.0/8": {
                            1: {
                                "index": 1,
                                "candidate_default": False,
                                "active": True,
                                "route": "10.121.0.0/8",
                                "source_protocol_codes": "SI",
                                "source_protocol": "static intervrf",
                                "metric": 0,
                                "route_preference": 1,
                                "next_hop": {
                                    "outgoing_interface_name": {
                                        "gig3": {
                                            "outgoing_interface_name": "gig3"
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