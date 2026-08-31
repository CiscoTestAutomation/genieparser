expected_output = {
    'vrf': {
        'red': {
            'address_family': {
                'ipv4': {
                    'multicast_group': {
                        '225.1.1.7/32': {
                            'source_address': {
                                '47.1.1.2/32': {
                                    'uptime': '00:09:12',
                                    'flags': 'ip mrib pim',
                                    'incoming_interface_list': [
                                        {
                                            'interface': 'Ethernet1/49',
                                            'rpf_nbr': '40.1.1.2',
                                        },
                                    ],
                                    'oil_count': 1,
                                    'outgoing_interface_list': [
                                        {
                                            'interface': 'Vlan10',
                                            'oil_uptime': '00:09:12',
                                            'oil_flags': 'mrib',
                                        },
                                    ],
                                },
                            },
                        },
                    },
                },
            },
        },
        'blue': {
            'address_family': {
                'ipv4': {
                    'multicast_group': {
                        '225.1.1.7/32': {
                            'source_address': {
                                '47.1.1.2/32': {
                                    'uptime': '00:09:14',
                                    'flags': 'ip mrib pim',
                                    'incoming_interface_list': [
                                        {
                                            'interface': 'Ethernet1/49',
                                            'rpf_nbr': '40.1.1.2',
                                        },
                                    ],
                                    'oil_count': 1,
                                    'outgoing_interface_list': [
                                        {
                                            'interface': 'Vlan11',
                                            'oil_uptime': '00:09:12',
                                            'oil_flags': 'mrib',
                                        },
                                    ],
                                    'extranet_receiver_list': {
                                        'vrf_count': 2,
                                        'oif_count': 2,
                                        'vrf': {
                                            'red': {
                                                'source_address': '47.1.1.2/32',
                                                'multicast_group': '225.1.1.7/32',
                                                'oif_count': 1,
                                            },
                                            'green': {
                                                'source_address': '47.1.1.2/32',
                                                'multicast_group': '225.1.1.7/32',
                                                'oif_count': 1,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        'green': {
            'address_family': {
                'ipv4': {
                    'multicast_group': {
                        '225.1.1.7/32': {
                            'source_address': {
                                '47.1.1.2/32': {
                                    'uptime': '00:09:14',
                                    'flags': 'ip mrib pim',
                                    'incoming_interface_list': [
                                        {
                                            'interface': 'Ethernet1/49',
                                            'rpf_nbr': '40.1.1.2',
                                        },
                                    ],
                                    'oil_count': 1,
                                    'outgoing_interface_list': [
                                        {
                                            'interface': 'Vlan12',
                                            'oil_uptime': '00:09:14',
                                            'oil_flags': 'mrib',
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
