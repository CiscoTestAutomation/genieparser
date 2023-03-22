expected_output = {
    'port_channel': {
        'Po1': {
            'age': '0d:00h:01m:16s',
            'logical_slot': '35/1',
            'number_of_ports': 2,
            'gc': '0x00010001',
            'protocol': 'PAgP',
            'port_security': 'Disabled',
            'switchover': 'disabled',
            'dampening': 'disabled',
            'ports': {
                'Tw1/0/14': {
                    'ec_state': 'Desirable-Sl',
                    'bits': 0,
                    'load': '00',
                    'index': 0
                },
                'Tw1/0/15': {
                    'ec_state': 'Desirable-Sl',
                    'bits': 0,
                    'load': '00',
                    'index': 0
                }
            }
        },
        'Po2': {
            'age': '1d:10h:01m:16s',
            'logical_slot': '5/1',
            'number_of_ports': 1,
            'gc': '0x00010',
            'protocol': 'PAgP',
            'port_security': 'Disabled',
            'switchover': 'disabled',
            'dampening': 'disabled',
            'ports': {
                'Tw10/0/14': {
                    'ec_state': 'Desirable-Sl',
                    'bits': 0,
                    'load': '00',
                    'index': 0
                }
            }
        }
    }
}