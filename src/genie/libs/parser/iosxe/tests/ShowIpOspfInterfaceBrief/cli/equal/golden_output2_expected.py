expected_output = {
    'instance': {
        '1': {
            'areas': {
                '0.0.0.0': {
                    'interfaces': {
                        'GigabitEthernet1': {
                            'cost': 1,
                            'ip_address': '192.168.12.1/24',
                            'nbrs_count': 1,
                            'nbrs_full': 1,
                            'state': 'BDR',
                        },
                        'GigabitEthernet2': {
                            'cost': 1,
                            'ip_address': '192.168.13.1/24',
                            'nbrs_count': 1,
                            'nbrs_full': 1,
                            'state': 'BDR',
                        },
                        'GigabitEthernet3': {
                            'cost': 1,
                            'ip_address': '192.168.14.1/24',
                            'nbrs_count': 1,
                            'nbrs_full': 1,
                            'state': 'BDR',
                        },
                        'Loopback0': {
                            'cost': 1,
                            'ip_address': '1.1.1.1/32',
                            'nbrs_count': 0,
                            'nbrs_full': 0,
                            'state': 'LOOP',
                        },
                    },
                },
            },
        },
        '2': {
            'areas': {
                '0.0.0.0': {
                    'interfaces': {
                        'GigabitEthernet1.10': {
                            'cost': 1,
                            'ip_address': '10.0.12.1/24',
                            'nbrs_count': 1,
                            'nbrs_full': 1,
                            'state': 'BDR',
                        },
                        'GigabitEthernet2.10': {
                            'cost': 1,
                            'ip_address': '10.0.13.1/24',
                            'nbrs_count': 1,
                            'nbrs_full': 1,
                            'state': 'BDR',
                        },
                        'GigabitEthernet3.10': {
                            'cost': 1,
                            'ip_address': '10.0.14.1/24',
                            'nbrs_count': 1,
                            'nbrs_full': 1,
                            'state': 'BDR',
                        },
                        'Loopback1': {
                            'cost': 1,
                            'ip_address': '1.1.1.1/32',
                            'nbrs_count': 0,
                            'nbrs_full': 0,
                            'state': 'LOOP',
                        },
                    },
                },
            },
        },
    },
}
