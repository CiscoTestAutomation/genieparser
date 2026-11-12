expected_output = {
    'vrf': {
        'venise': {
            'last_resort': {
                'gateway': 'not set',
            },
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.76.130.0/24': {
                            'route': '10.76.130.0/24',
                            'active': True,
                            'route_preference': 200,
                            'metric': 0,
                            'source_protocol': 'bgp',
                            'source_protocol_codes': 'B',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '172.28.224.129',
                                        'updated': '17w3d',
                                    },
                                },
                            },
                        },
                        '10.168.1.0/26': {
                            'route': '10.168.1.0/26',
                            'active': True,
                            'route_preference': 20,
                            'metric': 0,
                            'source_protocol': 'bgp',
                            'source_protocol_codes': 'B',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '10.168.2.186',
                                        'updated': '1w1d',
                                    },
                                },
                            },
                        },
                        '10.168.4.0/24': {
                            'route': '10.168.4.0/24',
                            'active': True,
                            'route_preference': 200,
                            'metric': 0,
                            'source_protocol': 'bgp',
                            'source_protocol_codes': 'B',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '172.28.224.129',
                                        'updated': '2d01h',
                                    },
                                    2: {
                                        'index': 2,
                                        'next_hop': '172.28.224.130',
                                        'updated': '2d01h',
                                    },
                                },
                            },
                        },
                        '10.168.5.0/24': {
                            'route': '10.168.5.0/24',
                            'active': True,
                            'route_preference': 200,
                            'metric': 0,
                            'source_protocol': 'bgp',
                            'source_protocol_codes': 'B',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '172.28.224.131',
                                        'updated': '05:12:40',
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
