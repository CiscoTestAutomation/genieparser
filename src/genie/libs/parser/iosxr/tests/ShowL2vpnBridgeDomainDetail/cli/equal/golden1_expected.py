expected_output = {
        'bridge_group': {
            'g1': {
                'bridge_domain': {
                    'bd1': {
                        'state': 'up',
                        'id': 0,
                        'shg_id': 0,
                        'mst_i': 0,
                        'mac_learning': 'enabled',
                        'mac_withdraw': 'disabled',
                        'flooding': {
                            'broadcast_multicast': 'enabled',
                            'unknown_unicast': 'enabled',
                        },
                        'mac_aging_time': 300,
                        'mac_aging_type': 'inactivity',
                        'mac_limit': 4000,
                        'mac_limit_action': 'none',
                        'mac_limit_notification': 'syslog',
                        'mac_limit_reached': 'yes',
                        'security': 'disabled',
                        'dhcp_v4_snooping': 'disabled',
                        'mtu': 1500,
                        'ac': {
                            'num_ac': 1,
                            'num_ac_up': 1,
                            'interfaces': {
                                'GigabitEthernet0/1/0/0': {
                                    'state': 'up',
                                    'type': 'Ethernet',
                                    'mtu': 1500,
                                    'xc_id': '0x2000001',
                                    'interworking': 'none',
                                    'mst_i': 0,
                                    'mst_i_state': 'unprotected',
                                    'mac_learning': 'enabled',
                                    'flooding': {
                                        'broadcast_multicast': 'enabled',
                                        'unknown_unicast': 'enabled',
                                    },
                                    'mac_aging_time': 300,
                                    'mac_aging_type': 'inactivity',
                                    'mac_limit': 4000,
                                    'mac_limit_action': 'none',
                                    'mac_limit_notification': 'syslog',
                                    'mac_limit_reached': 'yes',
                                    'security': 'disabled',
                                    'dhcp_v4_snooping': 'disabled',
                                    'static_mac_address': ['0000.0000.0000', '0001.00ff.0205'],
                                    'statistics': {
                                        'packet_totals': {
                                            'receive': 3919680,
                                            'send': 9328,
                                        },
                                        'byte_totals': {
                                            'receive': 305735040,
                                            'send': 15022146,
                                        },
                                    },
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 1,
                            '1': {
                                'neighbor': {
                                    '10.4.1.1': {
                                        'pw_id': {
                                            '1': {
                                                'state': 'up ( established )',
                                                'pw_class': 'mpls',
                                                'xc_id': '0xff000001',
                                                'encapsulation': 'MPLS',
                                                'protocol': 'LDP',
                                                'pw_type': 'Ethernet',
                                                'control_word': 'disabled',
                                                'interworking': 'none',
                                                'pw_backup_disable_delay': 0,
                                                'sequencing': 'not set',
                                                'mpls': {
                                                    'label': {
                                                        'local': '16003',
                                                        'remote': '16003',
                                                    },
                                                    'group_id': {
                                                        'local': '0x0',
                                                        'remote': '0x0',
                                                    },
                                                    'interface': {
                                                        'local': '1',
                                                        'remote': '1',
                                                    },
                                                    'mtu': {
                                                        'local': '1500',
                                                        'remote': '1500',
                                                    },
                                                    'control_word': {
                                                        'local': 'disabled',
                                                        'remote': 'disabled',
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
                                                        'local': '0x2',
                                                        'remote': '0x2',
                                                        'local_type': ['router alert label'],
                                                        'remote_type': ['router alert label'],
                                                    },
                                                },
                                                'create_time': '12/03/2008 14:03:00 (17:17:30 ago)',
                                                'last_time_status_changed': '13/03/2008 05:57:58 (01:22:31 ago)',
                                                'mac_withdraw_message': {
                                                    'send': 0,
                                                    'receive': 0,
                                                },
                                                'statistics': {
                                                    'packet_totals': {
                                                        'receive': 3918814,
                                                        'send': 3918024,
                                                    },
                                                    'byte_totals': {
                                                        'receive': 305667492,
                                                        'send': 321277968,
                                                    },
                                                },
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
                            'num_pw': 1,
                            'num_pw_up': 1,
                        },
                    },
                },
            },
        },
    }
