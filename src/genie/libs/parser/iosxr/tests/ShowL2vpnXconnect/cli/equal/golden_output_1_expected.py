

expected_output = {
    'groups': {
        'Test_XCONN_Group': {
            'name': {
                '1000': {
                    'status': 'DN',
                    'segment1': {
                        'GigabitEthernet0/0/0/5.1000': {
                            'status': 'UP',
                            'segment2': {
                                '10.4.1.206       1000': {
                                    'status': 'DN',
                                },
                            },
                        },
                    },
                },
                '2000': {
                    'status': 'DN',
                    'segment1': {
                        'GigabitEthernet0/0/0/5.2000': {
                            'status': 'UP',
                            'segment2': {
                                '10.4.1.206       2000': {
                                    'status': 'DN',
                                },
                            },
                        },
                    },
                },
            },
        },
        'Test_XCONN_Group2': {
            'name': {
                '3000': {
                    'status': 'UR',
                    'segment1': {
                        'GigabitEthernet0/0/0/5.3000': {
                            'status': 'UR',
                            'segment2': {
                                '10.4.1.206       3000': {
                                    'status': 'DN',
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
