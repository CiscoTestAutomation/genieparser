expected_output = {
        'vrf': {
            'HIPTV': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '172.25.254.37/32': {
                                'known_via': 'bgp 7992',
                                'ip': '172.25.254.37',
                                'metric': 0,
                                'installed': {
                                    'date': 'Feb 6 13:12:22.999',
                                    'for': '10w6d',
                                },
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'metric': 0,
                                            'next_hop': '172.25.253.121',
                                            'from': '172.25.253.121',
                                        },
                                    },
                                },
                                'active': True,
                                'distance': 20,
                                'route': '172.25.254.37/32',
                                'mask': '32',
                                'tag': '65525',
                                'type': 'external',
                            },
                        },
                    },
                },
            },
        },
    }
