

expected_output = {
    'vrf': {
        'VRF1': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        'rip-1': {
                            'routes': {
                                '2001:db8:1113:1113::/64': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'metric': 1,
                                            'next_hop': '0::',
                                            'redistributed': True,
                                            'tag': 5,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '2001:db8:1:2::/64': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'interface': 'Ethernet1/1.200',
                                            'metric': 1,
                                            'next_hop': '2001:db8:1:2::1',
                                            'route_type': 'connected',
                                            'tag': 0,
                                            },
                                        2: {
                                            'metric': 1,
                                            'next_hop': '0::',
                                            'redistributed': True,
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '2001:db8:1:3::/64': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'interface': 'Ethernet1/2.200',
                                            'metric': 1,
                                            'next_hop': '2001:db8:1:3::1',
                                            'route_type': 'connected',
                                            'tag': 0,
                                            },
                                        2: {
                                            'metric': 1,
                                            'next_hop': '0::',
                                            'redistributed': True,
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '2001:db8:2:3::/64': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:46',
                                            'interface': 'Ethernet1/1.200',
                                            'metric': 2,
                                            'next_hop': 'fe80::5c00:ff:fe01:7',
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
                                '2001:db8:1111:1111::/64': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'metric': 3,
                                            'next_hop': '0::',
                                            'redistributed': True,
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '2001:db8:1112:1112::/64': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'metric': 3,
                                            'next_hop': '0::',
                                            'redistributed': True,
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '2001:db8:1113:1113::/64': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'metric': 3,
                                            'next_hop': '0::',
                                            'redistributed': True,
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '2001:db8:1:2::/64': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'interface': 'Ethernet1/1.100',
                                            'metric': 1,
                                            'next_hop': '2001:db8:1:2::1',
                                            'route_type': 'connected',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 0,
                                    },
                                '2001:db8:1:3::/64': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'interface': 'Ethernet1/2.100',
                                            'metric': 1,
                                            'next_hop': '2001:db8:1:3::1',
                                            'route_type': 'connected',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 0,
                                    },
                                '2001:db8:2222:2222::/64': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:36',
                                            'interface': 'Ethernet1/2.100',
                                            'metric': 7,
                                            'next_hop': 'fe80::5c00:ff:fe02:7',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '2001:db8:2223:2223::/64': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:39',
                                            'interface': 'Ethernet1/1.100',
                                            'metric': 6,
                                            'next_hop': 'fe80::5c00:ff:fe01:7',
                                            'tag': 0,
                                            },
                                        },
                                    'next_hops': 1,
                                    },
                                '2001:db8:2:3::/64': {
                                    'best_route': True,
                                    'index': {
                                        1: {
                                            'expire_time': '00:02:36',
                                            'interface': 'Ethernet1/2.100',
                                            'metric': 2,
                                            'next_hop': 'fe80::5c00:ff:fe02:7',
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
