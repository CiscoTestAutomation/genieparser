

expected_output = {
    'clock_state': {'system_status': {'associations_address': '10.64.4.32',
                                      'clock_state': 'synchronized',
                                      'clock_stratum': 4,
                                      'root_delay': 0.02588}},
    'total_peers': 2,
    'vrf': {'default': {'peer': {'127.127.1.0': {'delay': 0.0,
                                                 'local': '10.100.100.1',
                                                 'mode': 'client',
                                                 'poll': 64,
                                                 'reach': 0,
                                                 'remote': '127.127.1.0',
                                                 'stratum': 8},
                                 '10.64.4.32': {'delay': 0.02588,
                                              'local': '10.100.100.1',
                                              'mode': 'synchronized',
                                              'poll': 64,
                                              'reach': 377,
                                              'remote': '10.64.4.32',
                                              'stratum': 4,
                                              'vrf': 'default'}}}}
}
