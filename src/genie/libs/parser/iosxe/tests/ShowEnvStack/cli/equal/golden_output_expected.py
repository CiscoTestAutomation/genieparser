expected_output = {
    'switch': {
        "1": {
            'fan': {
                "1": {
                    'state': 'ok'
                },
                "2": {
                    'state': 'ok'
                },
                "3": {
                    'state': 'ok'
                }
            },
            'power_supply': {
                "1": {
                    'state': 'not present'
                },
                "2": {
                    'state': 'ok'
                }
            },
            'system_temperature_state': 'ok',
            'system_temperature': {
                'value': "28",
                'state': 'green',
                'yellow_threshold': "41",
                'red_threshold': "56"
            }
        }
    }
}
