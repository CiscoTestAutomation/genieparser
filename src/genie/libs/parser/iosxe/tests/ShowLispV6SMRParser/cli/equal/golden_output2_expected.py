expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4100: {
                    'eid_table': 'red',
                    'entries': 3,
                    'prefix': {
                        '2001:192:168:1::/64': {
                            'producer': ['away table']
                            },
                        '2001:192:168:1::1/128': {
                            'producer': ['local EID']
                            },
                        '2001:192:168:1::71/128': {
                            'producer': ['local EID']
                            }
                        }
                    },
                    4101: {
                        'eid_table': 'blue',
                        'entries': 1,
                        'prefix': {
                            '2001:193:168:1::/64': {
                                'producer': ['away table']
                            }
                        }
                    }
                }
            }
        }
    }