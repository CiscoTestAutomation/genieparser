

expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "1": {
                            "areas": {
                                "0.0.0.0": {
                                    "database": {
                                        "lsa_types": {
                                            3: {
                                                "lsa_type": 3,
                                                "lsas": {
                                                    "10.186.3.0 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.186.3.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 65575,
                                                                            "mt_id": 0,
                                                                            "tos": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.16.2.2",
                                                                "age": 520,
                                                                "checksum": "0xaa4a",
                                                                "length": 28,
                                                                "lsa_id": "10.186.3.0",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "DC",
                                                                "seq_num": "80000001",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.229.3.0 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.229.3.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 65535,
                                                                            "mt_id": 0,
                                                                            "tos": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.16.2.2",
                                                                "age": 519,
                                                                "checksum": "0xd0e",
                                                                "length": 28,
                                                                "lsa_id": "10.229.3.0",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "DC",
                                                                "seq_num": "80000002",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.229.4.0 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.229.4.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 65535,
                                                                            "mt_id": 0,
                                                                            "tos": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.16.2.2",
                                                                "age": 297,
                                                                "checksum": "0x218",
                                                                "length": 28,
                                                                "lsa_id": "10.229.4.0",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "DC",
                                                                "seq_num": "80000002",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.19.4.0 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.19.4.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 65536,
                                                                            "mt_id": 0,
                                                                            "tos": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.16.2.2",
                                                                "age": 294,
                                                                "checksum": "0xfd1a",
                                                                "length": 28,
                                                                "lsa_id": "10.19.4.0",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "DC",
                                                                "seq_num": "80000002",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.64.4.4 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.64.4.4",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.255",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 65536,
                                                                            "mt_id": 0,
                                                                            "tos": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.16.2.2",
                                                                "age": 295,
                                                                "checksum": "0x9c87",
                                                                "length": 28,
                                                                "lsa_id": "10.64.4.4",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "DC",
                                                                "seq_num": "80000001",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                },
                                            }
                                        }
                                    }
                                },
                                "0.0.0.1": {
                                    "database": {
                                        "lsa_types": {
                                            3: {
                                                "lsa_type": 3,
                                                "lsas": {
                                                    "10.1.2.0 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.1.2.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 4294,
                                                                            "mt_id": 0,
                                                                            "tos": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.16.2.2",
                                                                "age": 675,
                                                                "checksum": "0xfc54",
                                                                "length": 28,
                                                                "lsa_id": "10.1.2.0",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "DC",
                                                                "seq_num": "80000001",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.1.2.0 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.1.2.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 151,
                                                                            "mt_id": 0,
                                                                            "tos": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.36.3.3",
                                                                "age": 521,
                                                                "checksum": "0x5655",
                                                                "length": 28,
                                                                "lsa_id": "10.1.2.0",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "No "
                                                                "DC",
                                                                "seq_num": "80000002",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.1.3.0 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.1.3.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 40,
                                                                            "mt_id": 0,
                                                                            "tos": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.36.3.3",
                                                                "age": 531,
                                                                "checksum": "0xf029",
                                                                "length": 28,
                                                                "lsa_id": "10.1.3.0",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "No "
                                                                "DC",
                                                                "routing_bit_enable": True,
                                                                "seq_num": "80000002",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.2.3.0 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.2.3.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 222,
                                                                            "mt_id": 0,
                                                                            "tos": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.16.2.2",
                                                                "age": 675,
                                                                "checksum": "0x4601",
                                                                "length": 28,
                                                                "lsa_id": "10.2.3.0",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "DC",
                                                                "seq_num": "80000001",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.2.3.0 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.2.3.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 262,
                                                                            "mt_id": 0,
                                                                            "tos": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.36.3.3",
                                                                "age": 287,
                                                                "checksum": "0x96a2",
                                                                "length": 28,
                                                                "lsa_id": "10.2.3.0",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "No "
                                                                "DC",
                                                                "seq_num": "80000003",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.16.2.2 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.16.2.2",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.255",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 1,
                                                                            "mt_id": 0,
                                                                            "tos": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.16.2.2",
                                                                "age": 676,
                                                                "checksum": "0xfa31",
                                                                "length": 28,
                                                                "lsa_id": "10.16.2.2",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "DC",
                                                                "seq_num": "80000001",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.36.3.3 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.36.3.3",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.255",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 1,
                                                                            "mt_id": 0,
                                                                            "tos": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.36.3.3",
                                                                "age": 531,
                                                                "checksum": "0x8eb4",
                                                                "length": 28,
                                                                "lsa_id": "10.36.3.3",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "No "
                                                                "DC",
                                                                "routing_bit_enable": True,
                                                                "seq_num": "80000002",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.94.44.44 10.64.4.4": {
                                                        "adv_router": "10.64.4.4",
                                                        "lsa_id": "10.94.44.44",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.255",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 1,
                                                                            "mt_id": 0,
                                                                            "tos": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.64.4.4",
                                                                "age": 291,
                                                                "checksum": "0x2b50",
                                                                "length": 28,
                                                                "lsa_id": "10.94.44.44",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "DC",
                                                                "routing_bit_enable": True,
                                                                "seq_num": "80000001",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                },
                                            }
                                        }
                                    }
                                },
                            }
                        }
                    }
                }
            }
        }
    }
}
