expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "65109": {
                            "areas": {
                                "0.0.0.8": {
                                    "database": {
                                        "lsa_types": {
                                            1: {
                                                "lsa_type": 1,
                                                "lsas": {
                                                    "192.168.165.220": {
                                                        "adv_router": "192.168.165.220",
                                                        "lsa_id": "192.168.165.220",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "192.168.165.220",
                                                                "age": 113,
                                                                "checksum": "0x007C93",
                                                                "link_count": 2,
                                                                "lsa_id": "192.168.165.220",
                                                                "seq_num": "0x800006E3",
                                                            }
                                                        },
                                                    },
                                                    "192.168.255.0": {
                                                        "adv_router": "192.168.255.0",
                                                        "lsa_id": "192.168.255.0",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "192.168.255.0",
                                                                "age": 1407,
                                                                "checksum": "0x00ADD6",
                                                                "link_count": 501,
                                                                "lsa_id": "192.168.255.0",
                                                                "seq_num": "0x800007BC",
                                                            }
                                                        },
                                                    },
                                                    "10.22.102.64": {
                                                        "adv_router": "10.22.102.64",
                                                        "lsa_id": "10.22.102.64",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "10.22.102.64",
                                                                "age": 2220,
                                                                "checksum": "0x008BD8",
                                                                "link_count": 3,
                                                                "lsa_id": "10.22.102.64",
                                                                "seq_num": "0x800003EC",
                                                            }
                                                        },
                                                    },
                                                    "172.31.197.252": {
                                                        "adv_router": "172.31.197.252",
                                                        "lsa_id": "172.31.197.252",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "172.31.197.252",
                                                                "age": 1272,
                                                                "checksum": "0x00B9E5",
                                                                "link_count": 6,
                                                                "lsa_id": "172.31.197.252",
                                                                "seq_num": "0x80000DBD",
                                                            }
                                                        },
                                                    },
                                                    "172.31.197.253": {
                                                        "adv_router": "172.31.197.253",
                                                        "lsa_id": "172.31.197.253",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "172.31.197.253",
                                                                "age": 663,
                                                                "checksum": "0x00FFD8",
                                                                "link_count": 4,
                                                                "lsa_id": "172.31.197.253",
                                                                "seq_num": "0x8000009D",
                                                            }
                                                        },
                                                    },
                                                    "172.31.197.254": {
                                                        "adv_router": "172.31.197.254",
                                                        "lsa_id": "172.31.197.254",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "172.31.197.254",
                                                                "age": 1900,
                                                                "checksum": "0x00D029",
                                                                "link_count": 3,
                                                                "lsa_id": "172.31.197.254",
                                                                "seq_num": "0x800000D9",
                                                            }
                                                        },
                                                    },
                                                },
                                            },
                                            2: {
                                                "lsa_type": 2,
                                                "lsas": {
                                                    "192.168.255.0": {
                                                        "adv_router": "172.31.197.252",
                                                        "lsa_id": "192.168.255.0",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "172.31.197.252",
                                                                "age": 26,
                                                                "checksum": "0x009E8D",
                                                                "lsa_id": "192.168.255.0",
                                                                "seq_num": "0x800000D1",
                                                            }
                                                        },
                                                    },
                                                    "10.22.102.50": {
                                                        "adv_router": "10.22.102.64",
                                                        "lsa_id": "10.22.102.50",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "10.22.102.64",
                                                                "age": 220,
                                                                "checksum": "0x003A0A",
                                                                "lsa_id": "10.22.102.50",
                                                                "seq_num": "0x800000AD",
                                                            }
                                                        },
                                                    },
                                                    "10.22.102.58": {
                                                        "adv_router": "10.22.102.64",
                                                        "lsa_id": "10.22.102.58",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "10.22.102.64",
                                                                "age": 1220,
                                                                "checksum": "0x00E2CD",
                                                                "lsa_id": "10.22.102.58",
                                                                "seq_num": "0x80000038",
                                                            }
                                                        },
                                                    },
                                                    "172.31.197.102": {
                                                        "adv_router": "192.168.165.220",
                                                        "lsa_id": "172.31.197.102",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "192.168.165.220",
                                                                "age": 113,
                                                                "checksum": "0x009ACA",
                                                                "lsa_id": "172.31.197.102",
                                                                "seq_num": "0x80000055",
                                                            }
                                                        },
                                                    },
                                                    "172.31.197.94": {
                                                        "adv_router": "172.31.197.254",
                                                        "lsa_id": "172.31.197.94",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "172.31.197.254",
                                                                "age": 911,
                                                                "checksum": "0x007ACC",
                                                                "lsa_id": "172.31.197.94",
                                                                "seq_num": "0x80000052",
                                                            }
                                                        },
                                                    },
                                                    "172.31.197.97": {
                                                        "adv_router": "172.31.197.253",
                                                        "lsa_id": "172.31.197.97",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "172.31.197.253",
                                                                "age": 663,
                                                                "checksum": "0x00AAB4",
                                                                "lsa_id": "172.31.197.97",
                                                                "seq_num": "0x80000037",
                                                            }
                                                        },
                                                    },
                                                },
                                            },
                                            3: {
                                                "lsa_type": 3,
                                                "lsas": {
                                                    "192.168.165.119": {
                                                        "adv_router": "172.31.197.252",
                                                        "lsa_id": "192.168.165.119",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "172.31.197.252",
                                                                "age": 1030,
                                                                "checksum": "0x007847",
                                                                "lsa_id": "192.168.165.119",
                                                                "seq_num": "0x800000D4",
                                                            }
                                                        },
                                                    },
                                                    "192.168.165.120": {
                                                        "adv_router": "172.31.197.252",
                                                        "lsa_id": "192.168.165.120",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "172.31.197.252",
                                                                "age": 26,
                                                                "checksum": "0x005160",
                                                                "lsa_id": "192.168.165.120",
                                                                "seq_num": "0x800003DE",
                                                            }
                                                        },
                                                    },
                                                    "192.168.165.48": {
                                                        "adv_router": "172.31.197.252",
                                                        "lsa_id": "192.168.165.48",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "172.31.197.252",
                                                                "age": 26,
                                                                "checksum": "0x0006F6",
                                                                "lsa_id": "192.168.165.48",
                                                                "seq_num": "0x800003DF",
                                                            }
                                                        },
                                                    },
                                                    "192.168.165.56": {
                                                        "adv_router": "172.31.197.252",
                                                        "lsa_id": "192.168.165.56",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "172.31.197.252",
                                                                "age": 1779,
                                                                "checksum": "0x00D42E",
                                                                "lsa_id": "192.168.165.56",
                                                                "seq_num": "0x800000D4",
                                                            }
                                                        },
                                                    },
                                                },
                                            },
                                            4: {
                                                "lsa_type": 4,
                                                "lsas": {
                                                    "192.168.165.119": {
                                                        "adv_router": "172.31.197.252",
                                                        "lsa_id": "192.168.165.119",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "172.31.197.252",
                                                                "age": 1030,
                                                                "checksum": "0x00605F",
                                                                "lsa_id": "192.168.165.119",
                                                                "seq_num": "0x800000D4",
                                                            }
                                                        },
                                                    },
                                                    "192.168.165.120": {
                                                        "adv_router": "172.31.197.252",
                                                        "lsa_id": "192.168.165.120",
                                                        "ospfv2": {
                                                            "header": {
                                                                "adv_router": "172.31.197.252",
                                                                "age": 26,
                                                                "checksum": "0x003978",
                                                                "lsa_id": "192.168.165.120",
                                                                "seq_num": "0x800003DE",
                                                            }
                                                        },
                                                    },
                                                },
                                            },
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
