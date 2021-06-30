expected_output = {
        'bridge_group': {
            'foo_group': {
                'bridge_domain': {
                    'foo_bd': {
                        'state': 'up',
                        'id': 0,
                        'shg_id': 0,
                        'mode': 'VPWS',
                        'mtu': 1500,
                        'ac': {
                            'num_ac': 1,
                            'num_ac_up': 0,
                            'interfaces': {
                                'GigabitEthernet0/5/1/4': {
                                    'state': 'admin down',
                                    'type': 'Ethernet',
                                    'mtu': 1500,
                                    'xc_id': '1',
                                    'interworking': 'none',
                                    'statistics': {
                                        'packet_totals': {
                                            'receive': 0,
                                            'send': 0,
                                        },
                                        'byte_totals': {
                                            'receive': 0,
                                            'send': 0,
                                        },
                                    },
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 1,
                            'foo_vfi': {
                                'neighbor': {
                                    '10.4.1.1': {
                                        'pw_id': {
                                            '1': {
                                                'state': 'up ( established )',
                                                'pw_class': 'not set',
                                                'encapsulation': 'MPLS',
                                                'protocol': 'LDP',
                                                'pw_type': 'Ethernet',
                                                'control_word': 'enabled',
                                                'interworking': 'none',
                                                'sequencing': 'not set',
                                                'mpls': {
                                                    'label': {
                                                        'local': '16001',
                                                        'remote': '16001',
                                                    },
                                                    'group_id': {
                                                        'local': 'unassigned',
                                                        'remote': 'unknown',
                                                    },
                                                    'interface': {
                                                        'local': 'siva/vfi',
                                                        'remote': 'siva/vfi',
                                                    },
                                                    'mtu': {
                                                        'local': '1500',
                                                        'remote': '1500',
                                                    },
                                                    'control_word': {
                                                        'local': 'enabled',
                                                        'remote': 'enabled',
                                                    },
                                                    'pw_type': {
                                                        'local': 'Ethernet',
                                                        'remote': 'Ethernet',
                                                    },
                                                    'vccv_cv_type': {
                                                        'local': '0x2',
                                                        'remote': '0x2',
                                                        'local_type': ['LSP ping verification'],
                                                        'remote_type': ['LSP ping verification'],
                                                    },
                                                    'vccv_cc_type': {
                                                        'local': '0x3',
                                                        'remote': '0x3',
                                                        'local_type': ['control word', 'router alert label'],
                                                        'remote_type': ['control word', 'router alert label'],
                                                    },
                                                },
                                                'create_time': '25/06/2007 05:29:42 (2w0d ago)',
                                                'last_time_status_changed': '27/06/2007 06:50:35 (1w5d ago)',
                                            },
                                            '2': {
                                                'state': 'up ( established )',
                                                'pw_class': 'not set',
                                                'encapsulation': 'MPLS',
                                                'protocol': 'LDP',
                                                'pw_type': 'Ethernet',
                                                'control_word': 'enabled',
                                                'interworking': 'none',
                                                'sequencing': 'not set',
                                                'mpls': {
                                                    'label': {
                                                        'local': '16002',
                                                        'remote': '16002',
                                                    },
                                                    'group_id': {
                                                        'local': 'unassigned',
                                                        'remote': 'unknown',
                                                    },
                                                    'monitor_interface': {
                                                        'local': 'siva/vfi',
                                                        'remote': 'siva/vfi',
                                                    },
                                                    'mtu': {
                                                        'local': '1500',
                                                        'remote': '1500',
                                                    },
                                                    'control_word': {
                                                        'local': 'enabled',
                                                        'remote': 'enabled',
                                                    },
                                                    'pw_type': {
                                                        'local': 'Ethernet',
                                                        'remote': 'Ethernet',
                                                    },
                                                    'vccv_cv_type': {
                                                        'local': '0x2',
                                                        'remote': '0x2',
                                                        'local_type': ['LSP ping verification'],
                                                        'remote_type': ['LSP ping verification'],
                                                    },
                                                    'vccv_cc_type': {
                                                        'local': '0x3',
                                                        'remote': '0x3',
                                                        'local_type': ['control word', 'router alert label'],
                                                        'remote_type': ['control word', 'router alert label'],
                                                    },
                                                },
                                                'create_time': '25/06/2007 05:29:42 (2w0d ago)',
                                                'last_time_status_changed': '27/06/2007 06:50:35 (1w5d ago)',
                                            },
                                        },
                                    },
                                },
                                'statistics': {
                                    'drop': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'num_pw': 2,
                            'num_pw_up': 2,
                        },
                    },
                },
            },
        },
    }
