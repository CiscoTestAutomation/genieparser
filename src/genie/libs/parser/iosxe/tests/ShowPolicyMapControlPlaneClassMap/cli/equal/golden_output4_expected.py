expected_output =  {
    'class_map': {
        'system-cpp-police-mcast-rpf-fail': {
            'bytes': 0,
            'match': ['none'],
            'match_evaluation': 'match-any',
            'packets': 0,
            'police': {
                'conformed': {
                    'actions': {
                        'transmit': True,
                    },
                    'bytes': 0,
                },
                'exceeded': {
                    'actions': {
                        'drop': True,
                    },
                    'bytes': 0,
                },
            },
            'rate': {
                'drop_rate_bps': 0,
                'interval': 300,
                'offered_rate_bps': 0,
            },
        },
    },
}
