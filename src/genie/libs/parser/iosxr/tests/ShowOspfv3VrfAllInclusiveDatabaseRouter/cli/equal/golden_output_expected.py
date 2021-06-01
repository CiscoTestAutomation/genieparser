expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'instance': {
                        'mpls1': {
                            'areas': {
                                '0.0.0.0': {
                                    'database': {
                                        'lsa_types': {
                                            1: {
                                                'lsa_type': 1,
                                                'lsas': {
                                                    '0 25.97.1.1': {
                                                        'adv_router': '25.97.1.1',
                                                        'lsa_id': 0,
                                                        'ospfv3': {
                                                            'body': {
                                                                'num_of_links': 2,
                                                                'links': {
                                                                    1: {
                                                                        'link_metric': 1,
                                                                        'local_interface_id': 6,
                                                                        'neighbor_interface_id': 6,
                                                                        'neighbor_router_id': '96.96.96.96',
                                                                        'type': 'transit network'
                                                                    },
                                                                    2: {
                                                                        'link_metric': 1,
                                                                        'local_interface_id': 7,
                                                                        'neighbor_interface_id': 6,
                                                                        'neighbor_router_id': '95.95.95.95',
                                                                        'type': 'another router (point-to-point)'
                                                                    }
                                                                },
                                                            },
                                                            'header': {
                                                                'adv_router': '25.97.1.1',
                                                                'age': 31,
                                                                'as_boundary_router': True,
                                                                'checksum': '0x440',
                                                                'length': 56,
                                                                'lsa_id': 0,
                                                                'options': 'V6-Bit E-Bit R-Bit DC-Bit',
                                                                'seq_num': '80000013',
                                                                'type': 'Router Links'
                                                            }
                                                        }
                                                    },
                                                    '0 95.95.95.95': {
                                                        'adv_router': '95.95.95.95',
                                                        'lsa_id': 0,
                                                        'ospfv3': {
                                                            'body': {
                                                                'num_of_links': 2,
                                                                'links': {
                                                                    1: {
                                                                        'link_metric': 10,
                                                                        'local_interface_id': 7,
                                                                        'neighbor_interface_id': 7,
                                                                        'neighbor_router_id': '96.96.96.96',
                                                                        'type': 'another router (point-to-point)'
                                                                    },
                                                                    2: {
                                                                        'link_metric': 1,
                                                                        'local_interface_id': 6,
                                                                        'neighbor_interface_id': 7,
                                                                        'neighbor_router_id': '25.97.1.1',
                                                                        'type': 'another router (point-to-point)'
                                                                    }
                                                                },
                                                            },
                                                            'header': {
                                                                'adv_router': '95.95.95.95',
                                                                'age': 789,
                                                                'as_boundary_router': True,
                                                                'checksum': '0x6fda',
                                                                'length': 56,
                                                                'lsa_id': 0,
                                                                'options': 'V6-Bit E-Bit R-Bit DC-Bit',
                                                                'routing_bit_enable': True,
                                                                'seq_num': '80000003',
                                                                'type': 'Router Links'
                                                            }
                                                        }
                                                    },
                                                    '0 96.96.96.96': {
                                                        'adv_router': '96.96.96.96',
                                                        'lsa_id': 0,
                                                        'ospfv3': {
                                                            'body': {
                                                                'num_of_links': 2,
                                                                'links': {
                                                                    1: {
                                                                        'link_metric': 1,
                                                                        'local_interface_id': 6,
                                                                        'neighbor_interface_id': 6,
                                                                        'neighbor_router_id': '96.96.96.96',
                                                                        'type': 'transit network'
                                                                    },
                                                                    2: {
                                                                        'link_metric': 10,
                                                                        'local_interface_id': 7,
                                                                        'neighbor_interface_id': 7,
                                                                        'neighbor_router_id': '95.95.95.95',
                                                                        'type': 'another router (point-to-point)'
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'adv_router': '96.96.96.96',
                                                                'age': 32,
                                                                'as_boundary_router': True,
                                                                'checksum': '0xc572',
                                                                'length': 56,
                                                                'lsa_id': 0,
                                                                'options': 'V6-Bit E-Bit R-Bit DC-Bit',
                                                                'routing_bit_enable': True,
                                                                'seq_num': '80000010',
                                                                'type': 'Router Links'
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
