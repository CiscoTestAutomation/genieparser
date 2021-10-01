

expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        'rip-1': {
                            'routes': {
                                '2001:10:12:120::/64': {
                                    'best_route': False,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:58',
                                            'interface': 'Ethernet1/2.120',
                                            'metric': 2,
                                            'next_hop': 'fe80::f816:3eff:fe8f:fbd9',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '2001:10:13:120::/64': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'interface': 'Ethernet1/2.120',
                                            'metric': 1,
                                            'next_hop': '2001:10:13:120::3',
                                            'route_type': 'connected',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 0,
                                    },
                                '2001:10:23:120::/64': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'interface': 'Ethernet1/1.120',
                                            'metric': 1,
                                            'next_hop': '2001:10:23:120::3',
                                            'route_type': 'connected',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 0,
                                    },
                                '2001:1:1:1::1/128': {
                                    'best_route': False,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:58',
                                            'interface': 'Ethernet1/2.120',
                                            'metric': 2,
                                            'next_hop': 'fe80::f816:3eff:fe8f:fbd9',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '2001:3:3:3::3/128': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'interface': 'loopback0',
                                            'metric': 1,
                                            'next_hop': '2001:3:3:3::3',
                                            'route_type': 'connected',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 0,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
