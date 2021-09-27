

expected_output = {
    'group': {
        'tjub_xc': {
            'xc': {
                'siva_p2p': {
                    'state': 'down',
                    'interworking': 'none',
                    'monitor_session': {
                        'pw-span-test': {
                            'state': 'configured',
                        },
                    },
                    'ac': {
                        'GigabitEthernet1/5/1/2': {
                            'state': 'up',
                            'type': 'Ethernet',
                            'mtu': 2611,
                            'xc_id': '0x6111112',
                            'interworking': 'none',
                            'msti': 0,
                            'statistics': {
                                'packet_totals': {
                                    'send': 100,
                                },
                                'byte_totals': {
                                    'send': 20798,
                                },
                            },
                        },
                    },
                    'pw': {
                        'neighbor': {
                            '10.19.2.2': {
                                'id': {
                                    2: {
                                        'state': 'down ( local ready )',
                                        'pw_class': 'not set',
                                        'xc_id': '0x6111112',
                                        'encapsulation': 'MPLS',
                                        'protocol': 'LDP',
                                        'type': 'Ethernet',
                                        'control_word': 'enabled',
                                        'interworking': 'none',
                                        'backup_disable_delay': 0,
                                        'sequencing': 'not set',
                                        'mpls': {
                                            'label': {
                                                'local': '41116',
                                                'remote': 'unknown',
                                            },
                                            'group_id': {
                                                'local': '0x6111411',
                                                'remote': '1x1',
                                            },
                                            'interface': {
                                                'local': 'GigabitEthernet1/5/1/2',
                                                'remote': 'unknown',
                                            },
                                            'monitor_interface': {
                                                'local': 'pw-span-test',
                                                'remote': 'GigabitEthernet1/4/1/2',
                                            },
                                            'mtu': {
                                                'local': '2611',
                                                'remote': 'unknown',
                                            },
                                            'control_word': {
                                                'local': 'enabled',
                                                'remote': 'unknown',
                                            },
                                            'pw_type': {
                                                'local': 'Ethernet',
                                                'remote': 'unknown',
                                            },
                                            'vccv_cv_type': {
                                                'local': '1x3',
                                                'remote': '1x1',
                                                'local_type': ['LSP ping verification'],
                                                'remote_type': ['none'],
                                            },
                                            'vccv_cc_type': {
                                                'local': '1x4',
                                                'remote': '1x1',
                                                'local_type': ['control word', 'router alert label'],
                                                'remote_type': ['none'],
                                            },
                                        },
                                        'create_time': '21/11/2008 11:35:17 (11:64:42 ago)',
                                        'last_time_status_changed': '21/01/2008 21:37:15 (01:10:34 ago)',
                                        'statistics': {
                                            'packet_totals': {
                                                'receive': 0,
                                            },
                                            'byte_totals': {
                                                'receive': 0,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'backup_pw': {
                        'neighbor': {
                            '10.66.3.3': {
                                'id': {
                                    3: {
                                        'state': 'up ( established )',
                                        'pw_class': 'not set',
                                        'xc_id': '1x1',
                                        'encapsulation': 'MPLS',
                                        'protocol': 'LDP',
                                        'type': 'Ethernet',
                                        'control_word': 'enabled',
                                        'interworking': 'none',
                                        'backup_disable_delay': 0,
                                        'sequencing': 'not set',
                                        'mpls': {
                                            'label': {
                                                'local': '41117',
                                                'remote': '27114',
                                            },
                                            'group_id': {
                                                'local': 'unassigned',
                                                'remote': '1x6111511',
                                            },
                                            'interface': {
                                                'local': 'unknown',
                                                'remote': 'GigabitEthernet1/5/1/3',
                                            },
                                            'mtu': {
                                                'local': '2611',
                                                'remote': '2611',
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
                                                'local': '1x3',
                                                'remote': '1x3',
                                                'local_type': ['LSP ping verification'],
                                                'remote_type': ['LSP ping verification'],
                                            },
                                            'vccv_cc_type': {
                                                'local': '1x4',
                                                'remote': '1x4',
                                                'local_type': ['control word', 'router alert label'],
                                                'remote_type': ['control word', 'router alert label'],
                                            },
                                        },
                                        'create_time': '21/11/2008 11:45:44 (00:32:54 ago)',
                                        'last_time_status_changed': '20/11/2008 21:45:48 (00:44:49 ago)',
                                        'statistics': {
                                            'packet_totals': {
                                                'receive': 0,
                                            },
                                            'byte_totals': {
                                                'receive': 0,
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
