expected_output = {
    "slot": {
        "1": {
            "ip_version": {
                "IPv4": {
                    "route_table": {
                        "default/base": {
                            "prefix": {
                                "1.1.1.1/32": {
                                    "next_hop": {
                                        "1.1.1.1": {
                                            "interface": "loopback0",
                                            "is_best": True
                                        }
                                    }
                                },
                                "1.1.1.2/32": {
                                    "next_hop": {
                                        "1.1.1.2": {
                                            "interface": "loopback1",
                                            "is_best": False
                                        }
                                    }
                                },
                                "2.2.2.2/32": {
                                    "next_hop": {
                                        "fe80::a111:2222:3333:e11": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False
                                        }
                                    }
                                },
                                "3.3.3.2/32": {
                                    "next_hop": {
                                        "fe80::a111:2222:3333:e11": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False
                                        }
                                    }
                                },
                                "4.4.4.2/32": {
                                    "next_hop": {
                                        "fe80::a111:2222:3333:e11": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False
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