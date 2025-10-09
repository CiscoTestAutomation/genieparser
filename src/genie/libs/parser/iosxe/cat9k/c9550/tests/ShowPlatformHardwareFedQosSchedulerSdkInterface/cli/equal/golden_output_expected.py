expected_output = {
    "interface": {
        "FiftyGigE2/0/31": {
            "interface_id": "0x4DD",
            "priority_propagation": "Disabled",
            "sub_interface_q_mode": "Disabled - No Priority Propagation",
            "logical_port": "Disabled",
            "tc_profile": {
                "sdk_oid": 164,
                "tc": {
                    "tc0": {
                        "voq_offset": 0
                    },
                    "tc1": {
                        "voq_offset": 1
                    },
                    "tc2": {
                        "voq_offset": 2
                    },
                    "tc3": {
                        "voq_offset": 3
                    },
                    "tc4": {
                        "voq_offset": 4
                    },
                    "tc5": {
                        "voq_offset": 5
                    },
                    "tc6": {
                        "voq_offset": 6
                    },
                    "tc7": {
                        "voq_offset": 7
                    }
                }
            },
            "interface_scheduler": {
                "oid": {
                    "1941": {
                        "ct_r": {
                            "C-R": {
                                "cir": 10506840064,
                                "eir_pir": 10506840064,
                                "is_eir": "PIR",
                                "wfq_weights": "C(16  ) E(16  )",
                                "hw_id": 1941
                            },
                            "T-R": {
                                "cir": 10506840064,
                                "eir_pir": 10506840064,
                                "is_eir": "PIR",
                                "wfq_weights": "C(16  ) E(16  )",
                                "hw_id": 1941
                            }
                        }
                    }
                }
            },
            "system_port_scheduler": {
                "oid": {
                    "1945": {
                        "c_pb": {
                            "M-B/W": {
                                "cir": 122149,
                                "burst": 0,
                                "tx_cir": 122149,
                                "tx_burst": 0,
                                "eir_wfq": 1,
                                "act_wfq": 63,
                                "pg_type": "OQPG-0",
                                "child_oid": {
                                    "1946": {
                                        "child_type": "OQHSE"
                                    },
                                    "1947": {
                                        "child_type": "OQHSE"
                                    },
                                    "1948": {
                                        "child_type": "OQHSE"
                                    },
                                    "1949": {
                                        "child_type": "OQHSE"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "oqhse_scheduler": {
                "oid": {
                    "1946": {
                        "mode": "2-I",
                        "cep_ir": {
                            "CIR": {
                                "rate": "969381120",
                                "burst": "8",
                                "type": "PARENT",
                                "weight": 63,
                                "hw_id": 124,
                                "hse_type": "Sys-P SCH",
                                "hse_oid": 0,
                                "link_point": "OQPG-1"
                            },
                            "PIR": {
                                "rate": "1438436480",
                                "burst": "8",
                                "type": "PARENT",
                                "weight": 63,
                                "hw_id": 124,
                                "hse_type": "Sys-P SCH",
                                "hse_oid": 0,
                                "link_point": "OQPG-0"
                            }
                        },
                        "child_group": {
                            0: {
                                "branch": "Left",
                                "load_balance_type": {
                                    "SP": {
                                        "s": 0,
                                        "c": 2
                                    },
                                    "WFQ": {
                                        "s": 2,
                                        "c": 2
                                    }
                                },
                                "weights": [
                                    0,
                                    0,
                                    255,
                                    255,
                                    0,
                                    0,
                                    0,
                                    0
                                ],
                                "child": {
                                    0: {
                                        "link": {
                                            "SP-Link": {
                                                "link_point": 1
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 990
                                    },
                                    1: {
                                        "link": {
                                            "RR/WFQ-Link": {
                                                "link_point": 3
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 990
                                    }
                                }
                            },
                            1: {
                                "branch": "Right",
                                "load_balance_type": {
                                    "SP": {
                                        "s": 4,
                                        "c": 2
                                    },
                                    "WFQ": {
                                        "s": 6,
                                        "c": 2
                                    }
                                },
                                "weights": [
                                    0,
                                    0,
                                    255,
                                    255,
                                    0,
                                    0,
                                    0,
                                    0
                                ],
                                "child": {
                                    0: {
                                        "link": {
                                            "SP-Link": {
                                                "link_point": 5
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 984
                                    },
                                    1: {
                                        "link": {
                                            "RR/WFQ-Link": {
                                                "link_point": 7
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 984
                                    }
                                }
                            }
                        }
                    },
                    "1947": {
                        "mode": "2-I",
                        "cep_ir": {
                            "CIR": {
                                "rate": "969381120",
                                "burst": "8",
                                "type": "PARENT",
                                "weight": 63,
                                "hw_id": 125,
                                "hse_type": "Sys-P SCH",
                                "hse_oid": 0,
                                "link_point": "OQPG-3"
                            },
                            "PIR": {
                                "rate": "969381120",
                                "burst": "8",
                                "type": "PARENT",
                                "weight": 63,
                                "hw_id": 125,
                                "hse_type": "Sys-P SCH",
                                "hse_oid": 0,
                                "link_point": "OQPG-2"
                            }
                        },
                        "child_group": {
                            0: {
                                "branch": "Left",
                                "load_balance_type": {
                                    "SP": {
                                        "s": 0,
                                        "c": 2
                                    },
                                    "WFQ": {
                                        "s": 2,
                                        "c": 2
                                    }
                                },
                                "weights": [
                                    0,
                                    0,
                                    255,
                                    255,
                                    0,
                                    0,
                                    0,
                                    0
                                ],
                                "child": {
                                    0: {
                                        "link": {
                                            "SP-Link": {
                                                "link_point": 1
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 1952
                                    },
                                    1: {
                                        "link": {
                                            "RR/WFQ-Link": {
                                                "link_point": 3
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 1952
                                    }
                                }
                            },
                            1: {
                                "branch": "Right",
                                "load_balance_type": {
                                    "SP": {
                                        "s": 4,
                                        "c": 2
                                    },
                                    "WFQ": {
                                        "s": 6,
                                        "c": 2
                                    }
                                },
                                "weights": [
                                    0,
                                    0,
                                    255,
                                    255,
                                    0,
                                    0,
                                    0,
                                    0
                                ],
                                "child": {
                                    0: {
                                        "link": {
                                            "SP-Link": {
                                                "link_point": 5
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 1951
                                    },
                                    1: {
                                        "link": {
                                            "RR/WFQ-Link": {
                                                "link_point": 7
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 1951
                                    }
                                }
                            }
                        }
                    },
                    "1948": {
                        "mode": "2-I",
                        "cep_ir": {
                            "CIR": {
                                "rate": "969381120",
                                "burst": "8",
                                "type": "PARENT",
                                "weight": 63,
                                "hw_id": 126,
                                "hse_type": "Sys-P SCH",
                                "hse_oid": 0,
                                "link_point": "OQPG-5"
                            },
                            "PIR": {
                                "rate": "969381120",
                                "burst": "8",
                                "type": "PARENT",
                                "weight": 63,
                                "hw_id": 126,
                                "hse_type": "Sys-P SCH",
                                "hse_oid": 0,
                                "link_point": "OQPG-4"
                            }
                        },
                        "child_group": {
                            0: {
                                "branch": "Left",
                                "load_balance_type": {
                                    "SP": {
                                        "s": 0,
                                        "c": 2
                                    },
                                    "WFQ": {
                                        "s": 2,
                                        "c": 2
                                    }
                                },
                                "weights": [
                                    0,
                                    0,
                                    255,
                                    255,
                                    0,
                                    0,
                                    0,
                                    0
                                ],
                                "child": {
                                    0: {
                                        "link": {
                                            "SP-Link": {
                                                "link_point": 1
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 1954
                                    },
                                    1: {
                                        "link": {
                                            "RR/WFQ-Link": {
                                                "link_point": 3
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 1954
                                    }
                                }
                            },
                            1: {
                                "branch": "Right",
                                "load_balance_type": {
                                    "SP": {
                                        "s": 4,
                                        "c": 2
                                    },
                                    "WFQ": {
                                        "s": 6,
                                        "c": 2
                                    }
                                },
                                "weights": [
                                    0,
                                    0,
                                    255,
                                    255,
                                    0,
                                    0,
                                    0,
                                    0
                                ],
                                "child": {
                                    0: {
                                        "link": {
                                            "SP-Link": {
                                                "link_point": 5
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 1953
                                    },
                                    1: {
                                        "link": {
                                            "RR/WFQ-Link": {
                                                "link_point": 7
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 1953
                                    }
                                }
                            }
                        }
                    },
                    "1949": {
                        "mode": "2-I",
                        "cep_ir": {
                            "CIR": {
                                "rate": "1938762240",
                                "burst": "8",
                                "type": "PARENT",
                                "weight": 63,
                                "hw_id": 127,
                                "hse_type": "Sys-P SCH",
                                "hse_oid": 0,
                                "link_point": "OQPG-7"
                            },
                            "PIR": {
                                "rate": "9506189312",
                                "burst": "8",
                                "type": "PARENT",
                                "weight": 63,
                                "hw_id": 127,
                                "hse_type": "Sys-P SCH",
                                "hse_oid": 0,
                                "link_point": "OQPG-6"
                            }
                        },
                        "child_group": {
                            0: {
                                "branch": "Left",
                                "load_balance_type": {
                                    "SP": {
                                        "s": 0,
                                        "c": 2
                                    },
                                    "WFQ": {
                                        "s": 2,
                                        "c": 2
                                    }
                                },
                                "weights": [
                                    0,
                                    0,
                                    255,
                                    255,
                                    0,
                                    0,
                                    0,
                                    0
                                ],
                                "child": {
                                    0: {
                                        "link": {
                                            "SP-Link": {
                                                "link_point": 1
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 1956
                                    },
                                    1: {
                                        "link": {
                                            "RR/WFQ-Link": {
                                                "link_point": 3
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 1956
                                    }
                                }
                            },
                            1: {
                                "branch": "Right",
                                "load_balance_type": {
                                    "SP": {
                                        "s": 4,
                                        "c": 2
                                    },
                                    "WFQ": {
                                        "s": 6,
                                        "c": 2
                                    }
                                },
                                "weights": [
                                    0,
                                    0,
                                    255,
                                    255,
                                    0,
                                    0,
                                    0,
                                    0
                                ],
                                "child": {
                                    0: {
                                        "link": {
                                            "SP-Link": {
                                                "link_point": 5
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 1955
                                    },
                                    1: {
                                        "link": {
                                            "RR/WFQ-Link": {
                                                "link_point": 7
                                            }
                                        },
                                        "hse_type": "SVCSE",
                                        "hse_oid": 1955
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "cstse_scheduler": {},
            "svcse_scheduler": {
                "oid": {
                    "984": {
                        "cep_ir": {
                            "CIR": {
                                "rate": "UNLIMITED",
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41008,
                                "hse_type": "OQHSE",
                                "hse_oid": 1946,
                                "link_point": 5
                            },
                            "PIR": {
                                "rate": 1438436480,
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41008,
                                "hse_type": "OQHSE",
                                "hse_oid": 1946,
                                "link_point": 7
                            }
                        },
                        "child": {
                            "hse_oid": {
                                "416": {
                                    "voq_id": 29024,
                                    "in_device": 1,
                                    "in_slice": 0,
                                    "hse_type": "VSC"
                                },
                                "480": {
                                    "voq_id": 29024,
                                    "in_device": 1,
                                    "in_slice": 1,
                                    "hse_type": "VSC"
                                }
                            }
                        }
                    },
                    "990": {
                        "cep_ir": {
                            "CIR": {
                                "rate": "UNLIMITED",
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41009,
                                "hse_type": "OQHSE",
                                "hse_oid": 1946,
                                "link_point": 1
                            },
                            "PIR": {
                                "rate": 969381120,
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41009,
                                "hse_type": "OQHSE",
                                "hse_oid": 1946,
                                "link_point": 3
                            }
                        },
                        "child": {
                            "hse_oid": {
                                "417": {
                                    "voq_id": 29025,
                                    "in_device": 1,
                                    "in_slice": 0,
                                    "hse_type": "VSC"
                                },
                                "481": {
                                    "voq_id": 29025,
                                    "in_device": 1,
                                    "in_slice": 1,
                                    "hse_type": "VSC"
                                }
                            }
                        }
                    },
                    "1952": {
                        "cep_ir": {
                            "CIR": {
                                "rate": "UNLIMITED",
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41011,
                                "hse_type": "OQHSE",
                                "hse_oid": 1947,
                                "link_point": 1
                            },
                            "PIR": {
                                "rate": 969381120,
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41011,
                                "hse_type": "OQHSE",
                                "hse_oid": 1947,
                                "link_point": 3
                            }
                        },
                        "child": {
                            "hse_oid": {
                                "419": {
                                    "voq_id": 29027,
                                    "in_device": 1,
                                    "in_slice": 0,
                                    "hse_type": "VSC"
                                },
                                "483": {
                                    "voq_id": 29027,
                                    "in_device": 1,
                                    "in_slice": 1,
                                    "hse_type": "VSC"
                                }
                            }
                        }
                    },
                    "1951": {
                        "cep_ir": {
                            "CIR": {
                                "rate": "UNLIMITED",
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41010,
                                "hse_type": "OQHSE",
                                "hse_oid": 1947,
                                "link_point": 5
                            },
                            "PIR": {
                                "rate": 969381120,
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41010,
                                "hse_type": "OQHSE",
                                "hse_oid": 1947,
                                "link_point": 7
                            }
                        },
                        "child": {
                            "hse_oid": {
                                "418": {
                                    "voq_id": 29026,
                                    "in_device": 1,
                                    "in_slice": 0,
                                    "hse_type": "VSC"
                                },
                                "482": {
                                    "voq_id": 29026,
                                    "in_device": 1,
                                    "in_slice": 1,
                                    "hse_type": "VSC"
                                }
                            }
                        }
                    },
                    "1953": {
                        "cep_ir": {
                            "CIR": {
                                "rate": "UNLIMITED",
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41012,
                                "hse_type": "OQHSE",
                                "hse_oid": 1948,
                                "link_point": 5
                            },
                            "PIR": {
                                "rate": 969381120,
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41012,
                                "hse_type": "OQHSE",
                                "hse_oid": 1948,
                                "link_point": 7
                            }
                        },
                        "child": {
                            "hse_oid": {
                                "420": {
                                    "voq_id": 29028,
                                    "in_device": 1,
                                    "in_slice": 0,
                                    "hse_type": "VSC"
                                },
                                "484": {
                                    "voq_id": 29028,
                                    "in_device": 1,
                                    "in_slice": 1,
                                    "hse_type": "VSC"
                                }
                            }
                        }
                    },
                    "1954": {
                        "cep_ir": {
                            "CIR": {
                                "rate": "UNLIMITED",
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41013,
                                "hse_type": "OQHSE",
                                "hse_oid": 1948,
                                "link_point": 1
                            },
                            "PIR": {
                                "rate": 969381120,
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41013,
                                "hse_type": "OQHSE",
                                "hse_oid": 1948,
                                "link_point": 3
                            }
                        },
                        "child": {
                            "hse_oid": {
                                "421": {
                                    "voq_id": 29029,
                                    "in_device": 1,
                                    "in_slice": 0,
                                    "hse_type": "VSC"
                                },
                                "485": {
                                    "voq_id": 29029,
                                    "in_device": 1,
                                    "in_slice": 1,
                                    "hse_type": "VSC"
                                }
                            }
                        }
                    },
                    "1955": {
                        "cep_ir": {
                            "CIR": {
                                "rate": "UNLIMITED",
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41014,
                                "hse_type": "OQHSE",
                                "hse_oid": 1949,
                                "link_point": 5
                            },
                            "PIR": {
                                "rate": "UNLIMITED",
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41014,
                                "hse_type": "OQHSE",
                                "hse_oid": 1949,
                                "link_point": 7
                            }
                        },
                        "child": {
                            "hse_oid": {
                                "422": {
                                    "voq_id": 29030,
                                    "in_device": 1,
                                    "in_slice": 0,
                                    "hse_type": "VSC"
                                },
                                "486": {
                                    "voq_id": 29030,
                                    "in_device": 1,
                                    "in_slice": 1,
                                    "hse_type": "VSC"
                                }
                            }
                        }
                    },
                    "1956": {
                        "cep_ir": {
                            "CIR": {
                                "rate": 1938762240,
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41015,
                                "hse_type": "OQHSE",
                                "hse_oid": 1949,
                                "link_point": 1
                            },
                            "PIR": {
                                "rate": "UNLIMITED",
                                "burst": "DEFLT",
                                "type": "PARENT",
                                "weight": 255,
                                "hw_id": 41015,
                                "hse_type": "OQHSE",
                                "hse_oid": 1949,
                                "link_point": 3
                            }
                        },
                        "child": {
                            "hse_oid": {
                                "423": {
                                    "voq_id": 29031,
                                    "in_device": 1,
                                    "in_slice": 0,
                                    "hse_type": "VSC"
                                },
                                "487": {
                                    "voq_id": 29031,
                                    "in_device": 1,
                                    "in_slice": 1,
                                    "hse_type": "VSC"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}