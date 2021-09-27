

expected_output = {
    'cpu': {
        'requested_percent': 1,
        'actual_percent': 0,
        'state_abbrev': "R",
        'state': "Running",
    },
    'memory': {
        'allocation_kb': 262144,
        'used_kb': 13400,
    },
    'storage': {
        "_rootfs": {
            'capacity_kb': 243823,
            'used_kb': 161690,
            'available_kb': 77537,
            'used_percent': 68,
        },
        "/cisco/core": {
            'capacity_kb': 2097152,
            'used_kb': 62216,
            'available_kb': 2034936,
            'used_percent': 3,
        },
    },
}
