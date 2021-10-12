

expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.4.1.1/32': {
                            'route': '10.4.1.1/32',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'active': True,
                                        'next_hop': '10.1.3.1',
                                        'next_hop_netmask': '32',
                                        'outgoing_interface': 'Ethernet1/2',
                                    },
                                },
                            },
                        },
                        '10.16.2.2/32': {
                            'route': '10.16.2.2/32',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'active': True,
                                        'next_hop': '10.2.3.2',
                                        'next_hop_netmask': '32',
                                        'outgoing_interface': 'Ethernet1/4',
                                    },
                                    2: {
                                        'index': 2,
                                        'active': True,
                                        'next_hop': '10.229.3.2',
                                        'next_hop_netmask': '32',
                                        'outgoing_interface': 'Ethernet1/1',
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
