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
                                                    "10.169.197.254 10.169.197.254": {
                                                        "adv_router": "10.169.197.254",
                                                        "lsa_id": "10.169.197.254",
                                                        "ospfv2": {
                                                            "body": {
                                                                "router": {
                                                                    "links": {
                                                                        "10.169.197.252": {
                                                                            "link_data": "10.169.197.94",
                                                                            "link_id": "10.169.197.252",
                                                                            "num_mtid_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 65535,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "another router (point-to-point)",
                                                                        },
                                                                        "10.169.197.254": {
                                                                            "link_data": "255.255.255.255",
                                                                            "link_id": "10.169.197.254",
                                                                            "num_mtid_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "stub network",
                                                                        },
                                                                        "10.169.197.92": {
                                                                            "link_data": "255.255.255.252",
                                                                            "link_id": "10.169.197.92",
                                                                            "num_mtid_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1000,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "stub network",
                                                                        },
                                                                    },
                                                                    "num_of_links": 3,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.169.197.254",
                                                                "age": 1141,
                                                                "checksum": "0x1D38",
                                                                "length": 60,
                                                                "lsa_id": "10.169.197.254",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "80000031",
                                                                "type": 1,
                                                            },
                                                        },
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
            }
        }
    }
}
