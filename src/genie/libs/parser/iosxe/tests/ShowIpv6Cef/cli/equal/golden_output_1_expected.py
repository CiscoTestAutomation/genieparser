expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "prefix": {
                        "::/0": {"nexthop": {"no route": {}}},
                        "::/127": {"nexthop": {"discard": {}}},
                        "2001:DB8:1:2::/64": {
                            "nexthop": {
                                "attached": {
                                    "outgoing_interface": {"GigabitEthernet2.100": {}}
                                }
                            }
                        },
                        "2001:DB8:1:2::1/128": {
                            "nexthop": {
                                "2001:DB8:1:2::1": {
                                    "outgoing_interface": {"GigabitEthernet2.100": {}}
                                }
                            }
                        },
                        "2001:DB8:1:2::2/128": {
                            "nexthop": {
                                "receive": {
                                    "outgoing_interface": {"GigabitEthernet2.100": {}}
                                }
                            }
                        },
                        "2001:DB8:1:3::/64": {
                            "nexthop": {
                                "FE80::F816:3EFF:FE86:1D6D": {
                                    "outgoing_interface": {"GigabitEthernet2.100": {}}
                                },
                                "FE80::F816:3EFF:FEF3:7B32": {
                                    "outgoing_interface": {"GigabitEthernet3.100": {}}
                                },
                            }
                        },
                        "2001:DB8:2:3::/64": {
                            "nexthop": {
                                "attached": {
                                    "outgoing_interface": {"GigabitEthernet3.100": {}}
                                }
                            }
                        },
                        "2001:DB8:64::4:5:0/112": {
                            "nexthop": {
                                "10.2.3.3": {
                                    "outgoing_interface": {
                                        "FastEthernet1/0/0": {
                                            "outgoing_label": ["17", "21"]
                                        }
                                    }
                                }
                            }
                        },
                    }
                }
            }
        }
    }
}
