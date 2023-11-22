
expected_output = {
    'Ethernet1/2': {
        'delay_measurement': {
            'last_advertisement': {
                'advertised_at': {
                    'day': 18,
                    'hour': 12,
                    'minute': 58,
                    'month': 10,
                    'second': 47,
                    'seconds_ago': 398,
                    'year': 2021
                },
                'advertised_delays': {
                    'average': 747,
                    'maximum': 5628,
                    'minimum': 496,
                    'variance': 234
                },
                'advertised_reason': 'First advertisement',
                'advertised_anomaly': 'INACTIVE'
            },
            'liveness_detection': {
                'backoff': 0,
                'last_state_change_timestamp': {
                    'day': 18,
                    'hour': 12,
                    'minute': 57,
                    'month': 10,
                    'second': 8.097
                },
                'loss_in_last_interval': {
                    'percent': 0,
                    'rx': 3,
                    'tx': 3
                },
                'missed_count': 0,
                'received_count': 166,
                'session_creation_timestamp': {
                    'day': 18,
                    'hour': 12,
                    'minute': 56,
                    'month': 10,
                    'second': 46.732
                },
                'session_state': 'Up',
                'unique_path_name': 'Path-3'
            },
            'next_advertisement': {
                'aggregated_delays': {
                    'average': 769,
                    'maximum': 882,
                    'minimum': 687,
                    'variance': 82
                },
                'check_scheduled': {
                    'check_scheduled': 120,
                    'in_n_more_probes': 2
                },
                'rolling_average': 757
            },
            'profile_name': 'Not configured',
            'session_id': 3
        },
        'delay_measurement_enabled': 'Enabled',
        'ifh': '0x8',
        'local_ipv4_address': '1.2.3.3',
        'local_ipv6_address': '1:2:3:3::1',
        'loss_measurement': {
            'current_probe': {
                'not_running_info': 'Platform not supported',
            },
            'last_advertisement': {
                'advertised_at': {
                    'day': 18,
                    'hour': 12,
                    'minute': 57,
                    'month': 10,
                    'second': 47,
                    'seconds_ago': 458,
                    'year': 2021
                },
                'advertised_loss': {
                    'average': 0.0,
                    'capped': 50.331642,
                    'maximum': 0.0,
                    'minimum': 0.0,
                    'variance': 0.0
                },
                'advertised_reason': 'First advertisement',
                'advertised_anomaly': 'ACTIVE'
            },
            'liveness_detection': {
                'backoff': 0,
                'last_state_change_timestamp': {
                    'day': 18,
                    'hour': 12,
                    'minute': 57,
                    'month': 10,
                    'second': 17.221
                },
                'loss_in_last_interval': {
                    'percent': 0,
                    'rx': 3,
                    'tx': 3
                },
                'missed_count': 0,
                'received_count': 33,
                'session_creation_timestamp': {
                    'day': 18,
                    'hour': 12,
                    'minute': 56,
                    'month': 10,
                    'second': 46.732
                },
                'session_state': 'Up',
                'unique_path_name': 'Path-3'
            },
            'next_advertisement': {
                'aggregated_loss': {
                    'average': 0.0,
                    'capped': 50.331642,
                    'maximum': 0.0,
                    'minimum': 0.0,
                    'variance': 0.0
                },
                'check_scheduled': 120,
                'rolling_average': 0.0
            },
            'profile_name': 'Not configured',
            'session_id': 4
        },
        'loss_measurement_enabled': 'Enabled',
        'state': 'Up'
    },
}