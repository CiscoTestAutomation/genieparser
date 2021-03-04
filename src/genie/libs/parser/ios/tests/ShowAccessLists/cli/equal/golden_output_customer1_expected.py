expected_output = {
    "acl1": {
        "name": "acl1",
        "type": "ipv4-acl-type",
        "acl_type": "extended",
        "aces": {
            "10": {
                "name": "10",
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "icmp",
                            "source_network": {"any": {"source_network": "any"}},
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                        }
                    },
                    "l4": {"icmp": {"established": False, "msg_type": "echo"}},
                },
            },
            "20": {
                "name": "20",
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "statistics": {"matched_packets": 1195},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "icmp",
                            "source_network": {"any": {"source_network": "any"}},
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                        }
                    },
                    "l4": {"icmp": {"established": False, "msg_type": "echo-reply"}},
                },
            },
            "30": {
                "name": "30",
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "icmp",
                            "source_network": {"any": {"source_network": "any"}},
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                        }
                    },
                    "l4": {"icmp": {"established": False, "msg_type": "ttl-exceeded"}},
                },
            },
            "40": {
                "name": "40",
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "icmp",
                            "source_network": {"any": {"source_network": "any"}},
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                        }
                    },
                    "l4": {"icmp": {"established": False, "msg_type": "unreachable"}},
                },
            },
            "50": {
                "name": "50",
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "icmp",
                            "source_network": {"any": {"source_network": "any"}},
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                        }
                    },
                    "l4": {
                        "icmp": {"established": False, "msg_type": "packet-too-big"}
                    },
                },
            },
            "60": {
                "name": "60",
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "icmp",
                            "source_network": {"any": {"source_network": "any"}},
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                        }
                    },
                    "l4": {"icmp": {"established": False}},
                },
            },
            "80": {
                "name": "80",
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "udp",
                            "source_network": {"any": {"source_network": "any"}},
                            "destination_network": {
                                "host 10.4.1.1": {
                                    "destination_network": "host 10.4.1.1"
                                }
                            },
                        }
                    },
                    "l4": {
                        "udp": {
                            "established": False,
                            "destination_port": {
                                "operator": {"operator": "eq", "port": 1985}
                            },
                        }
                    },
                },
            },
        },
    }
}
