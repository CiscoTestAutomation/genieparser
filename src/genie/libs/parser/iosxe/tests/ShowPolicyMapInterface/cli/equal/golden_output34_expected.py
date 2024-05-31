expected_output = {
    'TwentyFiveGigE1/1/2': {
        'service_policy': {
            'input': {
                'policy_name': {
                    'map1': {
                        'class_map': {
                            'class-default': {
                                'match': ['any'],
                                'match_evaluation': 'match-any',
                                'packets': 17,
                            },
                            'cs1': {
                                'match': ['dscp cs1 (8)'],
                                'match_evaluation': 'match-all',
                                'packets': 0,
                                'police': {
                                    'burst_bytes': 10240,
                                    'conformed': {
                                        'actions': {
                                            'transmit': True,
                                        },
                                        'bps': 0,
                                        'bytes': 0,
                                    },
                                    'exceeded': {
                                        'actions': {
                                            'drop': True,
                                        },
                                        'bps': 0,
                                        'bytes': 0,
                                    },
                                    'rate_bps': 100000000,
                                },
                            },
                            'cs2': {
                                'match': ['dscp cs2 (16)'],
                                'match_evaluation': 'match-all',
                                'packets': 0,
                                'police': {
                                    'burst_bytes': 10240,
                                    'conformed': {
                                        'actions': {
                                            'transmit': True,
                                        },
                                        'bps': 0,
                                        'bytes': 0,
                                    },
                                    'exceeded': {
                                        'actions': {
                                            'drop': True,
                                        },
                                        'bps': 0,
                                        'bytes': 0,
                                    },
                                    'rate_bps': 100000000,
                                },
                            },
                            'cs5': {
                                'match': ['dscp cs5 (40)'],
                                'match_evaluation': 'match-all',
                                'packets': 3643365,
                                'police': {
                                    'burst_bytes': 10240,
                                    'conformed': {
                                        'actions': {
                                            'transmit': True,
                                        },
                                        'bps': 88628000,
                                        'bytes': 3679932000,
                                    },
                                    'exceeded': {
                                        'actions': {
                                            'drop': True,
                                        },
                                        'bps': 86867000,
                                        'bytes': 3606798000,
                                    },
                                    'rate_bps': 500000000,
                                },
                                'qos_set': {
                                    'dscp': {
                                        'cs7': {
                                        },
                                    },
                                    'traffic-class': {
                                        '7': {
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