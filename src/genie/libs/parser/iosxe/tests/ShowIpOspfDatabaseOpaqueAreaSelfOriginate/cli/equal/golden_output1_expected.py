expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        '100': {
                            'areas': {
                                '0.0.0.0': {
                                    'database': {
                                        'lsa_types': {
                                            10: {
                                                'lsa_type': 10,
                                                'lsas': {
                                                    '1.0.0.0 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '1.0.0.0',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'mpls_te_router_id': '1.1.1.1',
                                                                    'num_of_links': 0
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '1.0.0.0',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_type': 1,
                                                                'opaque_id': 0,
                                                                'seq_num': '8000000E',
                                                                'checksum': '0x3EDE',
                                                                'length': 28,
                                                                'fragment_number': 0
                                                            }
                                                        }
                                                    },
                                                    '1.0.0.25 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '1.0.0.25',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'link_tlvs': {
                                                                        1: {
                                                                            'link_type': 1,
                                                                            'link_name': 'point-to-point network',
                                                                            'link_id': '1.1.1.6',
                                                                            'te_metric': 2,
                                                                            'max_bandwidth': 125000000,
                                                                            'admin_group': '0x80000001',
                                                                            'igp_metric': 1
                                                                        }
                                                                    },
                                                                    'num_of_links': 1
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '1.0.0.25',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_type': 1,
                                                                'opaque_id': 25,
                                                                'seq_num': '8000000E',
                                                                'checksum': '0xDD6',
                                                                'length': 120,
                                                                'fragment_number': 25
                                                            }
                                                        }
                                                    },
                                                    '4.0.0.0 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '4.0.0.0',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'router_capabilities_tlv': {
                                                                        1: {
                                                                            'tlv_type': 'Router Information',
                                                                            'length': 4,
                                                                            'information_capabilities': {
                                                                                'graceful_restart_helper': True,
                                                                                'stub_router': True
                                                                            }
                                                                        }
                                                                    },
                                                                    'sr_algorithm_tlv': {
                                                                        1: {
                                                                            'tlv_type': 'Segment Routing Algorithm',
                                                                            'length': 2,
                                                                            'algorithm': {
                                                                                'spf': True,
                                                                                'strict_spf': True
                                                                            }
                                                                        }
                                                                    },
                                                                    'sid_range_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Segment Routing Range',
                                                                            'length': 12,
                                                                            'range_size': 8000,
                                                                            'sub_tlvs': {
                                                                                1: {
                                                                                    'type': 'SID/Label',
                                                                                    'local_interface_id': 21,
                                                                                    'remote_interface_id': 20,
                                                                                    'length': 3,
                                                                                    'label': 16000
                                                                                }
                                                                            }
                                                                        }
                                                                    },
                                                                    'node_msd_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Segment Routing Node MSD',
                                                                            'length': 2,
                                                                            'sub_type': {
                                                                                'node_max_sid_depth_value': 16
                                                                            }
                                                                        }
                                                                    },
                                                                    'local_block_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Segment Routing Local Block',
                                                                            'length': 12,
                                                                            'range_size': 1000,
                                                                            'sub_tlvs': {
                                                                                1: {
                                                                                    'type': 'SID/Label',
                                                                                    'length': 3,
                                                                                    'label': 15000
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '4.0.0.0',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_id': 0,
                                                                'seq_num': '80000016',
                                                                'checksum': '0x2126',
                                                                'length': 76
                                                            }
                                                        }
                                                    },
                                                    '7.0.0.0 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '7.0.0.0',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'extended_prefix_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Extended Prefix',
                                                                            'length': 32,
                                                                            'prefix': '1.1.1.1/32',
                                                                            'af': 0,
                                                                            'route_type': 'Intra',
                                                                            'flags': 'N-bit',
                                                                            'sub_tlvs': {
                                                                                1: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'None',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'SPF',
                                                                                    'sid': 1
                                                                                },
                                                                                2: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'None',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'Strict SPF',
                                                                                    'sid': 101
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '7.0.0.0',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_id': 0,
                                                                'seq_num': '80000013',
                                                                'checksum': '0x8478',
                                                                'length': 56
                                                            }
                                                        }
                                                    },
                                                    '7.0.0.1 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '7.0.0.1',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'extended_prefix_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Extended Prefix',
                                                                            'length': 20,
                                                                            'prefix': '1.1.1.11/32',
                                                                            'af': 0,
                                                                            'route_type': 'Inter',
                                                                            'flags': 'N-bit, A-bit',
                                                                            'sub_tlvs': {
                                                                                1: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'None',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'Strict SPF',
                                                                                    'sid': 111
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '7.0.0.1',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_id': 1,
                                                                'seq_num': '8000000E',
                                                                'checksum': '0xB8D4',
                                                                'length': 44
                                                            }
                                                        }
                                                    },
                                                    '8.0.0.21 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '8.0.0.21',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'extended_link_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Extended Link',
                                                                            'length': 128,
                                                                            'link_name': 'another router (point-to-point)',
                                                                            'link_type': 1,
                                                                            'link_id': '1.1.1.6',
                                                                            'link_data': '0.0.0.21',
                                                                            'sub_tlvs': {
                                                                                1: {
                                                                                    'type': 'Adj SID',
                                                                                    'length': 7,
                                                                                    'flags': 'L-Bit, V-bit',
                                                                                    'mt_id': 0,
                                                                                    'weight': 0,
                                                                                    'label': 17
                                                                                },
                                                                                2: {
                                                                                    'type': 'Adj SID',
                                                                                    'length': 7,
                                                                                    'flags': 'L-Bit, V-bit, B-bit',
                                                                                    'mt_id': 0,
                                                                                    'weight': 0,
                                                                                    'label': 19
                                                                                },
                                                                                3: {
                                                                                    'type': 'Local / Remote Intf ID',
                                                                                    'local_interface_id': 21,
                                                                                    'remote_interface_id': 20
                                                                                },
                                                                                4: {
                                                                                    'type': 'ASLA',
                                                                                    'length': 4
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '8.0.0.21',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_id': 21,
                                                                'seq_num': '80000011',
                                                                'checksum': '0x1337',
                                                                'length': 152
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                '0.0.0.1': {
                                    'database': {
                                        'lsa_types': {
                                            10: {
                                                'lsa_type': 10,
                                                'lsas': {
                                                    '1.0.0.0 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '1.0.0.0',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'mpls_te_router_id': '1.1.1.1',
                                                                    'num_of_links': 0
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '1.0.0.0',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_type': 1,
                                                                'opaque_id': 0,
                                                                'seq_num': '8000000E',
                                                                'checksum': '0x3EDE',
                                                                'length': 28,
                                                                'fragment_number': 0
                                                            }
                                                        }
                                                    },
                                                    '4.0.0.0 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '4.0.0.0',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'router_capabilities_tlv': {
                                                                        1: {
                                                                            'tlv_type': 'Router Information',
                                                                            'length': 4,
                                                                            'information_capabilities': {
                                                                                'graceful_restart_helper': True,
                                                                                'stub_router': True
                                                                            }
                                                                        }
                                                                    },
                                                                    'sr_algorithm_tlv': {
                                                                        1: {
                                                                            'tlv_type': 'Segment Routing Algorithm',
                                                                            'length': 2,
                                                                            'algorithm': {
                                                                                'spf': True,
                                                                                'strict_spf': True
                                                                            }
                                                                        }
                                                                    },
                                                                    'sid_range_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Segment Routing Range',
                                                                            'length': 12,
                                                                            'range_size': 8000,
                                                                            'sub_tlvs': {
                                                                                1: {
                                                                                    'type': 'SID/Label',
                                                                                    'length': 3,
                                                                                    'label': 16000
                                                                                }
                                                                            }
                                                                        }
                                                                    },
                                                                    'node_msd_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Segment Routing Node MSD',
                                                                            'length': 2,
                                                                            'sub_type': {
                                                                                'node_max_sid_depth_value': 16
                                                                            }
                                                                        }
                                                                    },
                                                                    'local_block_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Segment Routing Local Block',
                                                                            'length': 12,
                                                                            'range_size': 1000,
                                                                            'sub_tlvs': {
                                                                                1: {
                                                                                    'type': 'SID/Label',
                                                                                    'length': 3,
                                                                                    'label': 15000
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '4.0.0.0',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_id': 0,
                                                                'seq_num': '80000016',
                                                                'checksum': '0x91A5',
                                                                'length': 76
                                                            }
                                                        }
                                                    },
                                                    '7.0.0.0 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '7.0.0.0',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'extended_prefix_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Extended Prefix',
                                                                            'length': 20,
                                                                            'prefix': '1.1.1.11/32',
                                                                            'af': 0,
                                                                            'route_type': 'Intra',
                                                                            'flags': 'N-bit',
                                                                            'sub_tlvs': {
                                                                                1: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'None',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'Strict SPF',
                                                                                    'sid': 111
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '7.0.0.0',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_id': 0,
                                                                'seq_num': '80000013',
                                                                'checksum': '0xA566',
                                                                'length': 44
                                                            }
                                                        }
                                                    },
                                                    '7.0.0.1 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '7.0.0.1',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'extended_prefix_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Extended Prefix',
                                                                            'length': 32,
                                                                            'prefix': '1.1.1.1/32',
                                                                            'af': 0,
                                                                            'route_type': 'Inter',
                                                                            'flags': 'N-bit, A-bit',
                                                                            'sub_tlvs': {
                                                                                1: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'None',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'SPF',
                                                                                    'sid': 1
                                                                                },
                                                                                2: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'None',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'Strict SPF',
                                                                                    'sid': 101
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '7.0.0.1',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_id': 1,
                                                                'seq_num': '8000000E',
                                                                'checksum': '0x97E6',
                                                                'length': 56
                                                            }
                                                        }
                                                    },
                                                    '7.0.0.2 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '7.0.0.2',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'extended_prefix_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Extended Prefix',
                                                                            'length': 32,
                                                                            'prefix': '1.1.1.2/32',
                                                                            'af': 0,
                                                                            'route_type': 'Inter',
                                                                            'flags': 'N-bit',
                                                                            'sub_tlvs': {
                                                                                1: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'NP-bit',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'SPF',
                                                                                    'sid': 2
                                                                                },
                                                                                2: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'NP-bit',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'Strict SPF',
                                                                                    'sid': 102
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '7.0.0.2',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_id': 2,
                                                                'seq_num': '8000000F',
                                                                'checksum': '0x6118',
                                                                'length': 56
                                                            }
                                                        }
                                                    },
                                                    '7.0.0.3 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '7.0.0.3',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'extended_prefix_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Extended Prefix',
                                                                            'length': 32,
                                                                            'prefix': '1.1.1.3/32',
                                                                            'af': 0,
                                                                            'route_type': 'Inter',
                                                                            'flags': 'N-bit',
                                                                            'sub_tlvs': {
                                                                                1: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'NP-bit',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'SPF',
                                                                                    'sid': 3
                                                                                },
                                                                                2: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'NP-bit',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'Strict SPF',
                                                                                    'sid': 103
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '7.0.0.3',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_id': 3,
                                                                'seq_num': '8000000E',
                                                                'checksum': '0xA7CE',
                                                                'length': 56
                                                            }
                                                        }
                                                    },
                                                    '7.0.0.4 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '7.0.0.4',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'extended_prefix_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Extended Prefix',
                                                                            'length': 32,
                                                                            'prefix': '1.1.1.4/32',
                                                                            'af': 0,
                                                                            'route_type': 'Inter',
                                                                            'flags': 'N-bit',
                                                                            'sub_tlvs': {
                                                                                1: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'NP-bit',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'SPF',
                                                                                    'sid': 4
                                                                                },
                                                                                2: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'NP-bit',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'Strict SPF',
                                                                                    'sid': 104
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '7.0.0.4',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_id': 4,
                                                                'seq_num': '8000000E',
                                                                'checksum': '0xEB86',
                                                                'length': 56
                                                            }
                                                        }
                                                    },
                                                    '7.0.0.5 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '7.0.0.5',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'extended_prefix_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Extended Prefix',
                                                                            'length': 20,
                                                                            'prefix': '1.1.1.14/32',
                                                                            'af': 0,
                                                                            'route_type': 'Inter',
                                                                            'flags': 'N-bit',
                                                                            'sub_tlvs': {
                                                                                1: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'NP-bit',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'Strict SPF',
                                                                                    'sid': 114
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '7.0.0.5',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_id': 5,
                                                                'seq_num': '8000000E',
                                                                'checksum': '0xC8FA',
                                                                'length': 44
                                                            }
                                                        }
                                                    },
                                                    '7.0.0.6 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '7.0.0.6',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'extended_prefix_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Extended Prefix',
                                                                            'length': 32,
                                                                            'prefix': '1.1.1.5/32',
                                                                            'af': 0,
                                                                            'route_type': 'Inter',
                                                                            'flags': 'N-bit',
                                                                            'sub_tlvs': {
                                                                                1: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'NP-bit',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'SPF',
                                                                                    'sid': 5
                                                                                },
                                                                                2: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'NP-bit',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'Strict SPF',
                                                                                    'sid': 105
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '7.0.0.6',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_id': 6,
                                                                'seq_num': '8000000F',
                                                                'checksum': '0x2448',
                                                                'length': 56
                                                            }
                                                        }
                                                    },
                                                    '7.0.0.7 1.1.1.1': {
                                                        'adv_router': '1.1.1.1',
                                                        'lsa_id': '7.0.0.7',
                                                        'ospfv2': {
                                                            'body': {
                                                                'opaque': {
                                                                    'extended_prefix_tlvs': {
                                                                        1: {
                                                                            'tlv_type': 'Extended Prefix',
                                                                            'length': 32,
                                                                            'prefix': '1.1.1.6/32',
                                                                            'af': 0,
                                                                            'route_type': 'Inter',
                                                                            'flags': 'N-bit',
                                                                            'sub_tlvs': {
                                                                                1: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'NP-bit',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'SPF',
                                                                                    'sid': 6
                                                                                },
                                                                                2: {
                                                                                    'type': 'Prefix SID',
                                                                                    'length': 8,
                                                                                    'flags': 'NP-bit',
                                                                                    'mt_id': 0,
                                                                                    'algo': 'Strict SPF',
                                                                                    'sid': 106
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'age': 1673,
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'type': 10,
                                                                'lsa_id': '7.0.0.7',
                                                                'adv_router': '1.1.1.1',
                                                                'opaque_id': 7,
                                                                'seq_num': '8000000F',
                                                                'checksum': '0x68FF',
                                                                'length': 56
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
            }
        }
    }
}
