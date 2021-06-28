expected_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.23.90.0/24': {
                                'route': '10.23.90.0/24',
                                'ip': '10.23.90.0',
                                'mask': '24',
                                'active': True,
                                'known_via': 'connected',
                                'metric': 0,
                                'distance': 0,
                                'installed': {
                                    'date': 'Oct  4 15:47:45.390',
                                    'for': '3w4d',
                                },
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.90': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.90',
                                            'metric': 0,
                                        },
                                    },
                                },
                                'redist_advertisers': {
                                    'eigrp/100': {
                                        'protoid': 5,
                                        'clientid': 22,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
