expected_output = {
    'cos': '5',
    'port': {
        'Gi1/0/20': {
            'protocol': {
                'cdp': {
                    'decaps_counter': '1',
                    'drop_counter': '0',
                    'drop_threshold': '30',
                    'encaps_counter': '7',
                    'shutdown_threshold': '40'
                },
                'lldp': {
                    'decaps_counter': '3',
                    'drop_counter': '0',
                    'drop_threshold': '20',
                    'encaps_counter': '4',
                    'shutdown_threshold': '----'
                },
                'stp': {
                    'decaps_counter': '207',
                    'drop_counter': '7',
                    'drop_threshold': '20',
                    'encaps_counter': '485',
                    'shutdown_threshold': '40'
                },
                'vtp': {
                    'decaps_counter': '0',
                    'drop_counter': '0',
                    'drop_threshold': '20',
                    'encaps_counter': '1',
                    'shutdown_threshold': '40'
                },
                'udld': {
                    'decaps_counter': '0',
                    'drop_counter': '0',
                    'drop_threshold': '----',
                    'encaps_counter': '0',
                    'shutdown_threshold': '----'
                }
            }
        }
    }
}
