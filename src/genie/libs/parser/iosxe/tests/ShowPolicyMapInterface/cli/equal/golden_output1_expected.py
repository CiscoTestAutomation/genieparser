expected_output = {
    'HundredGigE1/0/3': {
        'service_policy': {
            'input': {
                'policy_name': {
                    'map1_table': {
                        'class_map': {
                            'class-default': {
                                'match': ['any'],
                                'match_evaluation': 'match-any',
                                'packets': 2482448,
                                'police': {
                                    'burst_bytes': 10240,
                                    'conformed': {
                                        'actions': {
                                            'transmit': True,
                                        },
                                        'bps': 46055000,
                                        'bytes': 1865503500,
                                    },
                                    'exceeded': {
                                        'actions': {
                                            'drop': True,
                                        },
                                        'bps': 45873000,
                                        'bytes': 1858168500,
                                    },
                                    'rate_bps': 500000000,
                                },
                                'qos_set': {
                                    'dscp': {
                                        'dscp table t1': {
                                        },
                                    },
                                    'traffic-class': {
                                        'dscp table t1': {
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}