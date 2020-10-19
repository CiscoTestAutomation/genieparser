expected_output = {
    'interface': {
        'TenGigE 0/1/0/0': {
            'currently_suppressed': 'yes',
            'dampening_status': 'enabled',
            'half_life': 1,
            'index': {
                1: {
                    'capsulation': 'ipv6',
                    'penalty': 1625,
                    'protocol': 'ipv6',
                    'suppression': 'YES',
                    'suppression_remaining_sec': 42,
                    'underlying_state': 'Down'
                },
                2: {
                    'capsulation': 'ipv4',
                    'penalty': 1615,
                    'protocol': 'ipv4',
                    'suppression': 'NO',
                    'suppression_remaining_sec': 22,
                    'underlying_state': 'Down'
                }
            },
            'interface_handler': '0x01180020',
            'max_supress_time': 4,
            'penalty': 1625,
            'reuse': 1000,
            'suppress': 1500,
            'suppressed_secs_remaining': 42,
            'underlying_state': 'Down'
        }
    }
}
