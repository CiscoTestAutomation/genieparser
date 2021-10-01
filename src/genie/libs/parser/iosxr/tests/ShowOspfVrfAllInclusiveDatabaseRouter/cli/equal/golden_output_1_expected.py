

expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "mpls1": {
                            "areas": {
                                "0.0.0.1": {
                                    "database": {
                                        "lsa_types": {
                                            1: {
                                                "lsa_type": 1,
                                                "lsas": {
                                                    "10.229.11.11 10.229.11.11": {
                                                        "adv_router": "10.229.11.11",
                                                        "lsa_id": "10.229.11.11",
                                                        "ospfv2": {
                                                            "body": {
                                                                "router": {
                                                                    "links": {
                                                                        "10.186.5.1": {
                                                                            "link_data": "10.186.5.1",
                                                                            "link_id": "10.186.5.1",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.151.22.22": {
                                                                            "link_data": "0.0.0.14",
                                                                            "link_id": "10.151.22.22",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 111,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "another router (point-to-point)",
                                                                        },
                                                                    },
                                                                    "num_of_links": 2,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.229.11.11",
                                                                "age": 1713,
                                                                "area_border_router": True,
                                                                "as_boundary_router": True,
                                                                "checksum": "0x9ce3",
                                                                "length": 48,
                                                                "lsa_id": "10.229.11.11",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "DC",
                                                                "routing_bit_enable": True,
                                                                "seq_num": "8000003e",
                                                                "type": 1,
                                                            },
                                                        },
                                                    },
                                                    "10.151.22.22 10.151.22.22": {
                                                        "adv_router": "10.151.22.22",
                                                        "lsa_id": "10.151.22.22",
                                                        "ospfv2": {
                                                            "body": {
                                                                "router": {
                                                                    "links": {
                                                                        "10.229.11.11": {
                                                                            "link_data": "0.0.0.6",
                                                                            "link_id": "10.229.11.11",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "another router (point-to-point)",
                                                                        },
                                                                        "10.229.6.6": {
                                                                            "link_data": "10.229.6.2",
                                                                            "link_id": "10.229.6.6",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 40,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                    },
                                                                    "num_of_links": 2,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.151.22.22",
                                                                "age": 1539,
                                                                "area_border_router": True,
                                                                "as_boundary_router": True,
                                                                "checksum": "0xc41a",
                                                                "length": 48,
                                                                "lsa_id": "10.151.22.22",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "No "
                                                                "DC",
                                                                "routing_bit_enable": True,
                                                                "seq_num": "80000019",
                                                                "type": 1,
                                                            },
                                                        },
                                                    },
                                                    "10.36.3.3 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.36.3.3",
                                                        "ospfv2": {
                                                            "body": {
                                                                "router": {
                                                                    "links": {
                                                                        "10.19.7.7": {
                                                                            "link_data": "10.19.7.3",
                                                                            "link_id": "10.19.7.7",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.36.3.3",
                                                                "age": 217,
                                                                "area_border_router": True,
                                                                "as_boundary_router": True,
                                                                "checksum": "0x5646",
                                                                "length": 36,
                                                                "lsa_id": "10.36.3.3",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "80000036",
                                                                "type": 1,
                                                            },
                                                        },
                                                    },
                                                    "10.115.55.55 10.115.55.55": {
                                                        "adv_router": "10.115.55.55",
                                                        "lsa_id": "10.115.55.55",
                                                        "ospfv2": {
                                                            "body": {
                                                                "router": {
                                                                    "links": {
                                                                        "10.186.5.1": {
                                                                            "link_data": "10.186.5.5",
                                                                            "link_id": "10.186.5.1",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.115.6.6": {
                                                                            "link_data": "10.115.6.5",
                                                                            "link_id": "10.115.6.6",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 30,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.115.55.55": {
                                                                            "link_data": "255.255.255.255",
                                                                            "link_id": "10.115.55.55",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
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
                                                                "adv_router": "10.115.55.55",
                                                                "age": 1378,
                                                                "checksum": "0xe7bc",
                                                                "length": 60,
                                                                "lsa_id": "10.115.55.55",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "DC",
                                                                "routing_bit_enable": True,
                                                                "seq_num": "80000037",
                                                                "type": 1,
                                                            },
                                                        },
                                                    },
                                                    "10.84.66.66 10.84.66.66": {
                                                        "adv_router": "10.84.66.66",
                                                        "lsa_id": "10.84.66.66",
                                                        "ospfv2": {
                                                            "body": {
                                                                "router": {
                                                                    "links": {
                                                                        "10.229.6.6": {
                                                                            "link_data": "10.229.6.6",
                                                                            "link_id": "10.229.6.6",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.115.6.6": {
                                                                            "link_data": "10.115.6.6",
                                                                            "link_id": "10.115.6.6",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 30,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.166.7.6": {
                                                                            "link_data": "10.166.7.6",
                                                                            "link_id": "10.166.7.6",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 30,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.84.66.66": {
                                                                            "link_data": "255.255.255.255",
                                                                            "link_id": "10.84.66.66",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "stub "
                                                                            "network",
                                                                        },
                                                                    },
                                                                    "num_of_links": 4,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.84.66.66",
                                                                "age": 1578,
                                                                "checksum": "0x1282",
                                                                "length": 72,
                                                                "lsa_id": "10.84.66.66",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "routing_bit_enable": True,
                                                                "seq_num": "8000003c",
                                                                "type": 1,
                                                            },
                                                        },
                                                    },
                                                    "10.1.77.77 10.1.77.77": {
                                                        "adv_router": "10.1.77.77",
                                                        "lsa_id": "10.1.77.77",
                                                        "ospfv2": {
                                                            "body": {
                                                                "router": {
                                                                    "links": {
                                                                        "10.19.7.7": {
                                                                            "link_data": "10.19.7.7",
                                                                            "link_id": "10.19.7.7",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.166.7.6": {
                                                                            "link_data": "10.166.7.7",
                                                                            "link_id": "10.166.7.6",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 30,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit "
                                                                            "network",
                                                                        },
                                                                        "10.1.77.77": {
                                                                            "link_data": "255.255.255.255",
                                                                            "link_id": "10.1.77.77",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
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
                                                                "adv_router": "10.1.77.77",
                                                                "age": 1344,
                                                                "checksum": "0x1379",
                                                                "length": 60,
                                                                "lsa_id": "10.1.77.77",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "DC",
                                                                "routing_bit_enable": True,
                                                                "seq_num": "80000030",
                                                                "type": 1,
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
        },
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "mpls1": {
                            "areas": {
                                "0.0.0.0": {
                                    "database": {
                                        "lsa_types": {
                                            1: {
                                                "lsa_type": 1,
                                                "lsas": {
                                                    "10.4.1.1 10.4.1.1": {
                                                        "adv_router": "10.4.1.1",
                                                        "lsa_id": "10.4.1.1",
                                                        "ospfv2": {
                                                            "body": {
                                                                "router": {
                                                                    "links": {
                                                                        "10.4.1.1": {
                                                                            "link_data": "255.255.255.255",
                                                                            "link_id": "10.4.1.1",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "stub network",
                                                                        },
                                                                        "10.1.2.1": {
                                                                            "link_data": "10.1.2.1",
                                                                            "link_id": "10.1.2.1",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.1.4.4": {
                                                                            "link_data": "10.1.4.1",
                                                                            "link_id": "10.1.4.4",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                    },
                                                                    "num_of_links": 3,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.4.1.1",
                                                                "age": 1802,
                                                                "checksum": "0x6228",
                                                                "length": 60,
                                                                "lsa_id": "10.4.1.1",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "DC",
                                                                "routing_bit_enable": True,
                                                                "seq_num": "8000003d",
                                                                "type": 1,
                                                            },
                                                        },
                                                    },
                                                    "10.16.2.2 10.16.2.2": {
                                                        "adv_router": "10.16.2.2",
                                                        "lsa_id": "10.16.2.2",
                                                        "ospfv2": {
                                                            "body": {
                                                                "router": {
                                                                    "links": {
                                                                        "10.1.2.1": {
                                                                            "link_data": "10.1.2.2",
                                                                            "link_id": "10.1.2.1",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.2.3.3": {
                                                                            "link_data": "10.2.3.2",
                                                                            "link_id": "10.2.3.3",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.2.4.4": {
                                                                            "link_data": "10.2.4.2",
                                                                            "link_id": "10.2.4.4",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.16.2.2": {
                                                                            "link_data": "255.255.255.255",
                                                                            "link_id": "10.16.2.2",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "stub network",
                                                                        },
                                                                    },
                                                                    "num_of_links": 4,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.16.2.2",
                                                                "age": 756,
                                                                "checksum": "0x652b",
                                                                "length": 72,
                                                                "lsa_id": "10.16.2.2",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "No "
                                                                "DC",
                                                                "routing_bit_enable": True,
                                                                "seq_num": "80000014",
                                                                "type": 1,
                                                            },
                                                        },
                                                    },
                                                    "10.36.3.3 10.36.3.3": {
                                                        "adv_router": "10.36.3.3",
                                                        "lsa_id": "10.36.3.3",
                                                        "ospfv2": {
                                                            "body": {
                                                                "router": {
                                                                    "links": {
                                                                        "10.2.3.3": {
                                                                            "link_data": "10.2.3.3",
                                                                            "link_id": "10.2.3.3",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.3.4.4": {
                                                                            "link_data": "10.3.4.3",
                                                                            "link_id": "10.3.4.4",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.36.3.3": {
                                                                            "link_data": "255.255.255.255",
                                                                            "link_id": "10.36.3.3",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
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
                                                                "adv_router": "10.36.3.3",
                                                                "age": 1291,
                                                                "checksum": "0x75f8",
                                                                "length": 60,
                                                                "lsa_id": "10.36.3.3",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "DC",
                                                                "seq_num": "80000033",
                                                                "type": 1,
                                                            },
                                                        },
                                                    },
                                                    "10.64.4.4 10.64.4.4": {
                                                        "adv_router": "10.64.4.4",
                                                        "lsa_id": "10.64.4.4",
                                                        "ospfv2": {
                                                            "body": {
                                                                "router": {
                                                                    "links": {
                                                                        "10.1.4.4": {
                                                                            "link_data": "10.1.4.4",
                                                                            "link_id": "10.1.4.4",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.2.4.4": {
                                                                            "link_data": "10.2.4.4",
                                                                            "link_id": "10.2.4.4",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.3.4.4": {
                                                                            "link_data": "10.3.4.4",
                                                                            "link_id": "10.3.4.4",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.64.4.4": {
                                                                            "link_data": "255.255.255.255",
                                                                            "link_id": "10.64.4.4",
                                                                            "num_tos_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "stub network",
                                                                        },
                                                                    },
                                                                    "num_of_links": 4,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.64.4.4",
                                                                "age": 505,
                                                                "as_boundary_router": True,
                                                                "checksum": "0xa37d",
                                                                "length": 72,
                                                                "lsa_id": "10.64.4.4",
                                                                "option": "None",
                                                                "option_desc": "No "
                                                                "TOS-capability, "
                                                                "DC",
                                                                "routing_bit_enable": True,
                                                                "seq_num": "80000037",
                                                                "type": 1,
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
        },
    }
}
