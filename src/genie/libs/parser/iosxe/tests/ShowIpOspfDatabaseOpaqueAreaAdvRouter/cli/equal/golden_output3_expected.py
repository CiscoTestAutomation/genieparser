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
                                                                "age": 1663,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.0",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_type": 1,
                                                                "opaque_id": 0,
                                                                "seq_num": "8000013B",
                                                                "checksum": "0xE00E",
                                                                "length": 28,
                                                                "fragment_number": 0,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.3 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.0.3",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 1,
                                                                            "link_name": "point-to-point network",
                                                                            "link_id": "10.229.11.11",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "10.0.0.9": {}
                                                                            },
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.0.0.10": {}
                                                                            },
                                                                            "te_metric": 10,
                                                                            "max_bandwidth": 125000000,
                                                                            "igp_metric": 10,
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 1663,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.3",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_type": 1,
                                                                "opaque_id": 3,
                                                                "seq_num": "8000013B",
                                                                "checksum": "0xFF9E",
                                                                "length": 80,
                                                                "fragment_number": 3,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.4 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.0.4",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 1,
                                                                            "link_name": "point-to-point network",
                                                                            "link_id": "10.151.22.22",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "10.0.0.13": {}
                                                                            },
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.0.0.14": {}
                                                                            },
                                                                            "te_metric": 100,
                                                                            "max_bandwidth": 125000000,
                                                                            "igp_metric": 100,
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 1663,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.4",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_type": 1,
                                                                "opaque_id": 4,
                                                                "seq_num": "8000013B",
                                                                "checksum": "0xAE06",
                                                                "length": 80,
                                                                "fragment_number": 4,
                                                            },
                                                        },
                                                    },
                                                    "10.1.0.5 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.1.0.5",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "link_tlvs": {
                                                                        1: {
                                                                            "link_type": 1,
                                                                            "link_name": "point-to-point network",
                                                                            "link_id": "10.151.22.22",
                                                                            "remote_if_ipv4_addrs": {
                                                                                "10.0.0.25": {}
                                                                            },
                                                                            "local_if_ipv4_addrs": {
                                                                                "10.0.0.26": {}
                                                                            },
                                                                            "te_metric": 1000,
                                                                            "max_bandwidth": 125000000,
                                                                            "igp_metric": 1000,
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 1663,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.1.0.5",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_type": 1,
                                                                "opaque_id": 5,
                                                                "seq_num": "8000013B",
                                                                "checksum": "0xFE8D",
                                                                "length": 80,
                                                                "fragment_number": 5,
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
                                                                "age": 1663,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.16.0.0",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_id": 0,
                                                                "seq_num": "8000013B",
                                                                "checksum": "0x5BC8",
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
                                                                "age": 1663,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.49.0.0",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_id": 0,
                                                                "seq_num": "80000133",
                                                                "checksum": "0x88DB",
                                                                "length": 44,
                                                            },
                                                        },
                                                    },
                                                    "10.64.0.9 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.64.0.9",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "extended_link_tlvs": {
                                                                        1: {
                                                                            "tlv_type": "Extended Link",
                                                                            "length": 80,
                                                                            "link_name": "another router (point-to-point)",
                                                                            "link_type": 1,
                                                                            "link_id": "10.229.11.11",
                                                                            "link_data": "10.0.0.10",
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
                                                                                    "type": "Adj SID",
                                                                                    "length": 7,
                                                                                    "flags": "L-Bit, V-bit, B-bit",
                                                                                    "mt_id": 0,
                                                                                    "weight": 0,
                                                                                    "label": 19,
                                                                                },
                                                                                3: {
                                                                                    "type": "Remote Intf Addr",
                                                                                    "remote_interface_address": "10.0.0.9",
                                                                                },
                                                                                4: {
                                                                                    "type": "Local / Remote Intf ID",
                                                                                    "local_interface_id": 9,
                                                                                    "remote_interface_id": 9,
                                                                                },
                                                                            },
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 1663,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.64.0.9",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_id": 9,
                                                                "seq_num": "8000013C",
                                                                "checksum": "0xA666",
                                                                "length": 104,
                                                            },
                                                        },
                                                    },
                                                    "10.64.0.10 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.64.0.10",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "extended_link_tlvs": {
                                                                        1: {
                                                                            "tlv_type": "Extended Link",
                                                                            "length": 80,
                                                                            "link_name": "another router (point-to-point)",
                                                                            "link_type": 1,
                                                                            "link_id": "10.151.22.22",
                                                                            "link_data": "10.0.0.14",
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
                                                                                    "type": "Adj SID",
                                                                                    "length": 7,
                                                                                    "flags": "L-Bit, V-bit, B-bit",
                                                                                    "mt_id": 0,
                                                                                    "weight": 0,
                                                                                    "label": 21,
                                                                                },
                                                                                3: {
                                                                                    "type": "Remote Intf Addr",
                                                                                    "remote_interface_address": "10.0.0.13",
                                                                                },
                                                                                4: {
                                                                                    "type": "Local / Remote Intf ID",
                                                                                    "local_interface_id": 10,
                                                                                    "remote_interface_id": 8,
                                                                                },
                                                                            },
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 1663,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.64.0.10",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_id": 10,
                                                                "seq_num": "8000013C",
                                                                "checksum": "0xEBE6",
                                                                "length": 104,
                                                            },
                                                        },
                                                    },
                                                    "10.64.0.11 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.64.0.11",
                                                        "ospfv2": {
                                                            "body": {
                                                                "opaque": {
                                                                    "extended_link_tlvs": {
                                                                        1: {
                                                                            "tlv_type": "Extended Link",
                                                                            "length": 80,
                                                                            "link_name": "another router (point-to-point)",
                                                                            "link_type": 1,
                                                                            "link_id": "10.151.22.22",
                                                                            "link_data": "10.0.0.26",
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
                                                                                    "type": "Adj SID",
                                                                                    "length": 7,
                                                                                    "flags": "L-Bit, V-bit, B-bit",
                                                                                    "mt_id": 0,
                                                                                    "weight": 0,
                                                                                    "label": 20,
                                                                                },
                                                                                3: {
                                                                                    "type": "Remote Intf Addr",
                                                                                    "remote_interface_address": "10.0.0.25",
                                                                                },
                                                                                4: {
                                                                                    "type": "Local / Remote Intf ID",
                                                                                    "local_interface_id": 11,
                                                                                    "remote_interface_id": 9,
                                                                                },
                                                                            },
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            "header": {
                                                                "age": 1663,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 10,
                                                                "lsa_id": "10.64.0.11",
                                                                "adv_router": "10.4.1.1",
                                                                "opaque_id": 11,
                                                                "seq_num": "8000013D",
                                                                "checksum": "0xB8F1",
                                                                "length": 104,
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
