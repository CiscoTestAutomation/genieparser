expected_output = {
        'INTERNAL-route': {
            'statements': {
                10: {
                    'actions': {
                        'actions': 'drop',
                    },
                    'conditions': {
                        'match_ext_community_list': ['CMT-TP', 'CMT-OLDTP', 'CMT-SBTP', 'CMT-FP'],
                    },
                },
                20: {
                    'actions': {
                        'actions': 'pass',
                    },
                    'conditions': {
                    },
                },
            },
        },
    }