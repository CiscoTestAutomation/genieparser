expected_output = {
    'control_plane': {
        'service_policy': {
            'input': {
                'policy_name': 'copp-system-p-policy-strict',
                'class_map': {
                    'copp-system-p-class-l3uc-data': {
                        'match_type': 'match-any',
                        'matches': [
                            'exception glean',
                        ],
                        'set_cos': 1,
                        'police': {
                            'cir': 800,
                            'cir_unit': 'kbps',
                            'bc': 32000,
                            'bc_unit': 'bytes',
                        },
                        'module': {
                            1: {
                                'transmitted_packets': 373977,
                                'dropped_packets': 0,
                            },
                        },
                    },
                },
            },
        },
    },
}
