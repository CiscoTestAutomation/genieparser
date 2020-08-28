expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "rip": {
                            "routes": {
                                "10.0.0.0/8": {
                                    "index": {1: {"summary_type": "auto-summary"}}
                                },
                                "10.1.2.0/24": {
                                    "index": {
                                        1: {
                                            "route_type": "connected",
                                            "interface": "GigabitEthernet2.200",
                                        }
                                    }
                                },
                                "10.1.3.0/24": {
                                    "index": {
                                        1: {
                                            "route_type": "connected",
                                            "interface": "GigabitEthernet3.200",
                                        }
                                    }
                                },
                                "10.2.3.0/24": {
                                    "index": {
                                        1: {
                                            "next_hop": "10.1.2.2",
                                            "expire_time": "00:00:08",
                                            "interface": "GigabitEthernet2.200",
                                            "metric": 1,
                                        }
                                    }
                                },
                                "172.16.0.0/16": {
                                    "index": {1: {"summary_type": "auto-summary"}}
                                },
                                "172.16.11.0/24": {
                                    "index": {
                                        1: {
                                            "redistributed": True,
                                            "metric": 15,
                                            "next_hop": "0.0.0.0",
                                        }
                                    }
                                },
                                "172.16.22.0/24": {
                                    "index": {
                                        1: {
                                            "expire_time": "00:00:08",
                                            "interface": "GigabitEthernet2.200",
                                            "metric": 15,
                                            "next_hop": "10.1.2.2",
                                        }
                                    }
                                },
                                "192.168.1.0/24": {
                                    "index": {1: {"summary_type": "auto-summary"}}
                                },
                                "192.168.1.1/32": {
                                    "index": {
                                        1: {
                                            "redistributed": True,
                                            "metric": 1,
                                            "next_hop": "0.0.0.0",
                                        }
                                    }
                                },
                            }
                        }
                    }
                }
            }
        }
    }
}
