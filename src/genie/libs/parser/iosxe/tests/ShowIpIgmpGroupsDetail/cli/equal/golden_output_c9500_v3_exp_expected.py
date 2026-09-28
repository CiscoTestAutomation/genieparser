expected_output = {
    'vrf': {
        'default': {
            'interface': {
                'TwentyFiveGigE1/0/3': {
                    'group': {
                        '232.1.1.1': {
                            'flags': 'SSM',
                            'up_time': '00:00:13',
                            'group_mode': 'include',
                            'last_reporter': '10.20.99.2',
                            'source': {
                                '20.20.20.100': {
                                    'up_time': '00:00:13',
                                    'v3_exp': '00:02:49',
                                    'csr_exp': 'stopped',
                                    'forward': True,
                                    'flags': 'R',
                                },
                            },
                        },
                    },
                    'join_group': {
                        '232.1.1.1 20.20.20.100': {
                            'v3_exp': '00:02:49',
                            'csr_exp': 'stopped',
                            'forward': True,
                            'flags': 'SSM',
                            'group': '232.1.1.1',
                            'source': '20.20.20.100',
                            'up_time': '00:00:13',
                            'last_reporter': '10.20.99.2',
                        },
                    },
                },
            },
        },
    },
}
