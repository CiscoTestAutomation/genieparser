expected_output = {
    'switch': {
        '3': {
            'fan': {
                '1': {
                    'state': 'ok'
                },
                '2': {
                    'state': 'ok'
                },
                '3': {
                    'state': 'ok'
                }
            },
            'hotspot_temperature': {
                'red_threshold': '125',
                'state': 'green',
                'value': '55',
                'yellow_threshold': '105'
            },
            'inlet_temperature': {
                'red_threshold': '56',
                'state': 'green',
                'value': '32',
                'yellow_threshold': '46'
            },
            'outlet_temperature': {
                'red_threshold': '125',
                'state': 'green',
                'value': '42',
                'yellow_threshold': '105'
            },
            'power_supply': {
                '1': {
                    'pid': 'PWR-C1-715WAC',
                    'poe_power': 'good',
                    'serial_number': 'DCA2120G474',
                    'state': 'ok',
                    'status': 'ok',
                    'system_power': 'good',
                    'watts': '715'
                },
                '2': {
                    'state': 'not present',
                    'status': 'not present'
                }
            },
            'system_temperature_state': 'ok'
        }
    }
}