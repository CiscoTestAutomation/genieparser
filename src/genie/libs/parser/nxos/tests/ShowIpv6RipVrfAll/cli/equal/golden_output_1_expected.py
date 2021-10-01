

expected_output = {
    'isolate_mode': False,
    'mmode': 'Initialized',
    'vrf': {
        'VRF1': {
            'address_family': {
                'ipv6': {
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
                            'multicast_group': 'ff02::9',
                            'port': 521,
                            'redistribute': {
                                'direct': {
                                    'route_policy': 'ALL6',
                                    },
                                'static': {
                                    'route_policy': 'static-to-rip',
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
                'ipv6': {
                    'instance': {
                        'rip-1': {
                            'default_metric': 1,
                            'distance': 120,
                            'interfaces': {
                                'Ethernet1/1.100': {
                                    },
                                'Ethernet1/2.100': {
                                    },
                                },
                            'maximum_paths': 16,
                            'multicast_group': 'ff02::9',
                            'port': 521,
                            'redistribute': {
                                'static': {
                                    'route_policy': 'metric3_v6',
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
        },
    }
