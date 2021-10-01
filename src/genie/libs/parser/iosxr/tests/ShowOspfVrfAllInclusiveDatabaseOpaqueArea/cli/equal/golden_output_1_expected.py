

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
                                                            "header": {
                                                                "age": 1427,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.0",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_type": 1,
                                                                "opaque_id": 0,
                                                                "seq_num": "80000002",
                                                                "checksum": "0x56d2",
                                                                "length": 28,
                                                                "mpls_te_router_id": "10.4.1.1",
                                                            },
                                                            "body": {
                                                                "opaque": {
                                                                    "num_of_links": 0,
                                                                },
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.0 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.1.0.0",
                                                        "ospfv2": {
                                                            "header": {
                                                                "age": 653,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, No DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.0",
                                                                "adv_router": "10.16.2.2",
                                                                "opaque_type": 1,
                                                                "opaque_id": 0,
                                                                "seq_num": "80000003",
                                                                "checksum": "0x1c22",
                                                                "length": 28,
                                                                "mpls_te_router_id": "10.16.2.2",
                                                            },
                                                            "body": {
                                                                "opaque": {
                                                                    "num_of_links": 0,
                                                                },
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.0 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.1.0.0",
                                                        "ospfv2": {
                                                            "header": {
                                                                "age": 1175,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.0",
                                                                "adv_router": "10.36.3.3",
                                                                "opaque_type": 1,
                                                                "opaque_id": 0,
                                                                "seq_num": "80000002",
                                                                "checksum": "0x5eba",
                                                                "length": 28,
                                                                "mpls_te_router_id": "10.36.3.3",
                                                            },
                                                            "body": {
                                                                "opaque": {
                                                                    "num_of_links": 0,
                                                                },
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.1 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.0.1",
                                                        "ospfv2": {
                                                            "header": {
                                                                "age": 1427,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.1",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_type": 1,
                                                                "opaque_id": 1,
                                                                "seq_num": "80000002",
                                                                "checksum": "0x6586",
                                                                "length": 124,
                                                            },
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 2,
                                                                            "link_name": "broadcast network",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "remote_if_ipv4_addr": "0.0.0.0",
                                                                            },
                                                                            "link_id": "10.1.4.4",
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.1.4.1": {},
                                                                            },
                                                                            "te_metric": 1,
                                                                            "max_bandwidth": 125000000,
                                                                            "max_reservable_bandwidth": 93750000,
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
                                                                            "admin_group": "0",
                                                                            "igp_metric": 1,
                                                                        },
                                                                    },
                                                                    "num_of_links": 1,
                                                                },
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.2 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.0.2",
                                                        "ospfv2": {
                                                            "header": {
                                                                "age": 1427,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.2",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_type": 1,
                                                                "opaque_id": 2,
                                                                "seq_num": "80000002",
                                                                "checksum": "0xb43d",
                                                                "length": 124,
                                                            },
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 2,
                                                                            "link_name": "broadcast network",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "remote_if_ipv4_addr": "0.0.0.0",
                                                                            },
                                                                            "link_id": "10.1.2.1",
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.1.2.1": {},
                                                                            },
                                                                            "te_metric": 1,
                                                                            "max_bandwidth": 125000000,
                                                                            "max_reservable_bandwidth": 93750000,
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
                                                                            "admin_group": "0",
                                                                            "igp_metric": 1,
                                                                        },
                                                                    },
                                                                    "num_of_links": 1,
                                                                },
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.4 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.1.0.4",
                                                        "ospfv2": {
                                                            "header": {
                                                                "age": 1175,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.4",
                                                                "adv_router": "10.36.3.3",
                                                                "opaque_type": 1,
                                                                "opaque_id": 4,
                                                                "seq_num": "80000002",
                                                                "checksum": "0x915d",
                                                                "length": 160,
                                                            },
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 2,
                                                                            "link_name": "broadcast network",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "remote_if_ipv4_addr": "0.0.0.0",
                                                                            },
                                                                            "link_id": "10.3.4.4",
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.3.4.3": {},
                                                                            },
                                                                            "te_metric": 1,
                                                                            "max_bandwidth": 125000000,
                                                                            "max_reservable_bandwidth": 93750000,
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
                                                                            "admin_group": "0",
                                                                            "igp_metric": 1,
                                                                            "extended_admin_group": {
                                                                                "length": 8,
                                                                                "groups": {
                                                                                    0: {
                                                                                        "value": 0,
                                                                                    },
                                                                                    1: {
                                                                                        "value": 0,
                                                                                    },
                                                                                    2: {
                                                                                        "value": 0,
                                                                                    },
                                                                                    3: {
                                                                                        "value": 0,
                                                                                    },
                                                                                    4: {
                                                                                        "value": 0,
                                                                                    },
                                                                                    5: {
                                                                                        "value": 0,
                                                                                    },
                                                                                    6: {
                                                                                        "value": 0,
                                                                                    },
                                                                                    7: {
                                                                                        "value": 0,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                    "num_of_links": 1,
                                                                },
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.6 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.1.0.6",
                                                        "ospfv2": {
                                                            "header": {
                                                                "age": 1175,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.6",
                                                                "adv_router": "10.36.3.3",
                                                                "opaque_type": 1,
                                                                "opaque_id": 6,
                                                                "seq_num": "80000002",
                                                                "checksum": "0x5ec",
                                                                "length": 160,
                                                            },
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 2,
                                                                            "link_name": "broadcast network",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "remote_if_ipv4_addr": "0.0.0.0",
                                                                            },
                                                                            "link_id": "10.2.3.3",
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.2.3.3": {},
                                                                            },
                                                                            "te_metric": 1,
                                                                            "max_bandwidth": 125000000,
                                                                            "max_reservable_bandwidth": 93750000,
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
                                                                            "admin_group": "0",
                                                                            "igp_metric": 1,
                                                                            "extended_admin_group": {
                                                                                "length": 8,
                                                                                "groups": {
                                                                                    0: {
                                                                                        "value": 0,
                                                                                    },
                                                                                    1: {
                                                                                        "value": 0,
                                                                                    },
                                                                                    2: {
                                                                                        "value": 0,
                                                                                    },
                                                                                    3: {
                                                                                        "value": 0,
                                                                                    },
                                                                                    4: {
                                                                                        "value": 0,
                                                                                    },
                                                                                    5: {
                                                                                        "value": 0,
                                                                                    },
                                                                                    6: {
                                                                                        "value": 0,
                                                                                    },
                                                                                    7: {
                                                                                        "value": 0,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                    "num_of_links": 1,
                                                                },
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.37 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.1.0.37",
                                                        "ospfv2": {
                                                            "header": {
                                                                "age": 242,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, No DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.37",
                                                                "adv_router": "10.16.2.2",
                                                                "opaque_type": 1,
                                                                "opaque_id": 37,
                                                                "seq_num": "80000004",
                                                                "checksum": "0xe492",
                                                                "length": 116,
                                                            },
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 2,
                                                                            "link_name": "broadcast network",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "remote_if_ipv4_addr": "0.0.0.0",
                                                                            },
                                                                            "link_id": "10.2.3.3",
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.2.3.2": {},
                                                                            },
                                                                            "te_metric": 1,
                                                                            "max_bandwidth": 125000000,
                                                                            "max_reservable_bandwidth": 93750000,
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
                                                                            "admin_group": "0",
                                                                        },
                                                                    },
                                                                    "num_of_links": 1,
                                                                },
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.38 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.1.0.38",
                                                        "ospfv2": {
                                                            "header": {
                                                                "age": 233,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, No DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.38",
                                                                "adv_router": "10.16.2.2",
                                                                "opaque_type": 1,
                                                                "opaque_id": 38,
                                                                "seq_num": "80000004",
                                                                "checksum": "0x2350",
                                                                "length": 116,
                                                            },
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 2,
                                                                            "link_name": "broadcast network",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "remote_if_ipv4_addr": "0.0.0.0",
                                                                            },
                                                                            "link_id": "10.2.4.4",
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.2.4.2": {},
                                                                            },
                                                                            "te_metric": 1,
                                                                            "max_bandwidth": 125000000,
                                                                            "max_reservable_bandwidth": 93750000,
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
                                                                            "admin_group": "0",
                                                                        },
                                                                    },
                                                                    "num_of_links": 1,
                                                                },
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.39 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.1.0.39",
                                                        "ospfv2": {
                                                            "header": {
                                                                "age": 232,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, No DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.39",
                                                                "adv_router": "10.16.2.2",
                                                                "opaque_type": 1,
                                                                "opaque_id": 39,
                                                                "seq_num": "80000004",
                                                                "checksum": "0x4239",
                                                                "length": 116,
                                                            },
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 2,
                                                                            "link_name": "broadcast network",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "remote_if_ipv4_addr": "0.0.0.0",
                                                                            },
                                                                            "link_id": "10.1.2.1",
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.1.2.2": {},
                                                                            },
                                                                            "te_metric": 1,
                                                                            "max_bandwidth": 125000000,
                                                                            "max_reservable_bandwidth": 93750000,
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
                                                                            "admin_group": "0",
                                                                        },
                                                                    },
                                                                    "num_of_links": 1,
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        "VRF1": {"address_family": {"ipv4": {"instance": {"1": {},},},},},
    },
}
