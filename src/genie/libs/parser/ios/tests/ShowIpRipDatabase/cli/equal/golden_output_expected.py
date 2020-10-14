expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "rip": {
                            "routes": {
                                "0.0.0.0/0": {
                                    "index": {
                                        1: {"summary_type": "auto-summary"},
                                        2: {
                                            "redistributed": True,
                                            "next_hop": "172.16.1.254",
                                            "from": "0.0.0.0",
                                            "metric": 3,
                                        },
                                        3: {
                                            "redistributed": True,
                                            "next_hop": "172.16.1.254",
                                            "from": "0.0.0.0",
                                            "metric": 3,
                                        },
                                    }
                                },
                                "10.0.0.0/8": {
                                    "index": {1: {"summary_type": "auto-summary"}}
                                },
                                "10.1.2.0/24": {
                                    "index": {
                                        1: {
                                            "route_type": "connected",
                                            "interface": "GigabitEthernet2.100",
                                        }
                                    }
                                },
                                "10.1.3.0/24": {
                                    "index": {
                                        1: {
                                            "route_type": "connected",
                                            "interface": "GigabitEthernet3.100",
                                        }
                                    }
                                },
                                "10.2.3.0/24": {
                                    "index": {
                                        1: {
                                            "next_hop": "10.1.3.3",
                                            "expire_time": "00:00:05",
                                            "interface": "GigabitEthernet3.100",
                                            "metric": 1,
                                        },
                                        2: {
                                            "next_hop": "10.1.2.2",
                                            "expire_time": "00:00:21",
                                            "interface": "GigabitEthernet2.100",
                                            "metric": 1,
                                        },
                                    }
                                },
                                "172.16.0.0/16": {
                                    "index": {1: {"summary_type": "auto-summary"}}
                                },
                                "172.16.0.0/17": {
                                    "index": {
                                        1: {"summary_type": "int-summary"},
                                        2: {
                                            "next_hop": "10.1.2.2",
                                            "expire_time": "00:00:00",
                                            "interface": "GigabitEthernet2.100",
                                            "metric": 4,
                                        },
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
