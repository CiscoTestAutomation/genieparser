expected_output = {
    'tag': {
        'null': {
            'level': {
                2: {
                    'iolPE1.00-00': {
                        'local_router': True,
                        'lsp_sequence_num': '0x00000004',
                        'lsp_checksum': '0x271B',
                        'lsp_holdtime': '872',
                        'lsp_rcvd': '*',
                        'attach_bit': 0,
                        'p_bit': 0,
                        'overload_bit': 0,
                        'area_address': '49.0000',
                        'nlpid': '0xCC 0x8E',
                        'router_cap': '0.0.0.0',
                        'd_flag': False,
                        's_flag': False,
                        'srv6_o_flag': False,
                        'hostname': 'iolPE1',
                        'extended_is_neighbor': {
                            'iolP1.00': [
                                {
                                    'neighbor_id': 'iolP1.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2001:1::1',
                                    'neighbor_ipv6_address': '2001:1::2',
                                    'affinity': '0x00000008',
                                    'extended_affinity': ['0x00000008'],
                                    'admin_weight': 1000,
                                    'end_x_sid': 'FCCC:CCC1:A1:E000::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    },
                                {
                                    'neighbor_id': 'iolP1.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2001:2::1',
                                    'neighbor_ipv6_address': '2001:2::2',
                                    'affinity': '0x00000008',
                                    'extended_affinity': ['0x00000008'],
                                    'admin_weight': 1000,
                                    'end_x_sid': 'FCCC:CCC1:A1:E001::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    }
                                ],
                            'iolP2.00': [
                                {
                                    'neighbor_id': 'iolP2.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2012:2::1',
                                    'neighbor_ipv6_address': '2012:2::2',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:A1:E003::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    },
                                {
                                    'neighbor_id': 'iolP2.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2012:1::1',
                                    'neighbor_ipv6_address': '2012:1::2',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:A1:E002::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    }
                                ]
                            },
                        'ipv6_address': 'C01:1::1',
                        'ipv6_router_id': 'C01:1::1',
                        'ipv6_reachability': {
                            'FCCC:CCC1:A1::/48': [
                                {
                                    'ip_prefix': 'FCCC:CCC1:A1::',
                                    'prefix_len': '48',
                                    'metric': 0,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            'C01:1::/64': [
                                {
                                    'ip_prefix': 'C01:1::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                            }
                                    }
                                ],
                            '2001:1::/64': [
                                {
                                    'ip_prefix': '2001:1::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            '2001:2::/64': [
                                {
                                    'ip_prefix': '2001:2::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            '2012:1::/64': [
                                {
                                    'ip_prefix': '2012:1::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            '2012:2::/64': [
                                {
                                    'ip_prefix': '2012:2::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ]
                            },
                        'srv6_locator': 'FCCC:CCC1:A1::/48',
                        'srv6_metric': '0',
                        'srv6_algorithm': '0',
                        'end_sid': 'FCCC:CCC1:A1::',
                        'end_behavior': 'uN '
                                        '(PSP/USD)'
                        },
                    'iolPE2.00-00': {
                        'lsp_sequence_num': '0x00000005',
                        'lsp_checksum': '0xD603',
                        'lsp_holdtime': '844',
                        'lsp_rcvd': '1199',
                        'attach_bit': 0,
                        'p_bit': 0,
                        'overload_bit': 0,
                        'area_address': '49.0000',
                        'nlpid': '0xCC 0x8E',
                        'router_cap': '0.0.0.0',
                        'd_flag': False,
                        's_flag': False,
                        'srv6_o_flag': False,
                        'hostname': 'iolPE2',
                        'extended_is_neighbor': {
                            'iolP3.00': [
                                {
                                    'neighbor_id': 'iolP3.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2023:1::1',
                                    'neighbor_ipv6_address': '2023:1::2',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:C3:E000::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    },
                                {
                                    'neighbor_id': 'iolP3.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2023:2::1',
                                    'neighbor_ipv6_address': '2023:2::2',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:C3:E003::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    }
                                ],
                                'iolP1.00': [
                                    {
                                        'neighbor_id': 'iolP1.00',
                                        'metric': 10,
                                        'interface_ipv6_address': '2021:2::2',
                                        'neighbor_ipv6_address': '2021:2::1',
                                        'admin_weight': 10,
                                        'end_x_sid': 'FCCC:CCC1:C3:E002::',
                                        'end_x_b_flag': 0,
                                        'end_x_s_flag': 0,
                                        'end_x_p_flag': 0,
                                        'end_x_algorithm': 0,
                                        'end_x_weight': 0
                                        },
                                    {
                                        'neighbor_id': 'iolP1.00',
                                        'metric': 10,
                                        'interface_ipv6_address': '2021:1::2',
                                        'neighbor_ipv6_address': '2021:1::1',
                                        'admin_weight': 10,
                                        'end_x_sid': 'FCCC:CCC1:C3:E001::',
                                        'end_x_b_flag': 0,
                                        'end_x_s_flag': 0,
                                        'end_x_p_flag': 0,
                                        'end_x_algorithm': 0,
                                        'end_x_weight': 0
                                            }
                                        ]
                                    },
                        'ipv6_address': 'C02:1::2',
                        'ipv6_router_id': 'C02:1::1',
                        'ipv6_reachability': {
                            'FCCC:CCC1:C3::/48': [
                                {
                                    'ip_prefix': 'FCCC:CCC1:C3::',
                                    'prefix_len': '48',
                                    'metric': 0,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            'C02:1::/64': [
                                {
                                    'ip_prefix': 'C02:1::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            '2023:1::/64': [
                                {
                                    'ip_prefix': '2023:1::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            '2023:2::/64': [
                                {
                                    'ip_prefix': '2023:2::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                    }
                                }
                            ],
                            '2021:1::/64': [
                                {
                                    'ip_prefix': '2021:1::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            '2021:2::/64': [
                                {
                                    'ip_prefix': '2021:2::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ]
                            },
                        'srv6_locator': 'FCCC:CCC1:C3::/48',
                        'srv6_metric': '0',
                        'srv6_algorithm': '0',
                        'end_sid': 'FCCC:CCC1:C3::',
                        'end_behavior': 'uN '
                                        '(PSP/USD)'
                            },
                    'iolP1.00-00': {
                        'lsp_sequence_num': '0x00000005',
                        'lsp_checksum': '0x7340',
                        'lsp_holdtime': '844',
                        'lsp_rcvd': '1200',
                        'attach_bit': 0,
                        'p_bit': 0,
                        'overload_bit': 0,
                        'area_address': '49.0000',
                        'nlpid': '0xCC 0x8E',
                        'router_cap': '0.0.0.0',
                        'd_flag': False,
                        's_flag': False,
                        'srv6_o_flag': False,
                        'hostname': 'iolP1',
                        'extended_is_neighbor': {
                            'iolP3.00': [
                                {
                                    'neighbor_id': 'iolP3.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2013:1::1',
                                    'neighbor_ipv6_address': '2013:1::2',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:AA11:E004::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    }
                                ],
                            'iolPE1.00': [
                                {
                                    'neighbor_id': 'iolPE1.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2001:1::2',
                                    'neighbor_ipv6_address': '2001:1::1',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:AA11:E000::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    },
                                {
                                    'neighbor_id': 'iolPE1.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2001:2::2',
                                    'neighbor_ipv6_address': '2001:2::1',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:AA11:E001::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    }
                                ],
                            'iolPE2.00': [
                                {
                                    'neighbor_id': 'iolPE2.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2021:2::1',
                                    'neighbor_ipv6_address': '2021:2::2',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:AA11:E003::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    },
                                {
                                    'neighbor_id': 'iolPE2.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2021:1::1',
                                    'neighbor_ipv6_address': '2021:1::2',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:AA11:E002::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    }
                                ]
                            },
                            'ipv6_address': 'C1:1::1',
                            'ipv6_router_id': 'C1:1::1',
                            'ipv6_reachability': {
                                'FCCC:CCC1:AA11::/48': [
                                    {
                                        'ip_prefix': 'FCCC:CCC1:AA11::',
                                        'prefix_len': '48',
                                        'metric': 0,
                                        'prefix_attr': {
                                            'x_flag': False,
                                            'r_flag': False,
                                            'n_flag': False
                                            }
                                        }
                                    ],
                                'C1:1::/64': [
                                    {
                                        'ip_prefix': 'C1:1::',
                                        'prefix_len': '64',
                                        'metric': 10,
                                        'prefix_attr': {
                                            'x_flag': False,
                                            'r_flag': False,
                                            'n_flag': False
                                            }
                                        }
                                    ],
                                '2001:1::/64': [
                                    {
                                        'ip_prefix': '2001:1::',
                                        'prefix_len': '64',
                                        'metric': 10,
                                        'prefix_attr': {
                                            'x_flag': False,
                                            'r_flag': False,
                                            'n_flag': False
                                            }
                                        }
                                    ],
                                '2001:2::/64': [
                                    {
                                        'ip_prefix': '2001:2::',
                                        'prefix_len': '64',
                                        'metric': 10,
                                        'prefix_attr': {
                                            'x_flag': False,
                                            'r_flag': False,
                                            'n_flag': False
                                            }
                                        }
                                    ],
                                '2021:1::/64': [
                                    {
                                        'ip_prefix': '2021:1::',
                                        'prefix_len': '64',
                                        'metric': 10,
                                        'prefix_attr': {
                                            'x_flag': False,
                                            'r_flag': False,
                                            'n_flag': False
                                            }
                                        }
                                    ],
                                '2021:2::/64': [
                                    {
                                        'ip_prefix': '2021:2::',
                                        'prefix_len': '64',
                                        'metric': 10,
                                        'prefix_attr': {
                                            'x_flag': False,
                                            'r_flag': False,
                                            'n_flag': False
                                            }
                                        }
                                    ],
                                '2013:1::/64': [
                                    {
                                        'ip_prefix': '2013:1::',
                                        'prefix_len': '64',
                                        'metric': 10,
                                        'prefix_attr': {
                                            'x_flag': False,
                                            'r_flag': False,
                                            'n_flag': False
                                            }
                                        }
                                    ]
                                },
                            'srv6_locator': 'FCCC:CCC1:AA11::/48',
                            'srv6_metric': '0',
                            'srv6_algorithm': '0',
                            'end_sid': 'FCCC:CCC1:AA11::',
                            'end_behavior': 'uN (PSP/USD)'
                            },
                    'iolP2.00-00': {
                        'lsp_sequence_num': '0x00000001',
                        'lsp_checksum': '0xE018',
                        'lsp_holdtime': '871',
                        'lsp_rcvd': '1200',
                        'attach_bit': 0,
                        'p_bit': 0,
                        'overload_bit': 0,
                        'area_address': '49.0000',
                        'nlpid': '0xCC 0x8E',
                        'router_cap': '0.0.0.0',
                        'd_flag': False,
                        's_flag': False,
                        'srv6_o_flag': False,
                        'hostname': 'iolP2',
                        'extended_is_neighbor': {
                            'iolP3.00': [
                                {
                                    'neighbor_id': 'iolP3.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2032:2::1',
                                    'neighbor_ipv6_address': '2032:2::2',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:AA22:E003::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    },
                                {
                                    'neighbor_id': 'iolP3.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2032:1::1',
                                    'neighbor_ipv6_address': '2032:1::2',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:AA22:E000::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    }
                                ],
                            'iolPE1.00': [
                                {
                                    'neighbor_id': 'iolPE1.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2012:2::2',
                                    'neighbor_ipv6_address': '2012:2::1',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:AA22:E002::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    },
                                    {
                                    'neighbor_id': 'iolPE1.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2012:1::2',
                                    'neighbor_ipv6_address': '2012:1::1',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:AA22:E001::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    }
                                ]
                            },
                        'ipv6_address': 'C2:1::1',
                        'ipv6_router_id': 'C2:1::1',
                        'ipv6_reachability': {
                            '2032:1::/64': [
                                {
                                    'ip_prefix': '2032:1::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            '2012:1::/64': [
                                {
                                    'ip_prefix': '2012:1::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            '2012:2::/64': [
                                {
                                    'ip_prefix': '2012:2::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            '2032:2::/64': [
                                {
                                    'ip_prefix': '2032:2::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            'FCCC:CCC1:AA22::/48': [
                                {
                                    'ip_prefix': 'FCCC:CCC1:AA22::',
                                    'prefix_len': '48',
                                    'metric': 0,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            'C2:1::/64': [
                                {
                                    'ip_prefix': 'C2:1::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ]
                            },
                        'srv6_locator': 'FCCC:CCC1:AA22::/48',
                        'srv6_metric': '0',
                        'srv6_algorithm': '0',
                        'end_sid': 'FCCC:CCC1:AA22::',
                        'end_behavior': 'uN (PSP/USD)'
                        },
                    'iolP3.00-00': {
                        'lsp_sequence_num': '0x00000005',
                        'lsp_checksum': '0xA884',
                        'lsp_holdtime': '871',
                        'lsp_rcvd': '1199',
                        'attach_bit': 0,
                        'p_bit': 0,
                        'overload_bit': 0,
                        'area_address': '49.0000',
                        'nlpid': '0xCC 0x8E',
                        'router_cap': '0.0.0.0',
                        'd_flag': False,
                        's_flag': False,
                        'srv6_o_flag': False,
                        'hostname': 'iolP3',
                        'extended_is_neighbor': {
                            'iolP1.00': [
                                {
                                    'neighbor_id': 'iolP1.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2013:1::2',
                                    'neighbor_ipv6_address': '2013:1::1',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:AA33:E003::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    }
                                    ],
                            'iolPE2.00': [
                                {
                                    'neighbor_id': 'iolPE2.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2023:1::2',
                                    'neighbor_ipv6_address': '2023:1::1',
                                    'admin_weight': 15,
                                    'end_x_sid': 'FCCC:CCC1:AA33:E001::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    },
                                {
                                    'neighbor_id': 'iolPE2.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2023:2::2',
                                    'neighbor_ipv6_address': '2023:2::1',
                                    'admin_weight': 15,
                                    'end_x_sid': 'FCCC:CCC1:AA33:E002::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    }
                                ],
                            'iolP2.00': [
                                {
                                    'neighbor_id': 'iolP2.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2032:2::2',
                                    'neighbor_ipv6_address': '2032:2::1',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:AA33:E004::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    },
                                {
                                    'neighbor_id': 'iolP2.00',
                                    'metric': 10,
                                    'interface_ipv6_address': '2032:1::2',
                                    'neighbor_ipv6_address': '2032:1::1',
                                    'admin_weight': 10,
                                    'end_x_sid': 'FCCC:CCC1:AA33:E000::',
                                    'end_x_b_flag': 0,
                                    'end_x_s_flag': 0,
                                    'end_x_p_flag': 0,
                                    'end_x_algorithm': 0,
                                    'end_x_weight': 0
                                    }
                                ]
                            },
                        'ipv6_address': 'C3:1::1',
                        'ipv6_router_id': 'C3:1::1',
                        'ipv6_reachability': {
                            'FCCC:CCC1:AA33::/48': [
                                {
                                    'ip_prefix': 'FCCC:CCC1:AA33::',
                                    'prefix_len': '48',
                                    'metric': 0,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            'C3:1::/64': [
                                {
                                    'ip_prefix': 'C3:1::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                            }
                                        }
                                    ],
                            '2032:1::/64': [
                                {
                                    'ip_prefix': '2032:1::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            '2023:1::/64': [
                                {
                                    'ip_prefix': '2023:1::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                            }
                                        }
                                    ],
                            '2023:2::/64': [
                                {
                                    'ip_prefix': '2023:2::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ],
                            '2013:1::/64': [
                                {
                                    'ip_prefix': '2013:1::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                            }
                                        }
                                    ],
                            '2032:2::/64': [
                                {
                                    'ip_prefix': '2032:2::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                    'prefix_attr': {
                                        'x_flag': False,
                                        'r_flag': False,
                                        'n_flag': False
                                        }
                                    }
                                ]
                            },
                        'srv6_locator': 'FCCC:CCC1:AA33::/48',
                        'srv6_metric': '0',
                        'srv6_algorithm': '0',
                        'end_sid': 'FCCC:CCC1:AA33::',
                        'end_behavior': 'uN '
                                        '(PSP/USD)'
                        }
                    }
                }
        }
    }
}
