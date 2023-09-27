expected_output = {
    "Gi2/0/24#v4#33476254": {
        "name": "Gi2/0/24#v4#33476254",
        "type": "ipv4-acl-type",
        "acl_type": "extended",
        "aces": {
            "10": {
                "name": "10",
                "actions": {
                    "forwarding": "permit",
                    "logging": "log-none"
                },
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "any": {
                                    "source_network": "any"
                                }
                            },
                            "destination_network": {
                                "any": {
                                    "destination_network": "any"
                                }
                            }
                        }
                    },
                    "l4": {
                        "ipv4": {
                            "established": False
                        }
                    }
                }
            }
        }
    },
    "IP-Adm-V4-Int-ACL-global": {
        "name": "IP-Adm-V4-Int-ACL-global",
        "type": "ipv4-acl-type",
        "acl_type": "extended",
        "aces": {
            "10": {
                "name": "10",
                "actions": {
                    "forwarding": "permit",
                    "logging": "log-none"
                },
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "tcp",
                            "source_network": {
                                "any": {
                                    "source_network": "any"
                                }
                            },
                            "destination_network": {
                                "any": {
                                    "destination_network": "any"
                                }
                            }
                        }
                    },
                    "l4": {
                        "tcp": {
                            "established": False,
                            "destination_port": {
                                "operator": {
                                    "operator": "eq",
                                    "port": 80
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "IP-Adm-V4-LOGOUT-ACL": {
        "name": "IP-Adm-V4-LOGOUT-ACL",
        "type": "ipv4-acl-type",
        "acl_type": "extended",
        "aces": {
            "10": {
                "name": "10",
                "actions": {
                    "forwarding": "permit",
                    "logging": "log-none"
                },
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "tcp",
                            "source_network": {
                                "any": {
                                    "source_network": "any"
                                }
                            },
                            "destination_network": {
                                "host 200.1.1.1": {
                                    "destination_network": "host 200.1.1.1"
                                }
                            }
                        }
                    },
                    "l4": {
                        "tcp": {
                            "established": False,
                            "destination_port": {
                                "operator": {
                                    "operator": "eq",
                                    "port": 80
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "implicit_deny": {
        "name": "implicit_deny",
        "type": "ipv4-acl-type",
        "acl_type": "extended",
        "aces": {
            "10": {
                "name": "10",
                "actions": {
                    "forwarding": "deny",
                    "logging": "log-none"
                },
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "any": {
                                    "source_network": "any"
                                }
                            },
                            "destination_network": {
                                "any": {
                                    "destination_network": "any"
                                }
                            }
                        }
                    },
                    "l4": {
                        "ipv4": {
                            "established": False
                        }
                    }
                }
            }
        }
    },
    "implicit_permit": {
        "name": "implicit_permit",
        "type": "ipv4-acl-type",
        "acl_type": "extended",
        "aces": {
            "10": {
                "name": "10",
                "actions": {
                    "forwarding": "permit",
                    "logging": "log-none"
                },
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "any": {
                                    "source_network": "any"
                                }
                            },
                            "destination_network": {
                                "any": {
                                    "destination_network": "any"
                                }
                            }
                        }
                    },
                    "l4": {
                        "ipv4": {
                            "established": False
                        }
                    }
                }
            }
        }
    },
    "meraki-fqdn-dns": {
        "name": "meraki-fqdn-dns",
        "type": "ipv4-acl-type",
        "acl_type": "extended"
    },
    "preauth_v4": {
        "name": "preauth_v4",
        "type": "ipv4-acl-type",
        "acl_type": "extended",
        "aces": {
            "10": {
                "name": "10",
                "actions": {
                    "forwarding": "permit",
                    "logging": "log-none"
                },
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "udp",
                            "source_network": {
                                "any": {
                                    "source_network": "any"
                                }
                            },
                            "destination_network": {
                                "any": {
                                    "destination_network": "any"
                                }
                            }
                        }
                    },
                    "l4": {
                        "udp": {
                            "established": False,
                            "destination_port": {
                                "operator": {
                                    "operator": "eq",
                                    "port": 53
                                }
                            }
                        }
                    }
                }
            },
            "20": {
                "name": "20",
                "actions": {
                    "forwarding": "permit",
                    "logging": "log-none"
                },
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "tcp",
                            "source_network": {
                                "any": {
                                    "source_network": "any"
                                }
                            },
                            "destination_network": {
                                "any": {
                                    "destination_network": "any"
                                }
                            }
                        }
                    },
                    "l4": {
                        "tcp": {
                            "established": False,
                            "destination_port": {
                                "operator": {
                                    "operator": "eq",
                                    "port": 53
                                }
                            }
                        }
                    }
                }
            },
            "30": {
                "name": "30",
                "actions": {
                    "forwarding": "permit",
                    "logging": "log-none"
                },
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "udp",
                            "source_network": {
                                "any": {
                                    "source_network": "any"
                                }
                            },
                            "destination_network": {
                                "any": {
                                    "destination_network": "any"
                                }
                            }
                        }
                    },
                    "l4": {
                        "udp": {
                            "established": False,
                            "source_port": {
                                "operator": {
                                    "operator": "eq",
                                    "port": "bootps"
                                }
                            }
                        }
                    }
                }
            },
            "40": {
                "name": "40",
                "actions": {
                    "forwarding": "permit",
                    "logging": "log-none"
                },
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "udp",
                            "source_network": {
                                "any": {
                                    "source_network": "any"
                                }
                            },
                            "destination_network": {
                                "any": {
                                    "destination_network": "any"
                                }
                            }
                        }
                    },
                    "l4": {
                        "udp": {
                            "established": False,
                            "destination_port": {
                                "operator": {
                                    "operator": "eq",
                                    "port": 68
                                }
                            }
                        }
                    }
                }
            },
            "50": {
                "name": "50",
                "actions": {
                    "forwarding": "permit",
                    "logging": "log-none"
                },
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "udp",
                            "source_network": {
                                "any": {
                                    "source_network": "any"
                                }
                            },
                            "destination_network": {
                                "any": {
                                    "destination_network": "any"
                                }
                            }
                        }
                    },
                    "l4": {
                        "udp": {
                            "established": False,
                            "source_port": {
                                "operator": {
                                    "operator": "eq",
                                    "port": "bootpc"
                                }
                            }
                        }
                    }
                }
            },
            "60": {
                "name": "60",
                "actions": {
                    "forwarding": "deny",
                    "logging": "log-none"
                },
                "matches": {
                    "l3": {
                        "ipv4": {
                            "protocol": "ipv4",
                            "source_network": {
                                "any": {
                                    "source_network": "any"
                                }
                            },
                            "destination_network": {
                                "any": {
                                    "destination_network": "any"
                                }
                            }
                        }
                    },
                    "l4": {
                        "ipv4": {
                            "established": False
                        }
                    }
                }
            }
        }
    }
}