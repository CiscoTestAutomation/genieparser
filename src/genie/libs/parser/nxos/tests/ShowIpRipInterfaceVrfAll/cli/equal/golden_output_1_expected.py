

expected_output = {
    'vrf': {
        'VRF1': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        'rip-1': {
                            'interfaces': {
                                'Ethernet1/1.200': {
                                    'ipv4': {
                                        '10.1.2.1/24': {
                                            'ip': '10.1.2.1',
                                            'prefix_length': 24,
                                            },
                                        },
                                    'metric': 1,
                                    'oper_status': 'up',
                                    'split_horizon': True,
                                    'states': {
                                        'admin_state': 'up',
                                        'link_state': 'up',
                                        'protocol_state': 'up',
                                        },
                                    },
                                'Ethernet1/2.200': {
                                    'authentication': {
                                        'auth_key': {
                                            'crypto_algorithm': 'md5',
                                            },
                                        'auth_key_chain': {
                                            'key_chain': 'none',
                                            },
                                        },
                                    'ipv4': {
                                        '10.1.3.1/24': {
                                            'ip': '10.1.3.1',
                                            'prefix_length': 24,
                                            },
                                        },
                                    'metric': 1,
                                    'oper_status': 'up',
                                    'split_horizon': True,
                                    'states': {
                                        'admin_state': 'up',
                                        'link_state': 'up',
                                        'protocol_state': 'up',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        'rip-1': {
                            'interfaces': {
                                'Ethernet1/1.100': {
                                    'ipv4': {
                                        '10.1.2.1/24': {
                                            'ip': '10.1.2.1',
                                            'prefix_length': 24,
                                            },
                                        },
                                    'metric': 1,
                                    'oper_status': 'up',
                                    'passive': True,
                                    'split_horizon': True,
                                    'states': {
                                        'admin_state': 'up',
                                        'link_state': 'up',
                                        'protocol_state': 'up',
                                        },
                                    },
                                'Ethernet1/2.100': {
                                    'authentication': {
                                        'auth_key': {
                                            'crypto_algorithm': 'none',
                                            },
                                        'auth_key_chain': {
                                            'key_chain': '1',
                                            },
                                        },
                                    'ipv4': {
                                        '10.1.3.1/24': {
                                            'ip': '10.1.3.1',
                                            'prefix_length': 24,
                                            },
                                        },
                                    'metric': 1,
                                    'oper_status': 'up',
                                    'split_horizon': True,
                                    'states': {
                                        'admin_state': 'up',
                                        'link_state': 'up',
                                        'protocol_state': 'up',
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
