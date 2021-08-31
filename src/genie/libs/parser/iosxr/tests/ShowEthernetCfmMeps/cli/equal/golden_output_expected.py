expected_output = {
    'domain': {
        'dom3': {
            'level': 5,
            'service': 'ser3',
            'mep_type': {
                'down': {
                    'interface': {
                        'GigabitEthernet0/0/0/0': {
                            'mep_id': 1,
                            'id': {
                                10: {
                                    'mac_address': {
                                        '0001.02ff.0706': {
                                            'st': 'V',
                                            'port': 'Up',
                                            'up_down_time': '00:01:35',
                                            'ccm_rcvd': 2,
                                            'seq_err': 0,
                                            'rdi': 0,
                                            'error': 2,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        'dom4': {
            'level': 2,
            'service': 'ser4',
            'mep_type': {
                'down': {
                    'interface': {
                        'GigabitEthernet0/0/0/0': {
                            'mep_id': 1,
                            'id': {
                                20: {
                                    'mac_address': {
                                        '0001.02ff.0705': {
                                            'st': '>',
                                            'port': 'Up',
                                            'up_down_time': '00:00:03',
                                            'ccm_rcvd': 4,
                                            'seq_err': 1,
                                            'rdi': 0,
                                            'error': 0,
                                        },
                                    },
                                },
                                21: {
                                    'mac_address': {
                                        '0001.02ff.0706': {
                                            'st': '>',
                                            'port': 'Up',
                                            'up_down_time': '00:00:04',
                                            'ccm_rcvd': 3,
                                            'seq_err': 0,
                                            'rdi': 0,
                                            'error': 0,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        'dom5': {
            'level': 2,
            'service': 'dom5',
        },
    },
}
