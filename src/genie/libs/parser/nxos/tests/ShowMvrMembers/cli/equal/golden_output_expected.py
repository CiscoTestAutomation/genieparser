expected_output = {
    'vlans': {
        100: {
            'groups': {
                '230.1.1.1': {
                    'status': 'ACTIVE',
                    'members': [
                        'Port-channel201',
                        'Port-channel202',
                        'Port-channel203',
                        'Port-channel205',
                        'Port-channel206',
                    ],
                },
                '230.1.1.2': {
                    'status': 'ACTIVE',
                    'members': [
                        'Port-channel205',
                        'Port-channel206',
                        'Port-channel207',
                        'Port-channel208',
                    ],
                },
            },
        },
        340: {
            'groups': {
                '235.1.1.6': {
                    'status': 'ACTIVE',
                    'members': ['Ethernet102/1/1'],
                },
            },
        },
        101: {
            'groups': {
                '225.1.3.1': {
                    'status': 'ACTIVE',
                    'members': ['Ethernet1/10', 'Ethernet2/2'],
                },
                '228.1.2.241': {
                    'status': 'ACTIVE',
                    'members': ['Ethernet103/1/1', 'Ethernet103/1/2'],
                },
            },
        },
    },
}
