expected_output = {
    "NAT_ACL": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "10.2.0.0 0.0.255.255": {
                                    "source_network": "10.2.0.0 0.0.255.255"
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
                                "10.2.0.0 0.0.0.0": {
                                    "source_network": "10.2.0.0 0.0.0.0"
                                }
                            },
                        }
                    }
                },
                "name": "20",
            },
            "30": {
                "actions": {"forwarding": "deny"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    }
                },
                "name": "30",
            },
            "40": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "10.196.7.7 0.0.0.0": {
                                    "source_network": "10.196.7.7 0.0.0.0"
                                }
                            },
                        }
                    }
                },
                "name": "40",
            },
        },
        "name": "NAT_ACL",
        "type": "ipv4-acl-type",
        "acl_type": "standard",
    },
    "NAT_ACL2": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "10.2.0.0 0.0.255.255": {
                                    "source_network": "10.2.0.0 0.0.255.255"
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
                                "10.196.7.8 0.0.0.0": {
                                    "source_network": "10.196.7.8 0.0.0.0"
                                }
                            },
                        }
                    }
                },
                "name": "20",
            },
            "30": {
                "actions": {"forwarding": "deny"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    }
                },
                "name": "30",
            },
        },
        "name": "NAT_ACL2",
        "type": "ipv4-acl-type",
        "acl_type": "standard",
    },
    "PYATS_ACL_TEST": {
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
                            "source_network": {
                                "host 0.0.0.0": {"source_network": "host 0.0.0.0"}
                            },
                        }
                    },
                    "l4": {"ipv4": {"established": False}},
                },
                "name": "10",
            },
            "20": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "192.168.10.0 0.0.0.255": {
                                    "destination_network": "192.168.10.0 0.0.0.255"
                                }
                            },
                            "protocol": "ipv4",
                            "source_network": {
                                "192.0.2.0 0.0.0.255": {
                                    "source_network": "192.0.2.0 0.0.0.255"
                                }
                            },
                        }
                    },
                    "l4": {"ipv4": {"established": False}},
                },
                "name": "20",
            },
            "30": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "destination_network": {
                                "192.168.220.0 0.0.0.255": {
                                    "destination_network": "192.168.220.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "source_network": {
                                "10.55.0.0 0.0.0.255": {
                                    "source_network": "10.55.0.0 0.0.0.255"
                                }
                            },
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
                "name": "30",
            },
        },
        "name": "PYATS_ACL_TEST",
        "type": "ipv4-acl-type",
        "acl_type": "extended",
    },
    "PYATS_ACL_TEST_IPv6": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "ipv6",
                            "source_network": {
                                "2001:DB8::/64": {"source_network": "2001:DB8::/64"}
                            },
                        }
                    },
                    "l4": {"ipv6": {"established": False}},
                },
                "name": "10",
            },
            "20": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "esp",
                            "source_network": {
                                "host 2001:DB8:5::1": {
                                    "source_network": "host 2001:DB8:5::1"
                                }
                            },
                        }
                    },
                    "l4": {"esp": {"established": False}},
                },
                "name": "20",
            },
            "30": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "any": {"destination_network": "any"}
                            },
                            "protocol": "tcp",
                            "source_network": {
                                "host 2001:DB8:1::1": {
                                    "source_network": "host 2001:DB8:1::1"
                                }
                            },
                        }
                    },
                    "l4": {
                        "tcp": {
                            "destination_port": {
                                "operator": {"operator": "eq", "port": 179}
                            },
                            "established": False,
                            "source_port": {
                                "operator": {"operator": "eq", "port": "www"}
                            },
                        }
                    },
                },
                "name": "30",
            },
            "40": {
                "actions": {"forwarding": "permit", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv6": {
                            "destination_network": {
                                "host 2001:DB8:1::1": {
                                    "destination_network": "host 2001:DB8:1::1"
                                }
                            },
                            "protocol": "udp",
                            "source_network": {"any": {"source_network": "any"}},
                        }
                    },
                    "l4": {"udp": {"established": False}},
                },
                "name": "40",
            },
        },
        "name": "PYATS_ACL_TEST_IPv6",
        "type": "ipv6-acl-type",
        "acl_type": "ipv6",
    },
}
