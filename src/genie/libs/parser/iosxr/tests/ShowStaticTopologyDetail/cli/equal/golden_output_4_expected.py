

expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.15.20.2/32': {
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'active': False,
                                        'index': 1,
                                        'metrics': 1,
                                        'next_hop': '10.151.22.21',
                                        'outgoing_interface': 'Bundle-Ether2.25',
                                        'path_event': 'Path is configured at Apr 30 15:43:47.894',
                                        'path_status': '0x80',
                                        'path_version': 0,
                                        'preference': 1,
                                    },
                                },
                            },
                            'route': '10.15.20.2/32',
                        },
                    },
                    'safi': 'unicast',
                    'table_id': '0xe0000000',
                },
            },
        },
    },
}
