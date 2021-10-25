
expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'safi': 'unicast',
                    'table_id': '0xe0800000',
                    'routes': {
                        '2001:1:1:a::1/128': {
                            'route': '2001:1:1:a::1/128',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '2001:10:1:2::1',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/3',
                                        'metrics': 1,
                                        'preference': 1,
                                        'active': True,
                                        'path_event': 'Path is installed into RIB at Dec  7 21:52:00.843',
                                        'path_version': 1,
                                        'path_status': '0xa1',
                                        'tag': 0,
                                    },
                                    2: {
                                        'index': 2,
                                        'next_hop': '2001:20:1:2::1',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/0',
                                        'metrics': 1,
                                        'preference': 1,
                                        'active': True,
                                        'path_event': 'Path is installed into RIB at Dec  7 21:52:00.733',
                                        'path_version': 1,
                                        'path_status': '0xa1',
                                        'tag': 0,
                                    },
                                },
                            },
                        },
                        '2001:3:3:3::3/128': {
                            'route': '2001:3:3:3::3/128',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '2001:20:2:3::3',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/2',
                                        'metrics': 1,
                                        'preference': 1,
                                        'active': True,
                                        'path_event': 'Path is installed into RIB at Dec  7 21:52:00.763',
                                        'path_version': 1,
                                        'path_status': '0xa1',
                                        'tag': 0,
                                    },
                                    2: {
                                        'index': 2,
                                        'next_hop': '2001:10:2:3::3',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'metrics': 1,
                                        'preference': 1,
                                        'active': True,
                                        'path_event': 'Path is installed into RIB at Dec  7 21:52:00.753',
                                        'path_version': 1,
                                        'path_status': '0xa1',
                                        'tag': 0,
                                    },
                                    3: {
                                        'index': 3,
                                        'next_hop': '2001:20:2:3::3',
                                        'metrics': 1,
                                        'preference': 3,
                                        'active': False,
                                        'path_event': 'Path is configured at Dec  7 21:47:43.624',
                                        'path_version': 0,
                                        'path_status': '0x0',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        'VRF1': {
            'address_family': {
                'ipv6': {
                    'safi': 'unicast',
                    'table_id': '0xe0800010',
                    'routes': {
                        '2001:1:1:a::1/128': {
                            'route': '2001:1:1:a::1/128',
                            'next_hop': {
                                'outgoing_interface': {
                                    'Null0': {
                                        'outgoing_interface': 'Null0',
                                        'metrics': 1234,
                                        'preference': 99,
                                        'active': True,
                                        'path_event': 'Path is installed into RIB at Dec  7 21:51:47.424',
                                        'path_version': 1,
                                        'path_status': '0x21',
                                        'tag': 0,
                                    },
                                },
                            },
                        },
                        '2001:2:2:2::2/128': {
                            'route': '2001:2:2:2::2/128',
                            'next_hop': {
                                'outgoing_interface': {
                                    'Null0': {
                                        'outgoing_interface': 'Null0',
                                        'metrics': 3456,
                                        'preference': 101,
                                        'active': True,
                                        'path_event': 'Path is installed into RIB at Dec  7 21:51:47.424',
                                        'path_version': 1,
                                        'path_status': '0x21',
                                        'tag': 0,
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
