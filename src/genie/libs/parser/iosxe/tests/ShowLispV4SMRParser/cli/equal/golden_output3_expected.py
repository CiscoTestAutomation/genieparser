expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4100: {
                    'eid_table': 'red',
                    'entries': 3,
                    'prefix': {
                        '192.168.1.0/24': {
                            'producer': ['away table']
                            },
                        '192.168.1.1/32': {
                            'producer': ['local EID']
                            },
                        '192.168.1.71/32': {
                            'producer': ['local EID']
                            }
                        }
                    },
                    4101: {
                        'eid_table': 'blue',
                        'entries': 1,
                        'prefix': {
                            '193.168.1.0/24': {
                                'producer': ['away table']
                                }
                            }
                        }
                    }
                }
            }
        }