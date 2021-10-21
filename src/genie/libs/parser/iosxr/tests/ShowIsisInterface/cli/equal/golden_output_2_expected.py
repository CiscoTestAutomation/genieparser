

expected_output = {
    "instance": {
        "Genie": {
            "interface": {
                "Bundle-Ether2": {
                    "state": "Enabled",
                    "adjacency_formation": "Enabled",
                    "prefix_advertisement": "Disabled (Suppressed in IS-IS cfg)",
                    "ipv4_bfd": False,
                    "ipv6_bfd": False,
                    "bfd_min_interval": 150,
                    "bfd_multiplier": 3,
                    "rsi_srlg": "Registered",
                    "bandwidth": 100000000,
                    "circuit_type": "level-2-only",
                    "media_type": "P2P",
                    "circuit_number": 0,
                    "extended_circuit_number": 113,
                    "next_p2p_iih_in": 4,
                    "lsp_rexmit_queue_size": 1,
                    "level": {
                        2: {
                            "adjacency_count": 1,
                            "lsp_pacing_interval_ms": 33,
                            "psnp_entry_queue_size": 0,
                            "hello_interval_sec": 10,
                            "hello_multiplier": 3,
                        }
                    },
                    "clns_io": {
                        "protocol_state": "Up",
                        "mtu": 9199,
                        "snpa": "008a.96ff.1790",
                        "layer2_mcast_groups_membership": {
                            "all_level_1_iss": "Yes",
                            "all_level_2_iss": "Yes",
                        },
                    },
                    "topology": {
                        "ipv4 unicast": {
                            "state": "Enabled",
                            "adjacency_formation": "Running",
                            "prefix_advertisement": "Disabled (Intf suppressed in IS-IS cfg)",
                            "metric": {"level": {1: 10, 2: 10}},
                            "weight": {"level": {1: 0, 2: 0}},
                            "mpls": {
                                "mpls_max_label_stack": "3/3/12/0 (PRI/BKP/SRTE/SRAT)",
                                "ldp_sync": {"level": {1: "Disabled", 2: "Disabled"}},
                            },
                            "frr": {
                                "level": {
                                    1: {
                                        "state": "Enabled",
                                        "type": "per-prefix",
                                        "direct_lfa": {"state": "Enabled"},
                                        "remote_lfa": {
                                            "state": "Not Enabled",
                                            "tie_breaker": "Default",
                                            "line_card_disjoint": "30",
                                            "lowest_backup_metric": "20",
                                            "node_protecting": "40",
                                            "primary_path": "10",
                                        },
                                        "ti_lfa": {
                                            "state": "Enabled",
                                            "tie_breaker": "Default",
                                            "link_protecting": "Enabled",
                                            "line_card_disjoint": "0",
                                            "node_protecting": "100",
                                            "srlg_disjoint": "0",
                                        },
                                    },
                                    2: {
                                        "state": "Enabled",
                                        "type": "per-prefix",
                                        "direct_lfa": {"state": "Enabled"},
                                        "remote_lfa": {
                                            "state": "Not Enabled",
                                            "tie_breaker": "Default",
                                            "line_card_disjoint": "30",
                                            "lowest_backup_metric": "20",
                                            "node_protecting": "40",
                                            "primary_path": "10",
                                        },
                                        "ti_lfa": {
                                            "state": "Enabled",
                                            "tie_breaker": "Default",
                                            "link_protecting": "Enabled",
                                            "line_card_disjoint": "0",
                                            "node_protecting": "100",
                                            "srlg_disjoint": "0",
                                        },
                                    },
                                }
                            },
                        }
                    },
                    "address_family": {
                        "IPv4": {
                            "state": "Enabled",
                            "protocol_state": "Up",
                            "forwarding_address": ["172.18.0.1"],
                            "global_prefix": ["Unknown (Intf suppressed in IS-IS cfg)"],
                        }
                    },
                    "lsp": {
                        "transmit_timer_expires_ms": 0,
                        "transmission_state": "idle",
                        "lsp_transmit_back_to_back_limit_window_msec": 0,
                        "lsp_transmit_back_to_back_limit": 9,
                    },
                    "underlying_interface": {"HundredGigE0/0/0/1": {"index": "0x55"}},
                },
                "TenGigE0/0/0/0/0": {"state": "Disabled"},
                "TenGigE0/0/0/4/0": {
                    "state": "Enabled",
                    "adjacency_formation": "Enabled",
                    "prefix_advertisement": "Disabled (Suppressed in IS-IS cfg)",
                    "ipv4_bfd": True,
                    "ipv6_bfd": False,
                    "bfd_min_interval": 250,
                    "bfd_multiplier": 3,
                    "rsi_srlg": "Registered",
                    "bandwidth": 10000000,
                    "circuit_type": "level-2-only",
                    "media_type": "P2P",
                    "circuit_number": 0,
                    "extended_circuit_number": 27,
                    "next_p2p_iih_in": 5,
                    "lsp_rexmit_queue_size": 0,
                    "level": {
                        2: {
                            "adjacency_count": 1,
                            "lsp_pacing_interval_ms": 33,
                            "psnp_entry_queue_size": 0,
                            "hello_interval_sec": 10,
                            "hello_multiplier": 3,
                        }
                    },
                    "clns_io": {
                        "protocol_state": "Up",
                        "mtu": 9199,
                        "snpa": "008a.96ff.131b",
                        "layer2_mcast_groups_membership": {
                            "all_level_1_iss": "Yes",
                            "all_level_2_iss": "Yes",
                        },
                    },
                    "topology": {
                        "ipv4 unicast": {
                            "state": "Enabled",
                            "adjacency_formation": "Running",
                            "prefix_advertisement": "Disabled (Intf suppressed in IS-IS cfg)",
                            "metric": {"level": {1: 10, 2: 10}},
                            "weight": {"level": {1: 0, 2: 0}},
                            "mpls": {
                                "mpls_max_label_stack": "3/3/12/0 (PRI/BKP/SRTE/SRAT)",
                                "ldp_sync": {"level": {1: "Disabled", 2: "Disabled"}},
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
                            "forwarding_address": ["172.16.2.133"],
                            "global_prefix": ["Unknown (Intf suppressed in IS-IS cfg)"],
                        }
                    },
                    "lsp": {
                        "transmit_timer_expires_ms": 0,
                        "transmission_state": "idle",
                        "lsp_transmit_back_to_back_limit_window_msec": 0,
                        "lsp_transmit_back_to_back_limit": 9,
                    },
                },
            }
        }
    }
}
