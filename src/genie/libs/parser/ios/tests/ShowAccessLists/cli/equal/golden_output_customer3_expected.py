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
                "statistics": {"matched_packets": 198},
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
            "70": {
                "name": "70",
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "object-group grt-interface-nets": {
                                    "source_network": "object-group grt-interface-nets"
                                }
                            },
                            "destination_network": {
                                "object-group grt-interface-nets": {
                                    "destination_network": "object-group grt-interface-nets"
                                }
                            },
                        }
                    },
                    "l4": {"ipv4": {"established": False}},
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
            "90": {
                "name": "90",
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "statistics": {"matched_packets": 14},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "esp",
                            "source_network": {
                                "object-group vpn-endpoints-dummydpd": {
                                    "source_network": "object-group vpn-endpoints-dummydpd"
                                }
                            },
                            "destination_network": {
                                "host 10.4.1.1": {
                                    "destination_network": "host 10.4.1.1"
                                }
                            },
                        }
                    },
                    "l4": {"esp": {"established": False}},
                },
            },
            "100": {
                "name": "100",
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ahp",
                            "source_network": {
                                "object-group vpn-endpoints-dummydpd": {
                                    "source_network": "object-group vpn-endpoints-dummydpd"
                                }
                            },
                            "destination_network": {
                                "host 10.4.1.1": {
                                    "destination_network": "host 10.4.1.1"
                                }
                            },
                        }
                    },
                    "l4": {"ahp": {"established": False}},
                },
            },
            "110": {
                "name": "110",
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "statistics": {"matched_packets": 122},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "udp",
                            "source_network": {
                                "object-group vpn-endpoints-dummydpd": {
                                    "source_network": "object-group vpn-endpoints-dummydpd"
                                }
                            },
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
                                "operator": {"operator": "eq", "port": 500}
                            },
                        }
                    },
                },
            },
        },
    }
}
