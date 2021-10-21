

expected_output = {
    'groups': {
        'up-udpsf5-genie': {
            'name': {
                'up-udpsf5-genie': {
                    'status': 'UR',
                    'segment1': {
                        '10.154.219.82    2015030201': {
                            'status': 'UR',
                            'segment2': {
                                'Nonexistent': {
                                    'status': 'UR',
                                },
                            },
                        },
                    },
                },
            },
        },
        'up-udpsf2-genie': {
            'name': {
                'up-udpsf2-genie': {
                    'status': 'DN',
                    'segment1': {
                        'TenGigabitEthernet0/4/0/5': {
                            'status': 'UP',
                            'segment2': {
                                '10.154.219.83   1152': {
                                    'status': 'DN',
                                },
                            },
                        },
                    },
                },
            },
        },
        'UP-udpsf5genie-port': {
            'name': {
                'U-1-5-1-3': {
                    'status': 'UR',
                    'segment1': {
                        '10.154.219.84    4293089094': {
                            'status': 'UR',
                            'segment2': {
                                'Nonexistent': {
                                    'status': 'UR',
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
