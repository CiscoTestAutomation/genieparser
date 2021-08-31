
expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'safi': 'unicast',
                    'table_id': '0xe0000000',
                    'routes': {
                        '10.4.1.1/32': {
                            'route': '10.4.1.1/32',
                            'next_hop': {
                                'outgoing_interface': {
                                    'GigabitEthernet0/0/0/3': {
                                        'outgoing_interface': 'GigabitEthernet0/0/0/3',
                                        'metrics': 1,
                                        'preference': 1,
                                        'active': True,
                                        'path_event': 'Path is installed into RIB at Dec  7 21:52:00.853',
                                        'path_version': 1,
                                        'path_status': '0x21',
                                        'tag': 0,
                                    },
                                    'GigabitEthernet0/0/0/0': {
                                        'outgoing_interface': 'GigabitEthernet0/0/0/0',
                                        'metrics': 1,
                                        'preference': 1,
                                        'active': True,
                                        'path_event': 'Path is installed into RIB at Dec  7 21:52:00.733',
                                        'path_version': 1,
                                        'path_status': '0x21',
                                        'tag': 0,
                                    },
                                },
                            },
                        },
                        '10.36.3.3/32': {
                            'route': '10.36.3.3/32',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '10.229.3.3',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/2',
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
                                        'next_hop': '10.229.3.3',
                                        'metrics': 1,
                                        'preference': 3,
                                        'active': False,
                                        'path_event': 'Path is configured at Dec  7 21:47:43.624',
                                        'path_version': 0,
                                        'path_status': '0x0',
                                    },
                                    3: {
                                        'index': 3,
                                        'next_hop': '10.2.3.3',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'metrics': 1,
                                        'preference': 17,
                                        'track': 1,
                                        'active': False,
                                        'path_event': 'Path is configured at Dec  7 21:47:43.624',
                                        'path_version': 0,
                                        'path_status': '0x80',
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

