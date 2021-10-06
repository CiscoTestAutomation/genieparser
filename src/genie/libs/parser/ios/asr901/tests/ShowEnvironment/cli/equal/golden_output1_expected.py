expected_output = {
    'power_supply': {
        '12AV': {
            'volt': 0.0,
            'status': 'Failed'
        },
        '1.5V': {
            'volt': 1.49,
            'status': 'Normal'
        },
        '12BV': {
            'volt': 12.01,
            'status': 'Normal'
        },
        '2.5V': {
            'volt': 2.5,
            'status': 'Normal'
        },
        '1.05V': {
            'volt': 1.08,
            'status': 'Normal'
        },
        '1.2V': {
            'volt': 1.19,
            'status': 'Normal'
        },
        '1.8V': {
            'volt': 1.81,
            'status': 'Normal'
        },
        '0.75V': {
            'volt': 0.75,
            'status': 'Normal'
        },
        '1V': {
            'volt': 1.0,
            'status': 'Normal'
        },
        '3.3V': {
            'volt': 3.28,
            'status': 'Normal'
        },
        '5V': {
            'volt': 4.92,
            'status': 'Normal'
        }
    },
    'fan': {
        '1': {
            'status': 'Normal',
            'running_percent_speed': 53
        },
        '2': {
            'status': 'Failed',
            'running_percent_speed': 0
        },
        '3': {
            'status': 'Normal',
            'running_percent_speed': 54
        }
    },
    'board_temperature_alert': {
        'Board': {
            'warning_status': 'Enabled',
            'high_threshold': 90,
            'low_threshold': -40
        },
        'Inlet': {
            'warning_status': 'Enabled',
            'high_threshold': 80,
            'low_threshold': -40
        }
    },
    'board_temperature': {
        'board_temperature_status': 'Normal',
        'Board': {
            'temp_cels': 45,
            'status': ' Normal'
        },
        'Inlet': {
            'temp_cels': 0,
            'status': ' Normal'
        }
    },
    'environmental_events': {
        '1': {
            'env_event': 'Environmental monitor',
            'env_state': 'started',
            'env_time': '23:59:22 UTC Mon Aug 24 2015'
        },
        '2': {
            'env_event': 'Environmental monitor',
            'env_state': 'enabled',
            'env_time': '23:59:22 UTC Mon Aug 24 2015'
        },
        '1824': {
            'env_event': 'Fan',
            'env_state': '2 fail',
            'env_time': '04:01:40 CDT Mon Aug 23 2021'
        },
        '4148': {
            'env_event': '12AV Power supply',
            'env_state': 'failed',
            'env_time': '12:50:22 MEXICO Thu Mar 4 2021'
        }
    },
    'external_alarms': {
        '1': {
            'alarm_assert_status': 'asserted'
        },
        '2': {
            'alarm_assert_status': 'asserted'
        },
        '3': {
            'alarm_assert_status': 'not asserted'
        },
        '4': {
            'alarm_assert_status': 'asserted'
        }
    }
}