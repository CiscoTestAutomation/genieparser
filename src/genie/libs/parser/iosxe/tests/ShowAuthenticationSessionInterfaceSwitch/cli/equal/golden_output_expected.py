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
        'Te1/0/1': {
            'mac_address': {
                '0050.56bc.21a4': {
                    'domain': 'UNKNOWN',
                    'method': 'dot1x',
                    'session_id': '5E0D130B00013C30D4524D05',
                    'status': 'Unauth',
                },
            },
        },
    },
    'runnable_methods': {
        10: {
            'handle': 10,
            'name': 'dot1x',
            'priority': 5,
        },
        11: {
            'handle': 11,
            'name': 'dot1xSup',
            'priority': 5,
        },
        12: {
            'handle': 12,
            'name': 'mab',
            'priority': 15,
        },
        14: {
            'handle': 14,
            'name': 'webauth',
            'priority': 10,
        },
    }
}