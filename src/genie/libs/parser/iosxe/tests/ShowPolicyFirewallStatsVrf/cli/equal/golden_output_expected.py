expected_output = {
    'vrf': {
        'green': {
            'parameter_map': 'vrf-pmap',
            'interface_reference_count': 2,
            'total_session_count': 20,
            'total_session_exceed': 0,
            'total_session_aggressive_aging_period': 'Off',
            'total_session_event_count': 0,
            'half_open': {
                'protocol_stats': {
                    'All': {
                        'session_count': 20,
                        'exceed': 0
                    },
                    'UDP': {
                        'session_count': 0,
                        'exceed': 0
                    },
                    'ICMP': {
                        'session_count': 0,
                        'exceed': 0
                    },
                    'TCP': {
                        'session_count': 20,
                        'exceed': 0
                    }
                },
                'tcp_syn_flood_half_open_count': 20,
                'tcp_syn_flood_exceed': 834,
                'half_open_aggressive_aging_period': 'Off',
                'half_open_event_count': 0
            }
        }
    }
}
