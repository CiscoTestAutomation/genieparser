expected_output = {
        'prefix_set_name': {
            'name1': {
                'prefix_set_name': 'name1',
                'prefixes': {
                    '192.168.131.0/24 24..24': {
                        'masklength_range': '24..24',
                        'prefix': '192.168.131.0/24',
                    },
                },
                'protocol': 'ipv4',
            },
            'name2': {
                'prefix_set_name': 'name2',
                'prefixes': {
                    '10.246.13.0/24 32..32': {
                        'masklength_range': '32..32',
                        'prefix': '10.246.13.0/24',
                    },
                    '172.16.106.0/20 32..32': {
                        'masklength_range': '32..32',
                        'prefix': '172.16.106.0/20',
                    },
                },
                'protocol': 'ipv4',
            },
            'name3': {
                'prefix_set_name': 'name3',
                'prefixes': {
                    '10.19.196.5 32..32': {
                        'masklength_range': '32..32',
                        'prefix': '10.19.196.5',
                    },
                },
                'protocol': 'ipv4',
            },
        },
    }
