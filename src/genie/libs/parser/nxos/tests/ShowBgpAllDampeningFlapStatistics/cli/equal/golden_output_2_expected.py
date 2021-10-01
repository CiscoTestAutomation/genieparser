expected_output = {
    'vrf': 
        {'default': 
            {'address_family': 
                {'ipv4 multicast': 
                    {'dampened_paths': 0,
                    'dampening_enabled': True,
                    'history_paths': 0},
                'ipv4 unicast': 
                    {'dampened_paths': 0,
                    'dampening_enabled': True,
                    'history_paths': 0,
                    'network': 
                        {'10.4.0.0/24': 
                            {'best': True,
                            'current_penalty': 570,
                            'duration': '00:20:56',
                            'flaps': 1,
                            'pathtype': 'e',
                            'peer': '192.168.64.1',
                            'reuse_limit': 1000,
                            'status': '*',
                            'suppress_limit': 1500},
                        '10.4.1.0/24': 
                            {'best': True,
                            'current_penalty': 570,
                            'duration': '00:20:56',
                            'flaps': 1,
                            'pathtype': 'e',
                            'peer': '192.168.64.1',
                            'reuse_limit': 1000,
                            'status': '*',
                            'suppress_limit': 1500},
                        '10.4.2.0/24': 
                            {'best': True,
                            'current_penalty': 570,
                            'duration': '00:20:56',
                            'flaps': 1,
                            'pathtype': 'e',
                            'peer': '192.168.64.1',
                            'reuse_limit': 1000,
                            'status': '*',
                            'suppress_limit': 1500}}},
                'ipv6 multicast':
                    {'dampened_paths': 0,
                    'dampening_enabled': True,
                    'history_paths': 0}}}}}
