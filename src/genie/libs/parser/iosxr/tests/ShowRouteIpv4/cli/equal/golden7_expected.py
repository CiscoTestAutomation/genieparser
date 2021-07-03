expected_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.13.110.0/24': {
                                'route': '10.13.110.0/24',
                                'active': True,
                                'metric': 2,
                                'route_preference': 110,
                                'source_protocol_codes': 'O',
                                'source_protocol': 'ospf',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.12.110.1',
                                            'updated': '5d23h',
                                            'outgoing_interface': 'GigabitEthernet0/0/0/0.110',
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
