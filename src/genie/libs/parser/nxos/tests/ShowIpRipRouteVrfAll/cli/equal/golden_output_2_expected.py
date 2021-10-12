

expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        'rip-1': {
                            'routes': {
                                '10.1.0.0/8': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:33',
                                            'interface': 'Ethernet1/2.120',
                                            'metric': 2,
                                            'next_hop': '10.13.120.1',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '10.12.110.0/24': {
                                    'best_route': False,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:33',
                                            'interface': 'Ethernet1/2.120',
                                            'metric': 2,
                                            'next_hop': '10.13.120.1',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '10.12.115.0/24': {
                                    'best_route': False,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:33',
                                            'interface': 'Ethernet1/2.120',
                                            'metric': 2,
                                            'next_hop': '10.13.120.1',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '10.12.120.0/24': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:33',
                                            'interface': 'Ethernet1/2.120',
                                            'metric': 2,
                                            'next_hop': '10.13.120.1',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '10.12.90.0/24': {
                                    'best_route': False,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:33',
                                            'interface': 'Ethernet1/2.120',
                                            'metric': 2,
                                            'next_hop': '10.13.120.1',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '10.13.110.0/24': {
                                    'best_route': False,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:33',
                                            'interface': 'Ethernet1/2.120',
                                            'metric': 2,
                                            'next_hop': '10.13.120.1',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '10.13.115.0/24': {
                                    'best_route': False,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:33',
                                            'interface': 'Ethernet1/2.120',
                                            'metric': 2,
                                            'next_hop': '10.13.120.1',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '10.13.120.0/24': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'interface': 'Ethernet1/2.120',
                                            'metric': 1,
                                            'next_hop': '10.13.120.3',
                                            'route_type': 'connected',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 0,
                                    },
                                '10.13.90.0/24': {
                                    'best_route': False,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:33',
                                            'interface': 'Ethernet1/2.120',
                                            'metric': 2,
                                            'next_hop': '10.13.120.1',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '10.23.120.0/24': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'interface': 'Ethernet1/1.120',
                                            'metric': 1,
                                            'next_hop': '10.23.120.3',
                                            'route_type': 'connected',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 0,
                                    },
                                '10.36.3.3/32': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'interface': 'loopback0',
                                            'metric': 1,
                                            'next_hop': '10.36.3.3',
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
