expected_output = {
    'vrf': {
        'default': {
            'last_resort': {
                'gateway': 'not set',
            },
            'address_family': {
                'ipv6': {
                    'routes': {
                        '2001:db8:10::/64': {
                            'source_protocol': 'bgp',
                            'source_protocol_codes': 'B',
                            'route': '2001:db8:10::/64',
                            'active': True,
                            'route_preference': 200,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '::ffff:172.28.224.129',
                                        'updated': '2d01h',
                                        'nexthop_in_vrf': 'ENS-PROD',
                                    },
                                    2: {
                                        'index': 2,
                                        'next_hop': '::ffff:172.28.224.130',
                                        'updated': '2d01h',
                                        'nexthop_in_vrf': 'ENS-PROD',
                                    },
                                },
                            },
                        },
                        '2001:db8:20::/64': {
                            'source_protocol': 'bgp',
                            'source_protocol_codes': 'B',
                            'route': '2001:db8:20::/64',
                            'active': True,
                            'route_preference': 200,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '2001:db8::1',
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
