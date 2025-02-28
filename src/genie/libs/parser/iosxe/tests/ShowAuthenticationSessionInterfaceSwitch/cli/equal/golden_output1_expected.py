expected_output = {
    'interfaces': {
        'F': {
            'mac_address': {
                '-': {
                    'domain': 'Removal',
                    'method': 'Final',
                    'session_id': 'progress',
                    'status': 'in',
                },
            },
        },
        'Gi2/0/3': {
            'mac_address': {
                '001a.a136.c68a': {
                    'domain': 'VOICE',
                    'method': 'dot1x',
                    'session_id': '2300130B0000002ABD0A2AF1',
                    'status': 'Auth',
                },
                '0055.6677.8855': {
                    'domain': 'DATA',
                    'method': 'dot1x',
                    'session_id': '2300130B0000002CBD0A520E',
                    'status': 'Auth',
                },
            },
        },
        'I': {
            'mac_address': {
                '-': {
                    'domain': 'IIF',
                    'method': 'Awaiting',
                    'session_id': 'allocation',
                    'status': 'ID',
                },
            },
        },
    },
    'runnable_methods': {
        1: {
            'handle': 1,
            'name': 'dot1x',
            'priority': 5,
        },
        13: {
            'handle': 13,
            'name': 'dot1xSup',
            'priority': 5,
        },
        14: {
            'handle': 14,
            'name': 'mab',
            'priority': 15,
        },
        2: {
            'handle': 2,
            'name': 'webauth',
            'priority': 10,
        },
    }
}