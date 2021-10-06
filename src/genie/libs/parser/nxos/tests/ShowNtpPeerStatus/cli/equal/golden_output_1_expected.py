

expected_output = {
    'clock_state': {'system_status': {'associations_address': '10.4.1.1',
                                      'clock_state': 'synchronized',
                                      'clock_stratum': 8,
                                      'root_delay': 0.01311}},
    'vrf': {
        'default': {
            'peer': {'10.4.1.1': {'delay': 0.01311,
                                 'local': '0.0.0.0',
                                 'mode': 'synchronized',
                                 'poll': 16,
                                 'reach': 377,
                                 'remote': '10.4.1.1',
                                 'stratum': 8,
                                 'vrf': 'default'},
                    '10.16.2.2': {'delay': 0.01062,
                              'local': '0.0.0.0',
                              'mode': 'client',
                              'poll': 16,
                              'reach': 377,
                              'remote': '10.16.2.2',
                              'stratum': 9,
                              'vrf': 'default'},
                    '10.100.5.5': {'delay': 0.0,
                              'local': '0.0.0.0',
                              'mode': 'client',
                              'poll': 64,
                              'reach': 0,
                              'remote': '10.100.5.5',
                              'stratum': 16,
                              'vrf': 'default'}
            }
        },
        'VRF1': {
            'peer': {'10.64.4.4': {'delay': 0.0,
                                 'local': '0.0.0.0',
                                 'mode': 'client',
                                 'poll': 256,
                                 'reach': 0,
                                 'remote': '10.64.4.4',
                                 'stratum': 16,
                                 'vrf': 'VRF1'}
            }
        },
    },
    'total_peers': 4
}
