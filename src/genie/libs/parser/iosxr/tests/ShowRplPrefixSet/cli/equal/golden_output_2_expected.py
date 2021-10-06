expected_output = {
    'prefix_set_name': {
        'test': {
            'prefix_set_name': 'test',
            'protocol': 'ipv4',
            'prefixes': {
                '10.205.0.0/8 8..8': {
                    'prefix': '10.205.0.0/8',
                    'masklength_range': '8..8'
                },
                '10.205.0.0/8 8..16': {
                    'prefix': '10.205.0.0/8',
                    'masklength_range': '8..16'
                },
                '10.21.0.0/8 8..16': {
                    'prefix': '10.21.0.0/8',
                    'masklength_range': '8..16'
                },
                '10.94.0.0/8 24..32': {
                    'prefix': '10.94.0.0/8',
                    'masklength_range': '24..32'
                },
                '10.169.0.0/8 16..24': {
                    'prefix': '10.169.0.0/8',
                    'masklength_range': '16..24'
                }
            }
        }
    }
}
