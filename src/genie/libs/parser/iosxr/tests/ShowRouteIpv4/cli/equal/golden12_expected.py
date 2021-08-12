expected_output = {
        'vrf': {
            'L:192': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.2.2.2/32': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Null0': {
                                            'outgoing_interface': 'Null0',
                                            'updated': '00:06:36',
                                        },
                                    },
                                },
                                'route': '10.2.2.2/32',
                                'source_protocol': 'static',
                                'source_protocol_codes': 'S',
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
