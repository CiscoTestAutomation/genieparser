expected_output = {
    "OutFilter_IPv6": {
        "aces": {
            "120": {
                "statistics": {"matched_packets": 3974749339},
                "matches": {
                    "l4": {"ipv6": {"established": False}},
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "source_network": {"any": {"source_network": "any"}},
                            "protocol": "ipv6",
                        }
                    },
                },
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "name": "120",
            },
            "30": {
                "matches": {
                    "l4": {"icmp": {"established": False, "msg_type": "mld-query"}},
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "source_network": {"any": {"source_network": "any"}},
                            "protocol": "icmp",
                        }
                    },
                },
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "name": "30",
            },
            "100": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "ipv6",
                            "source_network": {
                                "2001:DB8:B30A:213::/64": {
                                    "source_network": "2001:DB8:B30A:213::/64"
                                }
                            },
                        }
                    },
                    "l4": {"ipv6": {"established": False}},
                },
                "name": "100",
            },
            "110": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "2001:db8:5254:1000::/35": {
                                    "destination_network": "2001:db8:5254:1000::/35"
                                }
                            },
                            "dscp": "default",
                            "protocol": "ipv6",
                            "source_network": {
                                "2001:db8:5254:1000::/35": {
                                    "source_network": "2001:db8:5254:1000::/35"
                                }
                            },
                        }
                    },
                    "l4": {"ipv6": {"established": False}},
                },
                "name": "110",
            },
            "90": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "ipv6",
                            "source_network": {
                                "2001:DB8:B30A:FE9B::/64": {
                                    "source_network": "2001:DB8:B30A:FE9B::/64"
                                }
                            },
                        }
                    },
                    "l4": {"ipv6": {"established": False}},
                },
                "name": "90",
            },
            "80": {
                "actions": {"forwarding": "permit", "logging": "log-syslog"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "2001:db8:1d14::/16": {
                                    "destination_network": "2001:db8:1d14::/16"
                                }
                            },
                            "protocol": "ipv6",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    },
                    "l4": {"ipv6": {"established": False}},
                },
                "name": "80",
            },
            "70": {
                "matches": {
                    "l4": {"icmp": {"established": False}},
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "source_network": {"any": {"source_network": "any"}},
                            "protocol": "icmp",
                        }
                    },
                },
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "name": "70",
            },
            "50": {
                "matches": {
                    "l2": {
                        "eth": {
                            "source_mac_address": "103",
                            "destination_mac_address": "any",
                            "ether_type": "any sequence 50",
                        }
                    }
                },
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "name": "50",
            },
            "60": {
                "matches": {
                    "l4": {
                        "icmp": {"established": False, "msg_type": "packet-too-big"}
                    },
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "source_network": {"any": {"source_network": "any"}},
                            "protocol": "icmp",
                        }
                    },
                },
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "name": "60",
            },
            "40": {
                "matches": {
                    "l4": {
                        "icmp": {
                            "established": False,
                            "msg_type": "router-advertisement",
                        }
                    },
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "source_network": {"any": {"source_network": "any"}},
                            "protocol": "icmp",
                        }
                    },
                },
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "name": "40",
            },
            "75": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "ipv6",
                            "source_network": {
                                "2001:DB8:B30A:F442::/64": {
                                    "source_network": "2001:DB8:B30A:F442::/64"
                                }
                            },
                        }
                    },
                    "l4": {"ipv6": {"established": False}},
                },
                "name": "75",
            },
            "74": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "ipv6",
                            "source_network": {
                                "2001:DB8:B30A:DC63::/64": {
                                    "source_network": "2001:DB8:B30A:DC63::/64"
                                }
                            },
                        }
                    },
                    "l4": {"ipv6": {"established": False}},
                },
                "name": "74",
            },
        },
        "name": "OutFilter_IPv6",
        "type": "ipv6-acl-type",
        "acl_type": "ipv6",
    }
}
