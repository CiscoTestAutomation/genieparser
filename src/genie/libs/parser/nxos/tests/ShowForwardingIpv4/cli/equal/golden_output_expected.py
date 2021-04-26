expected_output = {
    "slot": {
        "1": {
            "ip_version": {
                "IPv4": {
                    "route_table": {
                        "default/base": {
                            "prefix": {
                                "10.4.1.1/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.4.1.2/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": True,
                                        }
                                    }
                                },
                                "10.2.1.0/32": {
                                    "next_hop": {
                                        "Drop": {"interface": "Null0", "is_best": False}
                                    }
                                },
                                "10.2.1.1/32": {
                                    "next_hop": {
                                        "Receive": {
                                            "interface": "sup-eth1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.2.1.2/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.2.1.255/32": {
                                    "next_hop": {
                                        "Attached": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.16.2.1/32": {
                                    "next_hop": {
                                        "Receive": {
                                            "interface": "sup-eth1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.16.2.2/32": {
                                    "next_hop": {
                                        "Receive": {
                                            "interface": "sup-eth1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.229.1.0/32": {
                                    "next_hop": {
                                        "Drop": {"interface": "Null0", "is_best": False}
                                    }
                                },
                                "10.229.1.1/32": {
                                    "next_hop": {
                                        "Receive": {
                                            "interface": "sup-eth1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.229.1.2/32": {
                                    "next_hop": {
                                        "10.229.1.2": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.229.1.255/32": {
                                    "next_hop": {
                                        "Attached": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "192.168.195.1/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.36.3.1/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.36.3.2/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": True,
                                        }
                                    }
                                },
                                "10.64.4.1/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.64.4.2/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": True,
                                        }
                                    }
                                },
                                "10.166.98.98/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.189.99.99/32": {
                                    "next_hop": {
                                        "10.229.1.2": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        }
                                    }
                                },
                            }
                        }
                    }
                }
            }
        },
        "27": {
            "ip_version": {
                "IPv4": {
                    "route_table": {
                        "default/base": {
                            "prefix": {
                                "0.0.0.0/32": {
                                    "next_hop": {
                                        "Drop": {"interface": "Null0", "is_best": False}
                                    }
                                },
                                "10.4.1.1/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        },
                                        "10.229.1.2": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        },
                                    }
                                },
                                "10.4.1.2/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": True,
                                        },
                                        "10.229.1.2": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        },
                                    }
                                },
                                "10.1.1.0/24": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.2.1.0/24": {
                                    "next_hop": {
                                        "Attached": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.2.1.0/32": {
                                    "next_hop": {
                                        "Drop": {"interface": "Null0", "is_best": False}
                                    }
                                },
                                "10.2.1.1/32": {
                                    "next_hop": {
                                        "Receive": {
                                            "interface": "sup-eth1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.2.1.2/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.2.1.255/32": {
                                    "next_hop": {
                                        "Attached": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.3.1.0/24": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.4.1.0/24": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.69.111.0/24": {
                                    "next_hop": {
                                        "Drop": {"interface": "Null0", "is_best": False}
                                    }
                                },
                                "127.0.0.0/8": {
                                    "next_hop": {
                                        "Drop": {"interface": "Null0", "is_best": False}
                                    }
                                },
                                "10.16.2.1/32": {
                                    "next_hop": {
                                        "Receive": {
                                            "interface": "sup-eth1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.16.2.2/32": {
                                    "next_hop": {
                                        "Receive": {
                                            "interface": "sup-eth1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.186.1.0/24": {
                                    "next_hop": {
                                        "10.229.1.2": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.229.1.0/24": {
                                    "next_hop": {
                                        "Attached": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.229.1.0/32": {
                                    "next_hop": {
                                        "Drop": {"interface": "Null0", "is_best": False}
                                    }
                                },
                                "10.229.1.1/32": {
                                    "next_hop": {
                                        "Receive": {
                                            "interface": "sup-eth1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.229.1.2/32": {
                                    "next_hop": {
                                        "10.229.1.2": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.229.1.255/32": {
                                    "next_hop": {
                                        "Attached": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.19.1.0/24": {
                                    "next_hop": {
                                        "10.229.1.2": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.66.1.0/24": {
                                    "next_hop": {
                                        "10.229.1.2": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "192.168.195.1/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.205.0.0/16": {
                                    "next_hop": {
                                        "Drop": {"interface": "Null0", "is_best": False}
                                    }
                                },
                                "10.205.25.0/24": {
                                    "next_hop": {
                                        "Drop": {"interface": "Null0", "is_best": False}
                                    }
                                },
                                "255.255.255.255/32": {
                                    "next_hop": {
                                        "Receive": {
                                            "interface": "sup-eth1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.36.3.1/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        },
                                        "10.229.1.2": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        },
                                    }
                                },
                                "10.36.3.2/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": True,
                                        },
                                        "10.229.1.2": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        },
                                    }
                                },
                                "10.64.4.1/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        },
                                        "10.229.1.2": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        },
                                    }
                                },
                                "10.64.4.2/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": True,
                                        },
                                        "10.229.1.2": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        },
                                    }
                                },
                                "10.166.98.98/32": {
                                    "next_hop": {
                                        "10.2.1.2": {
                                            "interface": "Ethernet1/1",
                                            "is_best": False,
                                        }
                                    }
                                },
                                "10.189.99.99/32": {
                                    "next_hop": {
                                        "10.229.1.2": {
                                            "interface": "Ethernet1/2",
                                            "is_best": False,
                                        }
                                    }
                                },
                            }
                        }
                    }
                }
            }
        },
    }
}
