expected_output = {
    'pools_configured': 3,
    'protocol': {
        'IPv4': {
            'index': {
                1: {
                    'hsl_id': 1,
                    'is_single': 'TRUE',
                    'name': 'n64_pool',
                    'protocol': 'IPv4',
                    'range': '(172.0.0.1 - 172.0.0.100)'
                    },
                2: {
                    'hsl_id': 2,
                    'is_single': 'TRUE',
                    'name': 'nat64_v4_pool',
                    'protocol': 'IPv4',
                    'range': '(10.0.0.2 - 10.0.0.255)',
                    'ranges': '10.0.0.2 - 10.0.0.255',
                    'static_routes_dict': {
                        'static_routes': ['10.0.0.2/31',
                                          '10.0.0.4/30',
                                          '10.0.0.8/29',
                                          '10.0.0.16/28',
                                          '10.0.0.32/27',
                                          '10.0.0.64/26',
                                          '10.0.0.128/25'],
                    'static_routes_range': 7
                      }
                    },
                3: {
                    'hsl_id': 3,
                    'is_single': 'TRUE',
                    'name': 'nat64_v4_pool_1',
                    'protocol': 'IPv4',
                    'range': '(11.0.0.2 - 11.0.0.255)'
                    }
                }
            }
        }
    }