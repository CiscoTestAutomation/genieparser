expected_output = {
    'traceroute': {
        '10.4.1.1': {
            'address': '10.4.1.1',
            'hops': {
                '1': {
                    'paths': {
                        1: {
                            'address': '10.4.1.2',
                            'label_info': {
                                'MPLS': {
                                    'exp': 0,
                                    'label': '11111'}
                            },
                            'probe_msec': ['16',
                                           '4',
                                           '4']}
                    }
                },
                '2': {
                    'paths': {
                        1: {
                            'address': '10.9.1.3',
                            'probe_msec': ['9',
                                           '*',
                                           '8']}
                    }
                }
            }
        }
    }
}
