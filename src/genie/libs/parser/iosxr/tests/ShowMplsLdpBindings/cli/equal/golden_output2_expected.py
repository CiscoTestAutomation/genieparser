expected_output = {
    'lib_entry': {
        '10.9.9.98/32': {
                'rev': 6,
                'local_binding': {
                    'label': 'IMP-NULL'
                }
            },
        '10.10.2.0/24': {
            'rev': 12,
            'local_binding': {
                'label': 'IMP-NULL'
            },
            'remote_bindings': {
                'label': {
                    '16': {
                        'lsr_id': {
                            '10.255.255.255:0': {
                                'label': '16',
                                'lsr_id': '10.255.255.255:0'
                            }
                        }
                    },
                    'IMP-NULL': {
                        'lsr_id': {
                            '10.256.256.256:0': {
                                'label': 'IMP-NULL',
                                'lsr_id': '10.256.256.256:0'
                            }
                        }
                    }
                }
            }
        }
    }
}