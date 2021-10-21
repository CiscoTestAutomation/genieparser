

expected_output = {
    'interfaces': {
        'Port-channel1': {'bundle_id': 1,
                          'layer': 'switched',
                          'members': {'Ethernet1/42': {'flags': 'D'},
                                      'Ethernet1/43': {'flags': 'D'},
                                      'Ethernet1/45': {'flags': 'P'},
                                      'Ethernet1/46': {'flags': 'P'},
                                      'Ethernet1/47': {'flags': 'D'},
                                      'Ethernet1/48': {'flags': 'P'}},
                          'oper_status': 'up',
                          'protocol': 'lacp',
                          'type': 'eth'},
        'Port-channel2': {'bundle_id': 2,
                          'layer': 'switched',
                          'members': {'Ethernet1/50': {'flags': 'P'},
                                      'Ethernet1/51': {'flags': 'P'}},
                          'oper_status': 'up',
                          'protocol': 'lacp',
                          'type': 'eth'}}}
