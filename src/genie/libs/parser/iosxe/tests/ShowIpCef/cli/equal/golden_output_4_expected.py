expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "0.0.0.0/0": {
                            "nexthop": {
                                "10.1.2.1": {
                                    "outgoing_interface": {"GigabitEthernet2.100": {}}
                                }
                            }
                        },
                        "0.0.0.0/8": {"nexthop": {"drop": {}}},
                        "0.0.0.0/32": {"nexthop": {"receive": {}}},
                        "10.1.2.0/24": {
                            "nexthop": {
                                "attached": {
                                    "outgoing_interface": {"GigabitEthernet2.100": {}}
                                }
                            }
                        },
                        "10.1.2.0/32": {
                            "nexthop": {
                                "receive": {
                                    "outgoing_interface": {"GigabitEthernet2.100": {}}
                                }
                            }
                        },
                        "10.1.2.1/32": {
                            "nexthop": {
                                "attached": {
                                    "outgoing_interface": {"GigabitEthernet2.100": {}}
                                }
                            }
                        },
                        "10.1.2.2/32": {
                            "nexthop": {
                                "receive": {
                                    "outgoing_interface": {"GigabitEthernet2.100": {}}
                                }
                            }
                        },
                        "10.1.2.255/32": {
                            "nexthop": {
                                "receive": {
                                    "outgoing_interface": {"GigabitEthernet2.100": {}}
                                }
                            }
                        },
                        "10.1.3.0/24": {
                            "nexthop": {
                                "10.1.2.1": {
                                    "outgoing_interface": {"GigabitEthernet2.100": {}}
                                },
                                "10.2.3.3": {
                                    "outgoing_interface": {"GigabitEthernet3.100": {}}
                                },
                            }
                        },
                        "10.2.3.0/24": {
                            "nexthop": {
                                "attached": {
                                    "outgoing_interface": {"GigabitEthernet3.100": {}}
                                }
                            }
                        },
                    }
                }
            }
        }
    }
}
