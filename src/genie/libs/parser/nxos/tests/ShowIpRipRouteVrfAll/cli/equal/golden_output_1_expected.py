

expected_output = {
    'vrf': {
        'VRF1': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        'rip-1': {
                            'routes': {
                                '10.1.2.0/24': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'interface': 'Ethernet1/1.200',
                                            'metric': 1,
                                            'next_hop': '10.1.2.1',
                                            'route_type': 'connected',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 0,
                                    },
                                '10.1.3.0/24': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'interface': 'Ethernet1/2.200',
                                            'metric': 1,
                                            'next_hop': '10.1.3.1',
                                            'route_type': 'connected',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 0,
                                    },
                                '10.2.3.0/24': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:52',
                                            'interface': 'Ethernet1/1.200',
                                            'metric': 2,
                                            'next_hop': '10.1.2.2',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '172.16.11.0/24': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'metric': 15,
                                            'next_hop': '0.0.0.0',
                                            'redistributed': True,
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '192.168.2.2/32': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:52',
                                            'interface': 'Ethernet1/1.200',
                                            'metric': 2,
                                            'next_hop': '10.1.2.2',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '192.168.3.3/32': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:52',
                                            'interface': 'Ethernet1/1.200',
                                            'metric': 3,
                                            'next_hop': '10.1.2.2',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
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
                            'routes': {
                                '10.1.2.0/24': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'interface': 'Ethernet1/1.100',
                                            'metric': 1,
                                            'next_hop': '10.1.2.1',
                                            'route_type': 'connected',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 0,
                                    },
                                '10.1.3.0/24': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'interface': 'Ethernet1/2.100',
                                            'metric': 1,
                                            'next_hop': '10.1.3.1',
                                            'route_type': 'connected',
                                            'tag': 0,
                                            },
                                        2: {
                                            'expire_time': '00:00:05',
                                            'interface': 'Ethernet1/1.100',
                                            'metric': 3,
                                            'next_hop': '10.1.2.2',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '10.2.3.0/24': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'expire_time': '00:00:05',
                                            'interface': 'Ethernet1/1.100',
                                            'metric': 2,
                                            'next_hop': '10.1.2.2',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '172.16.22.0/24': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'expire_time': '00:00:05',
                                            'interface': 'Ethernet1/1.100',
                                            'metric': 2,
                                            'next_hop': '10.1.2.2',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '172.16.33.0/24': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'expire_time': '00:00:05',
                                            'interface': 'Ethernet1/1.100',
                                            'metric': 3,
                                            'next_hop': '10.1.2.2',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '192.168.2.2/32': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'expire_time': '00:00:05',
                                            'interface': 'Ethernet1/1.100',
                                            'metric': 2,
                                            'next_hop': '10.1.2.2',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '192.168.3.3/32': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'expire_time': '00:00:05',
                                            'interface': 'Ethernet1/1.100',
                                            'metric': 3,
                                            'next_hop': '10.1.2.2',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
