expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "prefix": {
                        "10.4.16.16/32": {
                            "version": 13285,
                            "internal": "0x1000001 0x0 (ptr 0x78b55d78) [2], 0x0 (0x78b064d8), 0xa00 (0x7a1a60a8)",
                            "updated": "Oct 13 18:18:19.680",
                            "length": 32,
                            "traffic_index": 0,
                            "precedence": "n/a",
                            "priority": 3,
                            "gateway_array": {
                                "reference_count": 2,
                                "source_lsd": 5,
                                "backups": 1,
                                "flags": {
                                    "flag_count": 3,
                                    "flag_type": 4,
                                    "flag_internal": "0x108441 (0x793d4b28) ext 0x0 (0x0)]"
                                },
                                "LW-LDI": {
                                    "type": 1,
                                    "refc": 1,
                                    "ptr": "0x78b064d8",
                                    "sh_ldi": "0x793d4b28"
                                },
                                "update": {
                                    "type_time": 1,
                                    "updated_at": "Oct 13 18:18:19.680"
                                }
                            },
                            "ldi_update_time": "Oct 13 18:18:19.691",
                            "LW-LDI-TS": {
                                "datetime": "Oct 13 18:18:19.691",
                                "via_entries": {
                                    "0": {
                                        "via_address": "10.55.0.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 0,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b4cbf8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.0.2/32",
                                                "path_idx_via": "10.55.0.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.0.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.1",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "1": {
                                        "via_address": "10.55.1.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 1,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b4fbf8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.1.2/32",
                                                "path_idx_via": "10.55.1.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.1.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.2",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "2": {
                                        "via_address": "10.55.2.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 2,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b4fcb8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.2.2/32",
                                                "path_idx_via": "10.55.2.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.2.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.3",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "3": {
                                        "via_address": "10.55.3.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 3,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b4dbb8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.3.2/32",
                                                "path_idx_via": "10.55.3.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.3.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.4",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "4": {
                                        "via_address": "10.55.4.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 4,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b4fe38 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.4.2/32",
                                                "path_idx_via": "10.55.4.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.4.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.5",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "5": {
                                        "via_address": "10.55.5.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 5,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b691b8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.5.2/32",
                                                "path_idx_via": "10.55.5.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.5.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.6",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "6": {
                                        "via_address": "10.55.6.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 6,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b4cb38 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.6.2/32",
                                                "path_idx_via": "10.55.6.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.6.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.7",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "7": {
                                        "via_address": "10.55.7.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 7,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b4d4f8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.7.2/32",
                                                "path_idx_via": "10.55.7.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.7.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.8",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "8": {
                                        "via_address": "10.55.8.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 8,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b4ccb8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.8.2/32",
                                                "path_idx_via": "10.55.8.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.8.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.9",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "9": {
                                        "via_address": "10.55.9.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 9,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b4cd78 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.9.2/32",
                                                "path_idx_via": "10.55.9.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.9.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.10",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "10": {
                                        "via_address": "10.55.10.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 10,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b44c78 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.10.2/32",
                                                "path_idx_via": "10.55.10.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.10.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.11",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "11": {
                                        "via_address": "10.55.11.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 11,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b448b8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.11.2/32",
                                                "path_idx_via": "10.55.11.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.11.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.12",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "12": {
                                        "via_address": "10.55.12.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 12,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b4deb8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.12.2/32",
                                                "path_idx_via": "10.55.12.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.12.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.13",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "13": {
                                        "via_address": "10.55.13.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 13,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b44bb8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.13.2/32",
                                                "path_idx_via": "10.55.13.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.13.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.14",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "14": {
                                        "via_address": "10.55.14.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 14,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b43bf8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.14.2/32",
                                                "path_idx_via": "10.55.14.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.14.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.15",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "15": {
                                        "via_address": "10.55.15.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 15,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b4ca78 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.55.15.2/32",
                                                "path_idx_via": "10.55.15.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.55.15.2/32",
                                                    "local_label_nh_interface": "Te0/4/0/15.16",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "16": {
                                        "via_address": "10.1.0.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 16,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b504f8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.0.2/32",
                                                "path_idx_via": "10.1.0.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.0.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.1",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "17": {
                                        "via_address": "10.1.1.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 17,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b50138 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.1.2/32",
                                                "path_idx_via": "10.1.1.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.1.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.2",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "18": {
                                        "via_address": "10.1.2.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 18,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b55bf8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.2.2/32",
                                                "path_idx_via": "10.1.2.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.2.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.3",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "19": {
                                        "via_address": "10.1.3.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 19,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b50678 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.3.2/32",
                                                "path_idx_via": "10.1.3.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.3.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.4",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "20": {
                                        "via_address": "10.1.4.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 20,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b50738 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.4.2/32",
                                                "path_idx_via": "10.1.4.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.4.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.5",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "21": {
                                        "via_address": "10.1.5.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 21,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b50378 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.5.2/32",
                                                "path_idx_via": "10.1.5.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.5.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.6",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "22": {
                                        "via_address": "10.1.6.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 22,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b55b38 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.6.2/32",
                                                "path_idx_via": "10.1.6.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.6.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.7",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "23": {
                                        "via_address": "10.1.7.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 23,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b508b8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.7.2/32",
                                                "path_idx_via": "10.1.7.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.7.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.8",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "24": {
                                        "via_address": "10.1.8.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 24,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b50978 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.8.2/32",
                                                "path_idx_via": "10.1.8.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.8.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.9",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "25": {
                                        "via_address": "10.1.9.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 25,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b505b8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.9.2/32",
                                                "path_idx_via": "10.1.9.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.9.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.10",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "26": {
                                        "via_address": "10.1.10.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 26,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b55ef8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.10.2/32",
                                                "path_idx_via": "10.1.10.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.10.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.11",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "27": {
                                        "via_address": "10.1.11.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 27,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b69878 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.11.2/32",
                                                "path_idx_via": "10.1.11.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.11.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.12",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "28": {
                                        "via_address": "10.1.12.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 28,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b50bb8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.12.2/32",
                                                "path_idx_via": "10.1.12.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.12.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.13",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "29": {
                                        "via_address": "10.1.13.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 29,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b507f8 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.13.2/32",
                                                "path_idx_via": "10.1.13.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.13.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.14",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "30": {
                                        "via_address": "10.1.14.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 30,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b55e38 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.14.2/32",
                                                "path_idx_via": "10.1.14.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.14.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.15",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    },
                                    "31": {
                                        "via_address": "10.1.15.2/32",
                                        "dependencies": 4,
                                        "via_flags": "recursive",
                                        "path": {
                                            "path_idx": 31,
                                            "nhid": "0x0",
                                            "nhid_hex": "0x78b4e938 0x0",
                                            "path_idx_nh": {
                                                "path_idx_address": "10.1.15.2/32",
                                                "path_idx_via": "10.1.15.2/32",
                                                "local_label_nh": {
                                                    "local_label": 24006,
                                                    "local_label_nh_address": "10.1.15.2/32",
                                                    "local_label_nh_interface": "Te0/3/0/15.16",
                                                    "local_label_nh_labels": "None"
                                                }
                                            }
                                        }
                                    }
                                },
                                "weight_distribution": {
                                    "0": {
                                        "slot": 0,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "1": {
                                        "slot": 1,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "2": {
                                        "slot": 2,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "3": {
                                        "slot": 3,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "4": {
                                        "slot": 4,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "5": {
                                        "slot": 5,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "6": {
                                        "slot": 6,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "7": {
                                        "slot": 7,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "8": {
                                        "slot": 8,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "9": {
                                        "slot": 9,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "10": {
                                        "slot": 10,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "11": {
                                        "slot": 11,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "12": {
                                        "slot": 12,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "13": {
                                        "slot": 13,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "14": {
                                        "slot": 14,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "15": {
                                        "slot": 15,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "16": {
                                        "slot": 16,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "17": {
                                        "slot": 17,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "18": {
                                        "slot": 18,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "19": {
                                        "slot": 19,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "20": {
                                        "slot": 20,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "21": {
                                        "slot": 21,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "22": {
                                        "slot": 22,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "23": {
                                        "slot": 23,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "24": {
                                        "slot": 24,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "25": {
                                        "slot": 25,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "26": {
                                        "slot": 26,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "27": {
                                        "slot": 27,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "28": {
                                        "slot": 28,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "29": {
                                        "slot": 29,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "30": {
                                        "slot": 30,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    },
                                    "31": {
                                        "slot": 31,
                                        "weight": 1,
                                        "normalized_weight": 1,
                                        "class": 0
                                    }
                                },
                                "load_distribution": {
                                    "distribution": "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31",
                                    "refcount": 3,
                                    "0": {
                                        "hash": 0,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.0.2"
                                    },
                                    "1": {
                                        "hash": 1,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.1.2"
                                    },
                                    "2": {
                                        "hash": 2,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.2.2"
                                    },
                                    "3": {
                                        "hash": 3,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.3.2"
                                    },
                                    "4": {
                                        "hash": 4,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.4.2"
                                    },
                                    "5": {
                                        "hash": 5,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.5.2"
                                    },
                                    "6": {
                                        "hash": 6,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.6.2"
                                    },
                                    "7": {
                                        "hash": 7,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.7.2"
                                    },
                                    "8": {
                                        "hash": 8,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.8.2"
                                    },
                                    "9": {
                                        "hash": 9,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.9.2"
                                    },
                                    "10": {
                                        "hash": 10,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.10.2"
                                    },
                                    "11": {
                                        "hash": 11,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.11.2"
                                    },
                                    "12": {
                                        "hash": 12,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.12.2"
                                    },
                                    "13": {
                                        "hash": 13,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.13.2"
                                    },
                                    "14": {
                                        "hash": 14,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.14.2"
                                    },
                                    "15": {
                                        "hash": 15,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.55.15.2"
                                    },
                                    "16": {
                                        "hash": 16,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.0.2"
                                    },
                                    "17": {
                                        "hash": 17,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.1.2"
                                    },
                                    "18": {
                                        "hash": 18,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.2.2"
                                    },
                                    "19": {
                                        "hash": 19,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.3.2"
                                    },
                                    "20": {
                                        "hash": 20,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.4.2"
                                    },
                                    "21": {
                                        "hash": 21,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.5.2"
                                    },
                                    "22": {
                                        "hash": 22,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.6.2"
                                    },
                                    "23": {
                                        "hash": 23,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.7.2"
                                    },
                                    "24": {
                                        "hash": 24,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.8.2"
                                    },
                                    "25": {
                                        "hash": 25,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.9.2"
                                    },
                                    "26": {
                                        "hash": 26,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.10.2"
                                    },
                                    "27": {
                                        "hash": 27,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.11.2"
                                    },
                                    "28": {
                                        "hash": 28,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.12.2"
                                    },
                                    "29": {
                                        "hash": 29,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.13.2"
                                    },
                                    "30": {
                                        "hash": 30,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.14.2"
                                    },
                                    "31": {
                                        "hash": 31,
                                        "ok": "Y",
                                        "interface": "recursive",
                                        "address": "10.1.15.2"
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
