

expected_output = {
    'clock_state': {
        'system_status': {
            'associations_address': '192.168.128.5',
            'associations_local_mode': 'client',
            'clock_offset': -0.56,
            'clock_refid': '10.81.254.131',
            'clock_state': 'synchronized',
            'clock_stratum': 2,
            'root_delay': 7.98}
    },
    'peer': {
        '192.168.128.5': {
            'local_mode': {
                'client': {
                    'configured': True,
                    'delay': 7.98,
                    'jitter': 0.108,
                    'local_mode': 'client',
                    'mode': 'synchronized',
                    'offset': -0.56,
                    'poll': 64,
                    'reach': 377,
                    'receive_time': 1,
                    'refid': '10.81.254.131',
                    'remote': '192.168.128.5',
                    'stratum': 2}
            }
        },
        '2001:db8:429a:3189::2': {
            'local_mode': {
                'client': {
                    'configured': True,
                    'delay': 6.0,
                    'jitter': 0.046,
                    'local_mode': 'client',
                    'mode': 'candidate',
                    'offset': -2.832,
                    'poll': 64,
                    'reach': 377,
                    'receive_time': 20,
                    'refid': '172.16.36.80',
                    'remote': '2001:db8:429a:3189::2',
                    'stratum': 3}
            }
        }
    },
    'vrf': {
        'default': {
            'address': {
                '192.168.128.5': {
                    'isconfigured': {
                        True: {
                            'address': '192.168.128.5',
                            'isconfigured': True}
                    },
                    'type': {
                        'peer': {
                            'address': '192.168.128.5',
                            'type': 'peer',
                            'vrf': 'default'}
                    }
                }
            }
        },
        'testAA': {
            'address': {
                '2001:db8:429a:3189::2': {
                    'isconfigured': {
                        True: {
                            'address': '2001:db8:429a:3189::2',
                            'isconfigured': True}
                    },
                    'type': {
                        'peer': {
                            'address': '2001:db8:429a:3189::2',
                            'type': 'peer',
                            'vrf': 'testAA'}
                    }
                }
            }
        }
    }
}
