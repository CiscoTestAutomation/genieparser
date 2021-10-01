

expected_output = {
'vrf': {
    'default': {
        'address_family': {
            'ipv4': {
                'routes': {
                    '10.106.0.0/8': {
                        'active': True,
                        'mbest': 0,
                        'metric': 0,
                        'next_hop': {
                            'next_hop_list': {
                                1: {
                                    'best_ucast_nexthop': True,
                                    'index': 1,
                                    'metric': 0,
                                    'next_hop': 'vrf default',
                                    'outgoing_interface': 'Null0',
                                    'route_preference': 20,
                                    'source_protocol': 'bgp',
                                    'source_protocol_status': 'external',
                                    'updated': '18:11:28',
                                },
                            },
                        },
                        'process_id': '333',
                        'route': '10.106.0.0/8',
                        'route_preference': 20,
                        'source_protocol': 'bgp',
                        'source_protocol_status': 'external',
                        'tag': 333,
                        'ubest': 1,
                    },
                    '10.106.0.5/8': {
                        'active': True,
                        'mbest': 0,
                        'metric': 0,
                        'next_hop': {
                            'next_hop_list': {
                                1: {
                                    'best_ucast_nexthop': True,
                                    'index': 1,
                                    'metric': 0,
                                    'next_hop': 'Null0',
                                    'route_preference': 1,
                                    'source_protocol': 'static',
                                    'updated': '18:47:42',
                                },
                            },
                        },
                        'route': '10.106.0.5/8',
                        'route_preference': 1,
                        'source_protocol': 'static',
                        'ubest': 1,
                    },
                    '10.16.1.0/24': {
                        'active': True,
                        'mbest': 0,
                        'metric': 4444,
                        'next_hop': {
                            'next_hop_list': {
                                1: {
                                    'best_ucast_nexthop': True,
                                    'index': 1,
                                    'metric': 4444,
                                    'next_hop': '2001:db8:8b05::1002',
                                    'next_hop_vrf': 'default',
                                    'outgoing_interface': 'Ethernet1/1',
                                    'route_preference': 200,
                                    'source_protocol': 'bgp',
                                    'source_protocol_status': 'internal',
                                    'updated': '15:57:39',
                                },
                            },
                        },
                        'process_id': '333',
                        'route': '10.16.1.0/24',
                        'route_preference': 200,
                        'source_protocol': 'bgp',
                        'source_protocol_status': 'internal',
                        'tag': 333,
                        'ubest': 1,
                    },
                },
            },
        },
    },
},
}
