expected_output = {
    "43": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit"},
                "statistics": {"matched_packets": 1168716},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "10.1.0.2 0.0.0.0": {
                                    "source_network": "10.1.0.2 0.0.0.0"
                                }
                            },
                        }
                    }
                },
                "name": "10",
            },
            "20": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "10.144.0.9 0.0.0.0": {
                                    "source_network": "10.144.0.9 0.0.0.0"
                                }
                            },
                        }
                    }
                },
                "name": "20",
            },
            "30": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "10.70.10.0 0.0.10.255": {
                                    "source_network": "10.70.10.0 0.0.10.255"
                                }
                            },
                        }
                    }
                },
                "name": "30",
            },
            "40": {
                "actions": {"forwarding": "permit"},
                "statistics": {"matched_packets": 8353358},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "10.196.0.0 0.0.255.255": {
                                    "source_network": "10.196.0.0 0.0.255.255"
                                }
                            },
                        }
                    }
                },
                "name": "40",
            },
        },
        "name": "43",
        "type": "ipv4-acl-type",
    }
}
