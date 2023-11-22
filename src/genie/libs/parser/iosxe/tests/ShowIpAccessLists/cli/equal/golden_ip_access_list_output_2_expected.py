expected_output = {
    'icmp_echo-01': {
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
                            'msg_type': 'echo',
                        },
                    },
                },
                'name': '10',
            },
        },
        'acl_type': 'role-based',
        'name': 'icmp_echo-01',
        'per_user': True,
        'type': 'ipv4-acl-type',
    },
} 
