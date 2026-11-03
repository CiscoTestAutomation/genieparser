expected_output = {
    'prefix': {
        '123.1.1.0/24': {
            'number_of_paths': 1,
            'update_time': 'Wed Jul 11 19:00:12 2018',
            'vobj_id': 141,
            'orig_as': 65002,
            'peer_as': 65100,
            'rnh': '10.3.0.2',
            'paths': {
                '10.4.0.2': {
                    'interface': 'Ethernet8/4',
                    'dmac': '0018.bad8.4dfd',
                    'packets': 2,
                    'bytes': 3484,
                    'repair_path': {
                        'next_hop': '10.3.0.2',
                        'interface': 'Ethernet8/3',
                        'dmac': '0018.bad8.4dfd',
                        'packets': 0,
                        'bytes': 1,
                    },
                },
            },
        },
    },
}
