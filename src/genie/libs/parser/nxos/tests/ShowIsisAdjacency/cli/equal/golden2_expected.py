expected_output = {
        'instance': {
            'test': {
                'vrf': {
                    'default': {
                        'interfaces': {
                            'Ethernet1/1.115': {
                                'adjacencies': {
                                    'R2_xr': {
                                        'neighbor_snpa': {
                                            'fa16.3eff.4abd': {
                                                'level': {
                                                    "1": {
                                                        'hold_time': '00:00:09',
                                                        'state': 'UP',
                                                    },
                                                    "2": {
                                                        'hold_time': '00:00:07',
                                                        'state': 'UP',
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'Ethernet1/2.115': {
                                'adjacencies': {
                                    'R1_ios': {
                                        'neighbor_snpa': {
                                            'fa16.3eff.0c11': {
                                                'level': {
                                                    "1": {
                                                        'hold_time': '00:00:07',
                                                        'state': 'UP',
                                                    },
                                                    "2": {
                                                        'hold_time': '00:00:10',
                                                        'state': 'UP',
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'VRF1': {
                        'interfaces': {
                            'Ethernet1/1.415': {
                                'adjacencies': {
                                    '2222.22ff.4444': {
                                        'neighbor_snpa': {
                                            'fa16.3eff.4abd': {
                                                'level': {
                                                    "1": {
                                                        'hold_time': '00:00:32',
                                                        'state': 'INIT',
                                                    },
                                                    "2": {
                                                        'hold_time': '00:00:24',
                                                        'state': 'INIT',
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
            },
        },
    }