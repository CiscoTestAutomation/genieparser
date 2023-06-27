
expected_output = {
    'Ethernet0/0': {
        'delay_measurement': {
            'last_advertisement': {
                'no_advertisements': True
            },
            'liveness_detection': {
                'backoff': 1,
                'last_state_change_timestamp': {
                    'day': 18,
                    'hour': 12,
                    'minute': 58,
                    'month': 10,
                    'second': 47.578
                },
                'loss_in_last_interval': {
                    'percent': 100,
                    'rx': 0,
                    'tx': 3
                },
                'missed_count': 173,
                'received_count': 0,
                'session_creation_timestamp': {
                    'day': 18,
                    'hour': 12,
                    'minute': 56,
                    'month': 10,
                    'second': 46.731
                },
                'session_state': 'Down',
                'unique_path_name': 'Path-1'
            },
            'next_advertisement': {
                'check_scheduled': {
                    'check_scheduled': 120,
                    'in_n_more_probes': 2
                },
                'no_probes': True
            },
            'profile_name': 'Not configured',
            'session_id': 1
        },
        'delay_measurement_enabled': 'Enabled',
        'ifh': '0x2',
        'local_ipv4_address': '19.1.1.3',
        'local_ipv6_address': '::',
        'loss_measurement_enabled': 'Disabled',
        'state': 'Up'
    },
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
    'Serial2/0': {
        'delay_measurement_enabled': 'Disabled',
        'ifh': '0xA',
        'local_ipv4_address': '0.0.0.0',
        'local_ipv6_address': '::',
        'loss_measurement_enabled': 'Disabled',
        'state': 'Down'
    }
}
