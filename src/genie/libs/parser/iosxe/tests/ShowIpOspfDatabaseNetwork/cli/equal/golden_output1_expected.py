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
                                            2: {
                                                "lsa_type": 2,
                                                "lsas": {
                                                    "10.1.2.1 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.2.1",
                                                        "ospfv2": {
                                                            "body": {
                                                                "network": {
                                                                    "attached_routers": {
                                                                        "10.4.1.1": {},
                                                                        "10.16.2.2": {},
                                                                    },
                                                                    "network_mask": "255.255.255.0",
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.4.1.1",
                                                                "age": 786,
                                                                "checksum": "0x3DD0",
                                                                "length": 32,
                                                                "lsa_id": "10.1.2.1",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "8000000F",
                                                                "type": 2,
                                                            },
                                                        },
                                                    },
                                                    "10.1.4.4 10.64.4.4": {
                                                        "adv_router": "10.64.4.4",
                                                        "lsa_id": "10.1.4.4",
                                                        "ospfv2": {
                                                            "body": {
                                                                "network": {
                                                                    "attached_routers": {
                                                                        "10.4.1.1": {},
                                                                        "10.64.4.4": {},
                                                                    },
                                                                    "network_mask": "255.255.255.0",
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.64.4.4",
                                                                "age": 1496,
                                                                "checksum": "0xA431",
                                                                "length": 32,
                                                                "lsa_id": "10.1.4.4",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "8000002E",
                                                                "type": 2,
                                                            },
                                                        },
                                                    },
                                                    "10.2.3.3 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.2.3.3",
                                                        "ospfv2": {
                                                            "body": {
                                                                "network": {
                                                                    "attached_routers": {
                                                                        "10.16.2.2": {},
                                                                        "10.36.3.3": {},
                                                                    },
                                                                    "network_mask": "255.255.255.0",
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.36.3.3",
                                                                "age": 774,
                                                                "checksum": "0x2ACF",
                                                                "length": 32,
                                                                "lsa_id": "10.2.3.3",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "8000000F",
                                                                "type": 2,
                                                            },
                                                        },
                                                    },
                                                    "10.2.4.4 10.64.4.4": {
                                                        "adv_router": "10.64.4.4",
                                                        "lsa_id": "10.2.4.4",
                                                        "ospfv2": {
                                                            "body": {
                                                                "network": {
                                                                    "attached_routers": {
                                                                        "10.16.2.2": {},
                                                                        "10.64.4.4": {},
                                                                    },
                                                                    "network_mask": "255.255.255.0",
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.64.4.4",
                                                                "age": 747,
                                                                "checksum": "0x9E6",
                                                                "length": 32,
                                                                "lsa_id": "10.2.4.4",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "8000000F",
                                                                "type": 2,
                                                            },
                                                        },
                                                    },
                                                    "10.3.4.4 10.64.4.4": {
                                                        "adv_router": "10.64.4.4",
                                                        "lsa_id": "10.3.4.4",
                                                        "ospfv2": {
                                                            "body": {
                                                                "network": {
                                                                    "attached_routers": {
                                                                        "10.36.3.3": {},
                                                                        "10.64.4.4": {},
                                                                    },
                                                                    "network_mask": "255.255.255.0",
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.64.4.4",
                                                                "age": 992,
                                                                "checksum": "0xF0DA",
                                                                "length": 32,
                                                                "lsa_id": "10.3.4.4",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "8000002E",
                                                                "type": 2,
                                                            },
                                                        },
                                                    },
                                                },
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "2": {
                            "areas": {
                                "0.0.0.1": {
                                    "database": {
                                        "lsa_types": {
                                            2: {
                                                "lsa_type": 2,
                                                "lsas": {
                                                    "10.186.5.1 10.229.11.11": {
                                                        "adv_router": "10.229.11.11",
                                                        "lsa_id": "10.186.5.1",
                                                        "ospfv2": {
                                                            "body": {
                                                                "network": {
                                                                    "attached_routers": {
                                                                        "10.229.11.11": {},
                                                                        "10.115.55.55": {},
                                                                    },
                                                                    "network_mask": "255.255.255.0",
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.229.11.11",
                                                                "age": 1445,
                                                                "checksum": "0xDFD8",
                                                                "length": 32,
                                                                "lsa_id": "10.186.5.1",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "80000032",
                                                                "type": 2,
                                                            },
                                                        },
                                                    },
                                                    "10.229.6.6 10.84.66.66": {
                                                        "adv_router": "10.84.66.66",
                                                        "lsa_id": "10.229.6.6",
                                                        "ospfv2": {
                                                            "body": {
                                                                "network": {
                                                                    "attached_routers": {
                                                                        "10.151.22.22": {},
                                                                        "10.84.66.66": {},
                                                                    },
                                                                    "network_mask": "255.255.255.0",
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.84.66.66",
                                                                "age": 1073,
                                                                "checksum": "0x415E",
                                                                "length": 32,
                                                                "lsa_id": "10.229.6.6",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "8000000F",
                                                                "type": 2,
                                                            },
                                                        },
                                                    },
                                                    "10.19.7.7 10.1.77.77": {
                                                        "adv_router": "10.1.77.77",
                                                        "lsa_id": "10.19.7.7",
                                                        "ospfv2": {
                                                            "body": {
                                                                "network": {
                                                                    "attached_routers": {
                                                                        "10.36.3.3": {},
                                                                        "10.1.77.77": {},
                                                                    },
                                                                    "network_mask": "255.255.255.0",
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.1.77.77",
                                                                "age": 849,
                                                                "checksum": "0x5C19",
                                                                "length": 32,
                                                                "lsa_id": "10.19.7.7",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "8000002A",
                                                                "type": 2,
                                                            },
                                                        },
                                                    },
                                                    "10.115.6.6 10.84.66.66": {
                                                        "adv_router": "10.84.66.66",
                                                        "lsa_id": "10.115.6.6",
                                                        "ospfv2": {
                                                            "body": {
                                                                "network": {
                                                                    "attached_routers": {
                                                                        "10.115.55.55": {},
                                                                        "10.84.66.66": {},
                                                                    },
                                                                    "network_mask": "255.255.255.0",
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.84.66.66",
                                                                "age": 564,
                                                                "checksum": "0x619C",
                                                                "length": 32,
                                                                "lsa_id": "10.115.6.6",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "80000029",
                                                                "type": 2,
                                                            },
                                                        },
                                                    },
                                                    "10.166.7.6 10.84.66.66": {
                                                        "adv_router": "10.84.66.66",
                                                        "lsa_id": "10.166.7.6",
                                                        "ospfv2": {
                                                            "body": {
                                                                "network": {
                                                                    "attached_routers": {
                                                                        "10.84.66.66": {},
                                                                        "10.1.77.77": {},
                                                                    },
                                                                    "network_mask": "255.255.255.0",
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.84.66.66",
                                                                "age": 1845,
                                                                "checksum": "0x980A",
                                                                "length": 32,
                                                                "lsa_id": "10.166.7.6",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "8000002A",
                                                                "type": 2,
                                                            },
                                                        },
                                                    },
                                                },
                                            }
                                        }
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
