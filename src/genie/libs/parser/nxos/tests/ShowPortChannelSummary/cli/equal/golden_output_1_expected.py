

expected_output = {
    'interfaces': {
        'Port-channel1': {
            'bundle_id': 1,
            'oper_status': 'up',
            'layer': 'routed',
            'protocol': 'lacp',
            'type': 'eth',
            'members': {
                'Ethernet1/1': {
                    'flags': 'P',
                },
                'Ethernet1/2': {
                    'flags': 'P'
                }
            },
        },
        'Port-channel2': {
            'bundle_id': 2,
            'oper_status': 'up',
            'layer': 'switched',
            'protocol': 'lacp',
            'type': 'eth',
            'members': {
                'Ethernet1/3': {
                    'flags': 'P',
                },
                'Ethernet1/4': {
                    'flags': 'P'
                },
                'Ethernet1/5': {
                    'flags': 'H'
                }
            },
        }
    }
}
