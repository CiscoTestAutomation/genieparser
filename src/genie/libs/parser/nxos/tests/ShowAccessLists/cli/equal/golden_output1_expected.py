expected_output = {
    "acl_name": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "ip",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    }
                },
                "name": "10",
            }
        },
        "name": "acl_name",
        "type": "ipv4-acl-type",
    },
    "ipv4_acl": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit"},
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
                                "operator": {"operator": "eq", "port": "www"}
                            }
                        }
                    },
                },
                "name": "10",
            },
            "20": {
                "actions": {"forwarding": "permit"},
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
                                "operator": {"operator": "eq", "port": "22"}
                            }
                        }
                    },
                },
                "name": "20",
            },
            "30": {
                "actions": {"forwarding": "permit"},
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
                                "operator": {"operator": "eq", "port": "443"}
                            }
                        }
                    },
                },
                "name": "30",
            },
        },
        "name": "ipv4_acl",
        "type": "ipv4-acl-type",
    },
    "ipv4_ext": {"name": "ipv4_ext", "type": "ipv4-acl-type"},
    "ipv6_acl": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit", "logging": "log-syslog"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "ipv6",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    }
                },
                "name": "10",
            },
            "20": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "2001:1::2/128": {
                                    "destination_network": "2001:1::2/128"
                                }
                            },
                            "protocol": "ipv6",
                            "source_network": {
                                "2001::1/128": {"source_network": "2001::1/128"}
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
                        "ipv6": {
                            "destination_network": {
                                "2001:2::2/128": {
                                    "destination_network": "2001:2::2/128"
                                }
                            },
                            "protocol": "tcp",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    },
                    "l4": {
                        "tcp": {
                            "source_port": {
                                "operator": {"operator": "eq", "port": "8443"}
                            }
                        }
                    },
                },
                "name": "30",
            },
        },
        "name": "ipv6_acl",
        "type": "ipv6-acl-type",
    },
    "ipv6_acl2": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "udp",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    }
                },
                "name": "10",
            }
        },
        "name": "ipv6_acl2",
        "type": "ipv6-acl-type",
    },
    "mac_acl": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l2": {
                        "eth": {
                            "destination_mac_address": "bbbb.ccff.aaaa bbbb.ccff.aaaa",
                            "ether_type": "aarp",
                            "source_mac_address": "aaaa.bbff.8888 0000.0000.0000",
                        }
                    }
                },
                "name": "10",
            },
            "20": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l2": {
                        "eth": {
                            "destination_mac_address": "any",
                            "source_mac_address": "0000.0000.0000 0000.0000.0000",
                        }
                    }
                },
                "name": "20",
            },
            "30": {
                "actions": {"forwarding": "deny"},
                "matches": {
                    "l2": {
                        "eth": {
                            "destination_mac_address": "aaaa.bbff.8888 0000.0000.0000",
                            "source_mac_address": "0000.0000.0000 0000.0000.0000",
                            "mac_protocol_number": "0x8041",
                        }
                    }
                },
                "name": "30",
            },
            "40": {
                "actions": {"forwarding": "deny"},
                "matches": {
                    "l2": {
                        "eth": {
                            "destination_mac_address": "any",
                            "source_mac_address": "any",
                            "vlan": 10,
                        }
                    }
                },
                "name": "40",
            },
            "50": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l2": {
                        "eth": {
                            "destination_mac_address": "any",
                            "ether_type": "aarp",
                            "source_mac_address": "aaaa.aaff.5555 ffff.ffff.0000",
                        }
                    }
                },
                "name": "50",
            },
        },
        "name": "mac_acl",
        "type": "eth-acl-type",
    },
    "test22": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "10.4.1.1/32": {"destination_network": "10.4.1.1/32"}
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
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "precedence": "network",
                            "protocol": "tcp",
                            "source_network": {
                                "10.16.2.2/32": {"source_network": "10.16.2.2/32"}
                            },
                            "ttl": 255,
                        }
                    },
                    "l4": {
                        "tcp": {
                            "source_port": {
                                "operator": {"operator": "eq", "port": "www"}
                            }
                        }
                    },
                },
                "name": "20",
            },
            "30": {
                "actions": {"forwarding": "deny"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "ip",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    }
                },
                "name": "30",
            },
        },
        "name": "test22",
        "type": "ipv4-acl-type",
    },
}
