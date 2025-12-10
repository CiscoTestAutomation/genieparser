expected_output = {
    'global_per_box_statistics': {
        'total_session_aggressive_aging_period': 'On',
        'total_session_event_count': 1,
        'half_open': {
            'protocol_stats': {
                'All': {
                    'session_count': 12,
                    'exceed': 0
                },
                'UDP': {
                    'session_count': 12,
                    'exceed': 0
                },
                'ICMP': {
                    'session_count': 0,
                    'exceed': 0
                },
                'TCP': {
                    'session_count': 0,
                    'exceed': 0
                }
            },
            'tcp_syn_flood_half_open_count': 0,
            'tcp_syn_flood_exceed': 0,
            'half_open_aggressive_aging_period': 'Off',
            'half_open_event_count': 0
        }
    }
}