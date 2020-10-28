expected_output = {
                    'interface': {
                        'GigabitEthernet0/0/0/0': {
                            'index': {
                                1: {
                                    'penalty': 629,
                                    'suppressed': 'NO'
                                }
                            }
                        },
                        'GigabitEthernet0/0/0/1': {
                            'index': {
                                1: {
                                    'penalty': 2389,
                                    'suppressed': 'YES'
                                }
                            }
                        },
                        'POS0/2/0/0': {
                            'index': {
                                1: {
                                    'penalty': 0,
                                    'suppressed': 'NO'
                                },
                                2: {
                                    'capsulation': 'ppp',
                                    'penalty': 0,
                                    'protocol': '<base>',
                                    'suppressed': 'NO'
                                },
                                3: {
                                    'capsulation': 'ipcp',
                                    'penalty': 0,
                                    'protocol': 'ipv4',
                                    'suppressed': 'NO'
                                }
                            }
                        }
                    }
                }