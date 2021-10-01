

expected_output = {
    'isolate_mode': False,
    'mmode': 'Initialized',
    'vrf': {
        'VRF1': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        'rip-1': {
                            'default_metric': 1,
                            'distance': 120,
                            'interfaces': {
                                'Ethernet1/1.200': {
                                    },
                                'Ethernet1/2.200': {
                                    },
                                },
                            'maximum_paths': 16,
                            'multicast_group': '224.0.0.9',
                            'port': 520,
                            'redistribute': {
                                'direct': {
                                    'route_policy': 'ALL',
                                    },
                                'static': {
                                    'route_policy': 'metric15',
                                    },
                                },
                            'process': 'up and running',
                            'timers': {
                                'expire_in': 180,
                                'collect_garbage': 120,
                                'update_interval': 30,
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
                            'default_metric': 3,
                            'distance': 120,
                            'interfaces': {
                                'Ethernet1/1.100': {
                                    },
                                'Ethernet1/2.100': {
                                    },
                                },
                            'maximum_paths': 16,
                            'multicast_group': '224.0.0.9',
                            'port': 520,
                            'redistribute': {
                                'direct': {
                                    'route_policy': 'ALL',
                                    },
                                'static': {
                                    'route_policy': 'ALL',
                                    },
                                },
                            'process': 'up and running',
                            'timers': {
                                'expire_in': 21,
                                'collect_garbage': 23,
                                'update_interval': 10,
                                },
                            },
                        },
                    },
                },
            },
        },
    }
