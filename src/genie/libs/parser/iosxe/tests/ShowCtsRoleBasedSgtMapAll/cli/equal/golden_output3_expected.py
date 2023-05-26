expected_output = {
    'ipv4_sgt_bindings': {
        '100.1.1.0/24': {
            'ip_address': '100.1.1.0/24',
            'sgt': 100,
            'source': 'l3if'
        },
        '200.1.1.0/24': {
            'ip_address': '200.1.1.0/24',
            'sgt': 200,
            'source': 'l3if'
        },
        'total_active': 2,
        'total_l3if': 2
    },
    'ipv6_sgt_bindings': {
        '100:1::/64': {
            'ip_address': '100:1::/64',
            'sgt': 100,
            'source': 'l3if'
        },
        '200:1::/64': {
            'ip_address': '200:1::/64',
            'sgt': 200,
            'source': 'l3if'
        },
        'total_active': 2,
        'total_l3if': 2
    }
}