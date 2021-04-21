expected_output = {
    "acl_name": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "ipv4",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    },
                    "l4": {"ipv4": {"established": False}},
                },
                "name": "10",
                "statistics": {"matched_packets": 10031},
            }
        },
        "name": "acl_name",
        "type": "ipv4-acl-type",
        "acl_type": "extended",
    },
    "ipv4_acl": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
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
                                "operator": {"operator": "eq", "port": 80}
                            },
                            "established": False,
                        }
                    },
                },
                "name": "10",
            },
            "20": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
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
                                "operator": {"operator": "eq", "port": 22}
                            },
                            "established": False,
                        }
                    },
                },
                "name": "20",
            },
        },
        "name": "ipv4_acl",
        "type": "ipv4-acl-type",
        "acl_type": "extended",
    },
    "ipv6_acl": {
        "aces": {
            "20": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "host 2001:1::2": {
                                    "destination_network": "host 2001:1::2"
                                }
                            },
                            "protocol": "ipv6",
                            "source_network": {
                                "host 2001::1": {"source_network": "host 2001::1"}
                            },
                        }
                    },
                    "l4": {"ipv6": {"established": False}},
                },
                "name": "20",
            },
            "30": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "host 2001:2::2": {
                                    "destination_network": "host 2001:2::2"
                                }
                            },
                            "protocol": "tcp",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    },
                    "l4": {
                        "tcp": {
                            "established": False,
                            "source_port": {
                                "operator": {"operator": "eq", "port": "www 8443"}
                            },
                        }
                    },
                },
                "name": "30",
            },
            "80": {
                "actions": {"forwarding": "permit", "logging": "log-syslog"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "2001:db8:1:1::1 2001:db8:24:24::6": {
                                    "destination_network": "2001:db8:1:1::1 2001:db8:24:24::6"
                                }
                            },
                            "protocol": "ipv6",
                            "source_network": {
                                "2001:db8:9:9::3 2001:db8:10:10::4": {
                                    "source_network": "2001:db8:9:9::3 2001:db8:10:10::4"
                                }
                            },
                        }
                    },
                    "l4": {"ipv6": {"established": False}},
                },
                "name": "80",
            },
        },
        "name": "ipv6_acl",
        "type": "ipv6-acl-type",
        "acl_type": "ipv6",
    },
    "mac_acl": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l2": {
                        "eth": {
                            "destination_mac_address": "any",
                            "source_mac_address": "any",
                        }
                    }
                },
                "name": "10",
            },
            "20": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l2": {
                        "eth": {
                            "destination_mac_address": "any",
                            "ether_type": "msdos",
                            "source_mac_address": "any",
                        }
                    }
                },
                "name": "20",
            },
            "30": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l2": {
                        "eth": {
                            "destination_mac_address": "any",
                            "source_mac_address": "any",
                            "vlan": 10,
                        }
                    }
                },
                "name": "30",
            },
            "40": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l2": {
                        "eth": {
                            "destination_mac_address": "host 0003.00ff.0306",
                            "lsap": "0x1 0xD8FE",
                            "source_mac_address": "host 0001.00ff.0235",
                        }
                    }
                },
                "name": "40",
            },
            "50": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l2": {
                        "eth": {
                            "cos": 4,
                            "destination_mac_address": "any",
                            "ether_type": "aarp",
                            "source_mac_address": "any",
                            "vlan": 20,
                        }
                    }
                },
                "name": "50",
            },
        },
        "name": "mac_acl",
        "type": "eth-acl-type",
        "acl_type": "extended",
    },
    "preauth_v6": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
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
                    "l4": {
                        "udp": {
                            "destination_port": {
                                "operator": {"operator": "eq", "port": 53}
                            },
                            "established": False,
                        }
                    },
                },
                "name": "10",
            },
            "20": {
                "actions": {"forwarding": "permit", "logging": "log-syslog"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "dscp": "cs7",
                            "protocol": "esp",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    },
                    "l4": {"esp": {"established": False}},
                },
                "name": "20",
            },
            "30": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "ipv6",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    },
                    "l4": {"ipv6": {"established": False}},
                },
                "name": "30",
            },
        },
        "name": "preauth_v6",
        "per_user": True,
        "type": "ipv6-acl-type",
        "acl_type": "ipv6",
    },
    "test1": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit", "logging": "log-syslog"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "dscp": "default",
                            "protocol": "pim",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    },
                    "l4": {"pim": {"established": False}},
                },
                "name": "10",
            },
            "20": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "icmp",
                            "source_network": {
                                "0.1.1.1 255.0.0.0": {
                                    "source_network": "0.1.1.1 255.0.0.0"
                                }
                            },
                        }
                    },
                    "l4": {"icmp": {"code": 66, "established": False, "type": 10}},
                },
                "name": "20",
            },
        },
        "name": "test1",
        "type": "ipv4-acl-type",
        "acl_type": "extended",
    },
    "test22": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit", "logging": "log-syslog"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "host 10.4.1.1": {
                                    "destination_network": "host 10.4.1.1"
                                }
                            },
                            "protocol": "tcp",
                            "source_network": {
                                "192.168.1.0 0.0.0.255": {
                                    "source_network": "192.168.1.0 0.0.0.255"
                                }
                            },
                        }
                    },
                    "l4": {"tcp": {"established": True}},
                },
                "name": "10",
            },
            "20": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "precedence": "network",
                            "protocol": "tcp",
                            "source_network": {
                                "host 10.16.2.2": {
                                    "source_network": "host 10.16.2.2"
                                }
                            },
                            "ttl": 255,
                            "ttl_operator": "eq",
                        }
                    },
                    "l4": {
                        "tcp": {
                            "established": False,
                            "source_port": {
                                "operator": {
                                    "operator": "eq",
                                    "port": "www telnet 443",
                                }
                            },
                        }
                    },
                },
                "name": "20",
            },
            "30": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "ipv4",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    },
                    "l4": {"ipv4": {"established": False}},
                },
                "name": "30",
            },
            "40": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "tcp",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    },
                    "l4": {
                        "tcp": {
                            "established": False,
                            "source_port": {
                                "range": {"lower_port": 20, "upper_port": 179}
                            },
                        }
                    },
                },
                "name": "40",
            },
        },
        "name": "test22",
        "type": "ipv4-acl-type",
        "acl_type": "extended",
    },
    "test33": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "10.120.194.64 0.0.0.63": {
                                    "destination_network": "10.120.194.64 0.0.0.63"
                                }
                            },
                            "protocol": "icmp",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    },
                    "l4": {"icmp": {"established": False}},
                },
                "name": "10",
            },
            "20": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "10.120.194.64 0.0.0.63": {
                                    "destination_network": "10.120.194.64 0.0.0.63"
                                }
                            },
                            "protocol": "tcp",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    },
                    "l4": {
                        "tcp": {
                            "established": False,
                            "source_port": {
                                "operator": {"operator": "eq", "port": "443"}
                            },
                        }
                    },
                },
                "name": "20",
            },
        },
        "name": "test33",
        "type": "ipv4-acl-type",
        "acl_type": "extended",
    },
}
