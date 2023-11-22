expected_output = {
    'Default_SGACL_1-02': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
                    'matched_packets': 480,
                },
            },
        },
        'acl_type': 'role-based',
        'name': 'Default_SGACL_1-02',
        'per_user': True,
        'type': 'ipv4-acl-type',
    },
}
