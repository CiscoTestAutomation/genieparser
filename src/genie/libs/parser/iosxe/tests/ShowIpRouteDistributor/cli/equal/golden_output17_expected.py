expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '0.0.0.0/0': {
                            'route': '0.0.0.0/0',
                            'active': True,
                            'route_preference': 1,
                            'metric': 0,
                            'source_protocol': 'static',
                            'source_protocol_codes': 'S*',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '5.40.0.1',
                                    },
                                },
                            },
                        },
                        '172.16.0.0/16': {
                            'route': '172.16.0.0/16',
                            'active': False,
                            'possibly_down': True,
                            'source_protocol': 'rip',
                            'source_protocol_codes': 'R',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '10.1.1.2',
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
