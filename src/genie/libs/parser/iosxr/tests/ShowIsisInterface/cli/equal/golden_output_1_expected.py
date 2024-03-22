

expected_output = {
    "instance": {
        "test": {
            "interface": {
                "Loopback0": {
                    "state": "Enabled",
                    "adjacency_formation": "Enabled",
                    "prefix_advertisement": "Enabled",
                    "ipv4_bfd": False,
                    "ipv6_bfd": False,
                    "bfd_min_interval": 150,
                    "bfd_multiplier": 3,
                    "bandwidth": 0,
                    "circuit_type": "level-1-2",
                    "media_type": "Loop",
                    "circuit_number": 0,
                    "level": {
                        1: {
                            "adjacency_count": 0,
                            "lsp_pacing_interval_ms": 33,
                            "psnp_entry_queue_size": 0,
                            "hello_interval_sec": 10,
                            "hello_multiplier": 3,
                        },
                        2: {
                            "adjacency_count": 0,
                            "lsp_pacing_interval_ms": 33,
                            "psnp_entry_queue_size": 0,
                            "hello_interval_sec": 10,
                            "hello_multiplier": 3,
                        },
                    },
                    "clns_io": {"protocol_state": "Up", "mtu": 1500},
                    "topology": {
                        "ipv4 unicast": {
                            "state": "Enabled",
                            "adjacency_formation": "Running",
                            "prefix_advertisement": "Running",
                            "metric": {"level": {1: 10, 2: 10}},
                            "weight": {"level": {1: 0, 2: 0}},
                            "mpls": {
                                "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                "ldp_sync": {"level": {1: "Disabled", 2: "Disabled"}},
                            },
                            "frr": {
                                "level": {
                                    1: {"state": "Not Enabled", "type": "None"},
                                    2: {"state": "Not Enabled", "type": "None"},
                                }
                            },
                        },
                        "ipv6 unicast": {
                            "state": "Enabled",
                            "adjacency_formation": "Running",
                            "prefix_advertisement": "Running",
                            "metric": {"level": {1: 10, 2: 10}},
                            "weight": {"level": {1: 0, 2: 0}},
                            "mpls": {
                                "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                "ldp_sync": {"level": {1: "Disabled", 2: "Disabled"}},
                            },
                            "frr": {
                                "level": {
                                    1: {"state": "Not Enabled", "type": "None"},
                                    2: {"state": "Not Enabled", "type": "None"},
                                }
                            },
                        },
                    },
                    "address_family": {
                        "IPv4": {
                            "state": "Enabled",
                            "protocol_state": "Up",
                            "forwarding_address": ["0.0.0.0"],
                            "global_prefix": ["10.36.3.0/24"],
                        },
                        "IPv6": {
                            "state": "Enabled",
                            "protocol_state": "Up",
                            "forwarding_address": ["::"],
                            "global_prefix": ["2001:db8:3:3:3::3/128"],
                        },
                    },
                    "lsp": {
                        "transmit_timer_expires_ms": 0,
                        "transmission_state": "idle",
                        "lsp_transmit_back_to_back_limit_window_msec": 0,
                        "lsp_transmit_back_to_back_limit": 10,
                    },
                },
                "GigabitEthernet0/0/0/0": {
                    "state": "Enabled",
                    "adjacency_formation": "Enabled",
                    "prefix_advertisement": "Enabled",
                    "ipv4_bfd": False,
                    "ipv6_bfd": False,
                    "bfd_min_interval": 150,
                    "bfd_multiplier": 3,
                    "bandwidth": 1000000,
                    "circuit_type": "level-1-2",
                    "media_type": "LAN",
                    "circuit_number": 7,
                    "level": {
                        1: {
                            "adjacency_count": 0,
                            "lan_id": "R3.07",
                            "priority": {"local": "64", "dis": "none (no DIS elected)"},
                            "next_lan_iih_sec": 5,
                            "lsp_pacing_interval_ms": 33,
                            "psnp_entry_queue_size": 0,
                            "hello_interval_sec": 10,
                            "hello_multiplier": 3,
                        },
                        2: {
                            "adjacency_count": 1,
                            "lan_id": "R3.07",
                            "priority": {"local": "64", "dis": "64"},
                            "next_lan_iih_sec": 3,
                            "lsp_pacing_interval_ms": 33,
                            "psnp_entry_queue_size": 0,
                            "hello_interval_sec": 10,
                            "hello_multiplier": 3,
                        },
                    },
                    "clns_io": {
                        "protocol_state": "Up",
                        "mtu": 1497,
                        "snpa": "fa16.3eff.52be",
                        "layer2_mcast_groups_membership": {
                            "all_level_1_iss": "Yes",
                            "all_level_2_iss": "Yes",
                        },
                    },
                    "topology": {
                        "ipv4 unicast": {
                            "state": "Enabled",
                            "adjacency_formation": "Running",
                            "prefix_advertisement": "Running",
                            "metric": {"level": {1: 10, 2: 10}},
                            "weight": {"level": {1: 0, 2: 0}},
                            "mpls": {
                                "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                "ldp_sync": {"level": {1: "Disabled", 2: "Disabled"}},
                            },
                            "frr": {
                                "level": {
                                    1: {"state": "Not Enabled", "type": "None"},
                                    2: {"state": "Not Enabled", "type": "None"},
                                }
                            },
                        },
                        "ipv6 unicast": {
                            "state": "Enabled",
                            "adjacency_formation": "Running",
                            "prefix_advertisement": "Running",
                            "metric": {"level": {1: 10, 2: 10}},
                            "weight": {"level": {1: 0, 2: 0}},
                            "mpls": {
                                "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                "ldp_sync": {"level": {1: "Disabled", 2: "Disabled"}},
                            },
                            "frr": {
                                "level": {
                                    1: {"state": "Not Enabled", "type": "None"},
                                    2: {"state": "Not Enabled", "type": "None"},
                                }
                            },
                        },
                    },
                    "address_family": {
                        "IPv4": {
                            "state": "Enabled",
                            "protocol_state": "Up",
                            "forwarding_address": ["10.2.3.3"],
                            "global_prefix": ["10.2.3.0/24"],
                        },
                        "IPv6": {
                            "state": "Enabled",
                            "protocol_state": "Up",
                            "forwarding_address": ["fe80::f816:3eff:feff:52be"],
                            "global_prefix": ["2001:db8:10:2::/64"],
                        },
                    },
                    "lsp": {
                        "transmit_timer_expires_ms": 0,
                        "transmission_state": "idle",
                        "lsp_transmit_back_to_back_limit_window_msec": 0,
                        "lsp_transmit_back_to_back_limit": 9,
                    },
                },
                "GigabitEthernet0/0/0/1": {
                    "state": "Enabled",
                    "adjacency_formation": "Enabled",
                    "prefix_advertisement": "Enabled",
                    "ipv4_bfd": False,
                    "ipv6_bfd": False,
                    "bfd_min_interval": 150,
                    "bfd_multiplier": 3,
                    "bandwidth": 1000000,
                    "circuit_type": "level-1-2",
                    "media_type": "LAN",
                    "circuit_number": 5,
                    "level": {
                        1: {
                            "adjacency_count": 1,
                            "lan_id": "R3.05",
                            "priority": {"local": "64", "dis": "64"},
                            "next_lan_iih_sec": 2,
                            "lsp_pacing_interval_ms": 33,
                            "psnp_entry_queue_size": 0,
                            "hello_interval_sec": 10,
                            "hello_multiplier": 3,
                        },
                        2: {
                            "adjacency_count": 0,
                            "lan_id": "R3.05",
                            "priority": {"local": "64", "dis": "none (no DIS elected)"},
                            "next_lan_iih_sec": 6,
                            "lsp_pacing_interval_ms": 33,
                            "psnp_entry_queue_size": 0,
                            "hello_interval_sec": 10,
                            "hello_multiplier": 3,
                        },
                    },
                    "clns_io": {
                        "protocol_state": "Up",
                        "mtu": 1497,
                        "snpa": "fa16.3eff.86bf",
                        "layer2_mcast_groups_membership": {
                            "all_level_1_iss": "Yes",
                            "all_level_2_iss": "Yes",
                        },
                    },
                    "topology": {
                        "ipv4 unicast": {
                            "state": "Enabled",
                            "adjacency_formation": "Running",
                            "prefix_advertisement": "Running",
                            "metric": {"level": {1: 10, 2: 10}},
                            "weight": {"level": {1: 0, 2: 0}},
                            "mpls": {
                                "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                "ldp_sync": {"level": {1: "Disabled", 2: "Disabled"}},
                            },
                            "frr": {
                                "level": {
                                    1: {"state": "Not Enabled", "type": "None"},
                                    2: {"state": "Not Enabled", "type": "None"},
                                }
                            },
                        },
                        "ipv6 unicast": {
                            "state": "Enabled",
                            "adjacency_formation": "Running",
                            "prefix_advertisement": "Running",
                            "metric": {"level": {1: 10, 2: 10}},
                            "weight": {"level": {1: 0, 2: 0}},
                            "mpls": {
                                "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                "ldp_sync": {"level": {1: "Disabled", 2: "Disabled"}},
                            },
                            "frr": {
                                "level": {
                                    1: {"state": "Not Enabled", "type": "None"},
                                    2: {"state": "Not Enabled", "type": "None"},
                                }
                            },
                        },
                    },
                    "address_family": {
                        "IPv4": {
                            "state": "Enabled",
                            "protocol_state": "Up",
                            "forwarding_address": ["10.3.6.3"],
                            "global_prefix": ["10.3.6.0/24"],
                        },
                        "IPv6": {
                            "state": "Enabled",
                            "protocol_state": "Up",
                            "forwarding_address": ["fe80::f816:3eff:feff:86bf"],
                            "global_prefix": ["2001:db8:10:3::/64"],
                        },
                    },
                    "lsp": {
                        "transmit_timer_expires_ms": 0,
                        "transmission_state": "idle",
                        "lsp_transmit_back_to_back_limit_window_msec": 0,
                        "lsp_transmit_back_to_back_limit": 9,
                    },
                },
                "GigabitEthernet0/0/0/2": {
                    "state": "Enabled",
                    "adjacency_formation": "Enabled",
                    "prefix_advertisement": "Enabled",
                    "ipv4_bfd": False,
                    "ipv6_bfd": False,
                    "bfd_min_interval": 150,
                    "bfd_multiplier": 3,
                    "bandwidth": 1000000,
                    "circuit_type": "level-1-2",
                    "media_type": "LAN",
                    "circuit_number": 3,
                    "level": {
                        1: {
                            "adjacency_count": 1,
                            "lan_id": "R3.03",
                            "priority": {"local": "64", "dis": "64"},
                            "next_lan_iih_sec": 1,
                            "lsp_pacing_interval_ms": 33,
                            "psnp_entry_queue_size": 0,
                            "hello_interval_sec": 10,
                            "hello_multiplier": 3,
                        },
                        2: {
                            "adjacency_count": 0,
                            "lan_id": "R3.03",
                            "priority": {"local": "64", "dis": "none (no DIS elected)"},
                            "next_lan_iih_sec": 6,
                            "lsp_pacing_interval_ms": 33,
                            "psnp_entry_queue_size": 0,
                            "hello_interval_sec": 10,
                            "hello_multiplier": 3,
                        },
                    },
                    "clns_io": {
                        "protocol_state": "Up",
                        "mtu": 1497,
                        "snpa": "fa16.3eff.d6b3",
                        "layer2_mcast_groups_membership": {
                            "all_level_1_iss": "Yes",
                            "all_level_2_iss": "Yes",
                        },
                    },
                    "topology": {
                        "ipv4 unicast": {
                            "state": "Enabled",
                            "adjacency_formation": "Running",
                            "prefix_advertisement": "Running",
                            "metric": {"level": {1: 10, 2: 10}},
                            "weight": {"level": {1: 0, 2: 0}},
                            "mpls": {
                                "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                "ldp_sync": {"level": {1: "Disabled", 2: "Disabled"}},
                            },
                            "frr": {
                                "level": {
                                    1: {"state": "Not Enabled", "type": "None"},
                                    2: {"state": "Not Enabled", "type": "None"},
                                }
                            },
                        },
                        "ipv6 unicast": {
                            "state": "Enabled",
                            "adjacency_formation": "Running",
                            "prefix_advertisement": "Running",
                            "metric": {"level": {1: 10, 2: 10}},
                            "weight": {"level": {1: 0, 2: 0}},
                            "mpls": {
                                "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                "ldp_sync": {"level": {1: "Disabled", 2: "Disabled"}},
                            },
                            "frr": {
                                "level": {
                                    1: {"state": "Not Enabled", "type": "None"},
                                    2: {"state": "Not Enabled", "type": "None"},
                                }
                            },
                        },
                    },
                    "address_family": {
                        "IPv4": {
                            "state": "Enabled",
                            "protocol_state": "Up",
                            "forwarding_address": ["10.3.4.3"],
                            "global_prefix": ["10.3.4.0/24"],
                        },
                        "IPv6": {
                            "state": "Enabled",
                            "protocol_state": "Up",
                            "forwarding_address": ["fe80::f816:3eff:feff:d6b3"],
                            "global_prefix": [
                                "None (No global addresses are configured)"
                            ],
                        },
                    },
                    "lsp": {
                        "transmit_timer_expires_ms": 0,
                        "transmission_state": "idle",
                        "lsp_transmit_back_to_back_limit_window_msec": 0,
                        "lsp_transmit_back_to_back_limit": 9,
                    },
                },
                "GigabitEthernet0/0/0/3": {
                    "state": "Enabled",
                    "adjacency_formation": "Enabled",
                    "prefix_advertisement": "Enabled",
                    "ipv4_bfd": False,
                    "ipv6_bfd": False,
                    "bfd_min_interval": 150,
                    "bfd_multiplier": 3,
                    "bandwidth": 1000000,
                    "circuit_type": "level-1-2",
                    "media_type": "LAN",
                    "circuit_number": 1,
                    "level": {
                        1: {
                            "adjacency_count": 1,
                            "lan_id": "R5.01",
                            "priority": {"local": "64", "dis": "64"},
                            "next_lan_iih_sec": 3,
                            "lsp_pacing_interval_ms": 33,
                            "psnp_entry_queue_size": 0,
                            "hello_interval_sec": 10,
                            "hello_multiplier": 3,
                        },
                        2: {
                            "adjacency_count": 1,
                            "lan_id": "R5.01",
                            "priority": {"local": "64", "dis": "64"},
                            "next_lan_iih_sec": 2,
                            "lsp_pacing_interval_ms": 33,
                            "psnp_entry_queue_size": 0,
                            "hello_interval_sec": 10,
                            "hello_multiplier": 3,
                        },
                    },
                    "clns_io": {
                        "protocol_state": "Up",
                        "mtu": 1497,
                        "snpa": "fa16.3eff.f442",
                        "layer2_mcast_groups_membership": {
                            "all_level_1_iss": "Yes",
                            "all_level_2_iss": "Yes",
                        },
                    },
                    "topology": {
                        "ipv4 unicast": {
                            "state": "Enabled",
                            "adjacency_formation": "Running",
                            "prefix_advertisement": "Running",
                            "metric": {"level": {1: 10, 2: 10}},
                            "weight": {"level": {1: 0, 2: 0}},
                            "mpls": {
                                "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                "ldp_sync": {"level": {1: "Disabled", 2: "Disabled"}},
                            },
                            "frr": {
                                "level": {
                                    1: {"state": "Not Enabled", "type": "None"},
                                    2: {"state": "Not Enabled", "type": "None"},
                                }
                            },
                        },
                        "ipv6 unicast": {
                            "state": "Enabled",
                            "adjacency_formation": "Running",
                            "prefix_advertisement": "Running",
                            "metric": {"level": {1: 10, 2: 10}},
                            "weight": {"level": {1: 0, 2: 0}},
                            "mpls": {
                                "mpls_max_label_stack": "1/3/10 (PRI/BKP/SRTE)",
                                "ldp_sync": {"level": {1: "Disabled", 2: "Disabled"}},
                            },
                            "frr": {
                                "level": {
                                    1: {"state": "Not Enabled", "type": "None"},
                                    2: {"state": "Not Enabled", "type": "None"},
                                }
                            },
                        },
                    },
                    "address_family": {
                        "IPv4": {
                            "state": "Enabled",
                            "protocol_state": "Up",
                            "forwarding_address": ["10.3.5.3"],
                            "global_prefix": ["10.3.5.0/24"],
                        },
                        "IPv6": {
                            "state": "Enabled",
                            "protocol_state": "Up",
                            "forwarding_address": ["fe80::f816:3eff:feff:f442"],
                            "global_prefix": [
                                "None (No global addresses are configured)"
                            ],
                        },
                    },
                    "lsp": {
                        "transmit_timer_expires_ms": 0,
                        "transmission_state": "idle",
                        "lsp_transmit_back_to_back_limit_window_msec": 0,
                        "lsp_transmit_back_to_back_limit": 9,
                    },
                },
                "tunnel-te105": {
                    "state": "Enabled",
                    "adjacency_formation": "Disabled",
                    "prefix_advertisement": "Enabled",
                    "ipv4_bfd": False,
                    "ipv6_bfd": False,
                    "bfd_min_interval": 150,
                    "bfd_multiplier": 3,
                    "rsi_srlg": "Registered",
                    "bandwidth": 0,
                    "circuit_type": "level-2-only",
                    "media_type": "P2P",
                    "circuit_number": 0,
                    "clns_io": {
                        "protocol_state": "Down (IMD did not notify that node exists)",
                        "mtu": -1,
                    },
                    "topology": {
                        "ipv4 unicast": {
                            "state": "Enabled",
                            "adjacency_formation": "Disabled",
                            "prefix_advertisement": "Running",
                            "metric": {"level": {1: 10, 2: 10}},
                            "weight": {"level": {1: 0, 2: 0}},
                            "mpls": {
                                "mpls_max_label_stack": "1/1/10/10 (PRI/BKP/SRTE/SRAT)",
                                "ldp_sync": {"level": {1: "Enabled", 2: "Enabled"}, 'status': 'Achieved'},
                            },
                            "frr": {
                                "level": {
                                    1: {"state": "Not Enabled", "type": "None"},
                                    2: {"state": "Not Enabled", "type": "None"},
                                }
                            },
                        }
                    },
                    "address_family": {
                        "IPv4": {
                            "state": "Enabled",
                            "protocol_state": "Up",
                            "forwarding_address": ["10.3.5.3"],
                            "global_prefix": ["None (Interface is unnumbered)"],
                        }
                    },
                },
            }
        }
    }
}
