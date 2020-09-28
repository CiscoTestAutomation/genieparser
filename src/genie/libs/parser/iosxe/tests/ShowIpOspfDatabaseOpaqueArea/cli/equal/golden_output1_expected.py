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
                                                    "10.1.0.0 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.0.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "num_of_links": 0,
                                                                    "mpls_te_router_id": "10.4.1.1",
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.4.1.1",
                                                                "age": 370,
                                                                "checksum": "0x56D2",
                                                                "fragment_number": 0,
                                                                "length": 28,
                                                                "lsa_id": "10.1.0.0",
                                                                "opaque_id": 0,
                                                                "opaque_type": 1,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "80000002",
                                                                "type": 10,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.0 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.1.0.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "num_of_links": 0,
                                                                    "mpls_te_router_id": "10.16.2.2",
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.16.2.2",
                                                                "age": 1420,
                                                                "checksum": "0x1E21",
                                                                "fragment_number": 0,
                                                                "length": 28,
                                                                "lsa_id": "10.1.0.0",
                                                                "opaque_id": 0,
                                                                "opaque_type": 1,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, No DC",
                                                                "seq_num": "80000002",
                                                                "type": 10,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.0 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.1.0.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "num_of_links": 0,
                                                                    "mpls_te_router_id": "10.36.3.3",
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.36.3.3",
                                                                "age": 123,
                                                                "checksum": "0x5EBA",
                                                                "fragment_number": 0,
                                                                "length": 28,
                                                                "lsa_id": "10.1.0.0",
                                                                "opaque_id": 0,
                                                                "opaque_type": 1,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "80000002",
                                                                "type": 10,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.1 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.0.1",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "admin_group": "0x0",
                                                                            "igp_metric": 1,
                                                                            "link_id": "10.1.4.4",
                                                                            "link_name": "broadcast network",
                                                                            "link_type": 2,
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.1.4.1": {}
                                                                            },
                                                                            "max_bandwidth": 125000000,
                                                                            "max_reservable_bandwidth": 93750000,
                                                                            "remote_if_ipv4_addrs": {
                                                                                "0.0.0.0": {}
                                                                            },
                                                                            "te_metric": 1,
                                                                            "total_priority": 8,
                                                                            "unreserved_bandwidths": {
                                                                                "0 93750000": {
                                                                                    "priority": 0,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "1 93750000": {
                                                                                    "priority": 1,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "2 93750000": {
                                                                                    "priority": 2,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "3 93750000": {
                                                                                    "priority": 3,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "4 93750000": {
                                                                                    "priority": 4,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "5 93750000": {
                                                                                    "priority": 5,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "6 93750000": {
                                                                                    "priority": 6,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "7 93750000": {
                                                                                    "priority": 7,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                            },
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.4.1.1",
                                                                "age": 370,
                                                                "checksum": "0x6586",
                                                                "fragment_number": 1,
                                                                "length": 124,
                                                                "lsa_id": "10.1.0.1",
                                                                "opaque_id": 1,
                                                                "opaque_type": 1,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "80000002",
                                                                "type": 10,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.2 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.0.2",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "admin_group": "0x0",
                                                                            "igp_metric": 1,
                                                                            "link_id": "10.1.2.1",
                                                                            "link_name": "broadcast network",
                                                                            "link_type": 2,
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.1.2.1": {}
                                                                            },
                                                                            "max_bandwidth": 125000000,
                                                                            "max_reservable_bandwidth": 93750000,
                                                                            "remote_if_ipv4_addrs": {
                                                                                "0.0.0.0": {}
                                                                            },
                                                                            "te_metric": 1,
                                                                            "total_priority": 8,
                                                                            "unreserved_bandwidths": {
                                                                                "0 93750000": {
                                                                                    "priority": 0,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "1 93750000": {
                                                                                    "priority": 1,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "2 93750000": {
                                                                                    "priority": 2,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "3 93750000": {
                                                                                    "priority": 3,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "4 93750000": {
                                                                                    "priority": 4,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "5 93750000": {
                                                                                    "priority": 5,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "6 93750000": {
                                                                                    "priority": 6,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "7 93750000": {
                                                                                    "priority": 7,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                            },
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.4.1.1",
                                                                "age": 370,
                                                                "checksum": "0xB43D",
                                                                "fragment_number": 2,
                                                                "length": 124,
                                                                "lsa_id": "10.1.0.2",
                                                                "opaque_id": 2,
                                                                "opaque_type": 1,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "80000002",
                                                                "type": 10,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.37 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.1.0.37",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "admin_group": "0x0",
                                                                            "link_id": "10.2.3.3",
                                                                            "link_name": "broadcast network",
                                                                            "link_type": 2,
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.2.3.2": {}
                                                                            },
                                                                            "max_bandwidth": 125000000,
                                                                            "max_reservable_bandwidth": 93750000,
                                                                            "remote_if_ipv4_addrs": {
                                                                                "0.0.0.0": {}
                                                                            },
                                                                            "te_metric": 1,
                                                                            "total_priority": 8,
                                                                            "unreserved_bandwidths": {
                                                                                "0 93750000": {
                                                                                    "priority": 0,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "1 93750000": {
                                                                                    "priority": 1,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "2 93750000": {
                                                                                    "priority": 2,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "3 93750000": {
                                                                                    "priority": 3,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "4 93750000": {
                                                                                    "priority": 4,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "5 93750000": {
                                                                                    "priority": 5,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "6 93750000": {
                                                                                    "priority": 6,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "7 93750000": {
                                                                                    "priority": 7,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                            },
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.16.2.2",
                                                                "age": 1010,
                                                                "checksum": "0xE691",
                                                                "fragment_number": 37,
                                                                "length": 116,
                                                                "lsa_id": "10.1.0.37",
                                                                "opaque_id": 37,
                                                                "opaque_type": 1,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, No DC",
                                                                "seq_num": "80000003",
                                                                "type": 10,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.38 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.1.0.38",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "admin_group": "0x0",
                                                                            "link_id": "10.2.4.4",
                                                                            "link_name": "broadcast network",
                                                                            "link_type": 2,
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.2.4.2": {}
                                                                            },
                                                                            "max_bandwidth": 125000000,
                                                                            "max_reservable_bandwidth": 93750000,
                                                                            "remote_if_ipv4_addrs": {
                                                                                "0.0.0.0": {}
                                                                            },
                                                                            "te_metric": 1,
                                                                            "total_priority": 8,
                                                                            "unreserved_bandwidths": {
                                                                                "0 93750000": {
                                                                                    "priority": 0,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "1 93750000": {
                                                                                    "priority": 1,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "2 93750000": {
                                                                                    "priority": 2,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "3 93750000": {
                                                                                    "priority": 3,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "4 93750000": {
                                                                                    "priority": 4,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "5 93750000": {
                                                                                    "priority": 5,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "6 93750000": {
                                                                                    "priority": 6,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "7 93750000": {
                                                                                    "priority": 7,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                            },
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.16.2.2",
                                                                "age": 1000,
                                                                "checksum": "0x254F",
                                                                "fragment_number": 38,
                                                                "length": 116,
                                                                "lsa_id": "10.1.0.38",
                                                                "opaque_id": 38,
                                                                "opaque_type": 1,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, No DC",
                                                                "seq_num": "80000003",
                                                                "type": 10,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.39 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.1.0.39",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "admin_group": "0x0",
                                                                            "link_id": "10.1.2.1",
                                                                            "link_name": "broadcast network",
                                                                            "link_type": 2,
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.1.2.2": {}
                                                                            },
                                                                            "max_bandwidth": 125000000,
                                                                            "max_reservable_bandwidth": 93750000,
                                                                            "remote_if_ipv4_addrs": {
                                                                                "0.0.0.0": {}
                                                                            },
                                                                            "te_metric": 1,
                                                                            "total_priority": 8,
                                                                            "unreserved_bandwidths": {
                                                                                "0 93750000": {
                                                                                    "priority": 0,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "1 93750000": {
                                                                                    "priority": 1,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "2 93750000": {
                                                                                    "priority": 2,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "3 93750000": {
                                                                                    "priority": 3,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "4 93750000": {
                                                                                    "priority": 4,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "5 93750000": {
                                                                                    "priority": 5,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "6 93750000": {
                                                                                    "priority": 6,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "7 93750000": {
                                                                                    "priority": 7,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                            },
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.16.2.2",
                                                                "age": 1000,
                                                                "checksum": "0x4438",
                                                                "fragment_number": 39,
                                                                "length": 116,
                                                                "lsa_id": "10.1.0.39",
                                                                "opaque_id": 39,
                                                                "opaque_type": 1,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, No DC",
                                                                "seq_num": "80000003",
                                                                "type": 10,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.4 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.1.0.4",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "admin_group": "0x0",
                                                                            "igp_metric": 1,
                                                                            "link_id": "10.3.4.4",
                                                                            "link_name": "broadcast network",
                                                                            "link_type": 2,
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.3.4.3": {}
                                                                            },
                                                                            "max_bandwidth": 125000000,
                                                                            "max_reservable_bandwidth": 93750000,
                                                                            "remote_if_ipv4_addrs": {
                                                                                "0.0.0.0": {}
                                                                            },
                                                                            "te_metric": 1,
                                                                            "total_priority": 8,
                                                                            "unreserved_bandwidths": {
                                                                                "0 93750000": {
                                                                                    "priority": 0,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "1 93750000": {
                                                                                    "priority": 1,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "2 93750000": {
                                                                                    "priority": 2,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "3 93750000": {
                                                                                    "priority": 3,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "4 93750000": {
                                                                                    "priority": 4,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "5 93750000": {
                                                                                    "priority": 5,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "6 93750000": {
                                                                                    "priority": 6,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "7 93750000": {
                                                                                    "priority": 7,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                            },
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.36.3.3",
                                                                "age": 123,
                                                                "checksum": "0x915D",
                                                                "fragment_number": 4,
                                                                "length": 160,
                                                                "lsa_id": "10.1.0.4",
                                                                "opaque_id": 4,
                                                                "opaque_type": 1,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "80000002",
                                                                "type": 10,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.6 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.1.0.6",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "admin_group": "0x0",
                                                                            "igp_metric": 1,
                                                                            "link_id": "10.2.3.3",
                                                                            "link_name": "broadcast network",
                                                                            "link_type": 2,
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.2.3.3": {}
                                                                            },
                                                                            "max_bandwidth": 125000000,
                                                                            "max_reservable_bandwidth": 93750000,
                                                                            "remote_if_ipv4_addrs": {
                                                                                "0.0.0.0": {}
                                                                            },
                                                                            "te_metric": 1,
                                                                            "total_priority": 8,
                                                                            "unreserved_bandwidths": {
                                                                                "0 93750000": {
                                                                                    "priority": 0,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "1 93750000": {
                                                                                    "priority": 1,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "2 93750000": {
                                                                                    "priority": 2,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "3 93750000": {
                                                                                    "priority": 3,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "4 93750000": {
                                                                                    "priority": 4,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "5 93750000": {
                                                                                    "priority": 5,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "6 93750000": {
                                                                                    "priority": 6,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                                "7 93750000": {
                                                                                    "priority": 7,
                                                                                    "unreserved_bandwidth": 93750000,
                                                                                },
                                                                            },
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.36.3.3",
                                                                "age": 123,
                                                                "checksum": "0x5EC",
                                                                "fragment_number": 6,
                                                                "length": 160,
                                                                "lsa_id": "10.1.0.6",
                                                                "opaque_id": 6,
                                                                "opaque_type": 1,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "80000002",
                                                                "type": 10,
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
                        "2": {},
                    }
                }
            }
        }
    }
}
