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
                                            10: {
                                                "lsa_type": 10,
                                                "lsas": {
                                                    "10.1.0.0 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.0.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "mpls_te_router_id": "10.4.1.1",
                                                                    "num_of_links": 0,
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 49,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.0",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_type": 1,
                                                                "opaque_id": 0,
                                                                "seq_num": "80000001",
                                                                "checksum": "0x58D1",
                                                                "length": 28,
                                                                "fragment_number": 0,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.15 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.0.15",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 1,
                                                                            "link_name": "point-to-point network",
                                                                            "link_id": "10.16.2.2",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "192.168.220.2": {}
                                                                            },
                                                                            "local_if_ipv4_addrs": {
                                                                                "192.168.220.1": {}
                                                                            },
                                                                            "te_metric": 1,
                                                                            "max_bandwidth": 176258176,
                                                                            "igp_metric": 1,
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 49,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.15",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_type": 1,
                                                                "opaque_id": 15,
                                                                "seq_num": "80000001",
                                                                "checksum": "0x917E",
                                                                "length": 80,
                                                                "fragment_number": 15,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.16 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.0.16",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 1,
                                                                            "link_name": "point-to-point network",
                                                                            "link_id": "10.16.2.2",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "192.168.111.2": {}
                                                                            },
                                                                            "local_if_ipv4_addrs": {
                                                                                "192.168.111.1": {}
                                                                            },
                                                                            "te_metric": 1,
                                                                            "max_bandwidth": 125000000,
                                                                            "igp_metric": 1,
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 49,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.16",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_type": 1,
                                                                "opaque_id": 16,
                                                                "seq_num": "80000001",
                                                                "checksum": "0x8A09",
                                                                "length": 80,
                                                                "fragment_number": 16,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.17 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.0.17",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 1,
                                                                            "link_name": "point-to-point network",
                                                                            "link_id": "10.16.2.2",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "192.168.4.2": {}
                                                                            },
                                                                            "local_if_ipv4_addrs": {
                                                                                "192.168.4.1": {}
                                                                            },
                                                                            "te_metric": 1,
                                                                            "max_bandwidth": 125000000,
                                                                            "igp_metric": 1,
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 49,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.17",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_type": 1,
                                                                "opaque_id": 17,
                                                                "seq_num": "80000001",
                                                                "checksum": "0xC2CD",
                                                                "length": 80,
                                                                "fragment_number": 17,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.18 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.0.18",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 1,
                                                                            "link_name": "point-to-point network",
                                                                            "link_id": "10.16.2.2",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "192.168.154.2": {}
                                                                            },
                                                                            "local_if_ipv4_addrs": {
                                                                                "192.168.154.1": {}
                                                                            },
                                                                            "te_metric": 1,
                                                                            "max_bandwidth": 125000000,
                                                                            "igp_metric": 1,
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 49,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.18",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_type": 1,
                                                                "opaque_id": 18,
                                                                "seq_num": "80000001",
                                                                "checksum": "0xFA92",
                                                                "length": 80,
                                                                "fragment_number": 18,
                                                            },
                                                        },
                                                    },
                                                    "10.16.0.0 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.16.0.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "router_capabilities_tlv": {
                                                                        1: {
                                                                            "tlv_type": "Router Information",
                                                                            "length": 4,
                                                                            "information_capabilities": {
                                                                                "graceful_restart_helper": True,
                                                                                "stub_router": True,
                                                                            },
                                                                        }
                                                                    },
                                                                    "sr_algorithm_tlv": {
                                                                        1: {
                                                                            "tlv_type": "Segment Routing Algorithm",
                                                                            "length": 2,
                                                                            "algorithm": {
                                                                                "spf": True,
                                                                                "strict_spf": True,
                                                                            },
                                                                        }
                                                                    },
                                                                    "sid_range_tlvs": {
                                                                        1: {
                                                                            "tlv_type": "Segment Routing Range",
                                                                            "length": 12,
                                                                            "range_size": 8000,
                                                                            "sub_tlvs": {
                                                                                1: {
                                                                                    "type": "SID/Label",
                                                                                    "length": 3,
                                                                                    "label": 16000,
                                                                                }
                                                                            },
                                                                        }
                                                                    },
                                                                    "node_msd_tlvs": {
                                                                        1: {
                                                                            "tlv_type": "Segment Routing Node MSD",
                                                                            "length": 2,
                                                                            "sub_type": {
                                                                                "node_max_sid_depth_value": 13
                                                                            },
                                                                        }
                                                                    },
                                                                    "local_block_tlvs": {
                                                                        1: {
                                                                            "tlv_type": "Segment Routing Local Block",
                                                                            "length": 12,
                                                                            "range_size": 1000,
                                                                            "sub_tlvs": {
                                                                                1: {
                                                                                    "type": "SID/Label",
                                                                                    "length": 3,
                                                                                    "label": 15000,
                                                                                }
                                                                            },
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 49,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.16.0.0",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_id": 0,
                                                                "seq_num": "80000001",
                                                                "checksum": "0xD28C",
                                                                "length": 76,
                                                            },
                                                        },
                                                    },
                                                    "10.49.0.0 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.49.0.0",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "extended_prefix_tlvs": {
                                                                        1: {
                                                                            "tlv_type": "Extended Prefix",
                                                                            "length": 20,
                                                                            "prefix": "10.4.1.1/32",
                                                                            "af": 0,
                                                                            "route_type": "Intra",
                                                                            "flags": "N-bit",
                                                                            "sub_tlvs": {
                                                                                1: {
                                                                                    "type": "Prefix SID",
                                                                                    "length": 8,
                                                                                    "flags": "None",
                                                                                    "mt_id": 0,
                                                                                    "algo": "SPF",
                                                                                    "sid": 1,
                                                                                }
                                                                            },
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 49,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.49.0.0",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_id": 0,
                                                                "seq_num": "80000001",
                                                                "checksum": "0xEFA7",
                                                                "length": 44,
                                                            },
                                                        },
                                                    },
                                                    "10.64.0.20 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.64.0.20",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "extended_link_tlvs": {
                                                                        1: {
                                                                            "tlv_type": "Extended Link",
                                                                            "length": 68,
                                                                            "link_name": "another router (point-to-point)",
                                                                            "link_type": 1,
                                                                            "link_id": "10.16.2.2",
                                                                            "link_data": "192.168.220.1",
                                                                            "sub_tlvs": {
                                                                                1: {
                                                                                    "type": "Adj SID",
                                                                                    "length": 7,
                                                                                    "flags": "L-Bit, V-bit",
                                                                                    "mt_id": 0,
                                                                                    "weight": 0,
                                                                                    "label": 19,
                                                                                },
                                                                                2: {
                                                                                    "type": "Remote Intf Addr",
                                                                                    "remote_interface_address": "192.168.220.2",
                                                                                },
                                                                                3: {
                                                                                    "type": "Local / Remote Intf ID",
                                                                                    "local_interface_id": 20,
                                                                                    "remote_interface_id": 20,
                                                                                },
                                                                            },
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 49,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.64.0.20",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_id": 20,
                                                                "seq_num": "80000001",
                                                                "checksum": "0xF52F",
                                                                "length": 92,
                                                            },
                                                        },
                                                    },
                                                    "10.64.0.21 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.64.0.21",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "extended_link_tlvs": {
                                                                        1: {
                                                                            "tlv_type": "Extended Link",
                                                                            "length": 68,
                                                                            "link_name": "another router (point-to-point)",
                                                                            "link_type": 1,
                                                                            "link_id": "10.16.2.2",
                                                                            "link_data": "192.168.111.1",
                                                                            "sub_tlvs": {
                                                                                1: {
                                                                                    "type": "Adj SID",
                                                                                    "length": 7,
                                                                                    "flags": "L-Bit, V-bit",
                                                                                    "mt_id": 0,
                                                                                    "weight": 0,
                                                                                    "label": 18,
                                                                                },
                                                                                2: {
                                                                                    "type": "Remote Intf Addr",
                                                                                    "remote_interface_address": "192.168.111.2",
                                                                                },
                                                                                3: {
                                                                                    "type": "Local / Remote Intf ID",
                                                                                    "local_interface_id": 21,
                                                                                    "remote_interface_id": 22,
                                                                                },
                                                                            },
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 49,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.64.0.21",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_id": 21,
                                                                "seq_num": "80000001",
                                                                "checksum": "0xB764",
                                                                "length": 92,
                                                            },
                                                        },
                                                    },
                                                    "10.64.0.22 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.64.0.22",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "extended_link_tlvs": {
                                                                        1: {
                                                                            "tlv_type": "Extended Link",
                                                                            "length": 68,
                                                                            "link_name": "another router (point-to-point)",
                                                                            "link_type": 1,
                                                                            "link_id": "10.16.2.2",
                                                                            "link_data": "192.168.4.1",
                                                                            "sub_tlvs": {
                                                                                1: {
                                                                                    "type": "Adj SID",
                                                                                    "length": 7,
                                                                                    "flags": "L-Bit, V-bit",
                                                                                    "mt_id": 0,
                                                                                    "weight": 0,
                                                                                    "label": 17,
                                                                                },
                                                                                2: {
                                                                                    "type": "Remote Intf Addr",
                                                                                    "remote_interface_address": "192.168.4.2",
                                                                                },
                                                                                3: {
                                                                                    "type": "Local / Remote Intf ID",
                                                                                    "local_interface_id": 22,
                                                                                    "remote_interface_id": 23,
                                                                                },
                                                                            },
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 49,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.64.0.22",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_id": 22,
                                                                "seq_num": "80000001",
                                                                "checksum": "0xF420",
                                                                "length": 92,
                                                            },
                                                        },
                                                    },
                                                    "10.64.0.23 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.64.0.23",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "extended_link_tlvs": {
                                                                        1: {
                                                                            "tlv_type": "Extended Link",
                                                                            "length": 68,
                                                                            "link_name": "another router (point-to-point)",
                                                                            "link_type": 1,
                                                                            "link_id": "10.16.2.2",
                                                                            "link_data": "192.168.154.1",
                                                                            "sub_tlvs": {
                                                                                1: {
                                                                                    "type": "Adj SID",
                                                                                    "length": 7,
                                                                                    "flags": "L-Bit, V-bit",
                                                                                    "mt_id": 0,
                                                                                    "weight": 0,
                                                                                    "label": 16,
                                                                                },
                                                                                2: {
                                                                                    "type": "Remote Intf Addr",
                                                                                    "remote_interface_address": "192.168.154.2",
                                                                                },
                                                                                3: {
                                                                                    "type": "Local / Remote Intf ID",
                                                                                    "local_interface_id": 23,
                                                                                    "remote_interface_id": 24,
                                                                                },
                                                                            },
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 49,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.64.0.23",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_id": 23,
                                                                "seq_num": "80000001",
                                                                "checksum": "0x32DB",
                                                                "length": 92,
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
