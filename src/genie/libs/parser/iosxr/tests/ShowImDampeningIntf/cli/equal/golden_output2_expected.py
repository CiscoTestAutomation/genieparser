expected_output = {
                    'interface': {
                        'TenGigE 0/1/0/0': {
                            'currently_suppressed': 'yes',
                            'dampening_status': 'enabled',
                            'half_life': 1,
                            'max_supress_time': 4,
                            'penalty': 1625,
                            'protocol': {
                                'ipv4': {
                                    'protocol_capsulation': 'ipv4',
                                    'protocol_penalty': 1615,
                                    'protocol_suppression': 'no',
                                    'protocol_suppression_timer': 22,
                                    'protocol_underlying_state': 'down'
                                },
                                'ipv6': {
                                    'protocol_capsulation': 'ipv6',
                                    'protocol_penalty': 1625,
                                    'protocol_suppression': 'yes',
                                    'protocol_suppression_timer': 42,
                                    'protocol_underlying_state': 'down'
                                }
                            },
                            'reuse': 1000,
                            'suppress': 1500,
                            'suppressed_secs_remaining': 42,
                            'underlying_state': 'down'
                        }
                    }
                }