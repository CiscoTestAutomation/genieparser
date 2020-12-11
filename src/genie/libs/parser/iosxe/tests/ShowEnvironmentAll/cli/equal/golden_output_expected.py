expected_output = {
    'switch': {
        '1': {
            'fan': {
                '1': {
                    'state': 'ok',
                },
                '2': {
                    'state': 'ok',
                },
                '3': {
                    'state': 'ok',
                },
                '4': {
                    'state': 'ok',
                },
                '5': {
                    'state': 'ok',
                },
            },
            'hotspot_temperature': {
                'red_threshold': '125',
                'state': 'green',
                'value': '55',
                'yellow_threshold': '105',
            },
            'inlet_temperature': {
                'red_threshold': '56',
                'state': 'green',
                'value': '29',
                'yellow_threshold': '46',
            },
            'outlet_temperature': {
                'red_threshold': '125',
                'state': 'green',
                'value': '40',
                'yellow_threshold': '105',
            },
            'power_supply': {
                '1': {
                    'pid': 'PWR-C4-950WAC-R',
                    'poe_power': 'n/a',
                    'serial_number': 'GEN222700VU',
                    'state': 'not present',
                    'status': 'no input power',
                    'system_power': 'bad',
                    'watts': '950',
                },
                '2': {
                    'pid': 'PWR-C4-950WAC-R',
                    'poe_power': 'n/a',
                    'serial_number': 'GEN222700VT',
                    'state': 'ok',
                    'status': 'ok',
                    'system_power': 'good',
                    'watts': '950',
                },
            },
            'system_temperature_state': 'ok',
        },
    },
}
				