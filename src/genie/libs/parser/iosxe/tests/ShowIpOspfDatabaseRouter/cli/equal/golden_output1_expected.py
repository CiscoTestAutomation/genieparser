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
                                                                            "num_mtid_metrics": 2,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                },
                                                                                32: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 32,
                                                                                },
                                                                                33: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 33,
                                                                                },
                                                                            },
                                                                            "type": "stub network",
                                                                        },
                                                                        "10.1.2.1": {
                                                                            "link_data": "10.1.2.1",
                                                                            "link_id": "10.1.2.1",
                                                                            "num_mtid_metrics": 0,
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
                                                                            "num_mtid_metrics": 0,
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
                                                                "age": 742,
                                                                "checksum": "0x6228",
                                                                "length": 60,
                                                                "lsa_id": "10.4.1.1",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "8000003D",
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
                                                                            "num_mtid_metrics": 0,
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
                                                                            "num_mtid_metrics": 0,
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
                                                                            "num_mtid_metrics": 0,
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
                                                                    },
                                                                    "num_of_links": 4,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.16.2.2",
                                                                "age": 1520,
                                                                "checksum": "0x672A",
                                                                "length": 72,
                                                                "lsa_id": "10.16.2.2",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, No DC",
                                                                "seq_num": "80000013",
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
                                                                            "num_mtid_metrics": 0,
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
                                                                            "num_mtid_metrics": 0,
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
                                                                    },
                                                                    "num_of_links": 3,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.36.3.3",
                                                                "age": 235,
                                                                "checksum": "0x75F8",
                                                                "length": 60,
                                                                "lsa_id": "10.36.3.3",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
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
                                                                            "num_mtid_metrics": 0,
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
                                                                            "num_mtid_metrics": 0,
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
                                                                            "num_mtid_metrics": 0,
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
                                                                    },
                                                                    "num_of_links": 4,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.64.4.4",
                                                                "age": 1486,
                                                                "as_boundary_router": True,
                                                                "checksum": "0xA57C",
                                                                "length": 72,
                                                                "lsa_id": "10.64.4.4",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "80000036",
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
                        },
                        "2": {
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
                                                                            "num_mtid_metrics": 0,
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
                                                                            "num_mtid_metrics": 0,
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
                                                                "age": 651,
                                                                "area_border_router": True,
                                                                "as_boundary_router": True,
                                                                "checksum": "0x9CE3",
                                                                "length": 48,
                                                                "lsa_id": "10.229.11.11",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "8000003E",
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
                                                                            "num_mtid_metrics": 0,
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
                                                                            "num_mtid_metrics": 0,
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
                                                                "age": 480,
                                                                "area_border_router": True,
                                                                "as_boundary_router": True,
                                                                "checksum": "0xC41A",
                                                                "length": 48,
                                                                "lsa_id": "10.151.22.22",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, No DC",
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
                                                                            "num_mtid_metrics": 0,
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
                                                                "age": 1128,
                                                                "area_border_router": True,
                                                                "as_boundary_router": True,
                                                                "checksum": "0x5845",
                                                                "length": 36,
                                                                "lsa_id": "10.36.3.3",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "80000035",
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
                                                                            "num_mtid_metrics": 0,
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
                                                                            "num_mtid_metrics": 0,
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
                                                                    },
                                                                    "num_of_links": 3,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.115.55.55",
                                                                "age": 318,
                                                                "checksum": "0xE7BC",
                                                                "length": 60,
                                                                "lsa_id": "10.115.55.55",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
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
                                                                            "num_mtid_metrics": 0,
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
                                                                            "num_mtid_metrics": 0,
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
                                                                            "num_mtid_metrics": 0,
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
                                                                    },
                                                                    "num_of_links": 4,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.84.66.66",
                                                                "age": 520,
                                                                "checksum": "0x1282",
                                                                "length": 72,
                                                                "lsa_id": "10.84.66.66",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "8000003C",
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
                                                                            "num_mtid_metrics": 0,
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
                                                                            "num_mtid_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 30,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "transit network",
                                                                        },
                                                                        "10.1.77.77": {
                                                                            "link_data": "255.255.255.255",
                                                                            "link_id": "10.1.77.77",
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
                                                                    },
                                                                    "num_of_links": 3,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.1.77.77",
                                                                "age": 288,
                                                                "checksum": "0x1379",
                                                                "length": 60,
                                                                "lsa_id": "10.1.77.77",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
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
                        },
                        "3": {
                            "areas": {
                                "0.0.0.0": {
                                    "database": {
                                        "lsa_types": {
                                            1: {
                                                "lsa_type": 1,
                                                "lsas": {
                                                    "10.115.11.11 10.115.11.11": {
                                                        "adv_router": "10.115.11.11",
                                                        "lsa_id": "10.115.11.11",
                                                        "ospfv2": {
                                                            "body": {
                                                                "router": {
                                                                    "links": {
                                                                        "10.115.11.11": {
                                                                            "link_data": "255.255.255.255",
                                                                            "link_id": "10.115.11.11",
                                                                            "num_mtid_metrics": 0,
                                                                            "topologies": {
                                                                                0: {
                                                                                    "metric": 1,
                                                                                    "mt_id": 0,
                                                                                    "tos": 0,
                                                                                }
                                                                            },
                                                                            "type": "stub network",
                                                                        }
                                                                    },
                                                                    "num_of_links": 1,
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.115.11.11",
                                                                "age": 50,
                                                                "as_boundary_router": True,
                                                                "checksum": "0x881A",
                                                                "length": 36,
                                                                "lsa_id": "10.115.11.11",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "80000001",
                                                                "type": 1,
                                                            },
                                                        },
                                                    }
                                                },
                                            }
                                        }
                                    }
                                },
                                "0.0.0.11": {
                                    "database": {
                                        "lsa_types": {
                                            1: {
                                                "lsa_type": 1,
                                                "lsas": {
                                                    "10.115.11.11 10.115.11.11": {
                                                        "adv_router": "10.115.11.11",
                                                        "lsa_id": "10.115.11.11",
                                                        "ospfv2": {
                                                            "body": {
                                                                "router": {
                                                                    "num_of_links": 0
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.115.11.11",
                                                                "age": 8,
                                                                "as_boundary_router": True,
                                                                "checksum": "0x1D1B",
                                                                "length": 24,
                                                                "lsa_id": "10.115.11.11",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "seq_num": "80000001",
                                                                "type": 1,
                                                            },
                                                        },
                                                    }
                                                },
                                            }
                                        }
                                    }
                                },
                            }
                        },
                    }
                }
            }
        }
    }
}
