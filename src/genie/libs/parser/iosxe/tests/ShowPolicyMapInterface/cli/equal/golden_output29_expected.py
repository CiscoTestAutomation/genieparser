expected_output =  {
    'HundredGigE1/0/5': {
        'service_policy': {
            'input': {
                'policy_name': {
                    'map1': {
                        'class_map': {
                            'cs1': {
                                'match': ['dscp cs1 (8)'],
                                'match_evaluation': 'match-all',
                                'packets': 0,
                                'police': {
                                    'burst_bytes': 1024000,
                                    'rate_bps': 1000000000,
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
                                    }
                                }
                            },
                            'cs2': {
                                'match': ['dscp cs2 (16)'],
                                'match_evaluation': 'match-all',
                                'packets': 0,
                                'police': {
                                    'burst_bytes': 1024000,
                                    'rate_bps': 1000000000,
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
                                    }
                                }
                            },
                            'cs5': {
                                'match': ['dscp cs5 (40)'],
                                'match_evaluation': 'match-all',
                                'packets': 105392304,
                                'police': {
                                    'burst_bytes': 1024000,
                                    'rate_bps': 1000000000,
                                    'conformed': {
                                        'actions': {
                                            'transmit': True,
                                        },
                                        'bps': 64863000,
                                        'bytes': 6955892064,
                                    },
                                    'exceeded': {
                                        'actions': {
                                            'drop': True,
                                        },
                                        'bps': 0,
                                        'bytes': 0,
                                    }
                                },
                                'qos_set': {
                                    'dscp': {
                                        'cs4': {
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}