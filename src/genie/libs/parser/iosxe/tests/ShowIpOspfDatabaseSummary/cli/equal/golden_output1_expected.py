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
                                                    "10.186.3.0 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.186.3.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 1,
                                                                            "mt_id": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.4.1.1",
                                                                "age": 422,
                                                                "checksum": "0x43DC",
                                                                "length": 28,
                                                                "lsa_id": "10.186.3.0",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC, Upward",
                                                                "seq_num": "80000001",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.186.3.0 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.186.3.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 40,
                                                                            "mt_id": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.36.3.3",
                                                                "age": 372,
                                                                "checksum": "0x6EA1",
                                                                "length": 28,
                                                                "lsa_id": "10.186.3.0",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, No DC, Upward",
                                                                "seq_num": "80000002",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.229.3.0 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.229.3.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 40,
                                                                            "mt_id": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.36.3.3",
                                                                "age": 372,
                                                                "checksum": "0x62AC",
                                                                "length": 28,
                                                                "lsa_id": "10.229.3.0",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, No DC, Upward",
                                                                "seq_num": "80000002",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.229.4.0 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.229.4.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 41,
                                                                            "mt_id": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.36.3.3",
                                                                "age": 131,
                                                                "checksum": "0x5DAD",
                                                                "length": 28,
                                                                "lsa_id": "10.229.4.0",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, No DC, Upward",
                                                                "seq_num": "80000004",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.19.4.0 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.19.4.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 40,
                                                                            "mt_id": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.36.3.3",
                                                                "age": 372,
                                                                "checksum": "0x4BC1",
                                                                "length": 28,
                                                                "lsa_id": "10.19.4.0",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, No DC, Upward",
                                                                "seq_num": "80000002",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.64.4.4 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.64.4.4",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.255",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 41,
                                                                            "mt_id": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.36.3.3",
                                                                "age": 131,
                                                                "checksum": "0xEF26",
                                                                "length": 28,
                                                                "lsa_id": "10.64.4.4",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, No DC, Upward",
                                                                "seq_num": "80000003",
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
                                                    "10.4.0.0 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.4.0.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.0.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 10,
                                                                            "mt_id": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.4.1.1",
                                                                "age": 424,
                                                                "checksum": "0x5CCA",
                                                                "length": 28,
                                                                "lsa_id": "10.4.0.0",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC, Upward",
                                                                "seq_num": "80000001",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.1.2.0 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.2.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 111,
                                                                            "mt_id": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.4.1.1",
                                                                "age": 422,
                                                                "checksum": "0xC6EF",
                                                                "length": 28,
                                                                "lsa_id": "10.1.2.0",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC, Upward",
                                                                "seq_num": "80000001",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.1.3.0 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.3.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 65535,
                                                                            "mt_id": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.4.1.1",
                                                                "age": 364,
                                                                "checksum": "0x5FC4",
                                                                "length": 28,
                                                                "lsa_id": "10.1.3.0",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC, Upward",
                                                                "seq_num": "80000002",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.2.3.0 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.2.3.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 65868,
                                                                            "mt_id": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.4.1.1",
                                                                "age": 365,
                                                                "checksum": "0x6174",
                                                                "length": 28,
                                                                "lsa_id": "10.2.3.0",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC, Upward",
                                                                "seq_num": "80000001",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.229.3.0 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.229.3.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 65575,
                                                                            "mt_id": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.4.1.1",
                                                                "age": 365,
                                                                "checksum": "0x628F",
                                                                "length": 28,
                                                                "lsa_id": "10.229.3.0",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC, Upward",
                                                                "seq_num": "80000001",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.229.4.0 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.229.4.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 65576,
                                                                            "mt_id": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.4.1.1",
                                                                "age": 130,
                                                                "checksum": "0x5D90",
                                                                "length": 28,
                                                                "lsa_id": "10.229.4.0",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC, Upward",
                                                                "seq_num": "80000003",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.19.4.0 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.19.4.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.0",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 65575,
                                                                            "mt_id": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.4.1.1",
                                                                "age": 365,
                                                                "checksum": "0x4BA4",
                                                                "length": 28,
                                                                "lsa_id": "10.19.4.0",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC, Upward",
                                                                "seq_num": "80000001",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.36.3.3 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.36.3.3",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.255",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 65536,
                                                                            "mt_id": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.4.1.1",
                                                                "age": 365,
                                                                "checksum": "0x8E97",
                                                                "length": 28,
                                                                "lsa_id": "10.36.3.3",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC, Upward",
                                                                "seq_num": "80000001",
                                                                "type": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.64.4.4 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.64.4.4",
                                                        "ospfv2": {
                                                            "body": {
                                                                "summary": {
                                                                    "network_mask": "255.255.255.255",
                                                                    "topologies": {
                                                                        0: {
                                                                            "metric": 65576,
                                                                            "mt_id": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.4.1.1",
                                                                "age": 130,
                                                                "checksum": "0xEF09",
                                                                "length": 28,
                                                                "lsa_id": "10.64.4.4",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC, Upward",
                                                                "seq_num": "80000002",
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
