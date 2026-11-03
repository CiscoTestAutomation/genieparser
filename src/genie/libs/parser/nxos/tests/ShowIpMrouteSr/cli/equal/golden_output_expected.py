expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'multicast_group': {
                        '229.0.0.1/32': {
                            'source_address': {
                                '172.16.1.10/32': {
                                    'uptime': '00:38:00',
                                    'flags': 'ip pim',
                                    'nat_mode': 'Egress',
                                    'nat_route_type': 'Pre',
                                    'incoming_interface_list': {
                                        'Ethernet1/1': {
                                            'rpf_nbr': '172.16.1.10',
                                            'internal': True,
                                        },
                                    },
                                    'oil_count_label': 'count',
                                    'oil_count': 0,
                                    'translation_list': {
                                        'count_label': 'count',
                                        'count': 1,
                                        'sr': [
                                            {
                                                'source_address': '172.16.1.10',
                                                'multicast_group': '2.0.0.10',
                                                'source_protocol': 'udp',
                                                'src_label': 'src',
                                                'src_port': 3000,
                                                'destination_protocol': 'udp',
                                                'dst_label': 'dst',
                                                'dst_port': 3000,
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
    },
}
