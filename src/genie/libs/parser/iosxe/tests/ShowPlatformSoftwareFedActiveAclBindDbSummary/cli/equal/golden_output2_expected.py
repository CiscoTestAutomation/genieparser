expected_output =  {
    'interface': {
        'GigabitEthernet1/0/25': {
            'feature': {
                'Racl': {
                    'cg_id': 17,
                    'direction': 'Ingress',
                    'protocol': 'IPv4',
                    'status': 'Success',
                },
            },
        },
        'GigabitEthernet1/0/26.11': {
            'feature': {
                'Racl': {
                    'cg_id': 13,
                    'direction': 'Egress',
                    'protocol': 'IPv4',
                    'status': 'Success',
                },
                'acl': {
                    'cg_id': 13,
                    'direction': 'Egress',
                    'protocol': 'IPv4',
                    'status': 'Success',
                },
            },
        },
    },
 }
