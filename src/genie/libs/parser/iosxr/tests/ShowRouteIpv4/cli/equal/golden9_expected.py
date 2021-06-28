expected_output = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '10.23.120.2/32': {
                                'route': '10.23.120.2/32',
                                'ip': '10.23.120.2',
                                'mask': '32',
                                'active': True,
                                'known_via': 'local',
                                'metric': 0,
                                'distance': 0,
                                'installed': {
                                    'date': 'Oct  4 15:47:45.368',
                                    'for': '3w4d',
                                },
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/0/1.420': {
                                            'outgoing_interface': 'GigabitEthernet0/0/0/1.420',
                                            'metric': 0,
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
