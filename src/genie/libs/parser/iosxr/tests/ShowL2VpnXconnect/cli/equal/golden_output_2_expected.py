

expected_output = {
    'groups': {
        'L2TPV3_V4_XC_GRP': {
            'name': {
                'L2TPV3_P2P_1': {
                    'status': 'UP',
                    'segment1': {
                        'GigabitEthernet0/2/0/1.2': {
                            'status': 'UP',
                            'segment2': {
                                '10.154.26.26     100': {
                                    'status': 'UP',
                                },
                            },
                        },
                    },
                },
                'L2TPV3_P2P_2': {
                    'status': 'UP',
                    'segment1': {
                        'GigabitEthernet0/2/0/1.3': {
                            'status': 'UP',
                            'segment2': {
                                '10.154.26.26     200': {
                                    'status': 'UP',
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
