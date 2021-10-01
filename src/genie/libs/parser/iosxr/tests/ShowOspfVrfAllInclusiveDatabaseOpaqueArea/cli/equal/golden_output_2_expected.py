
expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "64577": {
                            "areas": {
                                "0.0.0.0": {
                                    "database": {
                                        "lsa_types": {
                                            10: {
                                                "lsa_type": 10,
                                                "lsas": {
                                                    "10.16.0.0 10.154.219.84": {
                                                        "adv_router": "10.154.219.84",
                                                        "lsa_id": "10.16.0.0",
                                                        "ospfv2": {
                                                            "header": {
                                                                "age": 65,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.16.0.0",
                                                                "adv_router": "10.154.219.84",
                                                                "opaque_type": 4,
                                                                "opaque_id": 0,
                                                                "seq_num": "80004c15",
                                                                "checksum": "0xadfd",
                                                                "length": 76,
                                                            },
                                                            "body": {
                                                                "opaque": {
                                                                    "router_capabilities_tlv": {
                                                                        1: {
                                                                            "length": 4,
                                                                            "information_capabilities": {
                                                                                "graceful_restart_helper": True,
                                                                                "stub_router": True,
                                                                                "capability_bits": "0x60000000",
                                                                            },
                                                                        },
                                                                    },
                                                                    "sr_algorithm_tlv": {
                                                                        1: {
                                                                            "length": 2,
                                                                            "algorithm": {
                                                                                "0": True,
                                                                                "1": True,
                                                                            },
                                                                        },
                                                                    },
                                                                    "sid_range_tlvs": {
                                                                        1: {
                                                                            "length": 12,
                                                                            "tlv_type": "Segment Routing Range",
                                                                            "range_size": 65535,
                                                                            "sub_tlvs": {
                                                                                1: {
                                                                                    "length": 3,
                                                                                    "type": "SID",
                                                                                    "label": 16000,
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                    "node_msd_tlvs": {
                                                                        1: {
                                                                            "length": 2,
                                                                            "node_type": 1,
                                                                            "value": 10,
                                                                        },
                                                                    },
                                                                    "local_block_tlvs": {
                                                                        1: {
                                                                            "length": 12,
                                                                            "range_size": 1000,
                                                                            "sub_tlvs": {
                                                                                1: {
                                                                                    "length": 3,
                                                                                    "type": "SID",
                                                                                    "label": 15000,
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                    "10.49.0.1 10.154.219.84": {
                                                        "adv_router": "10.154.219.84",
                                                        "lsa_id": "10.49.0.1",
                                                        "ospfv2": {
                                                            "header": {
                                                                "age": 65,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.49.0.1",
                                                                "adv_router": "10.154.219.84",
                                                                "opaque_type": 7,
                                                                "opaque_id": 1,
                                                                "seq_num": "800009be",
                                                                "checksum": "0xf6d0",
                                                                "length": 48,
                                                            },
                                                            "body": {
                                                                "opaque": {
                                                                    "extended_prefix_tlvs": {
                                                                        1: {
                                                                            "length": 24,
                                                                            "af": 0,
                                                                            "prefix": "10.246.254.0/32",
                                                                            "range_size": 256,
                                                                            "flags": "0x0",
                                                                            "sub_tlvs": {
                                                                                1: {
                                                                                    "length": 8,
                                                                                    "type": "SID",
                                                                                    "flags": "0x60",
                                                                                    "mt_id": "0",
                                                                                    "algo": 0,
                                                                                    "sid": 1028,
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                    "10.64.0.78 10.154.219.85": {
                                                        "adv_router": "10.154.219.85",
                                                        "lsa_id": "10.64.0.78",
                                                        "ospfv2": {
                                                            "header": {
                                                                "age": 1057,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.64.0.78",
                                                                "adv_router": "10.154.219.85",
                                                                "opaque_type": 8,
                                                                "opaque_id": 78,
                                                                "seq_num": "800004bf",
                                                                "checksum": "0x9a5b",
                                                                "length": 100,
                                                            },
                                                            "body": {
                                                                "opaque": {
                                                                    "extended_link_tlvs": {
                                                                        1: {
                                                                            "length": 76,
                                                                            "link_type": 1,
                                                                            "link_id": "10.154.219.57",
                                                                            "link_data": "172.16.0.91",
                                                                            "sub_tlvs": {
                                                                                1: {
                                                                                    "length": 7,
                                                                                    "type": "Adj",
                                                                                    "flags": "0x60",
                                                                                    "mt_id": "0",
                                                                                    "weight": 0,
                                                                                    "label": 100479,
                                                                                },
                                                                                2: {
                                                                                    "length": 8,
                                                                                    "type": "Local-ID Remote-ID",
                                                                                    "local_interface_id": 78,
                                                                                    "remote_interface_id": 76,
                                                                                },
                                                                                3: {
                                                                                    "length": 4,
                                                                                    "type": "Remote If Address",
                                                                                    "neighbor_address": "172.16.0.90",
                                                                                },
                                                                                4: {
                                                                                    "length": 2,
                                                                                    "type": "Link MSD",
                                                                                    "node_type": 1,
                                                                                    "value": 10,
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.3 10.154.219.51": {
                                                        "adv_router": "10.154.219.51",
                                                        "lsa_id": "10.1.0.3",
                                                        "ospfv2": {
                                                            "header": {
                                                                "age": 586,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.3",
                                                                "adv_router": "10.154.219.51",
                                                                "opaque_type": 1,
                                                                "opaque_id": 3,
                                                                "seq_num": "80004036",
                                                                "checksum": "0xe06c",
                                                                "length": 136,
                                                            },
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 1,
                                                                            "link_name": "point-to-point network",
                                                                            "link_id": "10.154.219.106",
                                                                            "local_if_ipv4_addrs": {
                                                                                "172.16.1.153": {},
                                                                            },
                                                                            "neighbor_address": "172.16.1.152",
                                                                            "te_metric": 10000,
                                                                            "max_bandwidth": 750000000,
                                                                            "max_reservable_bandwidth": 750000000,
                                                                            "total_priority": 8,
                                                                            "unreserved_bandwidths": {
                                                                                "0 750000000": {
                                                                                    "priority": 0,
                                                                                    "unreserved_bandwidth": 750000000,
                                                                                },
                                                                                "1 750000000": {
                                                                                    "priority": 1,
                                                                                    "unreserved_bandwidth": 750000000,
                                                                                },
                                                                                "2 750000000": {
                                                                                    "priority": 2,
                                                                                    "unreserved_bandwidth": 750000000,
                                                                                },
                                                                                "3 750000000": {
                                                                                    "priority": 3,
                                                                                    "unreserved_bandwidth": 750000000,
                                                                                },
                                                                                "4 750000000": {
                                                                                    "priority": 4,
                                                                                    "unreserved_bandwidth": 750000000,
                                                                                },
                                                                                "5 750000000": {
                                                                                    "priority": 5,
                                                                                    "unreserved_bandwidth": 750000000,
                                                                                },
                                                                                "6 750000000": {
                                                                                    "priority": 6,
                                                                                    "unreserved_bandwidth": 750000000,
                                                                                },
                                                                                "7 750000000": {
                                                                                    "priority": 7,
                                                                                    "unreserved_bandwidth": 750000000,
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
                                                    "10.1.17.240 10.154.219.85": {
                                                        "adv_router": "10.154.219.85",
                                                        "lsa_id": "10.1.17.240",
                                                        "ospfv2": {
                                                            "header": {
                                                                "age": 1057,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.17.240",
                                                                "adv_router": "10.154.219.85",
                                                                "opaque_type": 1,
                                                                "opaque_id": 4592,
                                                                "seq_num": "800004c1",
                                                                "checksum": "0x827c",
                                                                "length": 80,
                                                            },
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 1,
                                                                            "link_name": "point-to-point network",
                                                                            "link_id": "10.154.219.58",
                                                                            "local_if_ipv4_addrs": {
                                                                                "172.16.0.99": {},
                                                                            },
                                                                            "neighbor_address": "172.16.0.98",
                                                                            "te_metric": 1000,
                                                                            "max_bandwidth": 1250000000,
                                                                            "igp_metric": 1000,
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
    },
}
