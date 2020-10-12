expected_output = {
                    'interface': {
                        'GigabitEthernet0/0/0/0': {
                            'protocol': {
                                'not_present': {
                                    'capsulation': 'not_present',
                                    'penalty': 629,
                                    'suppressed': 'no'
                                }
                            }
                        },
                        'GigabitEthernet0/0/0/1': {
                            'protocol': {
                                'not_present': {
                                    'capsulation': 'not_present',
                                    'penalty': 2389,
                                    'suppressed': 'yes'
                                }
                            }
                        },
                        'POS0/2/0/0': {
                            'protocol': {
                                '<base>': {
                                    'capsulation': 'ppp       ',
                                    'penalty': 0,
                                    'suppressed': 'no'
                                },
                                'ipv4': {
                                    'capsulation': 'ipcp      ',
                                    'penalty': 0,
                                    'suppressed': 'no'
                                },
                                'not_present': {
                                    'capsulation': 'not_present',
                                    'penalty': 0,
                                    'suppressed': 'no'
                                }
                            }
                        }
                    }
                }