

expected_output = {
    'group': {
        'qf2-to-tqjof2': {
            'xc': {
                'genie_bo3_vqt53_422': {
                    'state': 'up',
                    'interworking': 'none',
                    'ac': {
                        'TenGigE1/1/1/4/2.311': {
                            'state': 'up',
                            'type': 'VLAN',
                            'num_ranges': 1,
                            'vlan_ranges': ['311', '311'],
                            'rewrite_tags': '',
                            'mtu': 2611,
                            'xc_id': '1x3',
                            'interworking': 'none',
                            'statistics': {
                                'packet_totals': {
                                    'receive': 4,
                                    'send': 0,
                                },
                                'byte_totals': {
                                    'receive': 291,
                                    'send': 0,
                                },
                                'drops': {
                                    'illegal_vlan': 0,
                                    'illegal_length': 0,
                                },
                            },
                        },
                    },
                    'evpn': {
                        'neighbor': {
                            '78.81.320.94': {
                                'id': {
                                    'evi 21311': {
                                        'state': 'up ( established )',
                                        'ac_id': 41311,
                                        'xc_id': '1xd1111112',
                                        'encapsulation': 'MPLS',
                                        'source_address': '78.81.320.99',
                                        'encap_type': 'Ethernet',
                                        'control_word': 'enabled',
                                        'sequencing': 'not set',
                                        'lsp': 'Up',
                                        'evpn': {
                                            'label': {
                                                'local': '211124',
                                                'remote': '211121',
                                            },
                                            'mtu': {
                                                'local': '2611',
                                                'remote': 'unknown',
                                            },
                                            'control_word': {
                                                'local': 'enabled',
                                                'remote': 'enabled',
                                            },
                                            'ac_id': {
                                                'local': '31311',
                                                'remote': '41311',
                                            },
                                            'evpn_type': {
                                                'local': 'Ethernet',
                                                'remote': 'Ethernet',
                                            },
                                        },
                                        'create_time': '25/10/2019 14:17:28 (2x1e ago)',
                                        'last_time_status_changed': '25/10/2019 15:13:33 (2x1e ago)',
                                        'statistics': {
                                            'packet_totals': {
                                                'receive': 0,
                                                'send': 4,
                                            },
                                            'byte_totals': {
                                                'receive': 0,
                                                'send': 291,
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
        'qfw-to-tqjof2': {
            'xc': {
                'xstu_bo3_vqt2_211': {
                    'state': 'up',
                    'interworking': 'none',
                    'ac': {
                        'TenGigE1/1/1/4/2.211': {
                            'state': 'up',
                            'type': 'VLAN',
                            'num_ranges': 1,
                            'vlan_ranges': ['211', '211'],
                            'rewrite_tags': '',
                            'mtu': 2611,
                            'xc_id': '1x2',
                            'interworking': 'none',
                            'statistics': {
                                'packet_totals': {
                                    'receive': 4,
                                    'send': 0,
                                },
                                'byte_totals': {
                                    'receive': 291,
                                    'send': 0,
                                },
                                'drops': {
                                    'illegal_vlan': 0,
                                    'illegal_length': 0,
                                },
                            },
                        },
                    },
                    'evpn': {
                        'neighbor': {
                            '78.81.321.93': {
                                'id': {
                                    'evi 21211': {
                                        'state': 'up ( established )',
                                        'ac_id': 41211,
                                        'xc_id': '1xd111113',
                                        'encapsulation': 'MPLS',
                                        'source_address': '78.81.321.99',
                                        'encap_type': 'Ethernet',
                                        'control_word': 'enabled',
                                        'sequencing': 'not set',
                                        'lsp': 'Up',
                                        'evpn': {
                                            'label': {
                                                'local': '211123',
                                                'remote': '211111',
                                            },
                                            'mtu': {
                                                'local': '2611',
                                                'remote': 'unknown',
                                            },
                                            'control_word': {
                                                'local': 'enabled',
                                                'remote': 'enabled',
                                            },
                                            'ac_id': {
                                                'local': '31211',
                                                'remote': '31211',
                                            },
                                            'evpn_type': {
                                                'local': 'Ethernet',
                                                'remote': 'Ethernet',
                                            },
                                        },
                                        'create_time': '25/10/2019 15:10:17 (2x1e ago)',
                                        'last_time_status_changed': '25/10/2019 15:15:33 (2x1e ago)',
                                        'statistics': {
                                            'packet_totals': {
                                                'receive': 0,
                                                'send': 4,
                                            },
                                            'byte_totals': {
                                                'receive': 0,
                                                'send': 291,
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
