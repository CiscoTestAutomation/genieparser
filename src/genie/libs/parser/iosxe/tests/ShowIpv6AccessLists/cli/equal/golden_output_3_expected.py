expected_output = {
    "time_based": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "host 2002::1": {"destination_network": "host 2002::1"}
                            },
                            "protocol": "tcp",
                            "source_network": {
                                "host 2000::1": {"source_network": "host 2000::1"}
                            },
                        }
                    },
                    "l4": {"tcp": {"established": False}},
                },
                "name": "10",
                "time_range": {
                    "name": "GO",
                    "status": "active"
                }
            },
            "20": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "host 2002::1": {"destination_network": "host 2002::1"}
                            },
                            "protocol": "udp",
                            "source_network": {
                                "host 2000::1": {"source_network": "host 2000::1"}
                            },
                        }
                    },
                    "l4": {"udp": {"established": False}},
                },
                "name": "20",
            },
            "30": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "host 2003::1": {"destination_network": "host 2003::1"}
                            },
                            "protocol": "tcp",
                            "source_network": {
                                "host 2000::1": {"source_network": "host 2000::1"}
                            },
                        }
                    },
                    "l4": {"tcp": {"established": False}},
                },
                "name": "30",
            },
            "40": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "host 2003::1": {"destination_network": "host 2003::1"}
                            },
                            "protocol": "udp",
                            "source_network": {
                                "host 2000::1": {"source_network": "host 2000::1"}
                            },
                        }
                    },
                    "l4": {"udp": {"established": False}},
                },
                "name": "40",
                "time_range": {
                    "name": "GO",
                    "status": "active"
                }
            },
            "50": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "host 2004::1": {"destination_network": "host 2004::1"}
                            },
                            "protocol": "udp",
                            "source_network": {
                                "host 2000::1": {"source_network": "host 2000::1"}
                            },
                        }
                    },
                    "l4": {"udp": {"established": False}},
                },
                "name": "50",
                "time_range": {
                    "name": "GO",
                    "status": "active"
                }
            },
            "60": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "host 2004::1": {"destination_network": "host 2004::1"}
                            },
                            "protocol": "tcp",
                            "source_network": {
                                "host 2000::1": {"source_network": "host 2000::1"}
                            },
                        }
                    },
                    "l4": {"tcp": {"established": False}},
                },
                "name": "60",
            },
            "70": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "host 2004::1": {"destination_network": "host 2004::1"}
                            },
                            "protocol": "udp",
                            "source_network": {
                                "host 2000::1": {"source_network": "host 2000::1"}
                            },
                        }
                    },
                    "l4": {"udp": {"established": False}},
                },
                "name": "70",
            },
            "80": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "host 2004::1": {"destination_network": "host 2004::1"}
                            },
                            "protocol": "tcp",
                            "source_network": {
                                "host 2000::1": {"source_network": "host 2000::1"}
                            },
                        }
                    },
                    "l4": {"tcp": {"established": False}},
                },
                "name": "80",
                "time_range": {
                    "name": "GO",
                    "status": "active"
                }
            },
        },
        "name": "time_based",
        "type": "ipv6-acl-type",
        "acl_type": "ipv6",
    },
}