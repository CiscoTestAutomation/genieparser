expected_output = {
    'GigabitEthernet5': {
        'service_policy': {
            'input': {
                'policy_name': {
                    'check_exp': {
                        'class_map': {
                            'check_exp': {
                                'match_evaluation': 'match-any',
                                'packets': 0,
                                'bytes': 0,
                                'rate': {
                                    'interval': 300,
                                    'offered_rate_bps': 0,
                                    'drop_rate_bps': 0
                                },
                                'match': ['mpls experimental topmost 0'],
                                'match_stats': {
                                    'mpls experimental topmost 0': {
                                        'packets': 0,
                                        'bytes': 0,
                                        'rate': {
                                            'interval': 300,
                                            'offered_rate_bps': 0
                                        }
                                    },
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
