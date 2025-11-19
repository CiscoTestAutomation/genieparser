expected_output = {
    'ipv4_sgt_bindings': {
        '100.8.18.56': {
            'ip_address': '100.8.18.56',
            'sgt': 2,
            'source': 'internal',
        },
        '30.0.0.2': {
            'ip_address': '30.0.0.2',
            'sgt': 30,
            'source': 'local',
        },
        '40.0.0.2': {
            'ip_address': '40.0.0.2',
            'sgt': 40,
            'source': 'local',
        },
        'total_active': 3,
        'total_internal': 1,
        'total_local': 2,
    },
    'ipv6_sgt_bindings': {
        '1133:1:1::1': {
            'ip_address': '1133:1:1::1',
            'sgt': 2,
            'source': 'cli-hi',
        },
        '30::1200:ff:fe00:1101': {
            'ip_address': '30::1200:ff:fe00:1101',
            'sgt': 30,
            'source': 'local',
        },
        '30::9895:7599:f301:809b': {
            'ip_address': '30::9895:7599:f301:809b',
            'sgt': 30,
            'source': 'local',
        },
        '40::1200:ff:fe00:2202': {
            'ip_address': '40::1200:ff:fe00:2202',
            'sgt': 40,
            'source': 'local',
        },
        '40::2': {
            'ip_address': '40::2',
            'sgt': 40,
            'source': 'local',
        },
        'total_active': 5,
        'total_cli-hi': 1,
        'total_local': 4,
    },
}
