

expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        'rip-1': {
                            'interfaces': {
                                'Ethernet1/1.120': {
                                    'ipv4': {
                                        '10.23.120.3/24': {
                                            'ip': '10.23.120.3',
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
                                'Ethernet1/2.120': {
                                    'ipv4': {
                                        '10.13.120.3/24': {
                                            'ip': '10.13.120.3',
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
                                'loopback0': {
                                    'ipv4': {
                                        '10.36.3.3/32': {
                                            'ip': '10.36.3.3',
                                            'prefix_length': 32,
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
