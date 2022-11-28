expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "0.0.0.0/0": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "outgoing_interface": {
                                    "Null0": {"outgoing_interface": "Null0"}
                                }
                            },
                            "route": "0.0.0.0/0",
                            "route_preference": 6,
                            "source_protocol": "nat_dia",
                            "source_protocol_codes": "n*Nd",
                        },
                        "10.0.1.0/24": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.10",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:14:21",
                                    }
                                }
                            },
                            "route": "10.0.1.0/24",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                        "10.1.3.0/24": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.10",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:14:21",
                                    }
                                }
                            },
                            "route": "10.1.3.0/24",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                        "10.1.4.0/24": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.9",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:14:21",
                                    }
                                }
                            },
                            "route": "10.1.4.0/24",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                        "10.128.0.0/16": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.10",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:14:21",
                                    }
                                }
                            },
                            "route": "10.128.0.0/16",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                        "10.129.0.0/16": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.10",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:14:21",
                                    }
                                }
                            },
                            "route": "10.129.0.0/16",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                        "10.130.0.0/16": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.10",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:14:21",
                                    }
                                }
                            },
                            "route": "10.130.0.0/16",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                        "10.131.0.0/16": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.10",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:14:21",
                                    }
                                }
                            },
                            "route": "10.131.0.0/16",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                        "10.132.0.0/16": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.10",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:14:21",
                                    }
                                }
                            },
                            "route": "10.132.0.0/16",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                        "10.133.0.0/16": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.10",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:14:21",
                                    }
                                }
                            },
                            "route": "10.133.0.0/16",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                        "10.140.0.0/16": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.10",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:14:21",
                                    }
                                }
                            },
                            "route": "10.140.0.0/16",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                        "10.145.0.0/16": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.10",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:14:21",
                                    }
                                }
                            },
                            "route": "10.145.0.0/16",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                        "10.146.2.0/24": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.7",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:14:21",
                                    }
                                }
                            },
                            "route": "10.146.2.0/24",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                        "10.147.0.0/24": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.7",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:14:21",
                                    }
                                }
                            },
                            "route": "10.147.0.0/24",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                        "10.147.1.0/24": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.7",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:14:21",
                                    }
                                }
                            },
                            "route": "10.147.1.0/24",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                        "10.151.99.0/24": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.10",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:14:21",
                                    }
                                }
                            },
                            "route": "10.151.99.0/24",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                        "10.166.0.0/24": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.30.1.10",
                                        "outgoing_interface": "Sdwan-system-intf",
                                        "updated": "04:13:21",
                                    }
                                }
                            },
                            "route": "10.166.0.0/24",
                            "route_preference": 251,
                            "source_protocol": "omp",
                            "source_protocol_codes": "m",
                        },
                    }
                }
            }
        }
    }
}
