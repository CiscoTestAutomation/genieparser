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
        },
        'test6': {
            'prefix_set_name': 'test6',
            'protocol': 'ipv6',
            'prefixes': {
                '2001:db8:1::/64 64..64': {
                    'prefix': '2001:db8:1::/64',
                    'masklength_range': '64..64'
                },
                '2001:db8:2::/64 65..128': {
                    'prefix': '2001:db8:2::/64',
                    'masklength_range': '65..128'
                },
                '2001:db8:3::/64 64..128': {
                    'prefix': '2001:db8:3::/64',
                    'masklength_range': '64..128'
                },
                '2001:db8:4::/64 65..98': {
                    'prefix': '2001:db8:4::/64',
                    'masklength_range': '65..98'
                }
            }
        }
    }
}
