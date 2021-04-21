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
                    "l4": {"icmp": {"established": False}},
                },
            },
            "20": {
                "name": "20",
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "statistics": {"matched_packets": 67},
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
            "30": {
                "name": "30",
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "object-group dummydpd-local": {
                                    "source_network": "object-group dummydpd-local"
                                }
                            },
                            "destination_network": {
                                "object-group dummydpd-remote": {
                                    "destination_network": "object-group dummydpd-remote"
                                }
                            },
                        }
                    },
                    "l4": {"ipv4": {"established": False}},
                },
            },
        },
    }
}
