expected_output = {
    'pools': {
        'TestPool': {
            'utilization_mark': {'high': 100, 'low': 0},
            'subnet_size': {'first': 0, 'next': 0},
            'total_addresses': 254,
            'leased_addresses': 0,
            'excluded_addresses': 0,
            'pending_event': 'none',
            'subnets': {
                '192.168.1.1': {
                    'ip_range': '192.168.1.1 - 192.168.1.254',
                    'leased': 0,
                    'excluded': 0,
                    'total': 254
                }
            }
        }
    }
}
