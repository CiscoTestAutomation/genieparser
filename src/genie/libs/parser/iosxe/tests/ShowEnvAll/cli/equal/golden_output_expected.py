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
                    'state': 'ok',
                    'temperature': 'ok',
                    'pid': 'PWR-C2-1025WAC',
                    'serial_number': 'DCB1636C003',
                    'status': 'ok',
                    'system_power': 'good',
                    'poe_power': 'good',
                    'watts': '250/775'
                },
                "2": {
                    'status': 'not present',
                    'temperature': 'not present',
                    'state': 'not present'
                }
            },
            'system_temperature_state': 'ok',
            'system_temperature': {
                'value': "41",
                'state': 'green',
                'yellow_threshold': "66",
                'red_threshold': "76"
            },
            'redundant_power_system': {
                '<>': {
                    'status': 'not present'
                }
            }
        }
    }
}