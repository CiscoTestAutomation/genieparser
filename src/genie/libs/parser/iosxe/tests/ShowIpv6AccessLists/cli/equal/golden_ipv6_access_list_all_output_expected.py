expected_output = {
    "inbound": {
        "aces": {
            "10": {
                "statistics": {"matched_packets": 8},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "tcp",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    },
                    "l4": {
                        "tcp": {
                            "destination_port": {
                                "operator": {"operator": "eq", "port": 179}
                            },
                            "established": False,
                        }
                    },
                },
                "actions": {"logging": "log-none", "forwarding": "permit"},
                "name": "10",
            },
            "30": {
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "udp",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    },
                    "l4": {"udp": {"established": False}},
                },
                "actions": {"logging": "log-none", "forwarding": "permit"},
                "name": "30",
            },
            "20": {
                "statistics": {"matched_packets": 15},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "tcp",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    },
                    "l4": {
                        "tcp": {
                            "destination_port": {
                                "operator": {"operator": "eq", "port": 23}
                            },
                            "established": False,
                        }
                    },
                },
                "actions": {"logging": "log-none", "forwarding": "permit"},
                "name": "20",
            },
        },
        "name": "inbound",
        "type": "ipv6-acl-type",
        "acl_type": "ipv6",
    },
    "Virtual-Access2.1#427819008151": {
        "aces": {
            "1": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "host 2001:DB8:2::32": {
                                    "destination_network": "host 2001:DB8:2::32"
                                }
                            },
                            "protocol": "tcp",
                            "source_network": {
                                "host 2001:DB8:1::32": {
                                    "source_network": "host 2001:DB8:1::32"
                                }
                            },
                        }
                    },
                    "l4": {
                        "tcp": {
                            "destination_port": {
                                "operator": {"operator": "eq", "port": 11000}
                            },
                            "established": False,
                            "source_port": {
                                "operator": {"operator": "eq", "port": "bgp"}
                            },
                        }
                    },
                },
                "name": "1",
            },
            "2": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "host 2001:DB8:2::32": {
                                    "destination_network": "host 2001:DB8:2::32"
                                }
                            },
                            "protocol": "tcp",
                            "source_network": {
                                "host 2001:DB8:1::32": {
                                    "source_network": "host 2001:DB8:1::32"
                                }
                            },
                        }
                    },
                    "l4": {
                        "tcp": {
                            "destination_port": {
                                "operator": {"operator": "eq", "port": 11001}
                            },
                            "established": False,
                            "source_port": {
                                "operator": {"operator": "eq", "port": "telnet"}
                            },
                        }
                    },
                },
                "name": "2",
            },
        },
        "name": "Virtual-Access2.1#427819008151",
        "per_user": True,
        "type": "ipv6-acl-type",
        "acl_type": "ipv6",
    },
}
