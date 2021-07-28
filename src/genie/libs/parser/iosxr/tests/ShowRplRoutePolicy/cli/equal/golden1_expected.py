expected_output = {
        'test0': {
            'statements': {
                10: {
                    'actions': {
                        'actions': 'pass',
                    },
                    'conditions': {
                        'match_prefix_list': '(0.0.0.0/0)',
                    },
                },
            },
        },
        'test1': {
            'statements': {
                10: {
                    'actions': {
                        'set_spf_priority': 'high',
                    },
                    'conditions': {
                        'match_prefix_list': 'Test-test_test0',
                    },
                },
                20: {
                    'actions': {
                        'set_spf_priority': 'medium',
                    },
                    'conditions': {
                        'match_prefix_list': '(0.0.0.0/0 eq 32)',
                    },
                },
            },
        },
    }