expected_output = {
    "vrf": {
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
                                                    "25.97.1.1 25.97.1.1": {
                                                        "adv_router": "25.97.1.1",
                                                        "lsa_id": "25.97.1.1",
                                                        "ospfv2": {
                                                            "header": {
                                                                "age": 143,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 1,
                                                                "lsa_id": "25.97.1.1",
                                                                "adv_router": "25.97.1.1",
                                                                "seq_num": "80000008",
                                                                "checksum": "0x9817",
                                                                "length": 84,
                                                                "as_boundary_router": True,
                                                            },
                                                            "body": {
                                                                "router": {
                                                                    "num_of_links": 5,
                                                                    "links": {
                                                                        "25.97.1.1": {
                                                                            "link_id": "25.97.1.1",
                                                                            "type": "stub network",
                                                                            "topologies": {
                                                                                0: {
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                    "metric": 65535,
                                                                                }
                                                                            },
                                                                            "link_data": "255.255.255.255",
                                                                            "num_tos_metrics": 0,
                                                                        },
                                                                        "96.96.96.96": {
                                                                            "link_id": "96.96.96.96",
                                                                            "type": "another router (point-to-point)",
                                                                            "topologies": {
                                                                                0: {
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                    "metric": 65535,
                                                                                }
                                                                            },
                                                                            "link_data": "100.10.0.1",
                                                                            "num_tos_metrics": 0,
                                                                        },
                                                                        "100.10.0.0": {
                                                                            "link_id": "100.10.0.0",
                                                                            "type": "stub network",
                                                                            "topologies": {
                                                                                0: {
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                    "metric": 65535,
                                                                                }
                                                                            },
                                                                            "link_data": "255.255.255.252",
                                                                            "num_tos_metrics": 0,
                                                                        },
                                                                        "95.95.95.95": {
                                                                            "link_id": "95.95.95.95",
                                                                            "type": "another router (point-to-point)",
                                                                            "topologies": {
                                                                                0: {
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                    "metric": 65535,
                                                                                }
                                                                            },
                                                                            "link_data": "100.20.0.1",
                                                                            "num_tos_metrics": 0,
                                                                        },
                                                                        "100.20.0.0": {
                                                                            "link_id": "100.20.0.0",
                                                                            "type": "stub network",
                                                                            "topologies": {
                                                                                0: {
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                    "metric": 65535,
                                                                                }
                                                                            },
                                                                            "link_data": "255.255.255.252",
                                                                            "num_tos_metrics": 0,
                                                                        },
                                                                    },
                                                                }
                                                            },
                                                        },
                                                    },
                                                    "95.95.95.95 95.95.95.95": {
                                                        "adv_router": "95.95.95.95",
                                                        "lsa_id": "95.95.95.95",
                                                        "ospfv2": {
                                                            "header": {
                                                                "routing_bit_enable": True,
                                                                "age": 1160,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 1,
                                                                "lsa_id": "95.95.95.95",
                                                                "adv_router": "95.95.95.95",
                                                                "seq_num": "80000004",
                                                                "checksum": "0x4cb",
                                                                "length": 84,
                                                                "as_boundary_router": True,
                                                            },
                                                            "body": {
                                                                "router": {
                                                                    "num_of_links": 5,
                                                                    "links": {
                                                                        "95.95.95.95": {
                                                                            "link_id": "95.95.95.95",
                                                                            "type": "stub network",
                                                                            "topologies": {
                                                                                0: {
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                    "metric": 1,
                                                                                }
                                                                            },
                                                                            "link_data": "255.255.255.255",
                                                                            "num_tos_metrics": 0,
                                                                        },
                                                                        "25.97.1.1": {
                                                                            "link_id": "25.97.1.1",
                                                                            "type": "another router (point-to-point)",
                                                                            "topologies": {
                                                                                0: {
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                    "metric": 1,
                                                                                }
                                                                            },
                                                                            "link_data": "100.20.0.2",
                                                                            "num_tos_metrics": 0,
                                                                        },
                                                                        "100.20.0.0": {
                                                                            "link_id": "100.20.0.0",
                                                                            "type": "stub network",
                                                                            "topologies": {
                                                                                0: {
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                    "metric": 1,
                                                                                }
                                                                            },
                                                                            "link_data": "255.255.255.252",
                                                                            "num_tos_metrics": 0,
                                                                        },
                                                                        "96.96.96.96": {
                                                                            "link_id": "96.96.96.96",
                                                                            "type": "another router (point-to-point)",
                                                                            "topologies": {
                                                                                0: {
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                    "metric": 10,
                                                                                }
                                                                            },
                                                                            "link_data": "200.10.0.2",
                                                                            "num_tos_metrics": 0,
                                                                        },
                                                                        "200.10.0.0": {
                                                                            "link_id": "200.10.0.0",
                                                                            "type": "stub network",
                                                                            "topologies": {
                                                                                0: {
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                    "metric": 10,
                                                                                }
                                                                            },
                                                                            "link_data": "255.255.255.252",
                                                                            "num_tos_metrics": 0,
                                                                        },
                                                                    },
                                                                }
                                                            },
                                                        },
                                                    },
                                                    "96.96.96.96 96.96.96.96": {
                                                        "adv_router": "96.96.96.96",
                                                        "lsa_id": "96.96.96.96",
                                                        "ospfv2": {
                                                            "header": {
                                                                "routing_bit_enable": True,
                                                                "age": 1277,
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "type": 1,
                                                                "lsa_id": "96.96.96.96",
                                                                "adv_router": "96.96.96.96",
                                                                "seq_num": "80000005",
                                                                "checksum": "0xc01b",
                                                                "length": 84,
                                                                "as_boundary_router": True,
                                                            },
                                                            "body": {
                                                                "router": {
                                                                    "num_of_links": 5,
                                                                    "links": {
                                                                        "96.96.96.96": {
                                                                            "link_id": "96.96.96.96",
                                                                            "type": "stub network",
                                                                            "topologies": {
                                                                                0: {
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                    "metric": 1,
                                                                                }
                                                                            },
                                                                            "link_data": "255.255.255.255",
                                                                            "num_tos_metrics": 0,
                                                                        },
                                                                        "25.97.1.1": {
                                                                            "link_id": "25.97.1.1",
                                                                            "type": "another router (point-to-point)",
                                                                            "topologies": {
                                                                                0: {
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                    "metric": 1,
                                                                                }
                                                                            },
                                                                            "link_data": "100.10.0.2",
                                                                            "num_tos_metrics": 0,
                                                                        },
                                                                        "100.10.0.0": {
                                                                            "link_id": "100.10.0.0",
                                                                            "type": "stub network",
                                                                            "topologies": {
                                                                                0: {
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                    "metric": 1,
                                                                                }
                                                                            },
                                                                            "link_data": "255.255.255.252",
                                                                            "num_tos_metrics": 0,
                                                                        },
                                                                        "95.95.95.95": {
                                                                            "link_id": "95.95.95.95",
                                                                            "type": "another router (point-to-point)",
                                                                            "topologies": {
                                                                                0: {
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                    "metric": 10,
                                                                                }
                                                                            },
                                                                            "link_data": "200.10.0.1",
                                                                            "num_tos_metrics": 0,
                                                                        },
                                                                        "200.10.0.0": {
                                                                            "link_id": "200.10.0.0",
                                                                            "type": "stub network",
                                                                            "topologies": {
                                                                                0: {
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                    "metric": 10,
                                                                                }
                                                                            },
                                                                            "link_data": "255.255.255.252",
                                                                            "num_tos_metrics": 0,
                                                                        },
                                                                    },
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
}
