expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'safi': 'unicast',
                    'table_id': '0xe0000000',
                    'routes': {
                        '172.16.0.89/32': {
                            'route': '172.16.0.89/32',
                            'next_hop': {
                                'outgoing_interface': {
                                    'TenGigE0/0/1/2': {
                                        'outgoing_interface': 'TenGigE0/0/1/2',
                                        'metrics': 1,
                                        'preference': 1,
                                        'local_label': 'No label',
                                        'path_event': 'Path is configured at Sep 11 08:29:25.605',
                                        'path_version': 0,
                                        'path_status': '0x0',
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
