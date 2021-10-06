

expected_output = {
    'process_id': {
        1: {
            'policy': {
                'active': {
                    'sid': {
                        100: {
                            'prefix': '10.4.1.100/32',
                            'range': 20,
                        },
                        150: {
                            'prefix': '10.4.1.150/32',
                            'range': 10,
                        }
                    },
                    'number_of_mapping_entries': 2,
                },
                'backup': {
                    'sid': {
                        100: {
                            'prefix': '10.4.1.100/32',
                            'range': 20,
                        },
                        150: {
                            'prefix': '10.4.1.150/32',
                            'range': 10,
                        }
                    },
                    'number_of_mapping_entries': 2,
                },
            }
        }
    }
}
