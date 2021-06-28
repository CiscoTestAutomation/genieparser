expected_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '172.16.55.0/22': {
                                'active': True,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.154.219.128',
                                            'updated': '1w3d',
                                        },
                                    },
                                },
                                'route': '172.16.55.0/22',
                                'route_preference': 200,
                                'source_protocol': 'bgp',
                                'source_protocol_codes': 'B',
                            },
                            '172.16.21.0/22': {
                                'active': True,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.154.219.128',
                                            'updated': '1w3d',
                                        },
                                    },
                                },
                                'route': '172.16.21.0/22',
                                'route_preference': 200,
                                'source_protocol': 'bgp',
                                'source_protocol_codes': 'B',
                            },
                            '172.16.16.0/24': {
                                'active': True,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.154.219.128',
                                            'updated': '1w3d',
                                        },
                                    },
                                },
                                'route': '172.16.16.0/24',
                                'route_preference': 200,
                                'source_protocol': 'bgp',
                                'source_protocol_codes': 'B',
                            },
                        },
                    },
                },
            },
        },
    }
