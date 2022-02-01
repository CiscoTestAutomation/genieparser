expected_output = {
    'v6_sgacl': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'protocol': 'icmp',
                        },
                    },
                    'l4': {
                        'icmp': {
                            'established': False,
                        },
                    },
                },
                'name': '10',
                'statistics': {
                    'matched_packets': 19,
                },
            },
        },
        'acl_type': 'ipv6 role-based',
        'name': 'v6_sgacl',
        'type': 'ipv6-acl-type',
    },
}
