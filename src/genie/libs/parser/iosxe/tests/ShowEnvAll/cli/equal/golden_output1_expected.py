expected_output = {
    'switch': {
        '1': {
            'fan': {
                '1': {
                    'direction': 'front to back',
                    'speed': 5160,
                    'state': 'ok',
                },
                '2': {
                    'direction': 'front to back',
                    'speed': 5205,
                    'state': 'ok',
                },
            },
            'power_supply': {
                '1': {
                    'pid': 'PWR-C6-125WAC',
                    'poe_power': 'n/a',
                    'serial_number': 'LIT23283LP3',
                    'status': 'ok',
                    'system_power': 'good',
                    'watts': '125',
                },
                '2': {
                    'status': 'not present',
                },
            },
            'sensors_details': {
                'PS1 Curout': {
                    'location': '1',
                    'reading': 25000,
                    'state': 'GOOD',
                    'unit': 'mA',
                },
                'PS1 Fan Status': {
                    'location': '1',
                    'reading': 43008,
                    'state': 'GOOD',
                    'unit': 'rpm',
                },
                'PS1 Hotspot': {
                    'location': '1',
                    'reading': 24,
                    'state': 'GOOD',
                    'unit': 'Celsius',
                },
                'PS1 Powout': {
                    'location': '1',
                    'reading': 300000,
                    'state': 'GOOD',
                    'unit': 'mW',
                },
                'PS1 Vout': {
                    'location': '1',
                    'reading': 12000,
                    'state': 'GOOD',
                    'unit': 'mV',
                },
                'SYSTEM HOTSPOT': {
                    'location': '1',
                    'range': '0 - 125',
                    'reading': 38,
                    'state': 'GREEN',
                    'unit': 'Celsius',
                },
                'SYSTEM INLET': {
                    'location': '1',
                    'range': '0 - 56',
                    'reading': 23,
                    'state': 'GREEN',
                    'unit': 'Celsius',
                },
                'SYSTEM OUTLET': {
                    'location': '1',
                    'range': '0 - 125',
                    'reading': 28,
                    'state': 'GREEN',
                    'unit': 'Celsius',
                },
            },
        },
    },
}