

expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'multicast_group': {
                        '10.76.1.1/32': {
                            'source_address': {
                                '10.169.1.1/32': {
                                    'flags': 'ip mrib pim',
                                    'incoming_interface_list': {
                                        'Ethernet1/9': {
                                            'internal': True,
                                            'rpf_nbr': '10.169.1.1'
                                            }
                                        },
                                    'oil_count': 4,
                                    'outgoing_interface_list': {
                                        'Ethernet1/11': {
                                            'oil_flags': 'mrib',
                                            'oil_uptime': '1d22h',
                                        },
                                        'Vlan200': {
                                            'oil_flags': 'mrib, pim.',
                                            'oil_uptime': '01:25:19',
                                        },
                                        'Vlan30': {
                                            'oil_flags': 'mrib',
                                            'oil_uptime': '1d22h',
                                        },
                                        'port-channel12': {
                                            'oil_flags': 'pim',
                                            'oil_uptime': '01:24:28',
                                        },
                                    },
                                    'uptime': '1d22h',
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
