

expected_output = {
    'clock_state': {
        'system_status': {
            'associations_address': '172.19.69.1',
            'associations_local_mode': 'client',
            'clock_offset': 67.16,
            'clock_refid': '172.24.114.33',
            'clock_state': 'synchronized',
            'clock_stratum': 3,
            'root_delay': 2.0}
    },
    'peer': {
        '127.127.1.1': {
            'local_mode': {
                'client': {
                    'configured': True,
                    'delay': 0.0,
                    'jitter': 438.3,
                    'local_mode': 'client',
                    'mode': 'candidate',
                    'offset': 0.0,
                    'poll': 1024,
                    'reach': 37,
                    'receive_time': 5,
                    'refid': '127.127.1.1',
                    'remote': '127.127.1.1',
                    'stratum': 5}
            }
        },
        '172.19.69.1': {
            'local_mode': {
                'client': {
                    'configured': True,
                    'delay': 2.0,
                    'jitter': 0.0,
                    'local_mode': 'client',
                    'mode': 'synchronized',
                    'offset': 67.16,
                    'poll': 1024,
                    'reach': 1,
                    'receive_time': 13,
                    'refid': '172.24.114.33',
                    'remote': '172.19.69.1',
                    'stratum': 3}
            }
        }
    },
    'vrf': {
        'default': {
            'address': {
                '127.127.1.1': {
                    'isconfigured': {
                        True: {
                            'address': '127.127.1.1',
                            'isconfigured': True}
                    },
                    'type': {
                        'peer': {
                            'address': '127.127.1.1',
                            'type': 'peer',
                            'vrf': 'default'}
                    }
                },
                '172.19.69.1': {
                    'isconfigured': {
                        True: {
                            'address': '172.19.69.1',
                            'isconfigured': True}
                    },
                    'type': {
                        'peer': {
                            'address': '172.19.69.1',
                            'type': 'peer',
                            'vrf': 'default'}
                    }
                }
            }
        }
    }
}
