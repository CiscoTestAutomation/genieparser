expected_output = {
    'ipv4_sgt_bindings': {
        '100.1.1.0': {
            'ip_address': '100.1.1.0',
            'sgt': 10,
            'source': 'cli'
        },
        '100.1.1.1': {
            'ip_address': '100.1.1.1',
            'sgt': 20,
            'source': 'cli'
        },
        '100.1.1.2': {
            'ip_address': '100.1.1.2',
            'sgt': 10,
            'source': 'cli'
        },
        '100.1.1.3': {
            'ip_address': '100.1.1.3',
            'sgt': 20,
            'source': 'cli'
        },
        'total_active': 4,
        'total_cli': 4
    },
    'ipv6_sgt_bindings': {
        '100::': {
            'ip_address': '100::',
            'sgt': 10,
            'source': 'cli'
        },
        '100::1': {
            'ip_address': '100::1',
            'sgt': 20,
            'source': 'cli'
        },
        '100::2': {
            'ip_address': '100::2',
            'sgt': 10,
            'source': 'cli'
        },
        '100::3': {
            'ip_address': '100::3',
            'sgt': 20,
            'source': 'cli'
        },
        'total_active': 4,
        'total_cli': 4
    }
}