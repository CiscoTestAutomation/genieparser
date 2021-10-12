

expected_output = {
    'isolate_mode': False,
    'mmode': 'Initialized',
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        'rip-1': {
                            'default_metric': 1,
                            'distance': 120,
                            'interfaces': {
                                'Ethernet1/1.120': {
                                    },
                                'Ethernet1/2.120': {
                                    },
                                'loopback0': {
                                    },
                                },
                            'maximum_paths': 16,
                            'multicast_group': '224.0.0.9',
                            'port': 520,
                            'process': 'up and running',
                            'timers': {
                                'collect_garbage': 120,
                                'expire_in': 180,
                                'update_interval': 30,
                                },
                            },
                        },
                    },
                },
            },
        },
    }
