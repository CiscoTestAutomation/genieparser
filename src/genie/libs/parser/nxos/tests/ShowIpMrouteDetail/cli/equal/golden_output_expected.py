expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'count_multicast_total': 701,
                    'count_multicast_starg': 0,
                    'count_multicast_sg': 700,
                    'count_multicast_starg_prefix': 1,
                    'multicast_group': {
                        '224.1.24.0/32': {
                            'source_address': {
                                '192.205.38.2/32': {
                                    'uptime': '13:03:24',
                                    'client_count': {
                                        'nbm': 5,
                                        'pim': 0,
                                        'ip': 0,
                                    },
                                    'data_created': 'No',
                                    'statistics': {
                                        'packets': 3122,
                                        'bytes': 159222,
                                        'bitrate': 27.2,
                                        'bitrate_unit': 'bps',
                                        'flow_status': 'Active Flow',
                                    },
                                    'incoming_interface_list': [
                                        {
                                            'interface': 'Ethernet1/51',
                                            'uptime': '13:03:24',
                                            'internal': True,
                                        },
                                    ],
                                    'oil_count': 5,
                                    'outgoing_interface_list': [
                                        {
                                            'interface': 'Ethernet1/39',
                                            'oil_uptime': '13:03:24',
                                            'oil_flags': 'nbm',
                                        },
                                        {
                                            'interface': 'Ethernet1/40',
                                            'oil_uptime': '13:03:24',
                                            'oil_flags': 'nbm',
                                        },
                                        {
                                            'interface': 'Ethernet1/38',
                                            'oil_uptime': '13:03:24',
                                            'oil_flags': 'nbm',
                                        },
                                        {
                                            'interface': 'Ethernet1/37',
                                            'oil_uptime': '13:03:24',
                                            'oil_flags': 'nbm',
                                        },
                                        {
                                            'interface': 'Ethernet1/36',
                                            'oil_uptime': '13:03:24',
                                            'oil_flags': 'nbm',
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
