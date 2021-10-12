

expected_output = {
'vrf': {
    'default': {
        'address_family': {
            'ipv4': {
                'routes': {
                    '10.111.1.1/32': {
                        'active': True,
                        'mbest': 0,
                        'metric': 0,
                        'next_hop': {
                            'next_hop_list': {
                                1: {
                                    'index': 1,
                                    'metric': 0,
                                    'next_hop': '10.1.10.2',
                                    'route_preference': 4,
                                    'source_protocol': 'static',
                                    'updated': '13:35:01',
                                },
                                2: {
                                    'best_ucast_nexthop': True,
                                    'index': 2,
                                    'metric': 0,
                                    'next_hop': '10.144.10.2',
                                    'route_preference': 1,
                                    'source_protocol': 'static',
                                    'updated': '13:35:01',
                                },
                            },
                        },
                        'route': '10.111.1.1/32',
                        'route_preference': 1,
                        'source_protocol': 'static',
                        'ubest': 1,
                    },
                },
            },
        },
    },
},
}
