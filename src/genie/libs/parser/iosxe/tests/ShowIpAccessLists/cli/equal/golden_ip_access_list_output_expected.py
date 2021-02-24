expected_output = {
    "ACL_TEST": {
        "aces": {
            "80": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.7.0 0.0.0.255": {
                                    "source_network": "10.4.7.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "80",
            },
            "50": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.4.0 0.0.0.255": {
                                    "source_network": "10.4.4.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "50",
            },
            "10": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.69.188.0 0.0.0.255": {
                                    "source_network": "10.69.188.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "10",
            },
            "130": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.12.0 0.0.0.255": {
                                    "source_network": "10.4.12.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "130",
            },
            "90": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.8.0 0.0.0.255": {
                                    "source_network": "10.4.8.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "90",
            },
            "40": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.3.0 0.0.0.255": {
                                    "source_network": "10.4.3.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "40",
            },
            "150": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.14.0 0.0.0.255": {
                                    "source_network": "10.4.14.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "150",
            },
            "30": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.2.0 0.0.0.255": {
                                    "source_network": "10.4.2.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
            "120": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.11.0 0.0.0.255": {
                                    "source_network": "10.4.11.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "120",
            },
            "100": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.9.0 0.0.0.255": {
                                    "source_network": "10.4.9.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "100",
            },
            "170": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.16.0 0.0.0.255": {
                                    "source_network": "10.4.16.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "170",
            },
            "160": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.15.0 0.0.0.255": {
                                    "source_network": "10.4.15.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "160",
            },
            "20": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.1.0 0.0.0.255": {
                                    "source_network": "10.4.1.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "20",
            },
            "70": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.6.0 0.0.0.255": {
                                    "source_network": "10.4.6.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "70",
            },
            "110": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.10.0 0.0.0.255": {
                                    "source_network": "10.4.10.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "110",
            },
            "140": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.13.0 0.0.0.255": {
                                    "source_network": "10.4.13.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "140",
            },
            "60": {
                "actions": {"forwarding": "deny", "logging": "log-none"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "source_network": {
                                "10.4.5.0 0.0.0.255": {
                                    "source_network": "10.4.5.0 0.0.0.255"
                                }
                            },
                            "protocol": "tcp",
                            "destination_network": {
                                "host 192.168.16.1": {
                                    "destination_network": "host 192.168.16.1"
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
                "name": "60",
            },
        },
        "type": "ipv4-acl-type",
        "acl_type": "extended",
        "name": "ACL_TEST",
    }
}
