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
                                            10: {
                                                "lsa_type": 10,
                                                "lsas": {
                                                    "1.0.0.0 1.1.1.4": {
                                                        "adv_router": "1.1.1.4",
                                                        "lsa_id": "1.0.0.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "mpls_te_router_id": "1.1.1.4",
                                                                    "num_of_links": 0,
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 313,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "1.0.0.0",
                                                                "adv_router": "1.1.1.4",
                                                                "opaque_type": 1,
                                                                "opaque_id": 0,
                                                                "seq_num": "80000001",
                                                                "checksum": "0x64BF",
                                                                "length": 28,
                                                                "fragment_number": 0,
                                                            },
                                                        },
                                                    },
                                                    "1.0.0.5 1.1.1.4": {
                                                        "adv_router": "1.1.1.4",
                                                        "lsa_id": "1.0.0.5",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 1,
                                                                            "link_name": "point-to-point network",
                                                                            "link_id": "1.1.1.1",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "1.4.0.1": {}
                                                                            },
                                                                            "local_if_ipv4_addrs": {
                                                                                "1.4.0.4": {}
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
                                                                "age": 303,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "1.0.0.5",
                                                                "adv_router": "1.1.1.4",
                                                                "opaque_type": 1,
                                                                "opaque_id": 5,
                                                                "seq_num": "80000001",
                                                                "checksum": "0x8466",
                                                                "length": 80,
                                                                "fragment_number": 5,
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
}
