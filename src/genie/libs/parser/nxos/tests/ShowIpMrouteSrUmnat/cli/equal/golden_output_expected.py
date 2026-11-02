expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'multicast_group': {
                        '1.2.3.4/32': {
                            'source_address': {
                                '21.1.1.1/32': {
                                    'translation': {
                                        'source_address': '57.1.1.51/32',
                                        'multicast_group': '227.1.1.1/32',
                                        'protocol': 'udp',
                                        'udp_source_port': 1000,
                                        'udp_destination_port': 500,
                                    },
                                    'oil_count': 1,
                                    'outgoing_interface_list': [
                                        {
                                            'interface': 'Loopback100',
                                            'oil_uptime': '1d01h',
                                            'oil_flags': 'static',
                                        },
                                    ],
                                    'chained_translations': [
                                        {
                                            'source_address': '21.1.1.2',
                                            'multicast_group': '229.1.1.1',
                                            'outgoing_interface': 'Ethernet1/7',
                                        },
                                    ],
                                },
                            },
                        },
                        '1.2.3.5/32': {
                            'source_address': {
                                '21.1.1.1/32': {
                                    'translation': {
                                        'source_address': '57.1.1.51/32',
                                        'multicast_group': '227.1.1.1/32',
                                        'protocol': 'udp',
                                        'udp_source_port': 0,
                                        'udp_destination_port': 0,
                                    },
                                    'oil_count': 1,
                                    'outgoing_interface_list': [
                                        {
                                            'interface': 'Loopback100',
                                            'oil_uptime': '1d01h',
                                            'oil_flags': 'static',
                                        },
                                    ],
                                    'chained_translations': [
                                        {
                                            'source_address': '21.1.1.2',
                                            'multicast_group': '229.1.1.1',
                                            'outgoing_interface': 'Ethernet1/7',
                                        },
                                    ],
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
