expected_output = {
    'power_supplies': {
        'POWER SUPPLY-A': {
            'type': 'DC',
            'status': 'OK',
            'voltage': '24V',
        },
        'POWER SUPPLY-B': {
            'type': 'DC',
            'status': 'OK',
            'voltage': '54V',
        }
    },
    'temperatures': {
        'supervisor_temp_value': '48 C',
        'supervisor_temp_state': 'GREEN',
        'system_temperature_thresholds': {
            'minor_threshold': '80 C (Yellow)',
            'major_threshold': '90 C (Red)',
            'critical_threshold': '96 C'
            }
    },
    'alarms': {
        'ALARM CONTACT 1': {
            'status': 'not asserted',
            'description': 'external alarm contact 1',
            'severity': 'minor',
            'trigger': 'closed',
            },
        'ALARM CONTACT 2': {
            'status': 'not asserted',
            'description': 'external alarm contact 2',
            'severity': 'minor',
            'trigger': 'closed',
            }
    }
}