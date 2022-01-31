expected_output = {
    'permit_icmp': {
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
                            'msg_type': 'echo-reply',
                        },
                    },
                },
                'name': '10',
                'statistics': {
                    'matched_packets': 19,
                },
            },
        },
        'acl_type': 'role-based',
        'name': 'permit_icmp',
        'type': 'ipv4-acl-type',
    },
}
