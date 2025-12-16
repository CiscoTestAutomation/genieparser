expected_output = {
    'number_of_sensors': 6,
    'sensor_value_duration': {
        '0': {
            'durations': ['0s', '810s', '810s', '810s', '810s', '810s'],
        },
        '1': {
            'durations': ['150d', '150d', '0s', '0s', '150d', '150d'],
        },
        '2': {
            'durations': ['0s', '0s', '150d', '0s', '0s', '0s'],
        },
        '5': {
            'durations': ['0s', '0s', '0s', '150d', '0s', '0s'],
        },
    },
    'sensors': {
        'P1V1_FPGA': {
            'id': 0,
            'max_sensor_value': 1,
            'normal_range': '0 - 1',
        },
        'P1V2_FPGA': {
            'id': 1,
            'max_sensor_value': 1,
            'normal_range': '0 - 1',
        },
        'P1_1V': {
            'id': 4,
            'max_sensor_value': 1,
            'normal_range': '0 - 1',
        },
        'P1_8V': {
            'id': 5,
            'max_sensor_value': 1,
            'normal_range': '0 - 2',
        },
        'P2_5V': {
            'id': 2,
            'max_sensor_value': 2,
            'normal_range': '0 - 3',
        },
        'P5V': {
            'id': 3,
            'max_sensor_value': 5,
            'normal_range': '0 - 5',
        },
    },
}