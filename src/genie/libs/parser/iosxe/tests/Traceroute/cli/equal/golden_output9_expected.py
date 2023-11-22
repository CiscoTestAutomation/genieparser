expected_output = {
    'traceroute': {
        '192.168.0.20': {
            'address': '192.168.0.20',
            'hops': {
                '1': {
                    'paths': {
                        1: {
                            'address': '192.168.0.22',
                            'asn': 2516,
                            'probe_msec': ['0', '0', '1']
                        }
                    }
                },
                '2': {
                    'paths': {
                        1: {
                            'address': '192.168.0.23',
                            'asn': 2516,
                            'probe_msec': ['1', '1', '2']
                        }
                    }
                },
                '3': {
                    'paths': {
                        1: {
                            'address': '192.168.0.24',
                            'asn': 2516,
                            'probe_msec': ['2', '2', '2']
                        }
                    }
                },
                '4': {
                    'paths': {
                        1: {
                            'address': '192.168.0.25',
                            'asn': 2516,
                            'probe_msec': ['2']
                        }
                    }
                }
            }
        }
    }
}