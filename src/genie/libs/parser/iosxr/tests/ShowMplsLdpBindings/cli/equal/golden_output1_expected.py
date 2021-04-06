expected_output = {
    'lib_entry': {
        '25.97.1.1/32': {
            'rev': 2,
            'local_binding': {
                'label': 'ImpNull'
            },
            'remote_bindings': {
                'peer_count': 2,
                'label': {
                    '16002': {
                        'lsr_id': {
                            '95.95.95.95:0': {
                                'label': '16002',
                                'lsr_id': '95.95.95.95:0'
                            }
                        }
                    },
                    '16001': {
                        'lsr_id': {
                            '96.96.96.96:0': {
                                'label': '16001',
                                'lsr_id': '96.96.96.96:0'
                            }
                        }
                    }
                }
            }
        },
        '95.95.95.95/32': {
            'rev': 20,
            'local_binding': {
                'label': '24001'
            },
            'remote_bindings': {
                'peer_count': 2,
                'label': {
                    'ImpNull': {
                        'lsr_id': {
                            '95.95.95.95:0': {
                                'label': 'ImpNull',
                                'lsr_id': '95.95.95.95:0'
                            }
                        }
                    },
                    '16000': {
                        'lsr_id': {
                            '96.96.96.96:0': {
                                'label': '16000',
                                'lsr_id': '96.96.96.96:0'
                            }
                        }
                    }
                }
            }
        }
    }
}