
expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'routes': {
                        '2001:1:1:1::1/128': {
                            'route': '2001:1:1:1::1/128',
                            'active': True,
                            'source_protocol_codes': 'S',
                            'source_protocol': 'static',
                            'route_preference': 1,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '2001:20:1:2::1',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/0',
                                        'updated': '01:52:23'
                                    },
                                    2: {
                                        'index': 2,
                                        'next_hop': '2001:10:1:2::1',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/3',
                                        'updated': '01:52:23'
                                    },
                                },
                            },
                        },
                        '2001:2:2:2::2/128': {
                            'route': '2001:2:2:2::2/128',
                            'active': True,
                            'source_protocol_codes': 'L',
                            'source_protocol': 'local',
                            'next_hop': {
                                'outgoing_interface': {
                                    'Loopback0': {
                                        'outgoing_interface': 'Loopback0',
                                        'updated': '01:52:24'
                                    },
                                },
                            },
                        },
                        '2001:3:3:3::3/128': {
                            'route': '2001:3:3:3::3/128',
                            'active': True,
                            'source_protocol_codes': 'S',
                            'source_protocol': 'static',
                            'route_preference': 1,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '2001:10:2:3::3',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'updated': '01:52:23'
                                    },
                                    2: {
                                        'index': 2,
                                        'next_hop': '2001:20:2:3::3',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/2',
                                        'updated': '01:52:23'
                                    },
                                },
                            },
                        },
                        '2001:21:21:21::21/128': {
                            'route': '2001:21:21:21::21/128',
                            'active': True,
                            'source_protocol_codes': 'i L1',
                            'source_protocol': 'isis',
                            'route_preference': 115,
                            'metric': 20,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::5054:ff:fe54:6569',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/0',
                                        'updated': '00:56:34'
                                    },
                                    2: {
                                        'index': 2,
                                        'next_hop': 'fe80::5054:ff:fea5:829',
                                        'nexthop_in_vrf': 'default',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/3',
                                        'updated': '00:56:34'
                                    },
                                },
                            },
                        },
                        '2001:32:32:32::32/128': {
                            'route': '2001:32:32:32::32/128',
                            'active': True,
                            'source_protocol_codes': 'L',
                            'source_protocol': 'local',
                            'next_hop': {
                                'outgoing_interface': {
                                    'Loopback3': {
                                        'outgoing_interface': 'Loopback3',
                                        'updated': '01:52:24'
                                    },
                                },
                            },
                        },
                        '2001:33:33:33::33/128': {
                            'route': '2001:33:33:33::33/128',
                            'active': True,
                            'route_preference': 200,
                            'metric': 0,
                            'source_protocol_codes': 'B',
                            'source_protocol': 'bgp',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '2001:13:13:13::13',
                                        'updated': '00:53:22'
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'last_resort': {
                'gateway': 'not set'
                },
            },
        },
    }
