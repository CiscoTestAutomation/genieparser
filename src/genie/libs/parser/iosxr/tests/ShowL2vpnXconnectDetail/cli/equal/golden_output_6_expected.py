expected_output = {
    "group": {
        "EVPL-ACCT1412-VRF0301412-CoS": {
            "xc": {
                "VRF331412.12:14": {
                    "state": "up",
                    "interworking": "none",
                    "local_ce_id": 12,
                    "remote_ce_id": 14,
                    "discovery_state": "Advertised",
                    "ac": {
                        "TenGigE0/0/0/2.1412": {
                            "state": "up",
                            "type": "VLAN",
                            "num_ranges": 1,
                            "rewrite_tags": "",
                            "vlan_ranges": [
                                "1412",
                                "1412"
                            ],
                            "mtu": 9086,
                            "xc_id": "0x120000a",
                            "interworking": "none",
                            "statistics": {
                                "packet_totals": {
                                    "receive": 281821766,
                                    "send": 282110318
                                },
                                "byte_totals": {
                                    "receive": 394493304868,
                                    "send": 394895862950
                                },
                                "drops": {
                                    "illegal_vlan": 0,
                                    "illegal_length": 0
                                }
                            }
                        }
                    },
                    "pw": {
                        "neighbor": {
                            "8.33.10.3": {
                                "id": {
                                    786446: {
                                        "state": "up ( established )",
                                        "pw_class": "not set",
                                        "xc_id": "0xa0000005",
                                        "encapsulation": "MPLS",
                                        "protocol": "BGP",
                                        "source_address": "8.33.10.8",
                                        "backup_disable_delay": 0,
                                        "sequencing": "not set",
                                        "lsp": "Up",
                                        "load_balancing_hashing": "src-dst-ip",
                                        "configured_tx": 1,
                                        "configured_rx": 1,
                                        "negotiated_tx": 1,
                                        "negotiated_rx": 1,
                                        "mpls": {
                                            "label": {
                                                "local": "24438",
                                                "remote": "524283"
                                            },
                                            "mtu": {
                                                "local": "9086",
                                                "remote": "9082"
                                            },
                                            "control_word": {
                                                "local": "enabled",
                                                "remote": "enabled"
                                            },
                                            "pw_type": {
                                                "local": "Ethernet VLAN",
                                                "remote": "Ethernet VLAN"
                                            },
                                            "ce_id": {
                                                "local": "12",
                                                "remote": "14"
                                            }
                                        },
                                        "create_time": "26/07/2023 14:30:00 (9w1d ago)",
                                        "last_time_status_changed": "12/09/2023 19:10:58 (2w2d ago)",
                                        "statistics": {
                                            "packet_totals": {
                                                "receive": 282110318,
                                                "send": 281821766
                                            },
                                            "byte_totals": {
                                                "receive": 394895862950,
                                                "send": 394493304868
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
