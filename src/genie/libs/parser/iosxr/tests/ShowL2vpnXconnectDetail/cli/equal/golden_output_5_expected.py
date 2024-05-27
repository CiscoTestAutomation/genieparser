expected_output = {
    "group": {
        "dopa": {
            "xc": {
                "dopa_479": {
                    "state": "up",
                    "interworking": "none",
                    "ac": {
                        "TenGigE0/0/0/4.479": {
                            "state": "up",
                            "type": "VLAN",
                            "num_ranges": 1,
                            "rewrite_tags": "",
                            "vlan_ranges": [
                                "479",
                                "479"
                            ],
                            "mtu": 1500,
                            "xc_id": "0x23",
                            "interworking": "none",
                            "statistics": {
                                "packet_totals": {
                                    "receive": 64003097,
                                    "send": 86457638
                                },
                                "byte_totals": {
                                    "receive": 30130317833,
                                    "send": 60438650194
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
                            "118.174.224.162": {
                                "id": {
                                    2047920479: {
                                        "state": "up ( established )",
                                        "pw_class": "EO_CON",
                                        "xc_id": "0xc000000d",
                                        "encapsulation": "MPLS",
                                        "protocol": "LDP",
                                        "source_address": "10.244.244.52",
                                        "type": "Ethernet",
                                        "control_word": "enabled",
                                        "interworking": "none",
                                        "backup_disable_delay": 0,
                                        "sequencing": "not set",
                                        "ignore_mtu_mismatch": "Disabled",
                                        "transmit_mtu_zero": "Disabled",
                                        "lsp": "Up",
                                        "status_tlv": "not set",
                                        "mpls": {
                                            "label": {
                                                "local": "24040",
                                                "remote": "27425"
                                            },
                                            "group_id": {
                                                "local": "0xe8",
                                                "remote": "0xe1"
                                            },
                                            "interface": {
                                                "local": "TenGigE0/0/0/4.479",
                                                "remote": "Access PW"
                                            },
                                            "mtu": {
                                                "local": "1500",
                                                "remote": "1500"
                                            },
                                            "control_word": {
                                                "local": "enabled",
                                                "remote": "enabled"
                                            },
                                            "pw_type": {
                                                "local": "Ethernet",
                                                "remote": "Ethernet"
                                            },
                                            "vccv_cv_type": {
                                                "local": "0x2",
                                                "remote": "0x2",
                                                "local_type": [
                                                    "LSP ping verification"
                                                ],
                                                "remote_type": [
                                                    "LSP ping verification"
                                                ]
                                            },
                                            "vccv_cc_type": {
                                                "local": "0x7",
                                                "remote": "0x7",
                                                "local_type": [
                                                    "control word",
                                                    "router alert label",
                                                    "TTL expiry"
                                                ],
                                                "remote_type": [
                                                    "control word",
                                                    "router alert label",
                                                    "TTL expiry"
                                                ]
                                            }
                                        },
                                        "create_time": "20/05/2023 21:31:34 (49w5d ago)",
                                        "last_time_status_changed": "13/03/2024 07:32:03 (7w1d ago)",
                                        "last_time_pw_went_down": "13/03/2024 07:31:51 (7w1d ago)",
                                        "statistics": {
                                            "packet_totals": {
                                                "receive": 86457638,
                                                "send": 64003097
                                            },
                                            "byte_totals": {
                                                "receive": 60438650194,
                                                "send": 30130317833
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "backup_pw": {
                        "neighbor": {
                            "118.174.224.24": {
                                "id": {
                                    2047920479: {
                                        "state": "standby ( all ready )",
                                        "pw_class": "EO_CON_Backup",
                                        "xc_id": "0xc000000a",
                                        "encapsulation": "MPLS",
                                        "protocol": "LDP",
                                        "source_address": "10.244.244.52",
                                        "type": "Ethernet",
                                        "control_word": "enabled",
                                        "interworking": "none",
                                        "sequencing": "not set",
                                        "ignore_mtu_mismatch": "Disabled",
                                        "transmit_mtu_zero": "Disabled",
                                        "lsp": "Up",
                                        "status_tlv": "not set",
                                        "mpls": {
                                            "label": {
                                                "local": "26612",
                                                "remote": "26577"
                                            },
                                            "group_id": {
                                                "local": "0xe8",
                                                "remote": "0xc"
                                            },
                                            "interface": {
                                                "local": "TenGigE0/0/0/4.479",
                                                "remote": "Access PW"
                                            },
                                            "mtu": {
                                                "local": "1500",
                                                "remote": "1500"
                                            },
                                            "control_word": {
                                                "local": "enabled",
                                                "remote": "enabled"
                                            },
                                            "pw_type": {
                                                "local": "Ethernet",
                                                "remote": "Ethernet"
                                            },
                                            "vccv_cv_type": {
                                                "local": "0x2",
                                                "remote": "0x2",
                                                "local_type": [
                                                    "LSP ping verification"
                                                ],
                                                "remote_type": [
                                                    "LSP ping verification"
                                                ]
                                            },
                                            "vccv_cc_type": {
                                                "local": "0x7",
                                                "remote": "0x7",
                                                "local_type": [
                                                    "control word",
                                                    "router alert label",
                                                    "TTL expiry"
                                                ],
                                                "remote_type": [
                                                    "control word",
                                                    "router alert label",
                                                    "TTL expiry"
                                                ]
                                            }
                                        },
                                        "create_time": "10/04/2024 08:25:03 (3w1d ago)",
                                        "last_time_status_changed": "10/04/2024 08:25:03 (3w1d ago)"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "polis": {
            "xc": {
                "polis_434": {
                    "state": "up",
                    "interworking": "none",
                    "ac": {
                        "TenGigE0/0/0/4.434": {
                            "state": "up",
                            "type": "VLAN",
                            "num_ranges": 1,
                            "rewrite_tags": "",
                            "vlan_ranges": [
                                "434",
                                "434"
                            ],
                            "mtu": 1500,
                            "xc_id": "0x21",
                            "interworking": "none",
                            "statistics": {
                                "packet_totals": {
                                    "receive": 106049084,
                                    "send": 88219312
                                },
                                "byte_totals": {
                                    "receive": 10704088231,
                                    "send": 24897725734
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
                            "118.174.224.162": {
                                "id": {
                                    104340434: {
                                        "state": "up ( established )",
                                        "pw_class": "EO_CON",
                                        "xc_id": "0xc000000e",
                                        "encapsulation": "MPLS",
                                        "protocol": "LDP",
                                        "source_address": "10.244.244.52",
                                        "type": "Ethernet",
                                        "control_word": "enabled",
                                        "interworking": "none",
                                        "backup_disable_delay": 0,
                                        "sequencing": "not set",
                                        "ignore_mtu_mismatch": "Disabled",
                                        "transmit_mtu_zero": "Disabled",
                                        "lsp": "Up",
                                        "status_tlv": "not set",
                                        "mpls": {
                                            "label": {
                                                "local": "24038",
                                                "remote": "27442"
                                            },
                                            "group_id": {
                                                "local": "0xe8",
                                                "remote": "0xd7"
                                            },
                                            "monitor_interface": {
                                                "local": "TenGigE0/0/0/4.434",
                                                "remote": "Access PW"
                                            },
                                            "mtu": {
                                                "local": "1500",
                                                "remote": "1500"
                                            },
                                            "control_word": {
                                                "local": "enabled",
                                                "remote": "enabled"
                                            },
                                            "pw_type": {
                                                "local": "Ethernet",
                                                "remote": "Ethernet"
                                            },
                                            "vccv_cv_type": {
                                                "local": "0x2",
                                                "remote": "0x2",
                                                "local_type": [
                                                    "LSP ping verification"
                                                ],
                                                "remote_type": [
                                                    "LSP ping verification"
                                                ]
                                            },
                                            "vccv_cc_type": {
                                                "local": "0x7",
                                                "remote": "0x7",
                                                "local_type": [
                                                    "control word",
                                                    "router alert label",
                                                    "TTL expiry"
                                                ],
                                                "remote_type": [
                                                    "control word",
                                                    "router alert label",
                                                    "TTL expiry"
                                                ]
                                            }
                                        },
                                        "create_time": "20/05/2023 21:31:34 (49w5d ago)",
                                        "last_time_status_changed": "13/03/2024 07:32:03 (7w1d ago)",
                                        "last_time_pw_went_down": "13/03/2024 07:31:51 (7w1d ago)",
                                        "statistics": {
                                            "packet_totals": {
                                                "receive": 88219312,
                                                "send": 106049084
                                            },
                                            "byte_totals": {
                                                "receive": 24897725734,
                                                "send": 10704088231
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