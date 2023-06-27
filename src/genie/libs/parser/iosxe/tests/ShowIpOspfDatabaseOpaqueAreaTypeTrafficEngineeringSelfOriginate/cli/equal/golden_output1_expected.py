expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "10": {},
                        "1": {
                            "areas": {
                                "0.0.0.0": {
                                    "database": {
                                        "lsa_types": {
                                            10: {
                                                "lsa_type": 10,
                                                "lsas": {
                                                    "1.0.0.0 1.1.1.1": {
                                                        "adv_router": "1.1.1.1",
                                                        "lsa_id": "1.0.0.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "mpls_te_router_id": "1.1.1.1",
                                                                    "num_of_links": 0,
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 60,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "1.0.0.0",
                                                                "adv_router": "1.1.1.1",
                                                                "opaque_type": 1,
                                                                "opaque_id": 0,
                                                                "seq_num": "80000001",
                                                                "checksum": "0x58D1",
                                                                "length": 28,
                                                                "fragment_number": 0,
                                                            },
                                                        },
                                                    },
                                                    "1.0.0.5 1.1.1.1": {
                                                        "adv_router": "1.1.1.1",
                                                        "lsa_id": "1.0.0.5",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 1,
                                                                            "link_name": "point-to-point network",
                                                                            "link_id": "1.1.1.4",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "1.4.0.4": {}
                                                                            },
                                                                            "local_if_ipv4_addrs": {
                                                                                "1.4.0.1": {}
                                                                            },
                                                                            "te_metric": 10,
                                                                            "max_bandwidth": 1250000,
                                                                            "igp_metric": 10,
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 59,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "1.0.0.5",
                                                                "adv_router": "1.1.1.1",
                                                                "opaque_type": 1,
                                                                "opaque_id": 5,
                                                                "seq_num": "80000001",
                                                                "checksum": "0xC02A",
                                                                "length": 80,
                                                                "fragment_number": 5,
                                                            },
                                                        },
                                                    },
                                                    "1.0.0.26 1.1.1.1": {
                                                        "adv_router": "1.1.1.1",
                                                        "lsa_id": "1.0.0.26",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 2,
                                                                            "link_name": "broadcast network",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "0.0.0.0": {}
                                                                            },
                                                                            "link_id": "20.1.1.1",
                                                                            "local_if_ipv4_addrs": {
                                                                                "20.1.1.1": {}
                                                                            },
                                                                            "te_metric": 100,
                                                                            "max_bandwidth": 1250000,
                                                                            "admin_group": "0x2",
                                                                            "igp_metric": 100,
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 47,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "1.0.0.26",
                                                                "adv_router": "1.1.1.1",
                                                                "opaque_type": 1,
                                                                "opaque_id": 26,
                                                                "seq_num": "80000002",
                                                                "checksum": "0x933C",
                                                                "length": 88,
                                                                "fragment_number": 26,
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
