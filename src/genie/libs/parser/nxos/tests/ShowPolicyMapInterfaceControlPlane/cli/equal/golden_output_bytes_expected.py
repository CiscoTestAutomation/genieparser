expected_output = {
    'control_plane': {
        'service_policy': {
            'input': {
                'policy_name': 'copp-system-p-policy-strict',
                'class_map': {
                    'class-default': {
                        'match_type': 'match-any',
                        'set_cos': 0,
                        'police': {
                            'cir': 400,
                            'cir_unit': 'kbps',
                            'bc': 32000,
                            'bc_unit': 'bytes',
                        },
                        'module': {
                            23: {
                                'transmitted_bytes': 57928,
                                'offered_rate': {
                                    'interval': '5-minute',
                                    'rate': 0,
                                    'unit': 'bytes/sec',
                                },
                                'conformed': {
                                    'peak_rate': 23,
                                    'unit': 'bytes/sec',
                                    'time': 'Sat Sep 05 11:17:39 2026',
                                },
                                'dropped_bytes': 0,
                                'violate_rate': {
                                    'interval': '5-min',
                                    'rate': 0,
                                    'unit': 'byte/sec',
                                },
                                'violated': {
                                    'peak_rate': 0,
                                    'unit': 'byte/sec',
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
