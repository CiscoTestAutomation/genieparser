expected_output = {
   'alarm_logger_level': 'Disabled',
    'alarm_relay_mode': 'Positive',
    'input_alarm_1': {
        'alarm': 'Enabled',
        'notifies': 'Disabled',
        'relay': '',
        'syslog': 'Enabled',
    },
    'input_alarm_2': {
        'alarm': 'Enabled',
        'notifies': 'Disabled',
        'relay': '',
        'syslog': 'Enabled',
    },
    'power_supply': {
        'alarm': 'Enabled',
        'notifies': 'Disabled',
        'relay': '',
        'syslog': 'Enabled',
    },
    'sd_card': {
        'alarm': 'Disabled',
        'notifies': 'Disabled',
        'relay': '',
        'syslog': 'Disabled',
    },
    'temperature_primary': {
        'alarm': 'Enabled',
        'notifies': 'Enabled',
        'relay': 'MAJ',
        'syslog': 'Enabled',
        'threshold': {
            'max_temp': '90C',
            'min_temp': '-40C',
        },
    },
    'temperature_secondary': {
        'alarm': 'Disabled',
        'notifies': 'Disabled',
        'relay': '',
        'syslog': 'Disabled',
        'threshold': {
        },
    },
}
