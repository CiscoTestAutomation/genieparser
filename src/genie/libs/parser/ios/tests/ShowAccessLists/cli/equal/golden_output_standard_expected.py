expected_output = {
    "1": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "172.20.10.10 0.0.0.0": {
                                    "source_network": "172.20.10.10 0.0.0.0"
                                }
                            },
                        }
                    }
                },
                "name": "10",
            }
        },
        "name": "1",
        "type": "ipv4-acl-type",
        "acl_type": "standard",
    },
    "10": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "10.66.12.12 0.0.0.0": {
                                    "source_network": "10.66.12.12 0.0.0.0"
                                }
                            },
                        }
                    }
                },
                "name": "10",
            }
        },
        "name": "10",
        "type": "ipv4-acl-type",
        "acl_type": "standard",
    },
    "12": {
        "aces": {
            "10": {
                "actions": {"forwarding": "deny"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "10.16.3.2 0.0.0.0": {
                                    "source_network": "10.16.3.2 0.0.0.0"
                                }
                            },
                        }
                    }
                },
                "name": "10",
            }
        },
        "name": "12",
        "type": "ipv4-acl-type",
        "acl_type": "standard",
    },
    "32": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "172.20.20.20 0.0.0.0": {
                                    "source_network": "172.20.20.20 0.0.0.0"
                                }
                            },
                        }
                    }
                },
                "name": "10",
            }
        },
        "name": "32",
        "type": "ipv4-acl-type",
        "acl_type": "standard",
    },
    "34": {
        "aces": {
            "10": {
                "actions": {"forwarding": "permit"},
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "10.24.35.56 0.0.0.0": {
                                    "source_network": "10.24.35.56 0.0.0.0"
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
                                "10.34.56.34 0.0.0.0": {
                                    "source_network": "10.34.56.34 0.0.0.0"
                                }
                            },
                        }
                    }
                },
                "name": "20",
            },
        },
        "name": "34",
        "type": "ipv4-acl-type",
        "acl_type": "standard",
    },
}
