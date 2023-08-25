expected_output= {
    'HundredGigE1/0/3': {
        'service_policy': {
            'input': {
                'policy_name': {
                    'map1_table': {
                        'class_map': {
                            'class-default': {
                                'match': ['any'],
                                'match_evaluation': 'match-any',
                                'packets': 24657219,
                                'police': {
                                    'burst_bytes': 1024000,
                                    'conformed': {
                                        'actions': {
                                            'transmit': True,
                                        },
                                        'bps': 94916000,
                                        'bytes': 3706836000,
                                    },
                                    'exceeded': {
                                        'actions': {
                                            'drop': True,
                                        },
                                        'bps': 852131000,
                                        'bytes': 33278992500,
                                    },
                                    'rate_bps': 1000000000,
                                },
                                'qos_set': {
                                    'traffic-class': {
                                        'cos table t1': {
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